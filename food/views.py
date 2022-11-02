from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'hello.html', {'name' : 'Teddy'})

def item(request):
    return HttpResponse('This will become an item view')