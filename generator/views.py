from django.shortcuts import render
from django.http import HttpResponse
import secrets
import string
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def id(request):
    length = int(request.GET.get('length', 8))
    lettercase = request.GET.get('case', 'mixed')

    case = {
        'mixed': string.ascii_letters,
        'upper': string.ascii_uppercase,
        'lower': string.ascii_lowercase
    }

    characters = case.get(lettercase, string.ascii_letters)

    numbers = ''
    if request.GET.get('numbers'):
        numbers = string.digits

    generatedid = ''.join(secrets.choice(characters + numbers) for _ in range(length))
    return render(request, 'generator/id.html', {'id': generatedid})

