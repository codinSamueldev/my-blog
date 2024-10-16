from django.urls import path

from . import views

urlpatterns = [
   path('personal/', views.personal_view, name="personal"),
   path('personal/<str:title>', views.personalspiritual_content, {'template_name': 'personal/personal_content.html'}, name="personal_content"),
   path('espiritualidad/', views.spirituality_view, name="spirituality"),
   path('espiritualidad/<str:title>', views.personalspiritual_content, {'template_name': 'spirituality/spirituality_content.html'}, name="spirituality_content"),
]

