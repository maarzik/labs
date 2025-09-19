from django.shortcuts import render

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def index(request):
    data = {
        "message": "Hello Django на MacBook!",
        "langs": ["Python", "JavaScript", "C#", "Java"],
        "user": Person("Tom", 23),
        "image_url": "https://www.w3schools.com/w3images/fjords.jpg"  # картинка из интернета
    }
    return render(request, "index.html", data)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")