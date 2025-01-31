from django.core.exceptions import PermissionDenied


def user_is_artisan(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'artisan':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_customer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'customer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
