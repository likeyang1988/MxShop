__author__ = 'likeyang'
__date__ = '2018/6/26 17:06'

import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        #需要传递的参数
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【刘江】您购买的{code}商品因库存不足，正在为您办理退款，3个工作日内退款将会原路返回到您的付款账户中。".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == "__main__":
    yun_pian = YunPian("5452959855f32ff243109568f64b8f4f")
    yun_pian.send_sms("2018", "15093809832")