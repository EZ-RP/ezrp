from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse("Main menu to go here")
