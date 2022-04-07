from django.urls import path

from .views import BuyerCarView, CarAdd, ChangeStatus, HomePage, ThankYou

urlpatterns = [
    path('car-add/', CarAdd, name="car_add"),
    path('home-page/', HomePage, name="home_page"),
    path('thank-you/', ThankYou, name="thank_you"),
    path('buy-car/<int:pk>/', BuyerCarView.as_view(), name="buy_car"),
    path('change-status/<int:pk>', ChangeStatus, name="change_status"),
]
