from django.urls import path
from .views import home, poetry_view, p_reflections, i_read_you_view, stories
app_name = "poetries"
urlpatterns = [
    path('',home, name='home'),

    path('poetry/',poetry_view, name='poetry'),

    path('p_reflections/',p_reflections, name='p_reflections'),

    path('i_read_you/',i_read_you_view, name='i_read_you'),

    path('stories/',stories, name='stories'),

]
