#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2006  Donald N. Allingham
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

# $Id: _AttrModel.py 9912 2008-01-22 09:17:46Z acraphae $

#-------------------------------------------------------------------------
#
# GTK libraries
#
#-------------------------------------------------------------------------
import gtk

#-------------------------------------------------------------------------
#
# GRAMPS classes
#
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#
# AttrModel
#
#-------------------------------------------------------------------------
class AttrModel(gtk.ListStore):

    def __init__(self, attr_list, db):
        gtk.ListStore.__init__(self, str, str, object)
        self.db = db
        for attr in attr_list:
            self.append(row=[
                str(attr.get_type()), 
                attr.get_value(), 
                attr, 
                ])
