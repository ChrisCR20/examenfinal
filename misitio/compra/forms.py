from django import forms
from .models import Usuario, Producto, Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'dpi', 'productos')

        #model = Compra
        #fields = ('cantidad','codigo_p')


def __init__ (self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields["productos"].widget = forms.widgets.ChoiceField()
        self.fields["productos"].help_text = "Agregue los productos "
        self.fields["productos"].queryset = Producto.objects.all()
