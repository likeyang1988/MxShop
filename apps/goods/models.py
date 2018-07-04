from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.

class GoodsCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30,verbose_name='类别名',help_text="类别名")
    code = models.CharField(default="", max_length=30,verbose_name="类别code",help_text="类别code")
    desc = models.TextField(default="",verbose_name="类别描述",help_text="类别描述")
    #目录树级别
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别",help_text="类目级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录",related_name="sub_cat")
    is_tab = models.BooleanField(default=False,help_text="是否导航",verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(GoodsCategory,  verbose_name="商品类目")
    name = models.CharField(default="", max_length=30,help_text="品牌名",verbose_name="品牌名")
    desc = models.TextField(default="", max_length=200,help_text="品牌描述",verbose_name="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="",verbose_name="商品唯一货号")
    name = models.CharField(max_length=100,verbose_name="商品名")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    sold_num = models.IntegerField(default=0,verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0,verbose_name="市场价格")
    shop_price = models.FloatField(default=0,verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500,verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    # 首页中展示的商品封面图
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    # 首页中新品展示
    is_new = models.BooleanField("是否新品",default=False)
    # 商品详情页的热卖商品，自行设置
    is_hot = models.BooleanField("是否热销",default=False)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class GoodsImage(models.Model):
    """
    单个商品展示
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    image_url = models.CharField(max_length=300,null=True,blank=True,verbose_name="图片url")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name





class Banner(models.Model):
    """
    首页轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name



