"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from proprietor import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('faq/',views.faq,name='faq'),
    path('login/', views.signin,name='login'),
    path('signup/', views.signup, name='signup'),
    
    path('owner_site/',views.owner,name='owner_site'),
    path('owner_site/add_property/',views.add_property,name='add_property'),
    path('owner_site/add_tenant/',views.add_tenant,name='add_tenant'),
    path('tenant_site/',views.tenant,name='tenant_site'),

    # path('owner_site/<int:p_id>/',views.add_tenant,name='add_tenant'),
    path('logout/',views.logout_user),
    path('owner_site/property_details/',views.property_details,name='property_details'),
    path('owner_site/tenant_details/',views.tenant_details,name='tenant_details'),
    path('owner_site/invite/',views.invite,name='invite'),
 
    path('owner_site/edit_profile/',views.edit_profile,name='edit_profile'),
    path('tenant_site/edit_profile_tenant/',views.edit_profile_tenant,name='edit_profile_tenant'), 
    path('owner_site/del_property/',views.del_prop,name='del_prop'),  
    path('remind_tenant/',views.rent_reminder,name='rent_reminder'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)