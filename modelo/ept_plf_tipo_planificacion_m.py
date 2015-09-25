#-*-coding: utf-8-*-
from openerp.osv import fields, osv
from openerp.http import request
import socket, time

class ept_plf_tipo_planificacion(osv.osv):
	_name='ept_plf.tipo_planificacion'
	_rec_name = 'nombre_tipo_planificacion'
	
	_columns={
		'nombre_tipo_planificacion':fields.char(
						'Nombre',
						size=50, 
						required=True,
						help='Este es el nombre del tipo de planificación'),
		'active':fields.boolean(
						'Activo',
						help='Indica si esta o no activo el estado'),
		'ip_usuario':fields.char(
						'Ip de usuario',
						size=15,
						help='Indica de que ip se esta haciendo'),
	}
	_defaults={
		'active':True,
		'ip_usuario' : lambda self,cr,uid,context: request.httprequest.remote_addr
		
	}
