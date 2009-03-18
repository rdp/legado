#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2003-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id: _SelectFamily.py 9912 2008-01-22 09:17:46Z acraphae $

#-------------------------------------------------------------------------
#
# internationalization
#
#-------------------------------------------------------------------------
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# gramps modules
#
#-------------------------------------------------------------------------
from DisplayModels import FamilyModel
from _BaseSelector import BaseSelector

#-------------------------------------------------------------------------
#
# SelectFamily
#
#-------------------------------------------------------------------------
class SelectFamily(BaseSelector):

    def get_window_title(self):
        return _("Select Family")
        
    def get_model_class(self):
        return FamilyModel

    def get_column_titles(self):
        return [
            (_('ID'),      75, BaseSelector.TEXT),
            (_('Father'), 200, BaseSelector.TEXT),
            (_('Mother'), 200, BaseSelector.TEXT),
            ]

    def get_from_handle_func(self):
        return self.db.get_family_from_handle
        
    def get_handle_column(self):
        return 6
    
    def column_order(self):
        """
        returns a tuple indicating the column order of the model
        """
        return self.db.get_family_list_column_order()
    
    def column_view_names(self):
        """
        Get correct column view names on which model is based
        """
        import DataViews
        return DataViews.FamilyListView.COLUMN_NAMES