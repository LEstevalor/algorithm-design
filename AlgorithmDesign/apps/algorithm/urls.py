from django.conf.urls import url
from rest_framework import routers

from . import views

urlpatterns = (
    url(r'^caculate/(dp|greedy|backtrack|dpplus)/', views.CaculateView.as_view()),  # 邮箱验证码发送
    url(r'^caculate_test/(dp|greedy|backtrack|dpplus)/', views.CaculateTestView.as_view()),  # 邮箱验证码验证
)
