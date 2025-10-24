from django.urls import path
from . import views
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>', views.CatalogDetailView.as_view(), name='catalog_detail'),
    #path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('buy-ajax/', views.buy_product_ajax, name='buy_product_ajax'),

]

