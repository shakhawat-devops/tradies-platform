from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MiddlewareUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Check if the middleware has already set the user data
        if not hasattr(request, '_user') or request._user is None:
            return None  # No user data from the middleware, move to the next authentication class

        user_data = request._user
        if not user_data:
            raise AuthenticationFailed("User data not available")

        request.user = user_data

        # Use the user_data that was set by the middleware
        return (user_data, None)  # Return user_data and None for authentication backend
