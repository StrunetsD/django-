from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from honey_app.views import add_comment
from .views import *

urlpatterns = [
    path('account_detail/', account_detail, name = 'account_detail'),
    path('add_honey/', add_honey, name = 'add_honey'),
    path('add_comment/', add_comment, name = 'add_comment'),
    path('delete_post_honey<int:honey_id>/', delete_post_honey, name = 'delete_post_honey'),
    path('update_honey_article/<int:honey_id>/', update_honey_article, name='update_honey_article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)