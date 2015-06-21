# you2xbmc
Youtube video to xbmc streaming using python with a gui

The python script initializes a Tkinter gui with a ttk styling to make it look decent enough.
It depends on Tkinter and ttk for a gui,
it also uses pafy to get the youtube video's stream URL,
and finally it uses python-xbmc to send the information via json.
It also creates a text file at the home user folder called xbmcIP.txt in which it reads from the last used ip address.
No support for username and password yet.

To install:

pip install pafy
to install pafy and
pip install xbmc-json

If you're using linux, then you also need to have the python tk package:
apt-get install python-tk
If you don't already have it.
