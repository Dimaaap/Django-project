from django.shortcuts import render

from .services import *


# def search_page_view(request):
#    query = request.GET.get("q")
#    search_query = give_search_query_service(query, 'chunk_title')
#    context = {'search_query': search_query, 'query': query}
#    return render(request, 'search/search_page.html', context=context)


def show_all_find_books(request):
    query = request.GET.get("q")
    search_query = give_search_query_service(query, 'chunk_title')
    context = {'entry_list': search_query}
    return render(request, 'search/search_page.html', context=context)
