from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service
from .serializers import ServiceSerializer


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Service.objects.all()
        checked_data = ServiceSerializer(queryset, many=True)
        return Response(checked_data.data)

    def post(self, request, *args, **kwargs):
        checked_data = ServiceSerializer(data=request.data)

        if checked_data.is_valid():
            checked_data.save()
            return Resonse(checked_data.data)
        return Response(checked_data.errors)#returns error if posted data is invalid
