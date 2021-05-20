import base64
import json
import requests
from django.http import HttpResponseForbidden, HttpResponseRedirect

OAUTH2_GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
OAUTH2_GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
OAUTH2_GOOGLE_KEY = r'651900659178-6dh7qogkqicf55rp0ald4jirar0loh4d.apps.googleusercontent.com'
OAUTH2_GOOGLE_SECRET = r'8VP07bi1J9Iq8Z5ij4MkQm8Q'
REDIRECT_URI = 'http://fanfics.nn.kiev.ua/oauth2/callback'


def oauth_callback(request):
    if request.method != 'GET':
        return HttpResponseForbidden('Ask with GET')

    if request.GET.get('error'):
        return HttpResponseForbidden('You rejected authorization')

    code = request.GET.get('code')
    if not code:
        return HttpResponseForbidden('No `code` from OAuth provider')

    resp = requests.post(OAUTH2_GOOGLE_TOKEN_URI,
                         data={
                             'code': code,
                             'client_id': OAUTH2_GOOGLE_KEY,
                             'client_secret': OAUTH2_GOOGLE_SECRET,
                             'redirect_uri': REDIRECT_URI,
                             'grant_type': 'authorization_code',
                         })

    if resp.status_code == 200:
        return HttpResponseForbidden('No tokens from OAuth provider')

    decoded = json.loads(resp.content)
    id_token = decoded['id_token']

    jwt_data = json.loads(base64.urlsafe_b64decode(id_token.split('.')[1] + '==='))

    request.session['login_type'] = 'google'
    request.session['login'] = jwt_data['email']
    return HttpResponseRedirect('/')
