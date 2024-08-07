from django.shortcuts import render

# Create your views here.
# views.py

from django.http import JsonResponse
from celeryapp.tasks import add

def add_view(request):
    result = add.delay(10, 21)
    return JsonResponse({'task_id': result.id})
