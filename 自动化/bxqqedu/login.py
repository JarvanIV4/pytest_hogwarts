import requests


class Login():

    def login_bxqqedu(self):
        url = "http://apitest.guojiangjiaoyu.com/user/auth/login"
        headers = {
            'Host': 'apitest.guojiangjiaoyu.com',
            'Connection': 'keep-alive',
            'Content-Length': '186',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64',
            'clientType': 'web',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://admintest.guojiangjiaoyu.com',
            'Referer': 'http://admintest.guojiangjiaoyu.com/login?redirect=http%3A%2F%2Fadmintest.guojiangjiaoyu.com%2Fdormitory%2FdormitoryInfo',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        }
        data = {"data":"6OXKs/x+ESZf7cxgMiklO1xAtYdO6x41u79FfWtz0dbrgxuJklqr/HuNy8tyoIguScgy4IRa+x+YTjIdW0GlCVsGogqe6l9aiR/voskbAritIkUJ8lHLmDJU34iPgVgA8mkZ6BBlxpG6PTNNrRL32g==","k":"R7MR6T5QNUI5DYEQ"}
        response = requests.post(url=url,data=data, headers=headers)
        return response.text


if __name__ == '__main__':
    t = Login()
    print(t.login_bxqqedu())
