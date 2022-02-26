# -*- coding: utf-8 -*-

# añadido ejecicio ( 3 ) inicio

from email.policy import default
from pickle import FALSE
from odoo import models, fields, api

class Partner(models.Model):
    _inherit="res.partner"

    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('open_academy.session', string="Sesiones Atendidas", readonly=True)


# añadido ejecicio ( 3 ) fin