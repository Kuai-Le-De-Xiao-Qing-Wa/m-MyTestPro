from django.urls import path
# from django.conf.urls import url
from django.views.generic.base import TemplateView

import app.admin
from app import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    # url(r'', TemplateView.as_view(template_name='index.html')),
    path('user/getlist/',app.admin.User.get_list),
    path('user/adduser/',app.admin.User.add_user),
    path('user/userinfo/<int:id>',app.admin.User.user_info),
    path('user/updata/<int:id>',app.admin.User.updata_user),
    path('user/deluser/<int:id>',app.admin.User.del_user)
]
