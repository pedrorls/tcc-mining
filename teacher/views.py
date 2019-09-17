import operator
from functools import reduce
from django.shortcuts import render, redirect, render_to_response
from django.db.models import Q

from .forms import TeacherForm
from .models import Professor, Word
from utils.mining_stages import text_processing


def home(request):
    search_term = request.GET.get("text")
    if search_term != "":
        query = reduce(
            operator.__or__, (Q(word__iexact=item) for item in search_term.split())
        )
        words = Word.objects.filter(query).filter(relative_frequency__gt=1)
        return render(request, "home.html", {"words": words})
    return render(request, "home.html", {})


def new_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            professor_name = form.cleaned_data["name"]
            filename = form.cleaned_data["curriculum"].name
            form.save()
            teacher = Professor.objects.get(name=professor_name)
            keys = text_processing(filename)
            words_obj_lst = [
                Word(
                    professor=teacher,
                    word=key["word"],
                    frequency=key["frequency"],
                    relative_frequency=key["relative_frequency"],
                )
                for key in keys
            ]
            Word.objects.bulk_create(words_obj_lst)
            return redirect("home")
    else:
        form = TeacherForm()
    return render(request, "new_teacher.html", {"form": form})

