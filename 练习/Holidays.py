class HolidaysUpdate:

    def __init__(self):
        self.req = {
            "ccy": "",
            "year": "",
            "holidays": []
        }

    def inter(self, ccy, year, *date):
        self.req["ccy"] = ccy
        self.req["year"] = year
        self.req["holidays"] = list(date)
        print(self.req)


HolidaysUpdate().inter("HKD", "2020", "01/20", "2/28", "1/6")
