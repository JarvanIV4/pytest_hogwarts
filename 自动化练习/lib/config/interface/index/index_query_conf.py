class IndexQueryConf:
    request_json = {
        "benchmark_code": '',
        "benchmark_name": '',
        "data_start_dt": '',
        "data_end_dt" : '',
    }
    api_data = {
        "url": "https://api.it120.cc/common/mobile-segment/location",
        "method": "get",
        "params": request_json
    }
    settings = {
        "header": {
            "Host": "",
            "Connection": "keep-alive",
            "Cookie": "JSESSIONID=FF6AE051654651156; BIGipServerPL_CSST_APP_80=rd50199999oo55555; loginType=local; lang=zh_CN; loginUserId=100301"}
    }