from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import *

class RegisterView(viewsets.generics.CreateAPIView):
    
    """
    * `api/v1/register/` -- for creating new user.
    """
    
    permission_classes = (AllowAny,)
    
    def create(self, request):
        data = request.data
        try:
            if User.objects.filter(username=data['username'], email=data['email']).exists():
                return Response({'error': 'user already exist'}, status=status.HTTP_403_FORBIDDEN)
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
            user.save()
            return Response({'success': 'user created'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'key-error:': 'missing ' + str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error:': str(e)}, status=status.HTTP_403_FORBIDDEN)

class InterestViewSet(viewsets.ModelViewSet):

    """
    * `api/v1/interests/` -- for listing interests below to the authenticated user.
    """

    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def list(self, request):
        queryset = Interest.objects.filter(user=request.user).order_by('-updated_at')
        serializer = InterestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        try:
            interest, _ = Interest.objects.update_or_create(user=request.user, path=data['path'], interest_id=data['id'], name=data['name'], audience_size=data['audience_size'])
            interest.save()
            return Response({'success': 'interest added'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'key-error:': 'missing ' + str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error:': str(e)}, status=status.HTTP_403_FORBIDDEN)
    
class RegionViewSet(viewsets.ModelViewSet):

    """
    * `api/v1/regions/` -- for listing regions below to the authenticated user.
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
    def list(self, request):
        queryset = Region.objects.filter(user=request.user).order_by('-updated_at')
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        try:
            region, _ = Region.objects.update_or_create(user=request.user, key=data['key'], city=data['name'], region_id=data['region_id'], region=data['region'], country_code=data['country_code'], country_name=data['country_name'])
            region.save()
            return Response({'success': 'region added'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'key-error:': 'missing ' + str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error:': str(e)}, status=status.HTTP_403_FORBIDDEN)
    
