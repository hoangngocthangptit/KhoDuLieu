from django.urls import path
from . import views
urlpatterns = [
    path('depositorMST', views.DepositorMstAPI.as_view(), name='getdepositor'),
    path('office', views.OfficeMstAPI.as_view(), name='getoffice'),
    path('payment-condition-registration',views.PaymentConditionRegistrationAPI.as_view(),name='post-payment')

]