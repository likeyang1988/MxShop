from django.views.generic.base import View
from goods.models import Goods



class GoodsListView(View):
    def get(self,request):
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["goods_front_image"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_list.append(json_dict)

        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize("json",goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)