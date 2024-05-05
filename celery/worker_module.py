from celery import Celery

celery = Celery(
    __name__,
    broker='pyamqp://dima:kushchevskyi@localhost:8080//'
)

@celery.task
def generate_report_task():
    print("Hello")


@celery.task(default_retry_delay=5, max_retries=3)
def retry_task():
    print("Trying")
    retry_task.retry()


@celery.on_after_configure.connect
def setup(sender, *args, **kwargs):
    sender.add_periodic_task(15.0, generate_report_task.s()) 
