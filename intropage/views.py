from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'intropage/main.html')

def audio(request):
    return render(request, 'index.html')