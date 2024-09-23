from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Class_views(TemplateView):
    template_name = 'class_template.html'

def func_views(request):
    return render(request, 'func_template.html')
