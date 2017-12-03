from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from .models import Reviews


class ReviewsForm(forms.Form):
    class Meta:
        model = Reviews

    name = forms.CharField(label='Ваше Имя', max_length=150, required=False)
    email = forms.CharField(label='Email', max_length=100, required=False)
    text = forms.CharField(label='Отзыв', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ReviewsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper ()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse ('review')
        self.helper.add_input (Submit ('submit', 'Добавить', css_class='btn-success '))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout (
            Fieldset ('',
                      Field ('name', placeholder=''),
                      Field ('email', placeholder=''),
                      Field ('number', placeholder=''),
                      Field ('text', placeholder=''),
                      ))
