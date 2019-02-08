# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery import task


# We can have either registered task
@task(name='summary')
def send_import_summary():
    # Magic happens here ...
    # or
    print('Something Something')


@shared_task
def send_notifiction():
    print('Here I\'m')
    # Another trick


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
