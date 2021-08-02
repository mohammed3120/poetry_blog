from django.urls import path
from .views import (dashboard_view,
                    dashboard_posts_view,
                    dashboard_users_view,
                    PostDetailView,
                    create_post_view,
                    update_post_view,
                    delete_post_view,
                    dashboard_filter_data_view)
app_name = "admins"
urlpatterns = [
   path('dashboard_posts/<post_type>',dashboard_posts_view, name='dashboard_posts'),

   path('dashboard_users/',dashboard_users_view, name='dashboard_users'),

   path('dashboard_post/<pk>',PostDetailView.as_view(), name='dashboard_post'),
   path('create_post/<post_type>',create_post_view, name='create_post'),
   path('update_post/<pk>',update_post_view, name='update_post'),
   path('delete_post/<pk>',delete_post_view, name='delete_post'),


   path('dashboard_filter_data/<post_type>',dashboard_filter_data_view, name='dashboard_filter_data'),


]
