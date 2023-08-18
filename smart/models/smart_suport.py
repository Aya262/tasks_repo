from odoo import models,fields ,api

class SmartSupport(models.Model):
    _name='smart.support'

    total_amount=fields.Float("Total Amount",digits="Amount precision")


class Tax_smart_support(models.Model):
    _inherit='smart.support'

    total_amount_with_tax=fields.Float("Total Amount With Tax" ,digits="Amount precision" ,compute="_compute_tax")

    @api.depends('total_amount')
    def _compute_tax(self):
        for record in self:
            record.total_amount_with_tax=record.total_amount-record.total_amount*(5/100)