# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = False
        template_id = self.env['mail.template'].search([('id', '=', self.env.user.so_template_id)]).id
        print("TEMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", template_id)
        if template_id :
            return template_id
        else :
            if force_confirmation_template or (self.state == 'sale' and not self.env.context.get('proforma', False)):
                template_id = int(self.env['ir.config_parameter'].sudo().get_param('sale.default_confirmation_template'))
                template_id = self.env['mail.template'].search([('id', '=', template_id)]).id
                if not template_id:
                    template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.mail_template_sale_confirmation', raise_if_not_found=False)
            if not template_id:
                template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.email_template_edi_sale', raise_if_not_found=False)

            return template_id