# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.http import request
from ept_plf_comunes import *
from datetime import datetime, date, time, timedelta

class ept_plf_actividad_etapas(osv.osv):
    _name='ept_plf.actividad_etapas'
    _rec_name='tipo_planificacion_id'
    _description=u"""Estas son las actividades que se programaran dentro/
                     de las  etapas que conformaran los periodos/
                     para la gestión de los proyectos de las Entidades/
                     Politicos Territoriales"""
    
    
    _columns={
        'etapas_id':fields.many2one(
                    'ept_plf.etapas',
                    """Etapas""",
                    required=True,
                    ondelete='cascade',),
        'tipo_planificacion_id':fields.many2one(
                    'ept_plf.tipo_planificacion',
                    """Actividades""",
                    required=True,),
        'fecha_inicio':fields.date(
                    'Fecha de Inicio',
                    required=True,
                    help='Aquí se coloca la fecha de inicio del periodo'),
        'fecha_fin':fields.date(
                    'Fecha Final',
                    required=True,
                    help='Aquí se coloca la fecha de final del periodo'),
        'ip_usuario':fields.char(
                    'Ip de usuario',
                    size=15,
                    help='Indica de que ip se esta haciendo'),
        }
   
   
    _defaults={
        'ip_usuario' : lambda self,cr,uid,context: request.httprequest.remote_addr,
            }
    
    def plf_fecha_actividad_etapa(  self, cr, uid, ids, fecha_inicio, 
                                    fecha_fin, fecha_ini_etapa, 
                                    fecha_fin_etapa, context=None):
        fechas={}
        mensaje={}
        if validar_fecha(fecha_inicio, fecha_fin).values()[0]!={}:
            fechas=validar_fecha(fecha_inicio, fecha_fin).values()[1]
            mensaje=validar_fecha(fecha_inicio, fecha_fin).values()[0]
            return {
                'warning':mensaje,
                'value':fechas
                    }
        if fecha_inicio and fecha_fin:
            fecha_inicio=datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_inicio =datetime.date(fecha_inicio)
            fecha_fin=datetime.strptime(fecha_fin, '%Y-%m-%d')
            fecha_fin =datetime.date(fecha_fin)
            fecha_ini_etapa=datetime.strptime(fecha_ini_etapa, '%Y-%m-%d')
            fecha_ini_etapa =datetime.date(fecha_ini_etapa)
            fecha_fin_etapa=datetime.strptime(fecha_fin_etapa, '%Y-%m-%d')
            fecha_fin_etapa =datetime.date(fecha_fin_etapa)
            if cmp(fecha_ini_etapa,fecha_inicio)==1 or cmp(fecha_fin,fecha_fin_etapa)==1:
                fechas={
                    'fecha_inicio':'',
                    'fecha_fin':'',
                        }
                mensaje={
                    'title':('Error de fecha'),
                    'message':('Las fechas de la actividad no se encuentran\
                                dentro del rango de fechas establacido para\
                                la etapa '),
                    }
            return {
                'warning':mensaje,
                'value':fechas
                    }
    
    def plf_limpiar_fecha_actividad_etapa(self, cr, uid, ids, fecha_inicio, context=None):
        return limpiar_campo_fecha(fecha_inicio)
        
    def plf_tipo_planificacion_id(self, cr, uid, ids, fecha_inicio,fecha_fin, context=None):
        if not fecha_inicio:
            raise osv.except_osv(('Fechas de la etapa no definida!'), 
                                ('Seleccione una fecha inicial y una fecha final.'))
        if not fecha_fin:
            raise osv.except_osv(('Fechas de la etapa no definida!'), 
                                ('Seleccione una fecha inicial y una fecha final.'))
        return True
    
