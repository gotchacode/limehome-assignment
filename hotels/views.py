from django.shortcuts import render

import requests
from django.http import Http404
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HotelAPIView(APIView):
    """
    The problem statement clearly says we need to find hotels, so we will just
    hardcode that for simplicity

    The main questions here is if we want just proxy the result or maintain
    the record in the DB itself.

    Merits of maintaingin in DB:
    - same result do not need API call to the location API backend.
    - It also gives faster result, as the result is obtained from the db directly
    rather than going over the wire.

    Disadvantages:
    - We need to obtain the whole dataset for it to be same as the API backend result.
    - There is a minor chance of this data being stale and we need to implement some sort
    of cache invalidation here.

    """
    def get(self, request, format=None):
        url = settings.API_REQUEST_BASE_URL
        app_id = settings.APP_ID
        app_code = settings.APP_CODE
        at = request.query_params.get("at")
        category = "hotel"
        final_url = f"{url}?at={at}&cat={category}&app_id={app_id}&app_code={app_code}"
        response = requests.get(final_url)
        if response.status_code == 200:
            results = response.json()['results']['items']
            return Response(data=results, status=status.HTTP_200_OK)
        return Response(data=[], status=status.HTTP_404_NOT_FOUND)

