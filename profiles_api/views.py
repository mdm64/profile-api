from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Api view test"""

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_api = [
            "HTTP methods (get, put, post, pastch, delete)",
            "Is similar to django view",
            "gives u the most controll over your api view"
        ]
        return Response({'masg':"Hello", 'an_apiView':an_api})