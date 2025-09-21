# from django.conf.urls import url
# from first_app import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^users/',views.user, name='user'),
#     url(r'^formpage/',views.form_name_view,name='form_name'),
# ]


from django.conf.urls import url
from first_app import views

# Template Tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]

