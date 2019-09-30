from django.shortcuts import render


def freeform(request):
    return render(request, "freefbaform/freefbaform.html")
