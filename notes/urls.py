from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('notes/', views.list_view, name='notes'),
    path('notes/<int:pk>/', views.detail_view, name='detail'),
    path('notes/create/', views.create_view, name='create'),
    path('notes/<int:pk>/update/', views.update_view, name='update'),
    path('notes/<int:pk>/delete/', views.delete_view, name='delete'),
]