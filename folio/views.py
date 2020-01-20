from django.shortcuts import render
from folio.models import Project

# Create your views here.
def project_shown(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project_shown.html',context)


def project_info(request, pk):
    title = "Portfolio"
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'title':title
    }
    return render(request, 'project_info.html', context)
