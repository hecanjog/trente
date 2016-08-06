from django.shortcuts import render
import models

def index(request):
    releases = models.Release.objects.all()

    return render(request, 'catalog/catalog.html', {
        'releases': releases,     
    })
