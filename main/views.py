from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .forms import ShortURLForm
from .utils import generate_short_code

# Create your views here.

def home_url(request):
    form = ShortURLForm()
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.short_code = generate_short_code()
            obj.save()
            return redirect('show_url', id=obj.id)
        
    return render(request, 'urlform.html', {'form':form})


def show_url(request, id):
    obj = get_object_or_404(ShortURL, id=id)
    short_url = request.build_absolute_uri(f"/{obj.short_code}")
    return render(request, 'showurl.html', {'short_url':short_url, 'date':obj.created_at})


def redirect_to_original(request, short_code):
    obj = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(obj.original_url)
