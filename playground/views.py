from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def calculate():
    x = 1
    y = 2
    return x


#first view function
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name' : 'Teddy'})
    #return HttpResponse('Hello World')
    #after created, map to a URL

