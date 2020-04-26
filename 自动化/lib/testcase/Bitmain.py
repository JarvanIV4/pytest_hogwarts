import requests


class Bitmain():

    def __init__(self):
        super().__init__()
        self.login_url = "https://account.bitmain.com/sign_in?method=2&service=https%3A%2F%2Fservice.bitmain.com.cn%2Fwetseasonfestival"
        self.click_time = "17:59:58"

    def login_bitmain(self, username, password):
        url = 'https://account.bitmain.com/api/vn/login'
        data = {"identifier": username,
                "password": password,
                "type": 3,
                "lt": "LT-8d14478e79fe7789ecee336f233130ea605579351aa5e872e3ae0d2fd7fd976d",
                "service": "https://service.bitmain.com.cn/wetseasonfestival",
                "locale": "zh-CN"}
        headers = {'cookie':'fidder抓包获取'}
        resp = requests.post(url=url, headers=headers)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    username = '2268035948@qq.com'
    password = 'M/6XlSUSej9Aym831+M5CVKc6eGuadKM8/OlbmpGO+uVRmVX2CVlafSbHSSTcHZdRxHmLbzvCIVBjheo+AVrp2TLMc77Ws+YbqCtllD4vpAAAkpAOye10QE8t7yAbtFtNXk/9IeIE/GJzldYMZeiDi3oJZwtThB3OqxsvlwbSRQ='
    b = Bitmain()
    b.login_bitmain(username, password)
