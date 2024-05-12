from rest_framework import permissions


class IsObjectOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    # This message will be returned if the permission is not granted
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user is the owner of the object.
        :param request: The request object
        :param view: The view object
        :param obj: The object to be checked
        :return: True if the requesting user is the owner of the object, False otherwise
        """
        return obj.user == request.user
