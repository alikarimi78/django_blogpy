from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class MapPage(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'map/map_html.html', context={})