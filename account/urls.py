from xml.etree.ElementInclude import include
from django.urls import path,include


from account import views


app_name = "account"


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout")
]


