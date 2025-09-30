from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    return render(request, 'hello/index.html')

def postuser(request):
    name = request.POST.get('name', 'Undefined')
    age = request.POST.get('age', 0)
    return HttpResponse(f"<h2>Name: {name} | Age: {age}</h2>")

def form_index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            age = userform.cleaned_data['age']
            return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
    return render(request, 'hello/form_index.html', {'form': userform})