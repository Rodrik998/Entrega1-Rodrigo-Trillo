from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def user_is_admin(     #? Decorator para verificar si un usuario es administrador
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator