from rest_framework.permissions import AllowAny
from rest_framework.viewsets import mixins, GenericViewSet
from users.serializers import UserSignupSerializer


class UserSignupViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    Register a user. Mixin must always be used with GenericViewSet
    """
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]
