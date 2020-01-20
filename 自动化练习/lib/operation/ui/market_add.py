from time import sleep

class Market:

    def market_add(self, market_data):
        self.click_ele(market_loc["新增投资市场设定"])
        sleep(2)
        input_tuple = ("市场代码", "投资市场", "投资市场英文名称")
        select_tuple = ("对应资产类别", "市场风险")
        # 输入框
        for market_key in input_tuple:
            if market_key in market_data.key():
                self.input_text(market_add_loc[market_key], market_data[market_key])
        for market_key in select_tuple:
            if market_key in market_data.key():
                self.click_ele(market_add_loc[market_key])
                sleep(2)
                self.click_ele(market_add_loc[str(market_key + "-" + market_data[market_key])])
            else:
                self.log.error("缺少Key值:" + market_key)