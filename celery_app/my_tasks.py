# Створимо завдання (Task) 
from celery import Celery

BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = "redis://localhost:6379/1"

celery = Celery("tasks", broker=BROKER_URL, backend=BACKEND_URL)
# В якості аргументів ми вказали:
# з'єднання з брокером BROKER_URL = 'redis://localhost:6379/0', 
# для збереження результатів обчислення задачі BACKEND_URL = 'redis://localhost:6379/1'

# створимо функцію, яку виконуватиме наш віддалений "працівник" (worker):
@celery.task(name="Add two numbers")
def add(x, y):
    return x + y

