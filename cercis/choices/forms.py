from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Column, Layout, Row, Submit
from django.forms import Form


class TitleFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("abbr", css_class="col-md-12 mb-0"),
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )


class ColorFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("text", css_class="col-md-12 mb-0"),
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )


class CountryFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("code", css_class="col-md-3 mb-0"),
                Column("text", css_class="col-md-9 mb-0"),
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )
