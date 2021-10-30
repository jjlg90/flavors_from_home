from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Reviews


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('title', 'user_rating', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #product = Product.objects.all()
        #product_friendly_names = [(p.id, p.get_name()) for p in product]

        #self.fields['product'].choices = product_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ('rounded-2')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    image_2 = forms.ImageField(label='Image_2', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
