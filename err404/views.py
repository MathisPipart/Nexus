from django.shortcuts import render

def err404(request):
    return render(request, 'err404.html')
