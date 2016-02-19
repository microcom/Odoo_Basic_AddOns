# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
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


from datetime import datetime
from openerp import api, fields, models
from openerp.tools.misc import formatLang


PAGE_SIZE = 3


# direct access at http://127.0.0.1:8069/report/html/city_partner.print_city_partner/3


class PrintCityPartner(models.AbstractModel):
    _name = 'report.city_partner.print_city_partner'

    def paginate(self, partner):
        city = partner.city
        street = partner.street
        neighbors = []
        for res_partner in partner.search([('city', '=', city)]):
            neighbors.append(res_partner)
        pages = []
        page_max = (len(neighbors) - 1) / PAGE_SIZE + 1
        for rank in range(0, len(neighbors), PAGE_SIZE):
            pages.append({
                'page_no': rank / PAGE_SIZE + 1,
                'page_max': page_max,
                'neighbors': neighbors[rank:rank+PAGE_SIZE],
            })
        return pages


    @api.multi
    def render_html(self, data=None):
        Report = self.env['report']
        report = Report._get_report_from_name('city_partner.print_city_partner')
        records = self.env['res.partner'].browse(self.ids)
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': records,
            'data': data,
            'paginate': self.paginate,
        }
        return Report.render('city_partner.print_city_partner', docargs)
