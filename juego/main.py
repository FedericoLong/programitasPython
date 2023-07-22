import tkinter as tk
from calculos import resultado_pipati

window = tk.Tk()

window.title("Piedra Papel o Tijera")
window.geometry("400x300")
def resultado_pipatiPiedra():
  result=resultado_pipati(1)
  resultado["text"]=result[0]
  resultado["fg"]=result[1]
def resultado_pipatiPapel():
  result=resultado_pipati(2)
  resultado["text"]=result[0]
  resultado["fg"]=result[1]
def resultado_pipatiTijera():
  result=resultado_pipati(3)
  resultado["text"]=result[0]
  resultado["fg"]=result[1]

bPiedra = tk.Button(text="Piedra", command=resultado_pipatiPiedra,font=("Nonito", 18, "italic"))
bPiedra.pack(side="top")

bPapel = tk.Button(text="Papel",command=resultado_pipatiPapel,font=("Nonito", 18, "italic"))
bPapel.pack()

bTijera = tk.Button(text="Tijera",command=resultado_pipatiTijera,font=("Nonito", 18, "italic"))
bTijera.pack()

bTerminar= tk.Button(text="Terminar Juego",font=("Nonito", 14, "normal"))
bTerminar.pack(side="bottom")

resultado=tk.Label(text="", font=("nonito",15),bg="white")
resultado.pack()

tk.mainloop()