from django.shortcuts import render

# Create your views here.from django.shortcuts import render  
from .models import Project  

def portfolio_view(request):  
    projects = Project.objects.all()  
    context = {'projects': projects}  
    return render(request, 'portfolio/index.html', context)