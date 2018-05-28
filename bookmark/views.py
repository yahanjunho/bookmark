from django.shortcuts import render, redirect

# Create your views here.
# 어떤 기능을 만들어 주는곳
# models.py는 보통 앱단에서 잠깐 작성?

# 최종의 urls.py에 내가 views.py에 만든 기능이 어떤 url로 접속했을때 동작하게 할것이냐!?? --> login.xx -> views.py내 def login ??
# 고객의 접근순서와 개발순서가 반대!?? urls -> views -> models ~~

from django.views.generic.base import TemplateView

# 어떤 화면을 만들때 기능을!? 사용, 화면에서 많이 사용되는 화면들? 회원가입, 글쓰기, 업데이트, 글쓰기, 디테일 화면 등등
# 이미 정의되어있는 화면들이 있어서, 독특한 화면이 아닌이상, 장고가 사전정의한 view들을 상속받아서 그대로 사용하면 된다.

class IndexPage(TemplateView):
    template_name = 'index.html'
    # 함수기반으로 만드는뷰 , 클래스로 만드는 뷰, 이렇게 2가지 뷰가 있다? 함수형, 클래스형 아무거나 상관없다.
    # 대부분 기본은 클래스형 뷰, 상속을 기반으로 작동, 간략하게 restapi등을 만들고 싶다 하면 함수형 view로 만든다.

from django.views.generic.list import ListView
from .models import Bookmark

class BookmarkListview(ListView): # List형 View, 바로 url에서 간략하게 처리하는것도 가능
    model = Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookmarkCreateView(CreateView):
    model = Bookmark
    template_name_suffix = '_create' # template_name, template_name_suffix 차이점을 알아야!!!
    fields = ['site_name', 'url']  # creates시에 필요한, 입력들, 사용자가 필요한 입력만 표기, complex form?? 두개의 모델을 이용해서 fields 로 받아줌

    def form_vaild(self, form):
        if form.is_valid: # 폼에 입력된 값이 이상이 없을때
            form.instance.save() # form을 인스턴스화해서 저장!!
            #print('out!!!')
            return redirect('/bookmark/')
        else:
            return self.render_to_response(f{'form':orm}) # 입력했던 화면으로 다시 돌려줌, 이 전에, js로 프론트 단에서 필드값 유효성을 먼저 점검함

# Bookmark update view!??
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update' # ~/bookmark/boomark_update.html을 사용!?


# success url을 만들거나, or get_absolte_url을 지정하는것
# 각 객체, 글이든, 사진이든 각각의 url을 지정, 즉 디테일 페이지

from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    from django.urls import reverse_lazy # reverse VS reverse_lazy, lazy는 실제로 호출이 이루어질때, url, 주소가 생성된다. 인터프리팅 시점에 없어도 기능을 작동시키는데는 무방하다. 실제로 필요했을떄, 호출 타이밍에 생성, 언제 주소가 만들어지느냐 시점의 차이
    model = Bookmark
    success_url = reverse_lazy('bookmark:index') # 삭제에 성공한 다음에 이동하는 url 지정

