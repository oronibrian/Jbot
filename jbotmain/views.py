from django.shortcuts import render
from django.views import generic
# Create your views here.

class Jbotview(generic.View):

    def get(self, request, *args, **kwargs):
            return HttpResponse("Hello World!")