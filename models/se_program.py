# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentList(models.Model):
    _name = 'se.program'
    _description = 'program List'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    parent_program = fields.Char(string="Parent Program")
    program_no = fields.Char(string="Program No.")
    minimum_Unit_Load= fields.Char(string="Minimum Unit Load")
    maximum_Unit_Load = fields.Char(string="Maximum Unit Load")
    evaluation_Type = fields.Char(string="Evaluation Type")
    reg_fee = fields.Char(string="Registration Fee")
    UGC_Program_Cluster = fields.Selection([('M','Agriculture'),('F','arts')],'UGC Program Cluster')
    UGC_Program_Subject = fields.Selection([('M','Agriculture'),('F','arts')],'UGC Program Cluster')
    field_name = fields.Text(string='Eligibility',)
    
    subjects_ids = fields.Many2many('se.subject', string= 'Subjects')
    
    


class StudentListp(models.Model):
    _name = 'program.listp'
    _description = 'program Listp'

    name = fields.Char(string="Program Name")
    code = fields.Char(string="Code")
    parent_program = fields.Char(string="Parent Program")
    
