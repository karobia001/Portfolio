from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects_shown(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project_shown.html',context)


