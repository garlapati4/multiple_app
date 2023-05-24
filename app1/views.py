from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse('<marquee><h1>This is app1_string</h1></marquee>')

def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')

    return HttpResponse('This is app2_string')
    
