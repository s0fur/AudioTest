from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('api/answers/noise', views.NoiseGet.as_view()),
    path('', views.test, name="test"),
    path('api/answers/noise/create', views.AnswerNoisePost.as_view()),
    path('api/answers/shorthand', views.ShorthandGet.as_view()),
    path('api/answers/shorthand/create', views.AnswerShorthandPost.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
