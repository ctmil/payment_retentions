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

from openerp.osv import fields, osv

class payment_retention(osv.osv):
    _name = 'payment.retention'
    _description = 'Payment Tax Retention'

    def _get_retention_agent(self, cr, uid, ids,field_name, args, context=None):
        res={}
        for id in self.browse(cr, uid, ids):
            if id.voucher_id:
                res[id.id] = id.voucher_id.partner_id.name
            else:
                res[id.id] = ""
        return res

    def _get_retention_agent_cuit(self, cr, uid, ids,field_name, args, context=None):
        res={}
        for id in self.browse(cr, uid, ids):
            if id.voucher_id:
                res[id.id] = id.voucher_id.partner_id.vat
            else:
                res[id.id] = ""
        return res


    _columns = {
        'voucher_id': fields.many2one('account.voucher','id','Voucher ID'),
	'certificate_nbr': fields.char('Certificate Number',size=32),
	'amount': fields.float('Amount'),
	'retention_agent': fields.function(_get_retention_agent,string='Retention Agent'),
	'retention_agent_cuit': fields.function(_get_retention_agent_cuit,string='Retention Agent VAT'),
	'tax_id': fields.many2one('account.tax','id','Tax ID'),
	'state_id': fields.many2one('res.country.state','id','State ID')
    }

payment_retention()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
