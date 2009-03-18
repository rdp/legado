#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2007  Donald N. Allingham
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

# $Id: mediaref.py 10103 2008-02-24 13:55:55Z acraphae $

"""
Media Reference class for GRAMPS.
"""

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from gen.lib.secondaryobj import SecondaryObject
from gen.lib.privacybase import PrivacyBase
from gen.lib.srcbase import SourceBase
from gen.lib.notebase import NoteBase
from gen.lib.refbase import RefBase
from gen.lib.attrbase import AttributeBase

#-------------------------------------------------------------------------
#
# MediaObject References for Person/Place/Source
#
#-------------------------------------------------------------------------
class MediaRef(SecondaryObject, PrivacyBase, SourceBase, NoteBase, RefBase,
               AttributeBase):
    """Media reference class."""
    def __init__(self, source=None):
        PrivacyBase.__init__(self, source)
        SourceBase.__init__(self, source)
        NoteBase.__init__(self, source)
        RefBase.__init__(self, source)
        AttributeBase.__init__(self, source)

        if source:
            self.rect = source.rect
        else:
            self.rect = None

    def serialize(self):
        """
        Convert the object to a serialized tuple of data.
        """
        return (PrivacyBase.serialize(self),
                SourceBase.serialize(self),
                NoteBase.serialize(self),
                AttributeBase.serialize(self),
                RefBase.serialize(self),
                self.rect)

    def unserialize(self, data):
        """
        Convert a serialized tuple of data to an object.
        """
        (privacy, source_list, note_list,attribute_list,ref,self.rect) = data
        PrivacyBase.unserialize(self, privacy)
        SourceBase.unserialize(self, source_list)
        NoteBase.unserialize(self, note_list)
        AttributeBase.unserialize(self, attribute_list)
        RefBase.unserialize(self, ref)
        return self

    def get_text_data_child_list(self):
        """
        Return the list of child objects that may carry textual data.

        @return: Returns the list of child objects that may carry textual data.
        @rtype: list
        """
        return self.attribute_list + self.source_list

    def get_sourcref_child_list(self):
        """
        Return the list of child secondary objects that may refer sources.

        @return: Returns the list of child secondary child objects that may 
                refer sources.
        @rtype: list
        """
        return self.attribute_list

    def get_note_child_list(self):
        """
        Return the list of child secondary objects that may refer notes.

        @return: Returns the list of child secondary child objects that may 
                refer notes.
        @rtype: list
        """
        return self.attribute_list + self.source_list

    def get_referenced_handles(self):
        """
        Return the list of (classname, handle) tuples for all directly
        referenced primary objects.
        
        @return: List of (classname, handle) tuples for referenced objects.
        @rtype: list
        """
        ret = self.get_referenced_note_handles()
        if self.ref:
            ret += [('MediaObject', self.ref)]
        return ret

    def get_handle_referents(self):
        """
        Return the list of child objects which may, directly or through
        their children, reference primary objects.
        
        @return: Returns the list of objects refereincing primary objects.
        @rtype: list
        """
        return self.attribute_list + self.source_list

    def set_rectangle(self, coord):
        """Set subection of an image."""
        self.rect = coord

    def get_rectangle(self):
        """Return the subsection of an image."""
        return self.rect