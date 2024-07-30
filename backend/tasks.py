from celery import shared_task
from model import Book
import flask_excel as excel

@shared_task(ignore_result=False)
def create_resource_csv():
    stud_res = Book.query.with_entities(
        Book.name, Book.author , ).all()

    csv_output = excel.make_response_from_query_sets(
        stud_res, ["Name", "Author"], "csv")
    filename = "test.csv"

    with open(filename, 'wb') as f:
        f.write(csv_output.data)
