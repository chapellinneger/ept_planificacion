# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.http import request
from datetime import datetime, date, time, timedelta
from ept_plf_comunes import *


class ept_plf_etapas(osv.osv):
    _name='ept_plf.etapas'
    _rec_name='nombre'
    _description=u"""Estas son las etapas que conformaran los periodos\
                     para la gestión de los proyectos de las Entidades\
                     Politicos Territoriales"""
        
    _columns={
        'nombre':fields.char(
                    'Nombre de la Etapa',
                    size=80,
                    required=True,
                    help='Nombre de la etapa a registrar'),
        'fecha_inicio':fields.date(
                    'Fecha de Inicio',
                    required=True,
                    help='Aquí se coloca la fecha de inicio del periodo'),
        'fecha_fin':fields.date(
                    'Fecha Final',
                    required=True,
                    help='Aquí se coloca la fecha de final del periodo'),
        'rango_accion':fields.selection(
                    [('todas', 'Todas las Entidades'),
                    ('algunas', 'Algunas Entidades')],
                     'Aplicar a:',
                    required=True,
                    help='Aquí se selecciona a cuales entidades se desean\
                     aplicar las reglas de la etapa que se esta creando.'),
         'active':fields.boolean(
                    'Activo',
                    help="""Si esta activo el motor lo incluira en la 
                    vista."""),
        'ip_usuario':fields.char(
                    'Ip de usuario',
                    size=15,
                    help='Indica de que ip se esta haciendo'),
        'periodo_id':fields.many2one(
                    'ept_plf.periodos',
                    """Periodos""",
                    required=True,
                    ondelete='cascade',),
        'actividades_etapas_ids':fields.one2many(
                                'ept_plf.actividad_etapas',
                                'etapas_id',
                                'Actividades',
                                 help='Aqui se seleccionaran las actividades\
                                    y las fechas a realizar en cada etapa',
                                #ondelete='restrict'
                                ),
        'tipo_entidades_ids':fields.many2many(
                                'ept_ent.tipo_entidades',
                                'ept_plf_etapas_tipo_entidades_rel',
                                'etapa_id',
                                'tipo_entidad_id',
                                'Tipos de Entidades',
                                required=False,
                                help='Aqui se seleccionaran los tipos de\
                                    entidades a los que se le aplicara la etapa' ),
        'entidades_ids': fields.many2many(
                                'ept_ent.entidades', 
                                'ept_plf_entidad_etapa_rel', 
                                'etapa_id', 
                                'entidad_id', 
                                'Entidades',
                                copy=False,
                                required=False,
                                help='Aqui se seleccionaran el grupo de\
                                    entidades a las que se le aplicara la etapa'
                                ),
        }
   
   
    _defaults={
        'active':True,
        'ip_usuario' : lambda self,cr,uid,context: request.httprequest.remote_addr,
            }
    _sql_constraints = [
        ('nombre_unico', 'unique (nombre)', 'El nombre de la etapa no debe repetirse')
    ]
    
    def plf_fecha_etapa(self, cr, uid, ids, fecha_inicio, fecha_fin, context=None):
        fechas={}
        mensaje={}
            
        if validar_fecha(fecha_inicio, fecha_fin).values()[0]!={}:
            fechas=validar_fecha(fecha_inicio, fecha_fin).values()[1]
            mensaje=validar_fecha(fecha_inicio, fecha_fin).values()[0]
            return {
                'warning':mensaje,
                'value':fechas
                    }
        if fecha_fin:
            fechas={
                'actividades_etapas_ids':''
                }
            return {
                'value':fechas
                    }
        
    def plf_limpiar_fecha_etapa(self, cr, uid, ids, fecha_inicio, context=None):
        fechas={}
        mensaje={}
        if fecha_inicio:
            hoy=date.today()
            fecha_inicio=datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_inicio =datetime.date(fecha_inicio)
            if cmp(hoy,fecha_inicio)==1:
                mensaje={
                    'title':('Error de fecha'),
                    'message':('La fecha de inicio no puede ser menor\
                                a la fecha de hoy'),
                    }
                fechas={
                    'fecha_inicio':'',
                    }
            else:
                fechas={
                    'fecha_fin':'',
                    'actividades_etapas_ids':''
                    }
        return {
            'warning':mensaje,
            'value':fechas
                }
            
    def plf_limpiar_rango_accion(self, cr, uid, ids, rango_accion, context=None):
        limpiar={}
        if rango_accion:
            limpiar={
                'tipo_entidades_ids':'',
                'entidades_ids':''
                }
        return {
            'value':limpiar
                }
    def create(self,cr,uid,vals,context=None):
        vals.update({
                'nombre':vals['nombre'].upper()
                })
        return super(ept_plf_etapas, self).create(cr, uid, vals, context=context)
      
        

