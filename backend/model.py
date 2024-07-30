# models.py

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(256), nullable=False)

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    books = db.relationship('Book', backref='section', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    poster = db.Column(db.String(200))  # Assuming poster link will be stored as string
    price = db.Column(db.Float)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

class UserBookAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    access_type = db.Column(db.String(50), nullable=False)  # Define the type of access (e.g., read, write, etc.)
    days = db.Column(db.Integer, nullable=False)  # Number of days the access is granted for
    book_name = db.Column(db.String(100))  # Add column for book name
    user_name = db.Column(db.String(80))   # Add column for user name
    request_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('book_access', cascade='all, delete-orphan'))
    book = db.relationship('Book', backref=db.backref('user_access', cascade='all, delete-orphan'))
