from odoo import _, api, fields, models

class TaskInfo(models.Model):
    _name = "task.info"
    _description = 'Task Basic Information'
    _rec_name ="hm_task_name"


    hm_task_name = fields.Char("Task Name",required=True)
    hm_task_manager_id = fields.Many2one(comodel_name="res.partner",required=True,string="Manager")
    hm_task_assignee_ids = fields.Many2many(comodel_name="res.partner",required=True,string="Assignee")
    hm_task_start_date = fields.Date("Start Date",default=fields.Date.today())
    hm_task_end_date = fields.Date("End Date")
