from django.shortcuts import render

# Create your functions.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})