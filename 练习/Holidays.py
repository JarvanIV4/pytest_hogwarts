class HolidaysUpdate:

    def inter(self, ccy, year, *date):
        req = {
            "ccy": "",
            "year": "",
            "holidays": []
        }
        req["ccy"] = ccy
        req["year"] = year
        req["holidays"] = list(date)
        return req

    def get_req_dict(self, req):
        req_dict = []
        INPUTARMX1_list = ["ccy", "holidays"]
        for i in range(len(req["holidays"])):
            req_list = []
            holidays = req["holidays"][i].split("/")
            date = req["year"] + "-" + holidays[0].zfill(2) + "-" + holidays[1].zfill(2) + " 00:00:00"
            req_list.append(req["ccy"])
            req_list.append(date)
            req_dict.append(dict(zip(INPUTARMX1_list, req_list)))
        print(req_dict)


if __name__ == '__main__':
    t = HolidaysUpdate()
    req = t.inter("HKD", "2020", "01/20", "2/28", "1/6", "12/6")
    t.get_req_dict(req)