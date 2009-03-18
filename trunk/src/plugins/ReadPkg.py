#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License,  or
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
# $Id: ReadPkg.py 10365 2008-03-21 22:25:44Z bmcage $

# Written by Alex Roitman, largely based on ReadNative.py by Don Allingham 

"Import from Gramps package"

#-------------------------------------------------------------------------
#
# Python modules
#
#-------------------------------------------------------------------------
import os
import tarfile
from gettext import gettext as _

#------------------------------------------------------------------------
#
# Set up logging
#
#------------------------------------------------------------------------
import logging
log = logging.getLogger(".ReadPkg")

#-------------------------------------------------------------------------
#
# GNOME/GTK+ modules
#
#-------------------------------------------------------------------------
import gtk

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
import const
from GrampsDbUtils import gramps_db_reader_factory
from QuestionDialog import ErrorDialog, WarningDialog
import Utils
from PluginUtils import register_import

#-------------------------------------------------------------------------
#
#
#
#-------------------------------------------------------------------------
def impData(database, name, cb=None, cl=0):
    # Create tempdir, if it does not exist, then check for writability
    #     THE TEMP DIR is named as the filname.gpkg.media and is created
    #     in the mediapath dir of the family tree we import too
    oldmediapath = database.get_mediapath()
    #use home dir if no media path
    media_path = Utils.media_path(database)
    media_dir = "%s.media" % os.path.basename(name)
    tmpdir_path = os.path.join(media_path, media_dir)
    if not os.path.isdir(tmpdir_path):
        try:
            os.mkdir(tmpdir_path, 0700)
        except:
            ErrorDialog( _("Could not create media directory %s") % 
                         tmpdir_path )
            return
    elif not os.access(tmpdir_path, os.W_OK):
        ErrorDialog(_("Media directory %s is not writable") % tmpdir_path)
        return
    else:    
        # mediadir exists and writable -- User could have valuable stuff in
        # it, have him remove it!
        ErrorDialog(_("Media directory %s exists. Delete it first, then"
                      " restart the import process") % tmpdir_path)
        return
    try:
        archive = tarfile.open(name)
        for tarinfo in archive:
            archive.extract(tarinfo, tmpdir_path)
        archive.close()
    except:
        ErrorDialog(_("Error extracting into %s") % tmpdir_path)
        return

    imp_db_name = os.path.join(tmpdir_path, const.XMLFILE)  

    importer = gramps_db_reader_factory(const.APP_GRAMPS_XML)
    info = importer(database, imp_db_name, cb)
    newmediapath = database.get_mediapath()
    #import of gpkg should not change media path as all media has new paths!
    if not oldmediapath == newmediapath :
        database.set_mediapath(oldmediapath)

    # Set correct media dir if possible, complain if problems
    if oldmediapath is None:
        database.set_mediapath(tmpdir_path)
        WarningDialog(
                _("Base path for relative media set"),
                _("The base media path of this family tree has been set to "
                    "%s. Consider taking a simpler path. You can change this "
                    "in the Preferences, while moving your media files to the "
                    "new position, and using the media manager tool, option "
                    "'Replace substring in the path' to set"
                    " correct paths in your media objects."
                 ) % tmpdir_path)
    else:
        WarningDialog(
                _("Cannot set base media path"),
                _("The family tree you imported into already has a base media "
                    "path: %(orig_path)s. The imported media objects however "
                    "are relative from the path %(path)s. You can change the "
                    "media path in the Preferences or you can convert the "
                    "imported files to the existing base media path. You can "
                    "do that by moving your media files to the "
                    "new position, and using the media manager tool, option "
                    "'Replace substring in the path' to set"
                    " correct paths in your media objects."
                    ) % {'orig_path': oldmediapath, 'path': tmpdir_path}
                    )
    
    # Remove xml file extracted to media dir we imported from
    os.remove(imp_db_name)
    
    return info

##     files = os.listdir(tmpdir_path) 
##     for filename in files:
##         os.remove(os.path.join(tmpdir_path, filename))
##     os.rmdir(tmpdir_path)

#------------------------------------------------------------------------
#
# Register with the plugin system
#
#------------------------------------------------------------------------
_mime_type = 'application/x-gramps-package'
_filter = gtk.FileFilter()
_filter.set_name(_('GRAMPS packages'))
_filter.add_mime_type(_mime_type)
_format_name = _('GRAMPS package')

register_import(impData, _filter, [_mime_type], 0, _format_name)
