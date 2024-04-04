from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Book


@require_http_methods(['GET'])
def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'base.html', {'book_list': book_list})
