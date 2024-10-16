from django.urls import path

from .views import personal_view, personal_content, spirituality_view, spirituality_content

urlpatterns = [
   path('personal/', personal_view, name="personal"),
   path('personal/<str:title>', personal_content, name="personal_content"),
   path('espiritualidad/', spirituality_view, name="spirituality"),
   path('espiritualidad/<str:title>', spirituality_content, name="spirituality_content"),
]

