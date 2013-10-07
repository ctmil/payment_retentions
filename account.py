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


class account_tax(osv.osv):

    _name = 'account.tax'
    _inherit = 'account.tax'

    _columns = {
	'retention_ids': fields.one2many('payment.retention','voucher_id','Retention IDs')
    }

account_tax()

class account_fiscal_position_retention(osv.osv):

	_name = 'account.fiscal.position.retention'
	_description = 'Allowed taxes in retention'

	_columns = {
		'position_id': fields.many2one('account.fiscal.position','Fiscal position'),
		'retention_tax_id': fields.many2one('account.tax','Tax')
		}

account_fiscal_position_retention()

class account_fiscal_position(osv.osv):

    _name = 'account.fiscal.position'
    _inherit = 'account.fiscal.position'

    _columns = {
	'tax_retention_ids': fields.one2many('account.fiscal.position.retention','retention_tax_id','Allowed Tax Ids in Retentions')
    }

account_fiscal_position()
