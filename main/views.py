from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def record(request):
    return render(request, 'main/record.html')

def identify(request):
    return render(request, 'main/identify.html')