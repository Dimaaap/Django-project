from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from books.models import Book


def give_search_query_service(query: callable, field_fo_search: str):
    search_vector = SearchVector(field_fo_search)
    search_query = SearchQuery(query)
    search_rank = SearchRank(search_vector, search_query)
    search_query = Book.objects.annotate(search=search_vector, rank=search_rank). \
        filter(search=query).order_by("-rank")
    return search_query


def validate_query_service(query):
    return len(query) > 5
