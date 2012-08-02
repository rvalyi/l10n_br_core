# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2010                                                            #
# @author Raphaël Valyi, Renato Lima						#
#                                                                               #
#This program is free software: you can redistribute it and/or modify           #
#it under the terms of the GNU Affero General Public License as published by    #
#the Free Software Foundation, either version 3 of the License, or              #
#(at your option) any later version.                                            #
#                                                                               #
#This program is distributed in the hope that it will be useful,                #
#but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#GNU Affero General Public License for more details.                            #
#                                                                               #
#You should have received a copy of the GNU Affero General Public License       #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#################################################################################

from osv import fields, osv


class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
                'origin': fields.selection((('0', 'Nacional'), ('1', 'Internacional'), ('2', 'Inter. Adiquirido Internamente')), 'Origem'),
                }
    _defaults = {
                 'origin': '0',
                 }

product_template()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
