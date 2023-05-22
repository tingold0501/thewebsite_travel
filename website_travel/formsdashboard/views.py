from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SlideForm 




def create_slide(request):
    form = SlideForm()
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            slide = form.save(commit=False)

            # Kiểm tra xem có tệp hình ảnh được gửi lên hay không
            if 'images' in request.FILES:
                image_file = request.FILES['images']
                slide.image.save(image_file.name, image_file)

            slide.save()
            return redirect('formsdashboard') 

    return render(request, 'indexFormsDashboard.html', {'form': form})




    