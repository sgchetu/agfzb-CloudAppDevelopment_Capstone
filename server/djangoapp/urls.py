from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for about view 
    path(route='about/', view=views.about, name='about'),
    # path for contact us view
    path(route='contact/', view=views.contact, name='contact'),
    path('signup/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view
    # path for dealer reviews view
    path('dealer_detail/<int:id>/', views.get_dealer_details, name='get_dealer_details'),
    # path for add a review view
    path('add_review/<int:id>/', views.add_review, name='add_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)