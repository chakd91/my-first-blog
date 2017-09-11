from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User') # 다른 모델에 대한 링크.
	title = models.CharField(max_length=200) # 글자수가 제한된 텍스트를 정의.
	text = models.TextField() # 글자수에 제한이 없는 긴 텍스트를 위한 정의. 블로그 콘텐츠로 담을 예정.
	created_date = models.DateTimeField( # 날짜와 시간.
			default = timezone.now)
	published_date = models.DateTimeField(
			blank = True, null = True)

	def publish(self): # publish: 메서드 이름.
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
