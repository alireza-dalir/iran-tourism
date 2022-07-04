from django import forms


class TravelogueForm(forms.Form):
    name = forms.CharField(label='نام جاذبه گردشگری')
    description = forms.CharField(
        label='نظرات یا خاطرات شما', widget=forms.Textarea)
    image = forms.ImageField(label='تصویر یادگاری')
