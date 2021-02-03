import json
import requests
from django.shortcuts import redirect, render


class AccessException(Exception):
    pass


def access_request(request, url):
    session = requests.session()
    try:
        token = request.COOKIES.get('Authorization', '')
        rest = json.loads(session.get(
            url, headers={'Authorization': token}).text)
        try:
            if rest['Authorization'] is False:
                raise AcessException()
        except:
            for i in rest:
                if list(i.keys()) == ['Authorization']:
                    if list(i.values()) == [False]:
                        raise AcessException()
    except:
        return (False, rest)
    return (True, rest)
