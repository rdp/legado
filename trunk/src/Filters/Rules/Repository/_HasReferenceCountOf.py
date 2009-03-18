#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2007  Stephane Charette
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

# $Id: _HasReferenceCountOf.py 8892 2007-08-30 08:04:28Z s_charette $

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
from Filters.Rules._HasReferenceCountBase import HasReferenceCountBase

#-------------------------------------------------------------------------
# "Repositories with a certain reference count"
#-------------------------------------------------------------------------
class HasReferenceCountOf(HasReferenceCountBase):
    """Repositories with a reference count of <count>"""

    name        = _('Repositories with a reference count of <count>')
    description = _("Matches repositories with a certain reference count")
