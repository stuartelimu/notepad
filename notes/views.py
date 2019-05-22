from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

# Create your views here.
class NoteList(ListView):
    context_object_name = 'notes'
    template_name = 'index.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-timestamp')


class NoteDetail(DetailView):
    queryset = Note.objects.all()
    context_object_name = 'note'
    template_name = 'detail.html'


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'url', 'image', 'description']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'url', 'image', 'description']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    template_name = 'confirm_delete_note.html'





