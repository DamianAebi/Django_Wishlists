from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from wishlists.models import Item, Wishlist
from wishlists.permissions import IsObjectOwner
from wishlists.serializers import ItemSerializer, WishlistSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed, created or edited.
    """
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()

    def get_permissions(self):
        """
        Sets the permissions for the ViewSet. By default, only authenticated users can access the ViewSet.
        If it's not a GET request, the user must be the owner of the object.
        :return: list of permissions
        """
        permission_classes = [IsAuthenticated()]
        if self.action not in ['retrieve']:
            permission_classes.append(IsObjectOwner())
        return permission_classes


class WishlistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wishlists to be viewed, created or edited.
    """
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()

    def get_queryset(self):
        """
        Only the wishlists of the requesting user are available.
        :return: QuerySet
        """
        return Wishlist.objects.filter(user=self.request.user)
