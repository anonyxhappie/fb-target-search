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
            if (Interest.objects.filter(user=request.user, interest_id=data.get('id')).exists()):
                    return Response({'error:': 'interest already added'}, status=status.HTTP_403_FORBIDDEN)
            
            interest = Interest.objects.create(
                user=request.user, 
                type=data.get('topic', None), 
                path=data.get('path', None), 
                interest_id=data.get('id'), 
                name=data.get('name', None), 
                audience_size=data.get('audience_size', None))
            interest.save()
            return Response({'success': 'interest added'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error:': 'missing ' + str(e)}, status=status.HTTP_403_FORBIDDEN)
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
            if (Region.objects.filter(user=request.user, region_id=data.get('region_id')).exists()):
                    return Response({'error:': 'region already added'}, status=status.HTTP_403_FORBIDDEN)
            
            region = Region.objects.create(
                user=request.user, 
                key=data.get('key', None), 
                city=data.get('name', None), 
                region_id=data.get('region_id'), 
                region=data.get('region', None), 
                country_code=data.get('country_code', None), 
                country_name=data.get('country_name', None))
            region.save()
            return Response({'success': 'region added'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error:': 'missing ' + str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error:': str(e)}, status=status.HTTP_403_FORBIDDEN)
    
