from xbmcjson import XBMC, PLAYER_VIDEO
import pafy
from Tkinter import Button, Entry, Tk, mainloop, CENTER, END
from ttk import Button, Entry
from os.path import *
from threading import Thread

class You2XBMC():
	def __init__(self):
		
		self.address=None
		self.video = None
		self.ipAddress = None
		self.home = expanduser("~")
		
		self.window = Tk()
		self.window.title("Send youtube video to XBMC")
		self.addressEntry = Entry()
		self.addressEntry.config(width=50)
		self.addressEntry.config(justify=CENTER)
		self.ipEntry = Entry()
		self.ipEntry.config(justify=CENTER)
		self.sendButton = Button(self.window, text="Play on XBMC", command=self.set_video)
		self.sendButton.config(width=30)
		self.clipboardButton = Button(text="Click to get from clipboard", command=self.get_clipboard)

		if not isfile(self.home+"/"+"xbmcIP.txt"):
			print "No File :("
			self.ipAddress = False
	
		elif isfile(self.home+"/"+"xbmcIP.txt"):
			print "File Exists :)"
			self.ipAddress = open(self.home+"/"+"xbmcIP.txt", "r").read().splitlines()[0]
			print self.ipAddress
			
		if self.ipAddress != False:
			self.ipEntry.insert(0, self.ipAddress)
			
	def set_video(self):
		x = Thread(target=self.set_video_callback)
		x.start()
		
	def set_video_callback(self):
		if self.ipAddress == False:
			self.ipAddress = self.ipEntry.get()
			xbmcIP = open(self.home+"/"+"xbmcIP.txt", "w")
			xbmcIP.write(str(self.ipAddress))
			xbmcIP.close()
	
		self.ipAddress = ("http://"+self.ipEntry.get()+"/jsonrpc")
		xbmc = XBMC(self.ipAddress)
		address = self.addressEntry.get()
		video = pafy.new(address)
		video = video.getbest()
		print xbmc.Player.Open(item={"file": video.url})

	def get_clipboard(self):
		string = self.window.clipboard_get()
		self.addressEntry.delete(0,END)
		self.addressEntry.insert(0, string)
		self.set_video()
		
	def pack_everything(self):
		self.addressEntry.pack()
		self.sendButton.pack()
		self.clipboardButton.pack()
		self.ipEntry.pack()

	def mainloop(self):
		mainloop()

if __name__ == "__main__":
	you2xbmc = You2XBMC()
	you2xbmc.pack_everything()
	you2xbmc.mainloop()
