from django.shortcuts import render
from shortcuts import RequestType, HttpResponse


from converter.load_logs import process_log


def main_page(request: RequestType) -> HttpResponse:

    logs = process_log()


    return render(request, 'converter/converter.html', {'logs': logs})
