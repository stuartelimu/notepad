from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='delete'),
]