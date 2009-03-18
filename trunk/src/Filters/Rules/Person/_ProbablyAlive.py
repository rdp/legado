#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
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

# $Id: _ProbablyAlive.py 9912 2008-01-22 09:17:46Z acraphae $

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from Utils import probably_alive
from Filters.Rules._Rule import Rule
import DateHandler

#-------------------------------------------------------------------------
# "People probably alive"
#-------------------------------------------------------------------------
class ProbablyAlive(Rule):
    """People probably alive"""

    labels      = [_("On date:")]
    name        =  _('People probably alive')
    description = _("Matches people without indications of death that are not too old")
    category    = _('General filters')

    def prepare(self,db):
        try:
            self.current_date = DateHandler.parser.parse(unicode(self.list[0]))
        except:
            self.current_date = None

    def apply(self,db,person):
        return probably_alive(person,db,self.current_date)
