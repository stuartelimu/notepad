from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Note
from .forms import NoteForm

# Create your views here.
def list_view(request):
    notes = Note.objects.filter(user=request.user).order_by('-timestamp')
    context = {
        'notes': notes,
    }

    return render(request, 'index.html', context)

def detail_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'detail.html', context)

def create_view(request):
    
    if request.method == 'POST':
        form = NoteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse('notes:detail', kwargs={'pk': form.instance.id }))
    else:
        form = NoteForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def update_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST or None, request.FILES or None, instance=note)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse('notes:detail', kwargs={'pk': form.instance.id }))
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def delete_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect(reverse('notes:notes'))




