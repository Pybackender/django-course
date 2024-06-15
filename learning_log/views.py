from django.shortcuts import  HttpResponse

# Create your views here.


def topicview(request):
    return HttpResponse("Hello, world. You're at the polls index.")