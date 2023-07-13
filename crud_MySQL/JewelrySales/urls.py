from django.urls import path
from . import views

urlpatterns = [
    path('home' , views.home, name='home'),

    path('khuyenmai', views.khuyenmai,name='khuyenmai'),
    path('trangsuc', views.trangsuc, name='trangsuc'),
    path('dichvu', views.dichvu, name='dichvu'),
    path('gioithieuvalienhe',views.gioithieuvalienhe, name='gioithieuvalienhe'),
    path('huongdandosize', views.huongdandosize, name='huongdandosize'),

    path('admin',views.admin, name='admin'),

    path('dangky',views.dangky, name='dangky'),
    path('quenmatkhau',views.quenmatkhau, name='quenmatkhau'),

    path('muasp',views.muasp, name='muasp'),
    path('shopingcart',views.shopingcart, name='shopingcart'),
    path('hoadon',views.hoadon, name='hoadon'),

    path('carlist', views.carslist, name = 'carslist'),
    path('addcar', views.addcar, name = 'addcar'),
    path('updatecar/<int:id>', views.updatecar, name = 'updatecar'),
    path('deletecar/<int:id>', views.deletecar, name = 'deletecar')
    
]
