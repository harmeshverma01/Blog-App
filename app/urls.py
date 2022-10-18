from django.urls import path, include
from . import views

app_name= "blog_app"

urlpatterns = [
   path('', views.HomePageView.as_view(),name="homepage"),
   path('login/', views.login_user, name="login_user"),
   path('logout/', views.logout_user, name="logout_user"),
   path('Signup/', views.Signup, name="Signup"),
   path('contact_page/', views.add_contact, name="add_contact"),
   path('<id>', views.SinglePostView.as_view(), name="single_post"),
   path('add_comment/<post_id>', views.AddCommentView.as_view(), name="add_comment"),
   path('about_page/', views.about_page, name="about_page"),
]