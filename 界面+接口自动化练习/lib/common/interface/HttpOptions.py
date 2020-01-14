import sys

class AuthenticaError(Exception):
    """Wrongly defined authentication information"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return  str(self.value)

class HttpOptions:
    def __init__(self, base_url=None, auth=None, insecure=False):
        self._base_url = base_url
        self._auth = self._read_authentication(auth)
        self._insecure = insecure

    @staticmethod
    def _read_authentication(auth):
        if auth is not None:
            auth_decomp = auth.split(':')
            if len(auth_decomp) != 2:
                raise AuthenticaError("Authentication information is")
            return auth_decomp[0], auth_decomp[1]
        return None

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def auth(self):
        return self._auth

    @property
    def insecure(self):
        return self._insecure


class UnsupportedMethodError(Exception):
    """Test types are not supported"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class TestMethod:
    GET = "get"
    PUT = "put"
    POST = "post"
    PATCH = "patch"
    DELETE = "delete"

    def __init__(self, method):
        if method not in {self.GET, self.POST, self.PUT, self.PATCH, self.DELETE}:
            raise UnsupportedMethodError("'%s' is not supported" % method)
        self._method = method

    @property
    def method(self):
        return self._method


if __name__ == '__main__':
    url = "https://www.baidu.com/"
    test = HttpOptions()
    print(test.base_url)


