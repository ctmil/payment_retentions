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


class account_voucher(osv.osv):

    _name = 'account.voucher'
    _description = 'Accounting Voucher'
    _inherit = 'account.voucher'

    _columns = {
	'retention_ids': fields.one2many('payment.retention','voucher_id','Retention IDs',readonly=True, states={'draft':[('readonly',False)]})
    }

    def proforma_voucher(self, cr, uid, ids, context=None):
        """ Creates the journal entries for the payment retentions lines """
	
        if context is None:
            context = {}
        move_pool = self.pool.get('account.move')
        move_line_pool = self.pool.get('account.move.line')
        for voucher in self.browse(cr, uid, ids, context=context):
            company_currency = self._get_company_currency(cr, uid, voucher.id, context)
            current_currency = self._get_current_currency(cr, uid, voucher.id, context)
            # we select the context to use accordingly if it's a multicurrency case or not
            context = self._sel_context(cr, uid, voucher.id, context)
            # But for the operations made by _convert_amount, we always need to give the date in the context
            ctx = context.copy()
            ctx.update({'date': voucher.date})
            # Create the account move record.
            move_id = move_pool.create(cr, uid, self.account_move_get(cr, uid, voucher.id, context=context), context=context)
            # Get the name of the account_move just created
            name = move_pool.browse(cr, uid, move_id, context=context).name
	    for retention in self.pool.get('payment.retention').browse(cr,uid,voucher.retention_ids,context=context):
		    dict_move_line = self.first_move_line_get(cr,uid,voucher.id, move_id, company_currency, current_currency, context)	
		    if voucher.type == 'sale':
		    	account_id = retention.id.tax_id.account_paid_id.id
			dict_move_line['credit'] = 0
			dict_move_line['debit'] = retention.id.amount
		    else:
		    	account_id = retention.id.tax_id.account_collected_id.id
			dict_move_line['credit'] = retention.id.amount
			dict_move_line['debit'] = 0
		    dict_move_line['account_id'] = account_id
		    move_line_id = move_line_pool.create(cr,uid,dict_move_line,context)
	            # Create the second line of the retention
		    if voucher.type == 'sale':
		   	    account_id = voucher.partner_id.property_account_receivable.id	     
			    dict_move_line['credit'] = retention.id.amount
			    dict_move_line['debit'] = 0
		    else:
		   	    account_id = voucher.partner_id.property_account_payable.id	     
			    dict_move_line['credit'] = 0
   			    dict_move_line['debit'] = retention.id.amount
		    dict_move_line['account_id'] = account_id
		    move_line_id = move_line_pool.create(cr,uid,dict_move_line,context)

        return super(account_voucher, self).proforma_voucher(cr, uid, ids, context=context)
	

account_voucher()

