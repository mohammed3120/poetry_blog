from django.urls import path
from .views import (dashboard_view,
                    dashboard_posts_view,
                    dashboard_users_view,
                    create_post_view,
                    update_post_view,
                    delete_post_view,
                    delete_all_posts_view,
                    dashboard_filter_data_view,
                    dashboard_filter_user_view,
                    dashboard_profile_view,
                    delete_user_view,
                    delete_all_users_view,
                    dashboard_update_profile_view)
app_name = "admins"
urlpatterns = [
   path('dashboard_posts/<post_type>',dashboard_posts_view, name='dashboard_posts'),

   path('dashboard_users/',dashboard_users_view, name='dashboard_users'),

   path('create_post/<post_type>',create_post_view, name='create_post'),
   path('update_post/<pk>',update_post_view, name='update_post'),
   path('delete_post/<pk>',delete_post_view, name='delete_post'),
   path('delete_all_posts/<post_type>',delete_all_posts_view, name='delete_all_posts'),


   path('dashboard_filter_data/<post_type>',dashboard_filter_data_view, name='dashboard_filter_data'),

   path('dashboard_filter_user/',dashboard_filter_user_view, name='dashboard_filter_user'),

   path('dashboard_profile/<pk>',dashboard_profile_view, name='dashboard_profile'),

   path('delete_user/<pk>',delete_user_view, name='delete_user'),
   
   path('delete_all_users',delete_all_users_view, name='delete_all_users'),


   path('dashboard_update_profile/<pk>',dashboard_update_profile_view, name='dashboard_update_profile'),






]
