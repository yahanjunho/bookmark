from django.db import models

# Create your models here.
# 내가 데이터베이스에 어떤 데이터를 어떻게 저장할 것이냐?!??! 를 정의
# 일반적으로는 내가 데이터베이스를 직접 다룰 일이 없다!! 나중에 쿼리 튜닝하기 등의 순간까지 온다면....
# 사실 DB이론을 몰라도 어느정도 규모까지는 그냥 운영이 가능하다. (정말 훗날!!)
# ORM == 클래스와 객체를 하나로 관계를 맺어서 정의한다!?
# 내가 클래스를 구성하면, 이에 맞대응되는 DB의 테이블이 생성되는데, 이때의 관계, CRUD를 대신 해주는것 ==> ORM

# models.py -> views.py -> urls.py -> template

# 데이터베이스 한 테이블을, 하나의 클래스로 묘사한다. 테이블 하나 추가? 모델 하나 추가 ㄱㄱ
# 모델은 항상  class로 구성한다.

# Model은 DB관련된 모든 기능을 다 포함한 클래스이다.
class Bookmark(models.Model):
    # 하나의 필드를 만든다.
    # 컬럼이름 = 컬럼 종류(제약조건)
    site_name = models.CharField(max_length=100)
    url = models.URLField('url') # 내부적으로는 텍스트필드, 대표하는 이름? verbose name??

    # 모델의 옵션
    class Meta: # 옵션부여!? 정렬 or 대표이름
        ordering = ['site_name'] # 디폴트가 오름차순, DB에서 꺼내올때, 이렇게 꺼내옴 관리자에서 다르게 보여주고 싶다? admin.py에 따로 수정, 반영

    def __str__(self): # 모델에 들어가는 메서드들은, 하나의 객체들 마다 반영된다. 던던? 매직펑션?
        # 클래스 인스턴스를 프린트로 화면에 바로 뽑아낼때, 객체의 주소가 아닌, 다른걸로 뽑고 싶다?, 관리자화면에서 어떻게 보일지도 여기 설정대로 먹힘
        return self.site_name

    def get_absolute_url(self):
        from django.urls import reverse
        # http://localhost:8000/bookmark/detail/4
        return reverse('bookmark:detail', args=[str(self.id)])