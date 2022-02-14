from django.shortcuts import HttpResponse


def index(id):
    return HttpResponse(f"{id}")