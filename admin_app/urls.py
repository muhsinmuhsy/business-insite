from django.urls import path
from .views import dashboard, logout_view, admin_login, service_add, service_delete, service_edit, service_list, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('logout/', logout_view, name='logout'),
    path('login/', admin_login, name='admin-login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='admin_app/pages/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='admin_app/pages/password_change_done.html'), name='password_change_done'),

    path('services/', service_list, name='service_list'),
    path('services/add/', service_add, name='service_add'),
    # path('services/<int:service_id>/view/', service_view, name='service_view'),
    path('services/<int:service_id>/edit/', service_edit, name='service_edit'),
    path('services/<int:service_id>/delete/', service_delete, name='service_delete'),

    path('profile/', profile, name='profile'),
]