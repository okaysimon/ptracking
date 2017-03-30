from django.http import HttpResponse
from django.views import generic

from ProjectTracking.models import Requirement


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    model = Requirement
    template_name = 'ProjectTracking/index.html'
