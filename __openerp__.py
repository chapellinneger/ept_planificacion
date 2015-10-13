<<<<<<< HEAD
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Planificación  de las Entidades Politico Territoriales',
    'version': '1.0',
    'depends': ['base_setup','ept_entidades'],
    'author': 'Jueventud Productiva Bicentenaria',
    'category': '',
    'description': """
    """,
    'update_xml': [],
    "data" : [
        'vistas/ept_plf_periodos_v.xml',
        'vistas/ept_plf_etapas_v.xml',
        'vistas/ept_plf_tipo_planificacion_v.xml',
        'vistas/ept_plf_tipo_planificacion_v.xml',
        'datos/ept_plf_tipo_planificacion_d.xml',
        ],
    'installable': True,
    'auto_install': False,
=======
#-*-coding: utf-8-*-

{
	'name':'PLanificacion EPT',
	'version':'1.0',
	'depends':['base'],
	'author':'Equipo CFG-JPV',
	'category':'Planificacion FCI',
	'description': """Modulos de Sistemas de Carga de Proyectos EPT""",
	'update_xml':[],
	'data':[
		#~ 'views/cfg_entidad_view.xml',
		'vista/ept_plf_tipo_planificacion_v.xml',
		'vista/ept_plf_menu_v.xml',
		
	],
	'installable':True,
	'auto_install':False,
>>>>>>> 6326cbe788f6e828bec880cd4e3282b4aaf01650
}
