from django.shortcuts import render

import requests
from django.http import Http404
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HotelAPIView(APIView):
    def get(self, request, format=None):
        url = settings.API_REQUEST_BASE_URL
        app_id = settings.APP_ID
        app_code = settings.APP_CODE
        at = request.query_params.get("at")
        cat = request.query_params.get("cat")
        print(request.query_params)
        final_url = f"{url}?at={at}&cat={cat}&app_id={app_id}&app_code={app_code}"
        print(final_url)
        response = requests.get(final_url)
        return Response(data=response.json(), status=status.HTTP_200_OK)

