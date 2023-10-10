from django import forms
from ejercicioApp1.models.producto import Producto
from ejercicioApp1.models.proveedor import Proveedor
from ejercicioApp1.models.temporada import Temporada


class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
            
class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class FormTemporada(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = '__all__' 