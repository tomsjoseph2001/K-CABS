
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.log_post),

    path('admins_home/',views.home),

    path('admins_add_driver/',views.admins_add_driver),
    path('admins_add_driver_post/',views.admins_add_driver_post),
    path('admins_add_driver_post/',views.admins_add_driver_post),
    path('admins_view_driver/',views.admins_view_driver),
    path('admins_view_driver_post/',views.admins_view_driver_post),
    path('admins_delete_driver/<id>',views.admins_delete_driver),
    path('admins_edit_driver/<id>',views.admins_edit_driver),
    path('admins_edit_driver_post/',views.admins_edit_driver_post),

    path('admins_view_complaints/',views.admins_view_complaints),
    path('admins_view_complaints_post/',views.admins_view_complaints_post),
    path('admins_sent_reply/<id>',views.admins_sent_reply),
    path('admins_sent_reply_post/',views.admins_sent_reply_post),



    path('admin_addvehicle/',views.admin_addvehicle),
    path('admin_addvehicle_post/',views.admin_addvehicle_post),

    path('admin_view_vehicle/',views.admin_view_vehicle),
    path('admin_view_vehicle_post/',views.admin_view_vehicle_post),
    path('admin_view_vehicle_post/',views.admin_view_vehicle_post),
    path('admin_delete_vehicles/<vid>',views.admin_delete_vehicles),
    path('admin_edit_vehicles/<id>',views.admin_edit_vehicles),
    path('admin_editvehicle_post/',views.admin_editvehicle_post),



    path('admin_change_password/',views.admin_change_password),
    path('admin_changepas_post/',views.admin_changepas_post),


    path('admin_car_driver_assign/',views.admin_car_driver_assign),
    path('admin_car_driver_assign_post/',views.admin_car_driver_assign_post),
    path('admin_view_car_driver_assign/',views.admin_view_car_driver_assign),
    path('admin_delete_car_assign/<id>',views.admin_delete_car_assign),
    path('admin_view_car_driver_assign_post/',views.admin_view_car_driver_assign_post),
    path('admin_view_users/',views.admin_view_users),
    path('admin_view_users_post/',views.admin_view_users_post),







    path('driverhome/',views.driverhome),
    path('driver_view_profile/',views.driver_view_profile),
    path('driver_change_password/',views.driver_change_password),
    path('driver_view_booking_new/',views.driver_view_booking_new),
    path('driver_view_booking_new_post/',views.driver_view_booking_new_post),
    path('driver_picked/<id>',views.driver_picked),
    path('driver_cancelled/<id>',views.driver_cancelled),
    path('driver_dropped/',views.driver_dropped),
    path('driver_change_password/',views.driver_change_password),
    path('driver_changepas_post/',views.driver_changepas_post),


    path('uhome/',views.uhome),
    path('user_signup/',views.user_signup),
    path('user_signup_post/',views.user_signup_post),
    path('user_view_profile/',views.user_view_profile),
    path('user_edit_profile/',views.user_edit_profile),
    path('user_editprofile_post/',views.user_editprofile_post),
    path('user_add_complaint/',views.user_add_complaint),
    path('user_add_complaint_post/',views.user_add_complaint_post),
    path('user_view_complaint/',views.user_view_complaint),
    path('user_view_complaint_post/',views.user_view_complaint_post),
    path('user_view_cabs/',views.user_view_cabs),
    path('user_view_cabs_post/',views.user_view_cabs_post),
    path('user_booking/<vid>',views.user_booking),
    path('user_booking_post/',views.user_booking_post),

    path('user_change_password/', views.user_change_password),
    path('user_changepas_post/', views.user_changepas_post),
    path('user_view_booking/', views.user_view_booking),
    path('user_view_booking_post/', views.user_view_booking_post),
    path('user_cancelled/<id>', views.user_cancelled),

    path('forget_password/', views.forget_password),
    path('forget_password_post/', views.forget_password_post),

    path('sa/', views.sa),
    path('get_vehicles/', views.get_vehicles),
    path('userpayment/<bid>/<totalkm>', views.userpayment),
    path('userpayment_post/', views.userpayment_post),
    path('raz_pay/<amount>',views.raz_pay),

    ]

