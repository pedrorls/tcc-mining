from django.shortcuts import render, redirect
from .forms import TeacherForm

# Create your views here.


def home(request):
    return render(request, "home.html", {"teachers_list": []})


def new_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeacherForm()
    return render(request, "new_teacher.html", {"form": form})

