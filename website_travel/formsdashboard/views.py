from django.shortcuts import render

# Create your views here.
def formsdashboard(request):
    return render (request, 'indexFormsDashboard.html')