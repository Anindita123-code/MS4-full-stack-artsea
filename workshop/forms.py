from django import forms
from .models import Workshop, Category
from .widgets import CustomClearableFileInput


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = '__all__'

    image = forms.ImageField(
        label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category_name'].choices = friendly_name

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


