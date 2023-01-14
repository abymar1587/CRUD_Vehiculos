from django import forms
from .models import Vehiculo
#from .models import Categoria

class VehiculoForm(forms.ModelForm):
    class Meta:
        model=Vehiculo
        fields='__all__'
    
    def __init__(self, *args,**kwargs):
        super(). __init__(*args,**kwargs)

        lista=['imagen','idCategoria', 'idSubcategoria', 'idMarca', 'idModelo', 'idColor', 'año', 'idEstado', 'kilometrosRec', 'numeroPasajeros', 'idNumeroPuertas', 'idTipoMotor', 'cilindraje', 'tipoTransmision', 'precio','IVA', 'disponibilidad']

        for campo in lista:
            self.fields[campo].widget.attrs.update({
                'class':'form-control',
        })