from celery import Celery, Task
from flask import current_app as app
def celery_init_app():
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery()
    celery_app.config_from_object("celeryconfig")
    # celery_app.set_default()
    # app.extensions["celery"] = celery_app
    return celery_app

celery_app = celery_init_app()