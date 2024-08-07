# yourapp/tasks.py

from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def add(x, y):
    logger.info(f'Adding {x} and {y}')
    return x + y
