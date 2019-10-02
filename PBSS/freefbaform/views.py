from django.shortcuts import render


def freefbaform(request):
    return render(request, "freefbaform/freefbaform.html")
