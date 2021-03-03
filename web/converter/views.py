import io

from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.core.files.uploadedfile import InMemoryUploadedFile

from shortcuts import RequestType, HttpResponse


from converter.load_logs import process_log


def upload_tour(request: RequestType) -> HttpResponse:

    if request.method == 'POST' and 'myfile' in request.FILES.keys():

        log_file: InMemoryUploadedFile = request.FILES['myfile']

        file = io.TextIOWrapper(log_file.file)

        try:
            logs = process_log(file)

            print(logs)

        except Exception as e:
            messages.warning(request, f"Ошибка конвертера: {e}")

        else:
            return render(request, 'converter/converter.html', {'logs': logs} )


    return render(request, 'converter/upload.html')


def convert_tour(request: RequestType) -> HttpResponse:
    return render(request, 'core/simple_upload.html')
