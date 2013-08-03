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

    _columns = {
        'voucher_id': fields.many2one('account.voucher','id','Voucher ID'),
	'certificate_nbr': fields.char('Certificate Number',size=32),
	'amount': fields.float('Amount'),
	'retention_agent': fields.char('Retention Agent',size=32),
	'retention_agent_cuit': fields.char('Retention Agent CUIT',size=32)
    }

payment_retention()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
