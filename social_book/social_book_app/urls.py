from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('authors-and-sellers/', views.authors_and_sellers, name='authors_and_sellers'),
    path('dummy/', views.dummy, name='dummy'),
    path('upload_books/', views.upload_books, name='upload_books'),
    path('uploaded_books/', views.uploaded_books, name='uploaded_books'),
           
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)