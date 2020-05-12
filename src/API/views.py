from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
from .forms import URLForm
from .base62 import encode

def route(request, token):
    long_url = URL.objects.filter(base62_id=token)[0]
    return redirect(long_url.long_url)

def home(request):
    form = URLForm(request.POST)
    b62 = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            qset = URL.objects.all()[::-1][0]
            b62 = encode((qset.id)+1)
            NewUrl.base62_id = b62
            NewUrl.save()
        else:
            form = URLForm()
            b62= "Invalid URL"

    return render(request, 'API/home.html', {'form': form, 'b62': b62})