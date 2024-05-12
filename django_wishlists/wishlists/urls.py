from rest_framework.routers import DefaultRouter
from users.views import UserSignupViewSet
from wishlists.views import ItemViewSet, WishlistViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'items', ItemViewSet, basename='items')
router.register(r'wishlists', WishlistViewSet, basename='wishlists')
