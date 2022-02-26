# -*- coding: utf-8 -*-

#from typing_extensions import Required
#from unicodedata import name
from operator import index
from os import times
from pickle import TRUE
from time import time
from odoo import models, fields, api

class Course(models.Model):
    _name='open_academy.course'
    _description='course'
    name=fields.Char(string='Titulo',required=True)
    description=fields.Text()
    duracion = fields.Integer(string='Tiempo [Años]')
    
 # vvvv para ejercicio Many2one  desde aqui vvvv

    id_responsable=fields.Many2one('res.users',string="responsable",index=True)
    # vvvv para ejercicio Many2one 
   

  # EJERCICIO  ( 2 ) ONE2MANY INICIO 
    id_session=fields.One2many('open_academy.session','id_course', string='sesiones')
  # EJERCICIO  ( 2 ) ONE2MANY FIN


class Session(models.Model):
    _name = "open_academy.session"
    _description="Sessiones de open academy"

    name = fields.Char( string="Nombre", required=True )
    start_date = fields.Date(string="Fecha de inicio")
    duration = fields.Float( string="Duración" ,digits=(6,2), help='duración en dias')
    seats = fields.Integer(string="número de asientos")
 
    # vvvv para ejercicio Many2one  desde aqui vvvv

    id_instructor = fields.Many2one('res.partner', string="Instructor",
                                    domain=['|', ('instructor', '=', True),
                                            ('category_id.name', 'ilike', "Teacher")])
  #  fin DOMAIN EDIT
    id_course=fields.Many2one('open_academy.course',string='Curso' ,index=True)
    #  para ejercicio Many2one 

  # EJERCICIO  ( 2 ) MANY2MANY INICIO 
    id_asistente= fields.Many2many('res.partner',string="asistentes")
    # EJERCICIO  ( 2 ) MANY2MANY FIN