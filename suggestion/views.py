from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Suggestions
from .utils import create_excel


def create_suggestions(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'create_suggestions.html')
    elif request.method == "POST":
        title = str(request.POST.get('title')).strip()
        if len(title) <= 1:
            raise Exception('Too short title')

        description = str(request.POST.get('description'))
        Suggestions.objects.create(
            author=request.user.username,
            title=title,
            description=description
        )

        return redirect(reverse('home'))
    else:
        raise Exception('Method is not allowed')


def home(request: HttpRequest) -> HttpResponse:
    # suggestions_obj = Suggestions.objects.all()
    suggestions_obj = Suggestions.objects.raw("""SELECT * FROM suggestion_suggestions""")
    return render(request, 'list.html', {'list': suggestions_obj})


def extract_data(request: HttpRequest) -> HttpResponse:
    suggestions_obj = Suggestions.objects.all()
    data = create_excel(suggestions_obj)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )

    response['Content-Disposition'] = 'attachment; filename={date}-suggestions.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    data.save(response)
    return response
