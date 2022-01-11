#Spēle akmens, šķēres, papīrīts
import tkinter as tk
import random

#Funkcionalitāte
def akmens(event):
  lbl_lietizv["text"] = "Tava izvēle: Akmens"
  dat_izveele()

def papirs(event):
  lbl_lietizv["text"] = "Tava izvēle: Papīrs"
  dat_izveele()

def skeres(event):
  lbl_lietizv["text"] = "Tava izvēle: Šķēres"
  dat_izveele()

def dat_izveele():
  izveeles = ["Akmens", "Šķēres", "Papīrs"]
  datizv = random.choice(izveeles)
  lbl_datoraizv["text"] = f"Datora izvēle: {datizv}"
  rezultati()

def rezultati():
  dators = lbl_datoraizv["text"]
  lietotajs = lbl_lietizv["text"]
  dators = dators.split() #Pēc noklusējuma dala pēc atstarpēm
  lietotajs = lietotajs.split()

  if dators[2] == lietotajs[2]:
    lbl_rezultats["text"] = "Rezultāts: Neizšķirts"
  else:
    lbl_rezultats["text"] = "Vēl jāsataisa"

#Definējam logu
window = tk.Tk()

#Jāpievieno elementi
#Informācija
lbl_info = tk.Label(text = "Sveicināts/a!\nŠī ir spēle akmens, šķēres, papīrīts!",
bg = "Green",
fg = "Blue")
#Kas jādara
lbl_darit = tk.Label(text = "Izvēlies kādu no zemāk piedāvātajiem variantiem: ")
#ko katrs ir izvēlējies
lbl_lietizv = tk.Label()
lbl_datoraizv = tk.Label()
#Rezultāts
lbl_rezultats = tk.Label()

#Izvēles pogas
btn_akmens = tk.Button(text = "Akmens")
btn_skeres = tk.Button(text = "Šķēres")
btn_papirs = tk.Button(text = "Papīrs")

#Pogu interaktivitāte - .bind()
btn_akmens.bind("<Button-1>", akmens)
btn_papirs.bind("<Button-1>", papirs)
btn_skeres.bind("<Button-1>", skeres)

#.pack(), .place(), .grid()
lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirs.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()


window.mainloop()