from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Navya(request):
    return HttpResponse('Navya belongs to second view')