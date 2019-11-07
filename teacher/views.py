import operator
from collections import defaultdict
from functools import reduce
from django.shortcuts import render, redirect, render_to_response
from django.db.models import Q, Count

from .forms import TeacherForm
from .models import Professor, Word
from utils.mining_stages import text_processing, remove_accents


def __sort_professors(key, value):
    cmp(value.hits[1])


def home(request):
    search_term = request.GET.get("text")
    if search_term is not None:
        query = reduce(
            operator.__or__,
            (Q(word__iexact=item) for item in remove_accents(search_term.split())),
        )
        words = Word.objects.filter(query).filter(relative_frequency__gt=1)

        data = defaultdict(lambda: {"frequency": 0, "bag_of_words": [], "hits": 0})
        for word in words:
            professor_name = word.professor.name
            data[professor_name]["frequency"] += word.relative_frequency
            data[professor_name]["hits"] += 1
            data[professor_name]["bag_of_words"].append(word.word)

        list_data = []
        for key, value in data.items():
            list_data.append(
                {
                    "name": key,
                    "frequency": value["frequency"],
                    "hits": value["hits"],
                    "bag_of_words": value["bag_of_words"],
                }
            )

        sorted_list_data = sorted(
            list_data, key=operator.itemgetter("frequency"), reverse=True
        )
        sorted_list_data = sorted(
            list_data, key=operator.itemgetter("hits"), reverse=True
        )

        return render(request, "home.html", {"data": sorted_list_data[:10]})
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

