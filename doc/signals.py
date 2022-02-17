from pathlib import Path
import os
from shutil import copyfile
from .models import Topic, Note

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=Topic)
def createTopic(sender, instance, created, **kwargs):
    if (created):
        topic = instance
        topic.filename = topic.topic.lower().replace(' ', '-')
        topic.save()
        # TODO: create topic dir in template dir
        NOTE_BASE_DIR = Path(__file__).parent
        topic_dir = os.path.join(
            NOTE_BASE_DIR, 'templates/doc/content/' + topic.filename + '/')
        Path(topic_dir).mkdir(parents=True, exist_ok=True)
        # print('Created dirs: {}'.format(topic_dir))
        
        # TODO: create static dir
        topic_dir = os.path.join(
            NOTE_BASE_DIR, 'static/doc/images/' + topic.filename + '/')
        Path(topic_dir).mkdir(parents=True, exist_ok=True)
        # print('Created dirs: {}'.format(topic_dir))


@receiver(pre_delete, sender=Topic)
def deleteTopic(sender, instance, **kwargs):
    # print('deleteTopicDir(): called')
    topic = instance
    # TODO: create topic dir in template dir
    NOTE_BASE_DIR = Path(__file__).parent
    topic_dir = os.path.join(
        NOTE_BASE_DIR, 'templates/doc/content/' + topic.filename + '/')
    try:
        # recursively remove files in dir
        for root, dirs, files in os.walk(topic_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(topic_dir)
        # print('Removed dirs: {}'.format(topic_dir))
    except OSError as e:
        print("Error: %s : %s" % (topic_dir, e.strerror))
        
    # TODO: remove static dir
    topic_dir = os.path.join(
        NOTE_BASE_DIR, 'static/doc/images/' + topic.filename + '/')
    try:
        # recursively remove files in dir
        for root, dirs, files in os.walk(topic_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(topic_dir)
        # print('Removed dirs: {}'.format(topic_dir))
    except OSError as e:
        print("Error: %s : %s" % (topic_dir, e.strerror))


@receiver(post_save, sender=Note)
def createNote(sender, instance, created, **kwargs):
    if (created):
        note = instance
        note.filename = note.title.lower().replace(' ', '-').replace('.', '-')
        note.save()
        
        # TODO: create note dir in template dir
        NOTE_BASE_DIR = Path(__file__).parent
        note_dir = os.path.join(NOTE_BASE_DIR, 'templates/doc/content/' +
                                note.belong_to.filename + '/' + note.filename + '/')
        Path(note_dir).mkdir(parents=True, exist_ok=True)
        # print('Created dirs: {}'.format(note_dir))

        # TODO: create md in md dir
        BASE_DIR = Path(__file__).parent.parent
        md_dir = os.path.join(BASE_DIR, 'md/' +
                              note.belong_to.filename + '/')
        filename = note.filename + '.md'
        if not os.path.exists(md_dir):
            os.makedirs(md_dir)
        dst = os.path.join(md_dir, filename)
        if not os.path.exists(dst): # if not created manually
            src = os.path.join(BASE_DIR, 'md/md-template.md')
            copyfile(src, dst)

        # TODO: update order automatically
        topic = note.belong_to
        order = topic.note_set.all().count()
        note.order = order
        note.save()


@receiver(pre_delete, sender=Note)
def deleteNote(sender, instance, **kwargs):
    # print('deleteNoteDir(): called')
    note = instance
    # TODO: create topic dir in template dir
    NOTE_BASE_DIR = Path(__file__).parent
    note_dir = os.path.join(NOTE_BASE_DIR, 'templates/doc/content/' +
                            note.belong_to.filename + '/' + note.filename + '/')
    try:
        # recursively remove files in dir
        for root, dirs, files in os.walk(note_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(note_dir)
        # print('Removed dirs: {}'.format(note_dir))
    except OSError as e:
        print("Error: %s : %s" % (note_dir, e.strerror))
