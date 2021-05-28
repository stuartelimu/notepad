from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse
from django.urls.base import resolve
from notes.views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete


class TestUrls(SimpleTestCase):

    def test_note_list_url_resolves_correct_view(self):
        url = reverse('notes:notes')
        view = resolve(url).func.view_class
        self.assertEquals(view, NoteList)

    def test_note_detail_url_resolves_correct_view(self):
        url = reverse('notes:detail', args=['test'])
        view = resolve(url).func.view_class
        self.assertEquals(view, NoteDetail)

    def test_note_create_url_resolves_correct_view(self):
        url = reverse('notes:create')
        view = resolve(url).func.view_class
        self.assertEquals(view, NoteCreate)

    def test_note_update_url_resolves_correct_view(self):
        url = reverse('notes:update', args=['test'])
        view = resolve(url).func.view_class
        self.assertEquals(view, NoteUpdate)

    def test_note_delete_url_resolves_correct_view(self):
        url = reverse('notes:delete', args=['test'])
        view = resolve(url).func.view_class
        self.assertEquals(view, NoteDelete)