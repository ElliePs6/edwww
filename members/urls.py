from django.urls import path
from  .import views

urlpatterns = [
    path('',views.first_home,name="first_home"),
    path('login/', views.login_user, name="login"),
    path('company_home/',views.company_home,name="company_home"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('logout_admin/', views.logout_admin, name="logout_admin"),
    path('employee_home/',views.employee_home,name="employee_home"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_company/',views.register_company,name="register_company"),
    path('register_employee/',views.register_employee,name="register_employee"),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('switch_to_company_login/', views.switch_to_company_login, name='switch_to_company_login'),





    
]