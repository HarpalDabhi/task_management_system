from odoo import _, api, fields, models

class TaskInfo(models.Model):
    _name = "sub.task.info"
    _description = 'Sub Task Basic Information'
    _rec_name ="hm_sub_task_name"


    parant_task_id = fields.Many2one(comodel_name="task.info",string="Parent Task")
    hm_sub_task_name = fields.Char("Task Name",required=True)
    hm_sub_task_assignee_id = fields.Many2one(comodel_name="res.partner",required=False,string="Assignee")
    # hm_sub_task_status = fields.Selection(selection=[
    #     "incomplete","Incomplete",
    #     "in_progress","InProgress",
    #     "complete","Complete",
    # ],default="incomplete",string="Status")


