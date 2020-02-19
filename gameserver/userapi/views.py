from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PlayerSerializer
from .models import Player
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST)
from django.utils.translation import ugettext_lazy as _


class HelloView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': _('Hello world!')}
        return Response(content)


class PlayerViewSet(APIView):
    serializer_class = PlayerSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(()):
            Player.objects.create_user(**serializer.validated_data)
            return Response(Response({'message': _('User created!')}, status=HTTP_201_CREATED))

        return Response({
            'status': _('Bad request'),
            'message': serializer.errors
        }, status=HTTP_400_BAD_REQUEST)
