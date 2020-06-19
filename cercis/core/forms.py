from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Column, Layout, Row, Submit
from django.forms import Form


class PoodleFilterForm(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name_registered", css_class="col-md-4 mb-0"),
                Column("name_call", css_class="col-md-4 mb-0"),
                Column("color", css_class="col-md-4 mb-0"),
                css_class="form-row mb-2",
            ),
            Row(
                Column("variety", css_class="col-md-4 mb-0"),
                Column("owners", css_class="col-md-4 mb-0"),
                Column("breeders", css_class="col-md-4 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("origin_country", css_class="col-md-3 mb-0"),
                Column("akc", css_class="col-md-3 mb-0"),
                Column("ukc", css_class="col-md-3 mb-0"),
                Column("addtl", css_class="col-md-3 mb-0"),
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )


class PersonFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("full_name", css_class="col-md-12 mb-0"),              
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )


class KennelFilterForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-12 mb-0"),
                css_class="form-row",
            ),
            Row(
                Submit('save', 'Save', css_class="btn-success"),
                Button('cancel', 'Cancel', css_class="btn-secondary"),
            )
        )
