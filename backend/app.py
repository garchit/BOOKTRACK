from flask import Flask , request , jsonify , json 
from flask_caching import Cache
import time
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource , reqparse
from sqlalchemy import Date , and_
from flask import Flask, send_from_directory
from worker import celery_init_app
from tasks import create_resource_csv
from model import db, User, Section, Book, UserBookAccess  # Import your models here
# from flask.json import JSONEncoder

app = Flask(__name__ , static_folder='static')
CORS(app , origin="*")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'grocery'
app.config["CACHE_TYPE"] = "redis"
app.config['CACHE_REDIS_sm_db'] = 0
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"



db.init_app(app)  # Initialize the database with your app

# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)

# Register the custom JSON encoder with Flask
# app.json_encoder = CustomJSONEncoder


# db = SQLAlchemy(app)
jwt = JWTManager(app)
celery_app = celery_init_app()
cache = Cache(app)
api = Api(app)
    
# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.String(256),nullable=False)
# # Don't need to create tables here
# class Section(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     description = db.Column(db.Text, nullable=True)
#     # Define the one-to-many relationship with Book
#     books = db.relationship('Book', backref='section', lazy=True)

# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     issue_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     poster = db.Column(db.String(200))  # Assuming poster link will be stored as string
#     price = db.Column(db.Float)
#     # Add a column to store PDF files
#     # pdf_file = db.Column(db.String(100))  # Assuming PDF will be stored as binary data    
#     section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    
    
# class UserBookAccess(db.Model):
#     # __tablename__ = 'user_book_access'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
#     access_type = db.Column(db.String(50), nullable=False)  # Define the type of access (e.g., read, write, etc.)
#     days = db.Column(db.Integer, nullable=False)  # Number of days the access is granted for
#     book_name = db.Column(db.String(100))  # Add column for book name
#     user_name = db.Column(db.String(80))   # Add column for user name
#     # request_date = db.Column(db.DateTime, nullable=False , default=datetime.utcnow)  # Column for request date
#     request_date = db.Column(Date, nullable=False, default=datetime.utcnow)
#     # Define the relationship with User and Book tables
#     user = db.relationship('User', backref=db.backref('book_access', cascade='all, delete-orphan'))
#     book = db.relationship('Book', backref=db.backref('user_access', cascade='all, delete-orphan'))

@app.route("/")
def hello():
    return "Hello World!"

# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     if User.query.filter_by(username=username).first():
#         return jsonify({'message': 'Username already exists'}), 400

#     user = User(username=username, 
#                 password=password)
#     db.session.add(user)
#     db.session.commit()

#     return jsonify({'message': 'User registered successfully'}), 201


class SignupResource(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        
        if User.query.filter_by(username=username).first():
            return {'error':'Username already exists'}, 400
        
        hashed = generate_password_hash(password,method='pbkdf2:sha256')
        if role == 'user':
            new_user = User(username=username,password=hashed,role='user')
        elif role == 'admin':
            new_user = User(username=username,password=hashed,role='admin')


        db.session.add(new_user)
        db.session.commit()

        return {'message':'Signup Successful'}, 201


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     user = User.query.filter_by(username=username).first()
#     if not user :
        
#         return jsonify({'message': 'Invalid credentials'}), 401
    
#     access_token = create_access_token(
#         identity=user.user_id, expires_delta=timedelta(days=1))
#     user_info = {
#         'user_id' : user.user_id,
#         'username': user.username,
       
#     }

#     return jsonify({'access_token': access_token, 'user': user_info}), 200


class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        print(user.user_id)

        if user and check_password_hash(user.password,password):
            access_token = create_access_token(identity={
                'username':user.username
            })

            return {'message':'Login Successful','access_token':access_token,'userRole':user.role , 'username' : user.username , 'user_id':user.user_id}, 200
        else:
            return {'error':'Invalid Username or Password'}, 401

@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    admin_username = 'admin'
    admin_password = 'admin_password'

    if username == admin_username and password == admin_password:
        access_token = create_access_token(identity=admin_username, expires_delta=timedelta(days=1))
        return jsonify({'access_token': access_token }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    
api.add_resource(SignupResource,'/signup')
api.add_resource(LoginResource,'/userlogin')


class SectionResource(Resource):
    # def get(self, section_id=None):
    #     if section_id is None:
    #         sections = Section.query.all()
    #         section_list = [{'id': section.id, 'name': section.name, 'description': section.description, 'date_created': section.date_created.strftime('%Y-%m-%d %H:%M:%S')} for section in sections]
    #         return jsonify(section_list)
    #     else:
    #         section = Section.query.get_or_404(section_id)
    #         return jsonify({'id': section.id, 'name': section.name, 'description': section.description, 'date_created': section.date_created.strftime('%Y-%m-%d %H:%M:%S')})
    def get(self):
        search_query = request.args.get('search')
        if search_query:
            sections = Section.query.filter(Section.name.ilike(f'%{search_query}%')).all()
        else:
            sections = Section.query.all()
        section_list = [{'id': section.id, 'name': section.name, 'description': section.description, 'date_created': section.date_created.strftime('%Y-%m-%d %H:%M:%S')} for section in sections]
        return jsonify(section_list)
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        section_name = args['name']

        if not section_name:
            return {'error': 'Section name is required'}, 400

        existing_section = Section.query.filter(db.func.lower(Section.name) == section_name.lower()).first()
        if existing_section:
            return {'error': 'Section already exists'}, 409

        new_section = Section(name=section_name, description=args['description'])
        db.session.add(new_section)
        db.session.commit()

        return {'message': 'Section created successfully', 'section': {'id': new_section.id, 'name': new_section.name, 'description': new_section.description}}, 201


    def put(self, section_id):
        section = Section.query.get_or_404(section_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        if args['name']:
            section.name = args['name']
        if args['description']:
            section.description = args['description']

        db.session.commit()
        return jsonify({'message': 'Section updated successfully'})

    def delete(self, section_id):
        section = Section.query.get_or_404(section_id)
        db.session.delete(section)
        db.session.commit()
        return jsonify({'message': 'Section deleted successfully'})
    
    
@app.route('/sections/<int:section_id>/books', methods=['POST'])
def add_book(section_id):
    data = request.form
    name = data.get('name')
    content = data.get('content')
    author = data.get('author')
    price = float(data.get('price'))
    poster = data.get('poster')
    # pdf_file = request.files['pdfFile']
    
    section = Section.query.get_or_404(section_id)
    
    new_book = Book(name=name, content=content, author=author, price=price, poster=poster, section=section)
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify(message='Book added successfully'), 201


# @app.route('/storebooks/<int:section_id>')
# def get_books(section_id):
#     # books = Book.query.all()
#     books = Book.query.filter_by(section_id=section_id).all()
#     books_data = [{'id': book.id, 'name': book.name, 'content': book.content, 'author': book.author,
#                    'issue_date': book.issue_date.strftime('%Y-%m-%d'), 'poster': book.poster,
#                    'price': book.price} for book in books]
#     return jsonify(books_data)

@app.route('/storebooks/<int:section_id>')
def get_books(section_id):
    search_query = request.args.get('search')
    print(f"Section ID: {section_id}")
    print(f"Search Query: {search_query}")

    if search_query:
        books = Book.query.filter(Book.section_id == section_id, Book.name.ilike(f'%{search_query}%')).all()
    else:
        books = Book.query.filter_by(section_id=section_id).all()

    print(f"Books found: {books}")

    books_data = [{'id': book.id, 'name': book.name, 'content': book.content, 'author': book.author,
                   'issue_date': book.issue_date.strftime('%Y-%m-%d'), 'poster': book.poster,
                   'price': book.price} for book in books]
    return jsonify(books_data)


class BookResource(Resource):
    def put(self, section_id, book_id):
        # Parse the request data
        data = request.json

        # Retrieve the book from the database
        book = Book.query.filter_by(section_id=section_id, id=book_id).first()

        # Check if the book exists
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        # Update the book attributes
        book.name = data.get('name', book.name)
        book.content = data.get('content', book.content)
        book.author = data.get('author', book.author)
        book.price = data.get('price', book.price)
        book.poster = data.get('poster', book.poster)

        # Commit changes to the database
        db.session.commit()

        return jsonify({'message': 'Book updated successfully'})

    def delete(self, section_id, book_id):
        # Retrieve the book from the database
        book = Book.query.filter_by(section_id=section_id, id=book_id).first()

        # Check if the book exists
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        # Delete the book from the database
        db.session.delete(book)
        db.session.commit()

        return jsonify({'message': 'Book deleted successfully'})

# Add BookResource to the API routing
api.add_resource(BookResource, '/books/<int:section_id>/<int:book_id>')

    
# class BookResource(Resource):
#     def post(self, section_id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True, help='Name is required')
#         parser.add_argument('content', type=str, required=True, help='Content is required')
#         parser.add_argument('author', type=str, required=True, help='Author is required')
#         parser.add_argument('price', type=float, required=True, help='Price is required')
#         parser.add_argument('poster', type=str)
#         args = parser.parse_args()

#         section = Section.query.get_or_404(section_id)
        
#         new_book = Book(name=args['name'], content=args['content'], author=args['author'],
#                         price=args['price'], poster=args['poster'], section=section)
#         db.session.add(new_book)
#         db.session.commit()
        
#         return jsonify(message='Book added successfully'), 201

#     def get(self, section_id):
#         books = Book.query.filter_by(section_id=section_id).all()
#         books_data = [{'id': book.id, 'name': book.name, 'content': book.content,
#                        'author': book.author, 'issue_date': book.issue_date.strftime('%Y-%m-%d'),
#                        'poster': book.poster, 'price': book.price} for book in books]
#         return jsonify(books_data)

#     def put(self, section_id, book_id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('content', type=str)
#         parser.add_argument('author', type=str)
#         parser.add_argument('price', type=float)
#         parser.add_argument('poster', type=str)
#         args = parser.parse_args()

#         book = Book.query.filter_by(section_id=section_id, id=book_id).first()
#         if not book:
#             return jsonify({'error': 'Book not found'}), 404

#         if args['name']:
#             book.name = args['name']
#         if args['content']:
#             book.content = args['content']
#         if args['author']:
#             book.author = args['author']
#         if args['price']:
#             book.price = args['price']
#         if args['poster']:
#             book.poster = args['poster']

#         db.session.commit()
#         return jsonify({'message': 'Book updated successfully'})

#     def delete(self, section_id, book_id):
#         book = Book.query.filter_by(section_id=section_id, id=book_id).first()
#         if not book:
#             return jsonify({'error': 'Book not found'}), 404

#         db.session.delete(book)
#         db.session.commit()
#         return jsonify({'message': 'Book deleted successfully'})


api.add_resource(SectionResource, '/sections', '/sections/<int:section_id>')
# api.add_resource(BookResource , '/books' , '/books/<int:section_id>')
# api.add_resource(BookResource, '/books/<int:section_id>')

@app.route('/api/request-access', methods=['POST'])
def request_access():
    data = request.json
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    days = data.get('days')
    book_name = data.get('book_name')
    user_name = data.get('user_name')

    if not user_id or not book_id or not days or not book_name or not user_name:
        return jsonify({'success': False, 'message': 'Missing data'}), 400

    if days < 1 or days > 7:
        return jsonify({'success': False, 'message': 'Invalid number of days'}), 400

    access_request = UserBookAccess(
        user_id=user_id,
        book_id=book_id,
        access_type='read',
        days=days,
        book_name=book_name,
        user_name=user_name,
        request_date=datetime.utcnow()
    )

    try:
        db.session.add(access_request)
        db.session.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
    
# Flask route to fetch user access data
@app.route('/api/user-access-data', methods=['GET'])
def get_user_access_data():
    try:
        # Query UserBookAccess table for all user access data
        user_access_data = UserBookAccess.query.all()
        
        # Prepare response data in JSON format
        access_data_list = []
        for access in user_access_data:
            access_data_list.append({
                'book_name': access.book_name,
                'user_id' : access.user_id,
                'username' : access.user_name,
                'bookId' : access.book_id,
                "RequestDate" : access.request_date,
                "id" : access.id,
                # 'section_name': access.section_name,  # Adjust based on your actual schema
                'days': access.days,
                'status': access.access_type  # Assuming you have a status field in UserBookAccess
            })
        
        return jsonify(access_data_list)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/update-access-status/<int:id>', methods=['POST'])
def update_access_status(id):
    try:
        data = request.json
        new_status = data.get('status')
        
        # Query the UserBookAccess entry by ID
        user_access = UserBookAccess.query.get(id)
        print("user_access",user_access)
        print("new_status",new_status)
        
        if not user_access:
            return jsonify({'error': 'UserBookAccess entry not found'}), 404

        # Update the access type
        user_access.access_type = new_status
        db.session.commit()
        
        return jsonify({'message': 'Status updated successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# @app.route('/static/<path:path>')
# def serve_static(path):
#     print(path)
#     return send_from_directory('static', path)


# @app.route('/api/get-pdf-url', methods=['GET'])
# def get_pdf_url():
#     pdf_url = '/src/assets/python certificate.pdf'
#     return jsonify({'pdf_url': pdf_url})

# # Serve static files
# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory('static', filename)

# Route to fetch book details by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    print(book_id)
    try:
        book = Book.query.get_or_404(book_id)
        return jsonify({
            'id': book.id,
            'name': book.name,
            'content': book.content,
            'author': book.author,
            'issue_date': book.issue_date.isoformat(),  # Format date as ISO string
            'poster': book.poster,
            'price': book.price,
            'section_id': book.section_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Endpoint to get the count of requested books for a user
@app.route('/api/requested-books-count', methods=['GET'])
def get_requested_books_count():
    user_id = request.args.get('user_id')
    print("userId in count mode",user_id)
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    try:
        count = db.session.query(UserBookAccess).filter_by(user_id=user_id, access_type='read').count()
        return jsonify({'count': count})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.get('/download-csv')
def download_csv():
    t = create_resource_csv.delay()
    return jsonify({"task-id": t.id})


@app.get('/get-csv/<task_id>')
def get_csv(task_id):
    res = AsyncResult(task_id)
    if res.ready():
        filename = res.result
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({"message": "Task Pending"}), 404



@app.route('/test')
@cache.cached(timeout=60)  # Cache this route for 60 seconds
def expensive_operation():
    time.sleep(10)  # Simulate a time-consuming operation
    result = {'message': 'This is a cached response!'}
    return jsonify(result)


if __name__ == "__main__":
    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()

        admin_username = 'admin'
        if not User.query.filter_by(username=admin_username).first(): 
            # Create the admin user if it doesn't exist
            admin_password = 'admin_password'
            hashed_password = generate_password_hash(admin_password, method='pbkdf2:sha256')   
            admin_user = User(username=admin_username, password=hashed_password,role='admin')
            db.session.add(admin_user)
            db.session.commit() 

    app.run(debug=True)
    

