#!/usr/bin/env python

# found on <http://files.majorsilence.com/rubbish/pygtk-book/pygtk-notebook-html/pygtk-notebook-latest.html#SECTION00430000000000000000>
# simple example of a tray icon application using PyGTK

import gtk
 
def message(data=None):
  "Function to display messages to the user."
  msg=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
    gtk.MESSAGE_INFO, gtk.BUTTONS_OK, data)
  msg.run()
  msg.destroy()

def button1_clicked(self ):
    self.set_label( "You clicked the right button")

def red_button_clicked(self):
    self.set_label( "Please don't press this button again")


def open_app(data=None):
    win = gtk.Window()
    win.set_border_width(5)
    win.set_title('Widget test')
    win.connect('delete-event', gtk.main_quit)
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(400, 200)
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
    label1 = gtk.Label( "Hello world")
    text_box1.pack_start( label1, padding=10)
    label1.show()
    text_box1.show()
    # box for buttons
    button_box1 = gtk.HBox()
    mainbox.pack_end( button_box1)
    # first button
    button1 = gtk.Button( "Press me")
    button1.connect( "clicked", button1_clicked)
    button_box1.pack_start( button1)
    button1.show()
    # second button
    button2 = gtk.Button( "Big red button")
    button2.connect( "clicked", red_button_clicked)
    button_box1.pack_start( button2)
    button2.show()
    # show the box
    button_box1.show()
    buffer1 = gtk.TextBuffer()

        # a textview (displays the buffer)
    textview = gtk.TextView(buffer=buffer1)
    mainbox.add(textview)
    mainbox.show()




  #  message(data)

#    scrolled_window = gtk.ScrolledWindow()
#    scrolled_window.set_border_width(5)
        # we scroll only if needed
   # scrolled_window.set_policy(
   # gtk.PolicyType.AUTOMATIC, gtk.PolicyType.AUTOMATIC)

        # a text buffer (stores text)
#    buffer1 = gtk.TextBuffer()

        # a textview (displays the buffer)
#    textview = gtk.TextView(buffer=buffer1)
        # wrap the text, if needed, breaking lines in between words
   # textview.set_wrap_mode(gtk.WrapMode.WORD)

        # textview is scrolled
#    scrolled_window.add(textview)
#    mainbox.add(scrolled_window)

    win.show_all()

 
def close_app(data=None):
 # message(data)
  gtk.main_quit()
 
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
  message("Status Icon Left Clicked")
 


if __name__ == '__main__':
  icon = gtk.status_icon_new_from_stock(gtk.STOCK_ABOUT)
  icon.connect('popup-menu', on_right_click)
  icon.connect('activate', on_left_click)
gtk.main()

