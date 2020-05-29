from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
from .forms import URLForm
from .base62 import encode
from rest_framework.views import APIView
from .serializers import URLSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def route(request, token):
    long_url = URL.objects.filter(base62_id=token)[0]
    return redirect(long_url.long_url)

# def home(request):
#     return render(request, 'API/home.html')

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

def index(request):
    return HttpResponse("Index of the API")

class URLAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        urls = URL.objects.all()
        serializer = URLSerializer(urls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class URLDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return URL.objects.get(pk=pk)
        except URL.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        url = self.get_object(pk)
        serializer = URLSerializer(url)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        url = self.get_object(pk)
        serializer = URLSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        url = self.get_object(pk)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)