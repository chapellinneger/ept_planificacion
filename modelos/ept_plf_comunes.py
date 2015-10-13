
#~ Este metodo valida los siguientes casos:
    #~ 1- Que la fecha final no sea menor a la fecha inicial.
    #~ 2. Que la fecha inicial no sea igual a la fecha final.
    #~ 3. Valida que la fecha inicial exista antes de seleccionar la fecha final.



def validar_fecha(fecha_inicio, fecha_fin):
        fechas={}
        mensaje={}
        if fecha_inicio and fecha_fin:
            if cmp(fecha_inicio,fecha_fin)==1:
                fechas={
                    'fecha_fin':'',
                        }
                mensaje={
                    'title':('Error de fecha'),
                    'message':('La fecha de inicio no puede ser mayor\
                                a la fecha final'),
                    }
            if cmp(fecha_inicio,fecha_fin)==0:
                fechas={
                    'fecha_fin':'',
                        }
                mensaje={
                    'title':('Error de fecha'),
                    'message':('La fecha de inicio no puede ser igual\
                                a la fecha final'),
                    }
        else:
            if fecha_fin:
                fechas={
                    'fecha_fin':'',
                        }
                mensaje={
                        'title':('Error de fecha'),
                        'message':('Debe seleccionar una fecha de inicio'),
                        }
        return {
            'warning':mensaje,
            'value':fechas
                }
                
#~ este metodo limpia el campo de la fecha final si la fecha inicial cambia.

def limpiar_campo_fecha(fecha_inicio):
    fecha={}
    if fecha_inicio:
        fecha={
            'fecha_fin':''
            }
    return {
        'value':fecha
            }

