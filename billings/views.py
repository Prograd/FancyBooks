from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, fancy world. You're at the billings index.")
