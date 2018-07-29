#!/usr/bin/env python

# found on <http://files.majorsilence.com/rubbish/pygtk-book/pygtk-notebook-html/pygtk-notebook-latest.html#SECTION00430000000000000000>
# simple example of a tray icon application using PyGTK

#mentions for code borrowing

#https://github.com/tobyhodges/timers/blob/master/clitimer.py
#https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file

import time, os, sys

import gtk,gobject
import subprocess

import pynotify
from ConfigParser import SafeConfigParser



win = gtk.Window()
textview = gtk.TextView()
button1 = gtk.Button( "Just Had One")
button2 = gtk.Button( "Skip Smoke")
label1 = gtk.Label( "Hello world")
start_time = 0
current_time = 0
finish_time = 0 
 
def sendmessage(message):
    pynotify.init("Test")
    notice = pynotify.Notification("aha", message)
    notice.show()
    #subprocess.Popen(['notify-send', message])
    return

def message(data=None):
  "Function to display messages to the user."
  msg=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
    gtk.MESSAGE_INFO, gtk.BUTTONS_OK, data)
  msg.run()
  msg.destroy()

def button1_clicked(self ):
    self.set_label( "Just Had One.")
   # text = textbuffer.get_text( startiter, enditer) 
    textbuffer = textview.get_buffer()
    text = textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter())
    label1.set_text(text)
    textbuffer.set_text("01:00:00")
    text = textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter())
    button2.set_label( "skipped smoke")

    clock = time.strftime("%H:%M:%S")
    if ':' in clock :
        hours,minutes, seconds = text.split(':')
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        #convert to seconds
        current_time = int (int(int(hours*60)*60) + int(minutes*60) + int(seconds))

    if ':' in text :
        hours,minutes, seconds = text.split(':')
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        #convert to seconds
        
        start_time = int (int(int(hours*60)*60) + int(minutes*60) + int(seconds))
        finish_time = start_time + current_time
    sendmessage("great")
    print hours
    print start_time

def Skipped_clicked(self):
    #label1.set_label( "skipped smoke")
   # skippedSmokeCount(1)
    #out = open( "test", 'w+')

    #with out as f:
    #    for r in f:
    #        if r == "":
    #            print("first smoke skipped")
    #            out.write(1)
    #        else:
    #            print(r)
    #            print("fount line in file")
    #            out.write(int(r)+1)

    fname = "config.ini"
    if os.path.isfile(fname):
        print("file exists ")



        config = SafeConfigParser()
        config.read('config.ini')

        key1 = config.get('main', 'key1') # -> "value1"
     #   print config.get('main', 'key2') # -> "value2"
    #    print config.get('main', 'key3') # -> "value3"

        # getfloat() raises an exception if the value is not a float
       # a_float = config.getfloat('main', 'a_float')

        # getint() and getboolean() also do this for their respective types
        #an_int = config.getint('main', 'an_int')




      #  config.add_section('main')
        config.set('main', 'key1', str(int(key1)+1))

        with open(fname, 'w') as f:
            config.write(f)
    else:
        print("no such file exists at this time")
        config = SafeConfigParser()
        config.read('config.ini')
        config.add_section('main')
        config.set('main', 'key1', '1')
        with open(fname, 'w') as f:
            config.write(f)
                    
       
    button1_clicked(label1)
    label1.set_text("thanks for skipping the smoke")
    #savings dollar a
    #pack cost 15 for 25 so 60 cents per smoke
    

def hide_app(self,data=None):
    #win.hide_on_delete()
    win.hide()

def close_app(data=None):
 # message(data)
   #win.hide_on_delete()
   #win.hide()
  gtk.main_quit()
   #     self.statusicon.set_tooltip("the window is hidden")

def quit(self):
        #quit the gtk main loop
         gtk.main_quit()
    



def open_app(data=None):

    win.set_border_width(5)
    win.set_title('Widget test')
    win.connect('delete-event', hide_app)
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(400, 200)
    win.set_keep_above(True)
    #win.set_title(title)
    #$win.create_interior()

   # frame = gtk.Frame("Example frame")
   # win.add(frame)

   # w = PyGtkWidget(TEXT)
   # frame.add(w)

    mainbox = gtk.VBox()
    win.add( mainbox)
    # box for text
    text_box1 = gtk.VBox()
    mainbox.pack_start( text_box1 )
  #  label1 = gtk.Label( "Hello world")
    text_box1.pack_start( label1, padding=10)
    label1.show()
    text_box1.show()
    # box for buttons
    button_box1 = gtk.HBox()
    mainbox.pack_end( button_box1)
    # first button
  #  button1 = gtk.Button( "Press me")
    button1.connect( "clicked", button1_clicked)
    button_box1.pack_start( button1)
    button1.show()
    # second button
 #   button2 = gtk.Button( "Big red button")
    button2.connect( "clicked", Skipped_clicked)
    button_box1.pack_start( button2)
    button2.show()
    # show the box
    button_box1.show()

    mainbox.add(textview)

    mainbox.show()

 #  clock = time.strftime("%H:%M:%S")
  #  label1.set_text(clock)
  #  message(data)

#    scrolled_window = gtk.ScrolledWindow()
#    scrolled_window.set_border_width(5)
        # we scroll only if needed
   # scrolled_window.set_policy(
   # gtk.PolicyType.AUTOMATIC, gtk.PolicyType.AUTOMATIC)

   # textview.set_wrap_mode(gtk.WrapMode.WORD)

        # textview is scrolled
#    scrolled_window.add(textview)
#    mainbox.add(scrolled_window)
    win.show_all()
    gobject.timeout_add(3000, timeout)

def timeout():
   # message("test")
    clock = time.strftime("%H:%M:%S")
    if ':' in clock :
        hours,minutes, seconds = clock.split(':')
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        #convert to seconds
        current_time = int (int(int(hours*60)*60) + int(minutes*60) + int(seconds))
    if int(start_time + current_time) == finish_time :
        print "alarm"

  #  print(clock)
    difference = int(finish_time - int(start_time + current_time))/60 #minutes
    label1.set_text(str(difference))
   # label1.set_text("test")
    #label1.set_label("test")
   # self.val +=1
   # self.scale.set_value(self.val)
    return True

 
def make_menu(event_button, event_time, data=None):
  menu = gtk.Menu()
  open_item = gtk.MenuItem("Open App")
  close_item = gtk.MenuItem("Close App")
  
  #Append the menu items  
  menu.append(open_item)
  menu.append(close_item)
  #add callbacks
  open_item.connect_object("activate", open_app, "Open App")
  close_item.connect_object("activate", close_app, "Close App")
  #Show the menu items
  open_item.show()
  close_item.show()
  
  #Popup the menu
  menu.popup(None, None, None, event_button, event_time)
 
def on_right_click(data, event_button, event_time):
  make_menu(event_button, event_time)
 
def on_left_click(event):
    #win.show_all()
#    open_app()
    win.show()
    #message("Status Icon Left Clicked")

#def main( self):
#      open_app()
#      gtk.main() 



if __name__ == '__main__':
      #  self.statusicon = gtk.status_icon_new_from_stock(gtk.STOCK_GOTO_TOP)
  icon = gtk.status_icon_new_from_stock(gtk.STOCK_ABOUT)
  icon.connect('popup-menu', on_right_click)
  icon.connect('activate', on_left_click)
  #m = MyGUI( "TextView example")
  #m.main()
  open_app()
  gtk.main()

