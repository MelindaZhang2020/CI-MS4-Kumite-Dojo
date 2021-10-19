from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductImage, Variation


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image", "featured", "active"]

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )


# class ProductVariationForm(forms.ModelForm):
#     class Meta:
#         model = Variation
#         fields = ["variation_category", "variation_value"]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         category = Variation.variation_category_choice.all()
#         value = Variation.variation_value.all()

#         self.fields["variation_category"].choices = category
#         for field_name, field in self.fields.items():
#             field.widget.attrs["class"] = "border-black rounded-0"
#         self.fields["variation_value"].choices = value
#         for field_name, field in self.fields.items():
#             field.widget.attrs["class"] = "border-black rounded-0"
