from django.urls import path
from . import views

urlpatterns = [
    path('', views.docHome, name="docHome"),
    path('<str:topicName>/<str:noteName>', views.pageView, name='page'),
]
