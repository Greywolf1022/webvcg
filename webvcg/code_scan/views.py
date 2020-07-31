from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import json
from .forms import FileUploadForm


# Create your views here.


def _handle_uploaded_file(file):
    """Deal with file upload
    """
    # Write the file to media folder
    destination = open(os.path.join(settings.BASE_DIR, 'media/{}'.format(file.name)), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()


def index(request):
    if request.method == 'POST':
        files = request.FILES.getlist('scan_files')
        for file in files:
            _handle_uploaded_file(file)
        return HttpResponse(json.dumps({'task_id': 'Have done :)'}), content_type='application/json')
    return render(request, 'code_scan/index.html')

