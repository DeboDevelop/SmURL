from django.shortcuts import render, redirect
from .models import URL
from .base62 import decode
from rest_framework.views import APIView
from .serializers import URLSerializer
from rest_framework.response import Response
from rest_framework import status
import requests

def route(request, token):
    """Gets the token, fetch the long url from table and redirect to it or render the notFound.html if it doesn't exist.

    Args:
        token (str): The token used to represent the longurl in database
    """

    num = decode(token)
    url = 'http://127.0.0.1:8000/api/urls/' + str(num)
    resp = requests.get(url=url)
    if resp.status_code == 200:
        data = resp.json()
        return redirect(data["long_url"])
    else:
        return render(request, 'API/notFound.html')

def home(request):
    """
    Renders the Home page.
    """
    return render(request, 'API/home.html')

def index(request):
    """
    Renders the notfound page if comebody try to opne the index of api.
    """
    return render(request, 'API/notFound.html')

class URLAPIView(APIView):
    """
    Define the Get All and Post Route for the API.
    """
    def get(self, request):
        """
        Fetch all the data in found in the table and return it as Response.
        """
        urls = URL.objects.all()
        serializer = URLSerializer(urls, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post the data received the the user.
        """
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class URLDetail(APIView):
    """
    Define the get one, update and delete route for the API.
    """
    def get_object(self, pk):
        """
        Finds the object using primary key.

        Args:
            pk (Number): The primary key of the data we are trying to find.
        """
        try:
            return URL.objects.get(pk=pk)
        except URL.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Returns the JSON of the data fetched using primary key.

        Args:
            pk (Number): The primary key of the data we are trying to find.
        """
        url = self.get_object(pk)
        serializer = URLSerializer(url)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update the data found using primary key.

        Args:
            pk (Number): The primary key of the data we are trying to find.
        """
        url = self.get_object(pk)
        serializer = URLSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete the data found using primary key.
        
        Args:
            pk (Number): The primary key of the data we are trying to find.
        """
        url = self.get_object(pk)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)