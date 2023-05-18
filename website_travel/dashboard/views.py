from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'index.html')

def charts(request):
    return render(request, 'charts-chartjs.html')

def profile(request):
    return render(request, 'pages-profile.html')