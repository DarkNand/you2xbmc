from xbmcjson import XBMC, PLAYER_VIDEO
import pafy
from Tkinter import Button, Entry, Tk, mainloop, CENTER, END
from ttk import Button, Entry
from os.path import *

address=None
video = None
ipAddress = None
home = expanduser("~")

if not isfile(home+"/"+"xbmcIP.txt"):
	print "No File :("
	ipAddress = False
	
elif isfile(home+"/"+"xbmcIP.txt"):
	print "File Exists :)"
	ipAddress = open(home+"/"+"xbmcIP.txt", "r").read().splitlines()[0]
	print ipAddress

window = Tk()
window.title("Send youtube video to XBMC")

def set_video():
	global address
	global video
	global ipAddress
	
	if ipAddress == False:
		ipAddress = ipEntry.get()
		xbmcIP = open(home+"/"+"xbmcIP.txt", "w")
		xbmcIP.write(str(ipAddress))
		xbmcIP.close()
	
	ipAddress = ("http://"+ipEntry.get()+"/jsonrpc")
	xbmc = XBMC(ipAddress)
	address = addressEntry.get()
	video = pafy.new(address)
	video = video.getbest()
	print xbmc.Player.Open(item={"file": video.url})

def get_clipboard():
	string = window.clipboard_get()
	addressEntry.delete(0,END)
	addressEntry.insert(0, string)
	set_video()
	
addressEntry = Entry()
addressEntry.config(width=50)
addressEntry.config(justify=CENTER)
ipEntry = Entry()
ipEntry.config(justify=CENTER)

if ipAddress != False:
	ipEntry.insert(0, ipAddress)

sendButton = Button(window, text="Play on XBMC", command=set_video)
sendButton.config(width=30)
clipboardButton = Button(text="Click to get from clipboard", command=get_clipboard)
addressEntry.pack()
sendButton.pack()
clipboardButton.pack()
ipEntry.pack()


mainloop()
