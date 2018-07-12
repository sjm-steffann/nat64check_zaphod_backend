from concurrent.futures import ThreadPoolExecutor

import requests
from django.utils import timezone
from requests.auth import AuthBase
from requests_futures.sessions import FuturesSession
from uwsgi_tasks import timer

from instances.models import Trillian


class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, req):
        req.headers['Authorization'] = 'Token {}'.format(self.token)
        return req


# noinspection PyUnusedLocal
@timer(seconds=60)
def check_trillians(signal_nr):
    print("Checking Trillians")

    trillians = Trillian.objects.all()
    info_requests = {}
    with FuturesSession(executor=ThreadPoolExecutor(max_workers=5)) as session:
        for trillian in trillians:
            if not trillian.token:
                print("Skipping Trillian {trillian.name} ({trillian.hostname})".format(trillian=trillian))
                if trillian.alive:
                    trillian.alive = False
                    trillian.save()
                continue

            info_requests[trillian.pk] = trillian, session.request(
                method='GET',
                url='https://{}/api/v1/info/'.format(trillian.hostname),
                auth=TokenAuth(trillian.token),
                timeout=(5, 10)
            )

        # Wait for all the responses to come back in
        info_responses = {}
        for pk, (trillian, request) in info_requests.items():
            info_responses[pk] = trillian, request.result()

    for trillian, response in info_responses.values():
        if response.status_code == requests.codes.ok:
            data = response.json()
            trillian.alive = True
            trillian.version = data['version']
            trillian.last_seen = timezone.now()
        else:
            trillian.alive = False

        trillian.save()