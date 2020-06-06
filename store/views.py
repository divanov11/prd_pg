from django.shortcuts import render
from .models import *


def home_pg(request):
    prdct = product.objects.all()
    context = {'prdcts':prdct}
    return render(request, 'index.html', context)
