from django.urls import path
from .views import MyProtectedView, client_credentials,access_protected_view,get_access_token

urlpatterns = [
    path('client-credentials/', client_credentials, name='client-credentials'),
    path('protected-view/', MyProtectedView, name='protected-view'),
    path('access/', access_protected_view, name='access-view'),
    path('geo/', get_access_token, name='access-token'),

]
