from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



class HelloApiView(APIView):
    """Api view test"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_api = [
            "HTTP methods (get, put, post, pastch, delete)",
            "Is similar to django view",
            "gives u the most controll over your api view"
        ]
        return Response({'masg':"Hello", 'an_apiView':an_api})
    
    def post(self, request):
        """create hello msg with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f"Hello {name}"
            return Response({'msg': msg})
        
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        return Response({"msg":"put"})
    
    def patch(self, request, pk=None):
        return Response({"msg":"patch"})
    
    def delete(self, request, pk=None):
        return Response({"msg":"delete"})
    

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewser"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello msg"""
        a_viewset = [
            "User actions (list, create, retrieve, update, partial_update)",
            "automatically map to the URLs using router",
            "provide more functionality with less code"
        ]
        return Response({'masg':"Hello", 'a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello {name}'
            return Response({"msg": msg})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):
        return Response({"http_method": "PUT"})
    
    def partial_update(self, request, pk=None):
        return Response({"http_method": "PATCH"})
    
    def destroy(self, request, pk=None):
        return Response({"http_method": "DELETE"})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly # make sure the user is authenticated for update
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
        
    