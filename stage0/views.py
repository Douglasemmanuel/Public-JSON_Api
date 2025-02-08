# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class InfoAPIView(APIView):
    def get(self, request):
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response_data = {
            'email': 'emmanueldouglas2121@gmail.com',
            'current_datetime': current_datetime,
            'github_link': 'https://github.com/Douglasemmanuel/Public-JSON_Api',
            'hng_hirepage':'https://hng.tech/hire/python-developers'
        }
        return Response(response_data, status=status.HTTP_200_OK)
