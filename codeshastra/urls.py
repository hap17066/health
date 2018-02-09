from django.conf.urls import url
from django.contrib import admin
from health import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^PatientRegister/$', views.PatientRegister),
    url(r'^FetchPatientDetails/$', views.FetchPatientDetails),
    url(r'^GetAllPatientRecords/$', views.GetAllPatientRecords),
]