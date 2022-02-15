from django.shortcuts import render
from .models import Note, Topic
from django.db.models import Q

# Create your views here.

def docHome(request):
    topics = Topic.objects.all()
    
    if (request.method == 'GET'):
        if request.GET.get('q') != None:
            q = request.GET.get('q')
        else:
            q = ''
        notes_found = Note.objects.filter(
            Q(title__icontains=q)
        )
    
    context = {
        'search_notes': notes_found,
        'topics': topics,
        'q': q,
    }
    
    return render(request, 'doc/home.html', context)

def pageView(request, topicName, noteName):
    
    context = {
        
    }
    
    return render(request, 'doc/home.html', context)