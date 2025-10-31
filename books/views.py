from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


books = [
    {
        'id': 1,
        'name': 'O\'tgan kunlar',
        'author': 'Abudlla Qodiriy'
    },
    {
        'id': 2,
        'name': 'Hamsa',
        'author': 'Alisher Navoiy'
    },
]

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')

def books_view(request: HttpRequest) -> HttpResponse:
    context = {
        'books': books,
    }
    return render(request=request, template_name='books.html', context=context)

def book_detail_view(request: HttpRequest, book_id: int) -> HttpResponse:
    for book in books:
        if book['id'] == book_id:
            context = {
                'book': book
            }
            return render(request=request, template_name='book_detail.html', context=context)
        
    return render(request=request, template_name='book.html')

