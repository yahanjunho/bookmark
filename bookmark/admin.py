from django.contrib import admin
from .models import Bookmark

# 관리자 페이지에 모델을 추가하거나,
# 기능을 커스터마이징 하고자 할때 수정하는 파일

class AdminBookmark(admin.ModelAdmin):
    # admin페이지에 옵션 추가가 가능
    list_display = ['id', 'site_name', 'url']


admin.site.register(Bookmark, AdminBookmark) # Bookmark를 등록하되, AdminBookmark옵션을 따르겠다!