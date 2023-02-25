import os
import ftplib
from tkinter import *
from tkinter import filedialog

class FTPClient:
    def __init__(self, master):
        self.master = master
        self.master.title("FTP Client")
        
        # Create FTP connection
        self.ftp = ftplib.FTP("ftp.adress.com")
        self.ftp.login(" user", "pass")
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Local file selector
        self.local_path = StringVar()
        self.local_path.set(os.getcwd())
        Label(self.master, text="Local Path:").grid(row=0, column=0)
        Entry(self.master, textvariable=self.local_path).grid(row=0, column=1)
        Button(self.master, text="Browse", command=self.browse_local).grid(row=0, column=2)
        
        # Remote file selector
        self.remote_path = StringVar()
        self.remote_path.set("/")
        Label(self.master, text="Remote Path:").grid(row=1, column=0)
        Entry(self.master, textvariable=self.remote_path).grid(row=1, column=1)
        
        # Upload button
        Button(self.master, text="Upload", command=self.upload).grid(row=2, column=0)
        
        # Quit button
        Button(self.master, text="Quit", command=self.quit).grid(row=2, column=1)
        
    def browse_local(self):
        local_path = filedialog.askdirectory()
        if local_path:
            self.local_path.set(local_path)
            
    def upload(self):
        # Switch to remote directory
        self.ftp.cwd(self.remote_path.get())
        
        # Upload file
        local_path = self.local_path.get()
        file_name = os.path.basename(local_path)
        with open(local_path, "rb") as f:
            self.ftp.storbinary(f"STOR {file_name}", f)
        
        # Print message
        print(f"Uploaded {file_name} to {self.ftp.pwd()}")
            
    def quit(self):
        self.ftp.quit()
        self.master.destroy()

root = Tk()
client = FTPClient(root)
root.mainloop()

