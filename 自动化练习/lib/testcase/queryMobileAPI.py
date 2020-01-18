from common.interface.HttpAPI import HttpAPI


class queryMobileAPI(HttpAPI):

    def queryMobile(self, mobile):
        requestJson = {
            "mobile": mobile
        }
        api_data = {
            "url": "https://api.it120.cc/common/mobile-segment/location",
            "method": "get",
            "params": requestJson
        }
        settings = {}
        resp = self.send_request(api_data, settings)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    t = queryMobileAPI()
    t.queryMobile("15391326584")
