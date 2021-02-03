import json
import requests
from django.shortcuts import redirect, render
from user.utils import AccessException


def access_request(request, url):
    session = requests.session()
    token = request.COOKIES.get('Authorization', '')
    rest = json.loads(session.get(url, headers={'Authorization': token}).text)
    try:
        if rest.get('detail') is not None:
            return False
    except:
        return (True, rest)
