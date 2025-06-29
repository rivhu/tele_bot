from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class PublicView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "Public endpoint accessible!"})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, you are authenticated!"})
