from django.shortcuts import render
from django.views.generic import View,ListView
from App.models import *
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'App/Home.html')

class School_List(ListView):
    model=School
    context_object_name='schools'
    #ordering=['name']