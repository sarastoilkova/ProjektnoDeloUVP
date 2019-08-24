from tkinter import *
import random
root = Tk()

class Igra():
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=680, height=493)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.ozadje = PhotoImage(file='Slike/IgralnaPodlaga.png')
        self.canvas.create_image(0, 0, image=self.ozadje, anchor=NW)
        self.canvas.bind("<Button-1>", self.narisi_krizec)
        self.seznam_sredisc = self.izracunaj(680, 493)
        self.slovar_indeksov = dict()
        for i in range(9):
            self.slovar_indeksov[i] = self.seznam_sredisc[i]
        #print(self.seznam_sredisc)

    def narisi_krizec(self, event):
        '''funkcija, ki narise krizec ob kliku levega gumba miske'''
        self.znak = PhotoImage(file='Slike/Krizec.png')
        self.krizec = self.znak.subsample(2, 2)
        self.center = self.center_slike((event.x, event.y))
        #print(self.center)
        self.canvas.create_image(self.center[0], self.center[1], image=self.krizec)
        self.indeks_sredisca_krizec = list(self.slovar_indeksov.values()).index(self.center)
        self.sosed = random.choice(self.poisce_sosed(self.indeks_sredisca_krizec))
        self.narisi_krozec(self.seznam_sredisc[self.sosed])

    def narisi_krozec(self, tocka):
        '''funkcija, ki narise krozec'''
        self.znak = PhotoImage(file='Slike/Krozec.png')
        self.krozec = self.znak.subsample(2, 2)
        self.canvas.create_image(tocka[0], tocka[1], image=self.krozec)


    def center_slike(self, tocka):
        self.tocka = (0, 0)
        self.razdalja = 1000
        for sredisce in self.seznam_sredisc:
            razdalja_do_sredisca = (((tocka[0] - sredisce[0]) ** 2) + ((tocka[1] - sredisce[1]) ** 2) ) ** (1/2)
            #print(sredisce,razdalja_do_sredisca)
            if razdalja_do_sredisca < self.razdalja:
                self.tocka = sredisce
                self.razdalja = razdalja_do_sredisca
        return self.tocka

    def poisce_sosed(self, stevilka):
        robne = [0, 2, 6, 8]
        notranje = [1, 3, 5, 7]
        sredinska = 4
        if stevilka == sredinska:
            return robne + notranje
        elif stevilka in robne:
            if stevilka == 0:
                return [1, 3, 4]
            elif stevilka == 2:
                return [1, 4, 5]
            elif stevilka == 6:
                return [3, 4, 7]
            elif stevilka == 8:
                return [4, 5, 7]
        elif stevilka in notranje:
            if stevilka == 1:
                return [0, 4, 2]
            elif stevilka == 3:
                return [0, 4, 6]
            elif stevilka == 5:
                return [2, 4, 8]
            elif stevilka == 7:
                return [6, 4, 8]










    def izracunaj(self, dolzina, sirina):
        '''funikcija računa središča kvadratov in jih vrača v seznam koordinat'''
        x_povecevalec = dolzina / 3
        y_povecevalec = sirina / 3
        seznam = []
        zacetni_y = 0
        koncni_y = y_povecevalec
        for i in range(3):
            zacetni_x = 0
            koncni_x = x_povecevalec
            y = (koncni_y + zacetni_y) / 2
            for j in range(3):
                x = (zacetni_x + koncni_x) / 2
                zacetni_x += x_povecevalec
                koncni_x += x_povecevalec
                seznam.append((x, y))
            zacetni_y += y_povecevalec
            koncni_y += y_povecevalec
        return seznam

aplikacija = Igra(root)
#root.state('zoomed') #windowed
root.mainloop()