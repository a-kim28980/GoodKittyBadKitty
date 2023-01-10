#importing necessary modules

from breezypythongui import EasyFrame
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, N, S, W, E
import random

class GoodKittyBadKitty(EasyFrame):

#setting up main window
    
    def __init__(self):
        EasyFrame.__init__(self, title = "Good Kitty Bad Kitty",
                           width = 1200, height = 1000)

        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = N+S+W+E)

        self.image = PhotoImage(file = "cat1.png")
        imageLabel["image"] = self.image
 
        self.addLabel(text = "Good kitty, bad kitty, which one will you get? If you are lucky, you can keep it as your pet!",
                      row = 0, column = 0)

        self.addButton(text = "Get me a kitty!", row = 3, column = 0,
                       columnspan = 2, command = self.getKitty)

        self.addButton(text = "Close", row = 4, column = 0,
                       columnspan = 2, command = self.close)

#determines output good or bad kitty and retrieves image
        
    def getKitty(self):
        
        i = random.randint(0, 1)
        
        if i == 1:
            self.messageBox(title = "Good Kitty",
                            message = "Congratulations! You got a good kitty! You can try and get another kitty or close out of the application.")
            
            imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = N+S+W+E)

            self.image = PhotoImage(file = "goodkitty.png")
            imageLabel["image"] = self.image
            
        else:
            self.messageBox(title = "Bad Kitty",
                            message = "Aww, shucks! You got a bad kitty! Try your luck again for a good kitty.")
            
            imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = N+S+W+E)

            self.image = PhotoImage(file = "badkitty.png")
            imageLabel["image"] = self.image

#close application
    
    def close(self):
        self.master.destroy()

GoodKittyBadKitty().mainloop()
