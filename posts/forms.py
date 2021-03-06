from django import forms
from .models import Post, Comment, Tag


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            # 'tag': forms.SelectMultiple(attrs={'class':'form-control'})
        }

class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class':'form-control'})
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control'})
        }
        # help_texts = {
        #     'text': 'max 500 char'
        # }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control'})
        }

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'جستجو در شابلاگ'}))
    options = (
        ('all', 'همه موارد'),
        ('title', 'عنوان'),
        ('text', 'متن'),
        ('tag__name', 'برچسب'),
        ('user', 'نویسنده'),
    )
    sub = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices = options)
        