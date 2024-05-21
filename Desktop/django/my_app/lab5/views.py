from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

people = []
    
class Person():
    def __init__(self, name, password):
        self.name = name
        self.password = password

def index(request):
    return render(request, "lab5/index.html", {
        "users": people
    })

class UserForm(forms.Form):
    name = forms.CharField(
        label="username",
        required=True
        )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="password",
        required=True
        )
    
def add(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            person = Person(name, password)
            people.append(person)

            return HttpResponseRedirect(reverse("lab5:index"))
        
        else:
            return render(request, "lab5/add.html", {
                "form": form
            })
        
    return render(request, "lab5/add.html", {
        "form": UserForm
    })