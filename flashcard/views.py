from django.views.generic import ListView
from .models import Flash

class FlashList(ListView):
    model=Flash
    template_name='flashcard.html'
    context_object_name='flashcards'
