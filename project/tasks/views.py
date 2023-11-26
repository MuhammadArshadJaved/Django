from django.shortcuts import render

# Create your views here.

task=['foo','baz','buz']

def index(request):
    return render(request, 'tasks/index.html',{
        'tasks': task
    })

