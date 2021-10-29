from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False

        # add regex to phone number field to avoid non numeric charaters being submitted
        # https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number
        self.fields["phone_number"].widget.attrs.update(
            {
                "pattern": "^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
            }
        )
        # adding regex to each field to avoid whitespace being submitted
        self.fields["full_name"].widget.attrs.update({"pattern": ".*\\S+.*"})
        self.fields["street_address1"].widget.attrs.update({"pattern": ".*\\S+.*"})
        self.fields["street_address2"].widget.attrs.update({"pattern": ".*\\S+.*"})
        self.fields["town_or_city"].widget.attrs.update({"pattern": ".*\\S+.*"})
        self.fields["county"].widget.attrs.update({"pattern": ".*\\S+.*"})
        self.fields["postcode"].widget.attrs.update({"pattern": ".*\\S+.*"})
