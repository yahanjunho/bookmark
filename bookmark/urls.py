
from django.urls import path, re_path
from .views import *

# namespace와 관련이 있는 app_name
app_name = 'bookmark'
urlpatterns = [
    # http://localhost:8000/bookmark/
   path('', BookmarkListview.as_view(), name='index'),
   path('create/', BookmarkCreateView.as_view(), name='create'),
   path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'), # pk가 있어야, 수정할 글을 바로 가져올 수 있다!?? 글번호 등등
   # 내부적으로 이미, int:pk에서 pk에 해당되는 값이, BookmarkUpdateView에 사전 정의되어있어서 그대로 써도 무방하다 (변경시 변경 내용을 반영해줘야한다.)
   path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
   path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),

]
