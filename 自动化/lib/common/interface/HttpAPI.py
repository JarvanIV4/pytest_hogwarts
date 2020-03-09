import json
import logging

import requests

from python_test.gitee.common.interface.HttpOptions import HttpOptions
from python_test.gitee.common.interface.HttpOptions import TestMethod
from python_test.gitee.common.interface.HttpOptions import UnsupportedMethodError


class HttpAPI:

    KEY_URL = "url"
    KEY_METHOD = "method"
    KEY_PARAMS = "params"
    KEY_DATA = "data"

    def __init__(self, api_data=None, options=None):
        self._api_data = api_data
        if api_data is not None:
            self._url = api_data[self.KEY_URL]
            self._method = TestMethod(api_data[self.KEY_METHOD])
            self._params = api_data.get(self.KEY_PARAMS, {})
            self._data = api_data.get(self.KEY_DATA)
        self._url = ""
        self._method = "post"
        self._params = {}
        self._data = {}
        if options is None:
            options = HttpOptions()
        self._options = options

    def _generate_param_string(self):
        param_str = "&".join([key + "=" + str(value) for key, value in self._params.items()])
        if param_str != "":
            param_str = "?" + param_str
        print("_generate_param_string: %s" % param_str)
        return param_str

    def send(self, **settings):
        method = self.method
        if method == TestMethod.GET:
            return requests.get(url=self.url, params=self.params, **settings)
        elif method == TestMethod.POST:
            return requests.post(url=self.url, data=self.data, **settings)
        elif method == TestMethod.PUT:
            return requests.put(url=self.url, data=self.data, **settings)
        elif method == TestMethod.PATCH:
            return requests.patch(url=self.url, data=self.data, **settings)
        elif method == TestMethod.DELETE:
            return requests.delete(url=self.url, **settings)
        else:
            raise UnsupportedMethodError("Unsupported method: %s" % method)

    def send_request(self, api_data=None, settings=None):
        if api_data is not None:
            self.api_data = api_data
        if settings is None:
            settings = {
                'timeout': 60,
                # 'auth ': self.auth,
                'verify': False,
                'headers': {'Content-Type': 'application/json', 'charset': 'UTF-8'}
            }
        response = self.send(**settings)
        return response

    def get_filed_value(self, content, key):
        try:
            objJson = json.loads(content)
            return objJson[key]
        except Exception as ex:
            logging.debug(ex.message)
            return "ERROR"

    @property
    def url(self):
        if self._api_data is not None:
            self._url = self._api_data[self.KEY_URL]
        if self._options is not None and self._options.base_url is not None:
            return self._options.base_url + self.url
        return self._url

    @property
    def method(self):
        return TestMethod(self._api_data[self.KEY_METHOD]).method

    @property
    def params(self):
        self._params = self._api_data.get(self.KEY_PARAMS, {})
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def api_data(self):
        return self._api_data

    @api_data.setter
    def api_data(self, value):
        self._api_data = value

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    @property
    def data(self):
        self._data = self._api_data.get(self.KEY_DATA)
        data = self.data
        if isinstance(self._data, dict):
            data = json.dumps(self._data, ensure_ascii=True) if self._data else None
        return data


if __name__ == '__main__':
    requestJson = {
        "mobile": "15012345678"
    }
    api_data = {
        "url": "https://api.it120.cc/common/mobile-segment/location",
        "method": "get",
        "params": requestJson
    }
    settings = {
        'headers': {
            "Host": "api.it120.cc",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Request-Origion": "SwaggerBootstrapUi",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
            "Referer": "https: // api.it120.cc / doc.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
    }
    settings1 = {}
    t = HttpAPI()
    resp = t.send_request(api_data, settings1)
    print(resp.status_code)
    print(resp.content)
