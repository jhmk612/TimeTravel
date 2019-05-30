from django import forms


class LocationForm(forms.Form):
    location = forms.CharField(max_length=100,

                               label='어디로 떠나고 싶으신가요?',
                           widget= forms.TextInput
                           (attrs={'placeholder':'지역을 입력해주세요', 'id':'keyword'}))

