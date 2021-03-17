import io
import logging
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
                team_size, logs = process_single_log_file(*files)

            else:
                team_size, logs = process_multiple_files(*files)

        except Exception as e:

            logging.exception(e, exc_info=True)

            # If converter inject error_line attribute in Exception
            # then it was raised during iteration through the file
            if hasattr(e, 'error_line'):
                err_msg = f"Ошибка в файле {e.filename} на строке {e.error_line}: {e}"
            else:
                err_msg = f"Ошибка при обработке файла: {e}"

            messages.warning(request, err_msg)

        else:
            return render(request, 'converter/converter.html', {'logs': logs, 'team_size': team_size})

    return render(request, 'converter/upload.html')


def convert_tour(request: RequestType) -> HttpResponse:
    return render(request, 'core/simple_upload.html')
