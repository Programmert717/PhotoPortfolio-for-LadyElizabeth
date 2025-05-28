from django.shortcuts import render
from .models import Photo
from django.utils import timezone
from .forms import PhotoForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {
        'photos': photos,
        'now': timezone.now(),
    })

@login_required
def upload_photo(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("У вас нет прав)")

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()

    return render(request, 'gallery/upload_photo.html', {'form': form})

@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        photo.delete()
        return redirect('home')
    return render(request, 'gallery/delete_photo.html', {'photo': photo})
