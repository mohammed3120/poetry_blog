from django.urls import path
from .views import (signup_view,
                    login_view, 
                    logout_view, home, 
                    posts_view, 
                    filter_data, 
                    likeTogle,
                    add_comment_view,
                    add_reply_view,
                    change_colors,
                    profile_view,
                    update_profile_view,
                    writer_profile_view,
                    update_post_view,
                    delete_post_view)
app_name = "poetries"
urlpatterns = [

    path('register/',signup_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),

    path('',home, name='home'),

    path('posts/<post_type>',posts_view, name='posts'),

    path('filter-data/<post_type>',filter_data, name='filter_data'),

    path('like/<pk>',likeTogle, name='like'),

    path('add-comment/<pk>',add_comment_view, name='add_comment'),

    path('add-reply/<pk>',add_reply_view, name='add_replyt'),

    path('change-color/<theme>',change_colors, name='change_colors'),

    path('profile_view/<pk>',profile_view, name='profile_view'),

    path('update_profile/<pk>',update_profile_view, name='update_profile'),

    path('writer_profile/<pk>',writer_profile_view, name='writer_profile'),

    path('update_post/<pk>',update_post_view, name='update_post'),

   path('delete_post/<pk>',delete_post_view, name='delete_post'),







]
