from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
        busstations = []
        for row in DictReader(f):
            busstations.append(row)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(busstations, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': paginator,
            'page': page,
        }
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    return render(request, 'stations/index.html', context)