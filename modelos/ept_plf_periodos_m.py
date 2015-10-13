# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.http import request
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import *
from ept_plf_comunes import *
import datetime

class ept_plf_periodos(osv.osv):
    _name='ept_plf.periodos'
    _rec_name='periodo_fiscal'
    _description=u"""Estos son los periodos para la gestión de los\
                proyectos de las Entidades Politicos Territoriales"""
                
    def plf_anio_seleccion(self, cursor, user_id, context=None):
        format="%Y"
        anio_actual=date.today()
        anio_ant=anio_actual+relativedelta(years=-1)
        anio_prox=anio_actual+relativedelta(years=+1)
        anio_ant=anio_ant.strftime(format)
        anio_actual=anio_actual.strftime(format)
        anio_prox=anio_prox.strftime(format)
        return (
            (anio_ant,anio_ant),
            (anio_actual,anio_actual),
            (anio_prox,anio_prox))
    
    _columns={ 
        'periodo_fiscal':fields.selection(
                    plf_anio_seleccion,
                    'Periodo Fiscal',
                    required=True,
                    help='Aquí se selecciona el año del periodo fiscal'),
        'fecha_inicio':fields.date(
                    'Fecha de Inicio',
                    readonly=True,
                    help='Aquí se coloca la fecha de inicio del periodo'),
        'fecha_fin':fields.date(
                    'Fecha Final',
                    readonly=True,
                    help='Aquí se coloca la fecha de final del periodo'),
         'active':fields.boolean(
                    'Activo',
                    help="""Si esta activo el motor lo incluira en la 
                    vista."""),
        'ip_usuario':fields.char(
                    'Ip de usuario',
                    size=15,
                    help='Indica de que ip se esta haciendo'),
        'etapas_ids':fields.one2many(
                        'ept_plf.etapas',
                        'periodo_id',
                        'Etapas',
                        help='Aqui se crearan las etapas que conformaran\
                                el periodo fiscal',
                        #ondelete='restrict'
                        ),
        'estado':fields.selection(
                    [('inactivo', 'Inactivo'),
                    ('activo', 'Activo')],
                     'Estado:',
                    help='Aquí se selecciona el estado, si esta activo,\
                        el sistema tomara este periodo como la\
                        planificacion ṕara todas las actividades.'),
        }
    
    _defaults={
        'active':True,
        'ip_usuario' : lambda self,cr,uid,context: request.httprequest.remote_addr,
        'estado' :'inactivo',
            }
    _order = "periodo_fiscal desc"
    
    _sql_constraints = [
        ('periodo_fiscal_unico', 'unique (periodo_fiscal)', 'El periodo fiscal ya existe')
    ]


    def plf_fecha_inicio_fin(self, cr, uid, ids, periodo_fiscal, context=None):
        fechas={}
        if periodo_fiscal:
            fecha_inicio="%s-01-01" % (periodo_fiscal,)
            fecha_fin="%s-12-31" % (periodo_fiscal,)
            
            fechas={
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'etapas_ids':'',
                }
            
            return {
                'value':fechas
                    }
    def create(self,cr,uid,vals,context=None):
        fechas=self.plf_fecha_inicio_fin(cr, uid,[], vals['periodo_fiscal'], context).values()[0]
        periodo_id=super(ept_plf_periodos, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,periodo_id,fechas,context=context)
        return periodo_id
