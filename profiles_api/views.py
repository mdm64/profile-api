from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
# from serializers import HelloSerializer
from rest_framework import status


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