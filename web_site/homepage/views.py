from django.shortcuts import render


def homepage(request):
    template_dir = "homepage/homepage.html"
    return render(request, template_dir)
