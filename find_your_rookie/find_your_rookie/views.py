from django.shortcuts import render, redirect
from django.urls import reverse
# from . import models

def index(request):
    return render(request, 'index.html')

# def option(request):
#     if request.POST:
#         number = int(request.POST['goals'])
#         models.Option.objects.create(list=number)
#         # return redirect(reverse('find_your_rookie:index'))
#     return render(request, 'index.html')