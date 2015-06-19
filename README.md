# you2xbmc
Youtube video to xbmc streaming using python with a gui

The python script initializes a Tkinter gui with a ttk styling to make it look decent enough.
It depends on Tkinter and ttk for a gui,
it also uses pafy to get the youtube video's stream URL,
and finally it uses python-xbmc to send the information via json.
It also creates a text file at the home user folder called xbmcIP.txt in which it reads from the last used ip address.
No support for username and password yet.
