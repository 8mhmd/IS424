from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

def index(request):
    return render(request, "exam1/index.html", {
    })