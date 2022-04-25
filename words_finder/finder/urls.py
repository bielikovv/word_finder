from django.urls import path
from .views import *

urlpatterns = [
    path('', show_main_page, name="main_page"),
    path('big-text/', show_big_text_page, name="big_page"),
    path('big-text/text/<str:unique_title>/<str:unique_number>/', show_big_text_searching, name="big_text_searching"),
]