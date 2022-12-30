from django.views.generic import ListView, DetailView
from .models import Flash

class FlashList(ListView):
    model=Flash
    template_name='flashcard.html'
    context_object_name='flashcards'
    ordering=['-created_at']

class FlashTest(DetailView):
    model=Flash
    template_name='flashtest.html'
    context_object_name='flashcard'
