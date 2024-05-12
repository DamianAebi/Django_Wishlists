from rest_framework.routers import DefaultRouter
from users.views import UserSignupViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'signup', UserSignupViewSet, basename='users-signup')
