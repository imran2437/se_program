# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubjectCore(models.Model):
    _name = 'se.subject'
    _description = 'subject List'

    name = fields.Char(string="Name")
    course= fields.Selection([('M','BAA'),('F','MBA')],'Course')
    code = fields.Char(string="Code")
    type = fields.Char(string="Type")
    subject_type = fields.Selection([('M','Agriculture'),('F','arts')],'Subject Type')
    company = fields.Selection([('M','My Company'),('F','X Company')],'Company')
   
    grade_weightage = fields.Selection(
        string=' Grade Weightage',
        selection=[('valor1', 'valor1'), ('valor2', 'valor2')]
    )
    