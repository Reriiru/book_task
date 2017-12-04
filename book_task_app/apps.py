from django.apps import AppConfig


class BookTaskAppConfig(AppConfig):
    name = 'book_task_app'
    
    def ready(self):
        import book_task_app.signals
