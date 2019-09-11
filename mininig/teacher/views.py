from django.shortcuts import render, redirect
from .forms import TeacherForm

# Create your views here.


def home(request):
    return render(request, "home.html", {"teachers_list": []})


def upload_curriculum(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeacherForm()
    return render(request, "upload_curriculum.html", {"form": form})

