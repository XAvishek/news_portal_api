from django.urls import path
from apis.accounts import views

urlpatterns = [
    path("users/create/", views.UserCreateAPIView.as_view(), name="create_user"),
    path("<int:reporter>/", views.ReporterNewsAPIView.as_view(), name="reporter_news"),
    
]
