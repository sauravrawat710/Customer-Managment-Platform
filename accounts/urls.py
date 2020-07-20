from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.userPage, name="userPage"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('products/', views.products, name="products"),
    path('account/', views.accountSettings, name="account"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('create_order/<int:pk>/', views.createOrder, name="createOrder"),
    path('update_order/<int:pk>/', views.updateOrder, name="updateOrder"),
    path('delete_order/<int:pk>/', views.deleteOrder, name="deleteOrder"),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
