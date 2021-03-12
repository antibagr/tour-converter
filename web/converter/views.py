import io
from typing import List

from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from django.core.files.uploadedfile import InMemoryUploadedFile

from shortcuts import RequestType, HttpResponse


from converter.load_logs import process_log


def upload_tour(request: RequestType) -> HttpResponse:

    if request.method == 'POST' and 'myfile' in request.FILES.keys():

        log_files: List[InMemoryUploadedFile] = request.FILES # ['myfile']

        files = [io.TextIOWrapper(request.FILES[log].file) for log in log_files]

        try:
            logs = process_log(*files)

        except Exception as e:
            messages.warning(request, f"Ошибка конвертера: {e}")

        else:
            return render(request, 'converter/converter.html', {'logs': logs} )


    return render(request, 'converter/upload.html')


def convert_tour(request: RequestType) -> HttpResponse:
    return render(request, 'core/simple_upload.html')
