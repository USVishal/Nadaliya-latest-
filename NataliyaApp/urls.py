from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #############################################################<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>>>>
    path('', views.index, name='index'),
    path('user_type', views.user_type, name='user_type'),
    path('login_main',views.login_main, name='login_main'),
    path('forgotPassword/', views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword,name='resetPassword'),
    path('logout/', views.logout,name='logout'),

    ############################################################ <<<<<<<<< Staff MODULE >>>>>>>>>>>>>>>>>
 
    path('staff_home/',views.staff_home,name='staff_home'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    # path('item_edit/<int:item_id>/', views.item_edit, name='item_edit'),
    path('staff_validate/',views.staff_validate,name='staff_validate'),
    ############################################################ <<<<<<<<< User MODULE >>>>>>>>>>>>>>>>>

    path('user_registration/',views.user_registration,name='user_registration'),
    path('index_user_confirmation/<int:user_id>/',views.index_user_confirmation,name='index_user_confirmation'),
    path('profile_user_creation/',views.profile_user_creation,name='profile_user_creation'),
    
    path('user_home/',views.user_home,name='user_home'),
    ############################################################ <<<<<<<<< products >>>>>>>>>>>>>>>>>
    path('items_view/', views.items_view, name='items_view'),
    path('product_view/<int:item_id>/', views.product_view, name='product_view'),
#####################bannerimag#############################
 path('upload_images', views.upload_images, name='upload_images'),

 
]
   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)