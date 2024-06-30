from rest_framework import viewsets
from .permissions import IsUserOwnerOrGetAndPostOnly
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Register,Login
from .Serializers import RegisterSerializers,LoginSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsUserOwnerOrGetAndPostOnly]
    queryset=Login.objects.all()
    serializer_class=LoginSerializer



    # views.py


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Create a User instance
            user = Login.objects.create_user(
                username=serializer.validated_data['name'],
                email=serializer.validated_data['emaill'],
                password=serializer.validated_data['Password']
            )

            # Create a Profile instance linked to the User
            profile = Login.objects.create(
                user=user
                # You can handle 'image' field from serializer if needed
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


