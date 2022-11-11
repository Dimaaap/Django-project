from django.shortcuts import render, HttpResponse


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def about_page_view(request):
    context = {'title': 'Про нас'}
    return render(request, 'index_page/about_page.html', context)
