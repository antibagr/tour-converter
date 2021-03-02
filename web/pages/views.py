import asyncio

from datetime import datetime

from django.http import HttpResponse
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from shortcuts import RequestType


def main_page(request: RequestType):

    # await asyncio.sleep(0.1)
    return render(request, 'pages/landing.html')

@login_required
def home(request: RequestType):

    return render(request, 'pages/home.html')


def about(request: RequestType):
    return render(request, 'pages/about.html')


def not_found(request: RequestType):
    # return HttpResponse("<h1>Not found</h1>")
    # assuming home has an urlconf name of 'home'
    return redirect('pages-home')


def change_password(request: RequestType):
    return redirect('account-change-password')
