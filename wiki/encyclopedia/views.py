from django.shortcuts import render, redirect
from . import util
import random
from markdown2 import markdown

# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown(content)
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": None
    })

def search(request):
    q = request.GET.get("q", "").strip()
    entries = util.list_entries()
    for entry in entries:
        if entry.lower() == q.lower():
            return redirect("encyclopedia:entry", title=entry)
    results = [entry for entry in entries if q.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": q
    })

def create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.entry_exists(title):
            return render(request, "encyclopedia/create.html", {
                "error": True,
                "title": title,
                "content": content
            })
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    return render(request, "encyclopedia/create.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def random_page(request):
    entries = util.list_entries()
    return redirect("encyclopedia:entry", title=random.choice(entries))