from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from App.models import *
from django.urls import reverse_lazy
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'App/Home.html')

class School_List(ListView):
    model=School
    context_object_name='schools'
    #ordering=['name']

class School_Detail(DetailView):
    model=School
    context_object_name='school'

class School_Create(CreateView):
    model=School
    fields='__all__'

class School_Update(UpdateView):
    model=School
    fields='__all__'

class School_Delete(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('School_List')