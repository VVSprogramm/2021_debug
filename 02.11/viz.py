'''Bibliotēkas ievietošana'''
import tkinter as tk

window = tk.Tk() #Loga definēšana

#Pirmais teksts
label = tk.Label(
  text = "Sveiki! Sveiki! Sveiki! Sveiki! Sveiki!",   #Teksts, kurš tiks parādīts
  foreground = "red",   #Krāsa tekstam
  background = "#34A2FE"   #Krāsa fonam
  )

#Otrais teksts
label1 = tk.Label(
  text = "Čau!",
  fg = "red",
  bg = "#34A2FE",
  width = 11,     #Teksta loga platums
  height = 7      #Teksta loga augstums
  )

label.pack()       #Iebūvētā metode teksta logu izvadīšanai
label1.pack()

window.mainloop()   #Koda noslēguma rinda, veido galveno ciklu
 