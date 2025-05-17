from django.shortcuts import render
from .models import Photo
from django.utils import timezone
from .forms import PhotoForm
from django.shortcuts import redirect

def home(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/home.html', {
        'photos':photos,
        'now' : timezone.now(),
    })

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PhotoForm()
    return render(request, 'gallery/upload_photo.html', {'form': form})
