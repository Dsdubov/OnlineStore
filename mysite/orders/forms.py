from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    def as_div(self):
        return self._html_output(
            normal_row = u'<div class="form-group" %(html_class_attr)s>\
                                <label class="col-md-4 control-label" %(label)s\
                                    <div class="col-md-4">\
                                        <input class="form-control input-md" required="" %(field)s\
                                    </div>\
                                </label>\
                            </div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)