from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from tinymce.widgets import TinyMCE

from .models import Reviews, Offers, Images


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


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['offer_title', 'offer_minorder', 'offer_minorder_value', 'offer_availability',
                  'offer_article', 'offer_price', 'offer_price_from', 'offer_price_to', 'offer_text']

        widgets = {
            'offer_text': TinyMCE(attrs={'rows': 45}),
        }


    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)


class ImageForm(forms.ModelForm):

    max_width = forms.IntegerField(label='Ширина', widget=forms.NumberInput(attrs={'style':'width:100px'}), required=False)
    max_height = forms.IntegerField(label='Высота', widget=forms.NumberInput(attrs={'style':'width:100px'}), required=False)

    class Meta:
        model = Images
        exclude = ('offer', 'id')

        labels = {
            'images_url': 'Ссылка на изображение',
            'images_file': 'Загрузка файла',
            'main': 'Главная',
            'delete': 'Удалить'
        }


ImageFormSet = forms.inlineformset_factory(Offers, Images, ImageForm)