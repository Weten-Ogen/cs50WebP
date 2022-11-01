from django.shortcuts import render

tasks = ['learning', 'cooking', 'fishing', 'cooking']
# Create your views here.
def index(request):
    return render(request, 'task/index.html',{
        'tasks': tasks
    })

def add(request):
    return render(request, 'task/add.html')