from django.forms import Form,CharField,DateField,FloatField
    
#Formulario de busqueda 


class FormularioBusqueda(Form):
    nombre_vegetal = CharField ( max_length=50,required=True)
    
    
class FormularioPerecederos(Form):
    nombre_perece = CharField(max_length=50)
    
 
class FormularioNoPerece(Form):
    nombre_noperece = CharField(max_length=50)

class FormularioVegetal(Form):
    nombre = CharField( max_length=50,)
    cosecha = DateField()
    precio = FloatField()
    
class FormularioPeredce(Form):
    nombre= CharField(max_length=50)    
    fecha_vencimiento = DateField()
    precio = FloatField()
    
    
class FormularioNoperece(Form):
    nombre = CharField( max_length=50,)
    precio = FloatField()