# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2009  Renato Lima - Akretion                                    #
#                                                                               #
#This program is free software: you can redistribute it and/or modify           #
#it under the terms of the GNU General Public License as published by           #
#the Free Software Foundation, either version 3 of the License, or              #
#(at your option) any later version.                                            #
#                                                                               #
#This program is distributed in the hope that it will be useful,                #
#but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#GNU General Public License for more details.                                   #
#                                                                               #
#You should have received a copy of the GNU General Public License              #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#################################################################################

from osv import fields, osv

class l10n_br_account_cst_template(osv.osv):
    _name = 'l10n_br_account.cst.template'
    _description = 'Modelo de Código de Situação Tributária'
    _columns = {
                'code': fields.char('Codigo', size=8,required=True),
                'name': fields.char('Descrição', size=64),
                'tax_code_template_id': fields.many2one('account.tax.code.template', 'Código do Imposto',required=True),
                }

	def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=80):
		if not args:
		    args = []
		if context is None:
		    context = {}
		ids = self.search(cr, user, ['|',('name',operator,name),('code',operator,name)] + args, limit=limit, context=context)
		return self.name_get(cr, user, ids, context)
    
	def name_get(self, cr, uid, ids, context=None):
        	if not ids:
            		return []
        	reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
        	res = []
		for record in reads:
		    name = record['name']
		    if record['code']:
			name = record['code'] + ' - '+name
		    res.append((record['id'], name))
		return res
    
l10n_br_account_cst_template()

class l10n_br_account_cst(osv.osv):
    _name = 'l10n_br_account.cst'
    _description = 'Código de Situação Tributária'
    _columns = {
                'code': fields.char('Codigo', size=8,required=True),
                'name': fields.char('Descrição', size=64),
                'tax_code_id': fields.many2one('account.tax.code', 'Modelo do Imposto',required=True),
                }
	
	def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=80):
		if not args:
		    args = []
		if context is None:
		    context = {}
		ids = self.search(cr, user, ['|',('name',operator,name),('code',operator,name)] + args, limit=limit, context=context)
		return self.name_get(cr, user, ids, context)
    
    	def name_get(self, cr, uid, ids, context=None):
		if not ids:
		    return []
		reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
		res = []
		for record in reads:
		    name = record['name']
		    if record['code']:
			name = record['code'] + ' - '+name
		    res.append((record['id'], name))
		return res
    
l10n_br_account_cst()
