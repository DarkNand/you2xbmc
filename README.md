# you2xbmc
Youtube video to xbmc streaming using python with a gui

The python script allows you to send youtube videos to an xbmc machine (like a raspberry pi running openelec).
It depends on Tkinter and ttk for a gui,
it also uses pafy to get the youtube video's stream URL, (pip install pafy)
and finally it uses python-xbmc to send the information via json. (pip install xbmc-json)
It also creates a text file at the home user folder called xbmcIP.txt in which it reads from the last used ip address.
No support for username and password yet.

To use:
Enter the video's address in the first entry, and in the second entry enter the ip address of the xbmc machine.
You can skip pasting the video's address by clicking the button that automatically pastes it from the clipboard for you.

If you're using linux, then you also need to have the python tk package:
apt-get install python-tk
If you don't already have it.
