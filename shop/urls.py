
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="About"),
    path("contactus/",views.contactus, name="Contact-Us"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("productview/",views.productview, name="ProductView"),
    path("search/",views.search, name="Search"),
    path("checkout/",views.checkout, name="CheeckOut"),
    path("setting/",views.setting, name="Setting"),
    path("address/",views.address, name="Address"),
]
