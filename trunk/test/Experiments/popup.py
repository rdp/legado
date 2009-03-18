#!/usr/bin/env python

# example entry.py

import pygtk
pygtk.require('2.0')
import gtk

class EntryExample:
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("GTK Entry")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        vbox = gtk.VBox(True, 0)
        window.add(vbox)
        vbox.show()

        frame = gtk.Frame()
        label = gtk.Label("This is a Normal label")
        frame.add(label)
        
         
        userId = gtk.Entry()
        userId.set_max_length(50)
        userId.connect("activate", self.enter_callback, userId)
        userId.set_text("hello")
        userId.insert_text(" world", len(userId.get_text()))
        userId.select_region(0, len(userId.get_text()))
        
        frame.add(userId)
        vbox.pack_start(frame, True, True, 0)
        userId.show()
        
#        entry = gtk.Entry()
#        entry.set_max_length(50)
#        entry.connect("activate", self.enter_callback, entry)
#        entry.set_text("hello")
#        entry.insert_text(" world", len(entry.get_text()))
#        entry.select_region(0, len(entry.get_text()))
#        entry.set_visibility(False)
#        vbox.pack_start(entry, True, True, 0)
#        entry.show()

        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()
                                  
#        check = gtk.CheckButton("Editable")
#        hbox.pack_start(check, True, True, 0)
#        check.connect("toggled", self.entry_toggle_editable, entry)
#        check.set_active(True)
#        check.show()
#    
#        check = gtk.CheckButton("Visible")
#        hbox.pack_start(check, True, True, 0)
#        check.connect("toggled", self.entry_toggle_visibility, entry)
#        check.set_active(True)
#        check.show()
                                   
        button = gtk.Button("Login")
        button.connect("clicked", lambda w: gtk.main_quit())
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    EntryExample()
    main()
