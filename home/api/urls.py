from django.urls import path, include
from .views import *


urlpatterns = [
    path('Userss/', UserList.as_view()),
    path('users/', UserMixinList.as_view()),
    path('users/<int:pk>/', UserMixinDetail.as_view()),

    # path('swagger/', schema_view),
    # path('docs/', include_docs_urls(title='learning System')),
]
