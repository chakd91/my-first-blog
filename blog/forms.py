from django import forms
from .models import Post

class PostForm(forms.ModelForm):  # Postform: 만들 폼의 이름. forms.ModelForm: 장고에 이 폼이 ModelForm 이라는 것을 알려줘야 함.
	class Meta:
		model = Post
		fields = ('title', 'text',)
