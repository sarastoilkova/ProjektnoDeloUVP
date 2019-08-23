from tkinter import *
root = Tk()

class Igra():
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=680, height=493)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.ozadje = PhotoImage(file='Slike/IgralnaPodlaga.png')
        self.canvas.create_image(0, 0, image= self.ozadje, anchor=NW)
        self.canvas.bind("<Button-1>", self.narisi_krizec)

    def narisi_krizec(self, event):
        '''funkcija, ki narise krizec ob kliku levega gumba miske'''
        self.znak = PhotoImage(file='Slike/Krizec.png')
        self.krizec = self.znak.subsample(2, 2)
        self.canvas.create_image(event.x, event.y, image=self.krizec)

    def narisi_krozec(self, event):
        '''funkcija, ki narise krozec'''
        self.znak = PhotoImage(file='Slike/Krozec.png')
        self.krozec = self.znak.subsample(2, 2)
        self.canvas.create_image(event.x, event.y, image=self.krozec)



    def izracunaj(dolzina, sirina):
        '''funikcija računa središča kvadratov in jih vrača v seznam koordinat'''
        x_povecevalec = dolzina / 3
        y_povecevalec = sirina / 3
        seznam = []
        zacetni_y = 0
        for i in range(3):
            zacetni_x = 0
            y = (y_povecevalec + zacetni_y) / 2
            for j in range(3):
                x = (zacetni_x + x_povecevalec) / 2
                zacetni_x = zacetni_x + x_povecevalec
                seznam.append((x, y))
            zacetni_y = zacetni_y + y_povecevalec
        return seznam



aplikacija = Igra(root)
#root.state('zoomed') #windowed
root.mainloop()