
# =============================================================================
# contrapartes/widgets.py
# =============================================================================
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'comunicacion/css/colorpicker.css',
            )
        }
        js = (
          
            settings.STATIC_URL + 'comunicacion/js/colorpicker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').colorPicker();
            </script>''' % name)
