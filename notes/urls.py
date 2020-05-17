from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteList.as_view(), name='notes'),
    path('create/', views.NoteCreate.as_view(), name='create'),
    path('notes/<slug:slug>/', views.NoteDetail.as_view(), name='detail'),
    path('notes/<slug:slug>/update/', views.NoteUpdate.as_view(), name='update'),
    path('notes/<slug:slug>/delete/', views.NoteDelete.as_view(), name='delete'),
]