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
    topic = Topic.objects.get(filename=topicName)
    note = Note.objects.get(belong_to=topic, filename=noteName)
    
    # find pre and next in db
    try:
        pre = Note.objects.get(order=note.order-1, belong_to=note.belong_to)
    except:
        pre = None
    try:
        next = Note.objects.get(order=note.order+1, belong_to=note.belong_to)
    except:
        next = None
        
    context = {
        'topic': topic,
        'cur': note,
        'pre': pre,
        'next': next,
        'contentURL': 'doc/content/' + topic.filename + '/' + note.filename + '/' + note.filename + '.html',
        'tableURL': 'doc/content/' + topic.filename + '/' + note.filename + '/' + note.filename + '-table.html',
    }

    return render(request, 'doc/page.html', context)

