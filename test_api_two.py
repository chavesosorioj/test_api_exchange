import pytest
import requests
import json
import function
import http.client
from codecs import encode


def test_post_log_in():
    r = function.get_authenticator()
    data = r.json()
    #  print('Token -> ', data.get("access_token"))
    token = data.get("access_token")
    assert r.status_code == 200
    return token


def test_get_list():
    token = function.get_token()
    #   print('Token -> ', token)
    params = {"search": "api", "status": ["development", "published", "deprecated"], "types": "http-api",
              "masterOrganizationId": "fb9adb70-6649-43e4-8954-59f69b7577b8"}
    h = {"Authorization": "Bearer " + token}
    r = requests.get("https://stgx.anypoint.mulesoft.com/exchange/api/v2/assets", params=params, headers=h)
    data = r.json()
    assert r.status_code == 200
    return data


def test_put_edit():
    token = function.get_token()
    path = "https://stgx.anypoint.mulesoft.com/exchange/api/v2/assets/fb9adb70-6649-43e4-8954-59f69b7577b8/test-10/" \
           "1.0.0/portal/draft/pages/home"
    payload = "Quam nulla porttitor massa id neque aliquam vestibulum morbi blandit. Id faucibus nisl tincidunt eget " \
              "nullam. Scelerisque purus semper eget duis at tellus at. Non diam phasellus vestibulum lorem. Libero" \
              " nunc consequat interdum varius."
    h = {"Content-Type": "text/markdown",
         "Authorization": "Bearer " + token}
    r = requests.put(path, payload, headers=h)
    assert r.status_code == 204


def test_patch_edit():
    token = function.get_token()
    path = "https://stgx.anypoint.mulesoft.com/exchange/api/v1/assets/fb9adb70-6649-43e4-8954-59f69b7577b8/" \
           "test-10/1.0.0"
    h = {"Authorization": "Bearer " + token}
    r = requests.patch(path, headers=h)
    assert r.status_code == 204
