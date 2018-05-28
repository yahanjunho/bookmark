"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from bookmark.views import IndexPage, BookmarkListview

urlpatterns = [
    # localhost:8000/bookmark/List
    # 각 path 경로안의 name들, index?? name을 구분하기 위해, namespace를 더 추가해준다. -> 구체적으로는 app_name.name ~ 으로 작동
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls), # url, regex이용가능?

    # 1차 urls.py파일에서, 2차 url로 라우팅을 해준다. (앱으로 토스해준다.), 어떤기능을 할지는, 앱이 정하게 함, 여기서는 안정함
    #path('', IndexPage.as_view(), name='index'),  # 클래스형 뷰들은, 뒷쪽에 as_view로 정의해야 사용가능, name으로 url를 찾을 수 있다.
    path('', BookmarkListview.as_view(), name='index'),
    # 이름만 정의해놓으면, url이나 뷰가 변경되어도, 이름으로 찾아서 사용이 가능하다.
    # re_path(''),

    # url(r'^$', include('bookmark.urls', namespace='bookmark')), // 범위가 넓을수록, url을 이용한 패턴은 아래로 빼줘야한다. 위쪽은 좁은범위, 아래쪽으로 내려올수록 넓은 범위로 잡아줘야한다.for
    # url(r'admin/$', admin.site.urls),
    # url(r'', BookmarkListview.as_view(), name='index'),

]
