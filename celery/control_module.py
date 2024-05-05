import datetime

from worker_module import generate_report_task, retry_task

if __name__ == "__main__":
    # generate_report_task.apply_async()
    # generate_report_task.delay()

    publish_after = 10
    generate_report_task.apply_async(countdown=publish_after)

    # retry_task.delay()
