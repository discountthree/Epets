from django.conf.urls import url

from app import views

urlpatterns = [
    # 主页
    url(r'^homepage/(\d+)/$', views.homepage, name='homepage'),
    # 主页
    url(r'^homepage/$', views.homepage1, name='homepage1'),
    # 购物车
    url(r'^shopcar/$', views.shopcar, name='shopcar'),
    # 商品详情一
    url(r'^goodsdetail/(\d+)/$', views.goodsdetail, name='goodsdetail'),
    # 商品详情二
    url(r'^goodsdetail2/(\d+)/$', views.goodsdetail2, name='goodsdetail2'),
    # 注册
    url(r'^register/$', views.register, name='register'),
    # 登录
    url(r'^login/$', views.login, name='login'),
    # 注销
    url(r'^logout/$', views.logout, name='logout'),
    # 添加到购物车
    url(r'^addshopcar/$', views.addshopcar, name='addshopcar'),
    # 从购物车移除
    url(r'^delshopcar/$', views.delshopcar, name='delshopcar'),

]
