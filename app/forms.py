from django import forms
from app.models import Post

# form html 문자열을 렌더링
# html form을 통해 저장을 시도하는 값에 대한 유효성 검사 및 db로의 저장


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
