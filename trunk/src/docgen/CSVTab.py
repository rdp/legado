#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2004  Donald N. Allingham
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

# $Id: CSVTab.py 10406 2008-03-28 07:34:40Z acraphae $

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
import csv

#-------------------------------------------------------------------------
#
# gramps modules
#
#-------------------------------------------------------------------------
from docgen import TabbedDoc

class CSVTab(TabbedDoc):

    def __init__(self, columns):
        TabbedDoc.__init__(self, columns)
        self.filename = None
        self.f = None
        self.dlist = []
        self.writer = None

    def open(self, filename):

        if filename[-4:] != ".csv":
            self.filename = filename + ".csv"
        else:
            self.filename = filename

        self.f = open(self.filename, "wb")
        self.writer = csv.writer(self.f)

    def close(self):
        assert(self.f)
        self.f.close()

    def start_row(self):
        self.dlist = []

    def end_row(self):
        self.writer.writerow(self.dlist)

    def write_cell(self, text):
        self.dlist.append(text)

    def start_page(self):
        pass

    def end_page(self):
        pass

if __name__ == "__main__":


    file = CSVTab(2, 3)
    file.open("test.csv")
    file.start_page()
    for i in [ ('one', 'two', 'three'), ('fo"ur', 'fi,ve', 'six') ]:
        file.start_row()
        for j in i:
            file.write_cell(j)
        file.end_row()
    file.end_page()
    file.close()
