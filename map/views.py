from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
import os
from . import geoserver_rest


def map_page(request):
    return render(request, 'map/map_html.html', context={})


def upload_tiff(request):
    if request.method == 'POST' and request.FILES.get('tiff_file'):
        tiff_file = request.FILES['tiff_file']
        file_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_tiffs', tiff_file.name)

        with open(file_path, 'wb') as destination:
            for chunk in tiff_file.chunks():
                destination.write(chunk)

        geoserver_rest.tiff_to_geoserver()
        return redirect('OSM_page')

    return render(request, 'map/upload_tiff.html', context={})
