from .oauth import GOOGLE_URL


def get_login_context(request, base_context: dict = None):
    auth_context = {
        'logged_in': request.user.is_authenticated,
        'username': request.user.username,
        'google_url': GOOGLE_URL}
    if base_context:
        context = base_context
        base_context.update(auth_context)
        return context
    return auth_context
