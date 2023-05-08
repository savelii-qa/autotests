import requests
import copy
import json
import logging
import config

api_url = config.API_URL


DEFAULT_HEADERS = {
    "content-type": "application/json"
}


def execute_and_log(func):
    def wrapper(self):
        logging.debug('========== HTTP request ==========')
        logging.debug('method: {}, route: {}'.format(self._method.upper(), self._url))
        logging.debug('headers: {}'.format(self._headers))
        logging.debug('body: {}'.format(self._body))
        logging.debug('files: {}'.format(self._files))
        func(self)
        logging.debug('============ RESPONSE ============')
        logging.debug('Status code: {}'.format(self.status_code))
        logging.debug('Response: {}'.format(self.json))
        logging.debug('End of http request')
    return wrapper


class HTTPRequest(object):
    def __init__(self, method, uri, headers=None, params=None, body=None, files=None):
        self.status_code = None
        self.json = None
        self.r = None
        self.text = None
        self._url = api_url + uri if not uri.startswith('http') else uri
        self._method = method.lower()
        self._headers = copy.deepcopy(DEFAULT_HEADERS)
        if headers:
            self._headers.update(headers)
        self._files = files
        if self._files:
            self._headers = headers
        self._body = body
        self._params = params

        self.__request()

    @execute_and_log
    def __request(self):
        r = requests.request(method=self._method, url=self._url, headers=self._headers,
                             data=json.dumps(self._body) if self._body else None, files=self._files, params=self._params,
                             )
        logging.debug('Request url with params: {}'.format(r.url))
        self.status_code = r.status_code
        try:
            self.json = r.json()
        except Exception as e:
            logging.warn('Cannot parse json from response!')
            logging.warn('Response text: {}'.format(r.text))
            logging.error(e)
            self.text = r.text

