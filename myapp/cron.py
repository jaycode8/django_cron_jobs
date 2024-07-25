from .models import Jaymoh
import random

def my_scheduled_job():
    num = random.randint(0, 100)
    Jaymoh.objects.create(name=num)

