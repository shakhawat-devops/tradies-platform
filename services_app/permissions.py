from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        print(f"Service provider: {obj.service_provider}, Request user ID: {request.user.id}")
        # # Write permissions are only allowed to the owner of the snippet.
        return int(obj.service_provider) == int(request.user.id)
        # return True
    

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.service_provider == request.user.id
    

