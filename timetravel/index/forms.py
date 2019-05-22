from django.forms import ModelForm
from .models import Location

class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields = ['location']

        def __init__(self, *args, **kwargs):
            super(MemberForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
