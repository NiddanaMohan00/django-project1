from django.shortcuts import render
from app1.models import Book
# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class BookListView(ListView):
    model=Book

class BookListView2(ListView):
    model=Book
    template_name='app1/books.html'
    context_object_name='books'
    
class BookDetailView(DetailView):
    model =Book
class BookCreateView(CreateView):
    model= Book
    fields='__all__'

class BookUpdateView(UpdateView):
    model=Book
    fields=('pages','price')
from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('list')
        
    
    
    

