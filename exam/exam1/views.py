from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

def index(request):
    return render(request, "exam1/index.html", {
    })
    
def part3(request):
    return render(request, "exam1/part3.html", {
    })
    
def part1(request):
    return render(request, "exam1/part1.html", {
    })
    
def part4(request):
    return render(request, "exam1/part4.html", {
    })