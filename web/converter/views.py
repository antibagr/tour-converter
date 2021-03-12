import io
from typing import List

from django.conf import settings
from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from shortcuts import HttpResponse, RequestType

from converter.load_logs import process_single_log_file, process_multiple_files


def upload_tour(request: RequestType) -> HttpResponse:

    if request.method == 'POST' and 'myfile' in request.FILES.keys():

        log_files: List[InMemoryUploadedFile] = request.FILES

        files = [io.TextIOWrapper(log) for log in log_files.getlist('myfile')]

        try:
            if len(files) == 1:
                logs = process_single_log_file(*files)
            else:
                logs = process_multiple_files(*files)

        except Exception as e:
            messages.warning(request, f"Ошибка конвертера: {e}")

        else:
            return render(request, 'converter/converter.html', {'logs': logs})

    return render(request, 'converter/upload.html')


def convert_tour(request: RequestType) -> HttpResponse:
    return render(request, 'core/simple_upload.html')
