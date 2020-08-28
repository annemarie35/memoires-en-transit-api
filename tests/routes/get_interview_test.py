import os
import requests

from tests.utils import pretty_print_request, pretty_print_response

WGF_API_URL = os.environ.get('WGF_API_URL')
WGF_API_KEY = os.environ.get('WGF_API_KEY')
WGF_API_SIG = os.environ.get('WGF_API_SIG')

url = "{}?api_key={}&api_sig={}&method=paragraph.getAll&format=json&order=post_id&page=1&per_page=100&parent_id=4150842&html_return=true&".format(
    WGF_API_URL,
    WGF_API_KEY,
    WGF_API_SIG
)

def test_renvoie_une_interview_avec_ses_paragraphes():
    # given
    payload = {}
    headers = {
        'Host': "www.wegofunk.com"
    }

    # when
    response = requests.request("GET", url, data=payload, headers=headers)

    # then
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['0']['parent_id'] == "4150842"

    # print full request and response
    pretty_print_request(response.request)
    pretty_print_response(response)
