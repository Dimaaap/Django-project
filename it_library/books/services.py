from django.core.paginator import Paginator

from .filters import ValuesFilter


def get_objects_from_model_by_filter_service(model, field, value):
    filter_fields = ValuesFilter()
    return model.objects.get(**filter_fields(field, value))


def get_all_objects_from_db_service(model: callable):
    return model.objects.all()


def filter_objects_from_db_service(model: callable, field: str, value: callable):
    filter_fields = ValuesFilter()
    return model.objects.filter(**filter_fields(field, value))


def annotate_models_service(model: callable, function_to_annotate: callable, field: str):
    return model.objects.annotate(function_to_annotate(field))


def get_pagination_service(request, data_to_pagination, size_of_pagination):
    paginator = Paginator(data_to_pagination, size_of_pagination)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


# DELETED
def temp_operations(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b


