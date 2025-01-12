# CarroStream/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('home.urls')),  
    path('about/', include('about.urls')),  
    path('services/', include('services.urls')),  
    path('accounts/', include('accounts.urls')),  
    path('dashboard/', include('dashboard.urls')),  
    # path('booking/', include('booking.urls')), 
    path('payments/', include('payments.urls')),  
    path('rewards/', include('rewards.urls')),  
    path('faq/', include('faq.urls')),  
    path('contact/', include('contact.urls')),  
    path('policies/', include('policies.urls')),  
    path('tracking/', include('tracking.urls')),  
    path('feedback/', include('feedback.urls')),  
    path('blog/', include('blog.urls')), 
    path('pricing/', include('pricing.urls')),
    path('newsletter/', include('newsletters.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
