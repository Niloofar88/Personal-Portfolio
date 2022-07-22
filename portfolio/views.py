from django.shortcuts import render
from .models import Project

# this line of code grabes everything out of the database turns them into python objects and then put them inside of a list.
def home(request):
   projects = Project.objects.all()
   return render(request, 'portfolio/home.html', {'projects':projects})
