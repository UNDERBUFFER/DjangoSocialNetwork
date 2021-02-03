import json
import requests
from django.shortcuts import redirect, render


def auth_request(request, url, data, template):
    session = requests.session()
    try:
        rest = json.loads(session.post(url, data=data).text)
        rest["token"] = 'Token ' + rest["token"]
        rest["url"] = 'http://{host}{url}'.format(
            host=request.get_host(), url=rest["url"])
    except:
        return render(request, template)
    response = redirect(rest['url'])
    response.set_cookie(key='Authorization', value=rest['token'])
    return response
