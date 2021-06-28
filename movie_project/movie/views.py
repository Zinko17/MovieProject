from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from bs4 import BeautifulSoup
from .models import *
from .serializers import *



class MovieView(APIView):

    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        base_movie = 0
        new_movie = 0
        if serializer.is_valid():
            movie_name = serializer.data.get('movie_name')
            for urls in movie_name:
                url = urls
                try:
                   movie = Movie.objects.get(url=url)
                   print(movie)
                   base_movie += 1
                except Movie.DoesNotExist:
                    r = requests.get(url=url)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    name = soup.find('title').string
                    score = soup.find("span", {"itemprop" : "ratingValue"}).string
                    description = soup.find("div",{'class':'summary_text'}).string.strip()
                    photo = soup.find("div",{'class':'ipc-lockup-overlay_screen'})
                    print(name, score, description,)
                    Movie.objects.create(name=name, score=score, description=description, url=url)
                    new_movie += 1


            return Response({base_movie:new_movie})


