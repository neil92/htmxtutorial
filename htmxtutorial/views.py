from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, "basic/index.html")

def snippet(request):
    return render(request, "basic/snippet.html")