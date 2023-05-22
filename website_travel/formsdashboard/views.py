from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SlideForm



def create_slide(request):
    form = SlideForm()
    if request.method == 'POST':
        form = SlideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formsdashboard')  # Thay 'home' bằng tên URL pattern của trang chủ

    return render(request, 'indexFormsDashboard.html', {'form': form})

    