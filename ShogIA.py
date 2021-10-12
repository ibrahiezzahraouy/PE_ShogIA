from tkinter import *
from tkinter.ttk import *
import subprocess
import shogi_graphics
import os
ind= -1
ind2 = -1
ind3= -1
ind4 = -1
ind5 = -1
ind6 = -1
### MENU 

class FenPrincipale(Tk): # la fenetre principale
    def __init__(self):
        Tk.__init__(self)
        bg = 'test.gif'
        photo = PhotoImage(file=bg)
        
        self.__background_label = Label(self, image=photo)
        self.__background_label.photo=photo
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.iconbitmap('shogi.ico')
        self.geometry("1200x800+200+100")
         
        self.mode = "Contre l'IA"
        self.level = 2
        
        #Creation des boutons en haut et du compteur d'echec
        # Titre
        self.__label = Label(self,text = '将棋', background = "#EED3A4")  # Titre
        font10 = "-family {DejaVu Sans} -size 22 -weight normal -underline 0 -overstrike 0" # Police
        self.__label.configure(font=font10)
        self.__label.place(x = 560, y = 280)
        
        Style().configure("TButton", padding=6,relief = 'flat')
        
        #Boutons
        self.__boutonStart = Button(self, text ='Start', command = self.Launch)
        self.__boutonStart.place(x = 550, y = 350)
        
        self.__boutonTuto = Button(self, text ='Tutoriel', command = self.LanceTuto)
        self.__boutonTuto.place(x = 550, y = 390)
        
        self.__boutonOptions = Button(self, text ='Options', command = self.LanceOption)
        self.__boutonOptions.place(x = 550, y = 430)
        
        self.__boutonQuitter = Button(self, text ='Quitter', command = self.destroy)
        self.__boutonQuitter.place(x = 550, y = 470)
        
    def Launch(self): # Lance le programme shogi_graphics
        self.iconify()
        wind = shogi_graphics.Window(self.mode,self.level)
        wind.mainloop()

    def updatebg(self,delay=50):  # Fonction nécessaire à l'affichage du gif
        global ind
        ind += 1
        if ind == 150: ind = 0
        self.__background_label.photo.configure(format="gif -index " + str(ind))
        self.after(delay, self.updatebg)
        
    def LanceTuto(self): 
        self.__tuto = Tutoriel(self)
        self.__tuto.menuTuto()
        self.__tuto.updateParachutage()
        self.__tuto.updatePromotion()
        self.__tuto.updatePieces()
        self.__tuto.updatePlateau()
        
    def LanceOption(self):
        self.option = Option(self)
        
class Option(Toplevel):
    def __init__(self,main):
        Toplevel.__init__(self)
        self.main = main
        
        self.variableLevel = IntVar(self)
        self.variableLevel.set(self.main.level)
        
        self.Framelvl = Frame(self)
        
        self.labellvl = Label(self.Framelvl, text ='Difficulté de l\'IA : ')
        self.labellvl.pack(side = LEFT, padx = 5, pady = 5)
        
        self.levelSelectionMenu = OptionMenu(self.Framelvl,self.variableLevel, self.variableLevel.get(), 1, 2, 3)
        self.levelSelectionMenu.pack(side = RIGHT, padx = 5, pady = 5)
        
        self.FrameMode = Frame(self)
        
        self.labelmode = Label(self.FrameMode, text ='Mode de jeu : ')
        self.labelmode.pack(side = LEFT, padx = 5, pady = 5)
        self.variableMode = StringVar(self)
        
        self.variableMode.set(self.main.mode)
        
        self.modeSelectionMenu = OptionMenu(self.FrameMode,self.variableMode, self.variableMode.get(), "Contre l'IA", "2 Joueurs")
        self.modeSelectionMenu.pack(side = RIGHT, padx = 5, pady = 5)
        
        self.Framelvl.pack(side = TOP,padx = 5, pady = 5)
        self.FrameMode.pack(side = TOP,padx = 5, pady = 5)
        
        
        self.buttonConfirm = Button(self, text ='Confirmer', command = self.confirmer)
        self.buttonConfirm.pack(side = BOTTOM, padx = 5, pady = 5)
        
    def confirmer(self):
        
        self.main.mode = self.variableMode.get()
        self.main.level = self.variableLevel.get()
        self.destroy()
        
        
###Tutoriel
class Tutoriel(Toplevel): # classe définissant le tutoriel
    def __init__(self,main):
        Toplevel.__init__(self)
        self.__main = main
        
        #Import des images utiles
        nomImage = 'floche.png' # on affice l'image correspondante
        self.__floche = PhotoImage(file=nomImage)
        nomImagereversed = 'flocher.png' # on affice l'image correspondante
        self.__flocher = PhotoImage(file=nomImagereversed)
        nomPlateau = 'Shogiban.gif'
        self.__plateau = PhotoImage(file=nomPlateau)
        nomParachutage = 'Parachutage.gif'
        self.__parachutage = PhotoImage(file=nomParachutage)
        nomPromotion = 'Promotion.gif'
        self.__promotion = PhotoImage(file=nomPromotion)
        nomZone = 'Zone.png'
        self.__zone = PhotoImage(file=nomZone)
        
        nomFouIco = 'pieces\shogi_bb.png'
        self.__FouIco = PhotoImage(file=nomFouIco)
        nomTourIco = 'pieces\shogi_rb.png'
        self.__TourIco = PhotoImage(file=nomTourIco)
        nomSilverIco = 'pieces\shogi_sb.png'
        self.__SilverIco = PhotoImage(file=nomSilverIco)
        nomGoldIco = 'pieces\shogi_Gb.png'
        self.__GoldIco = PhotoImage(file=nomGoldIco)
        nomKingIco = 'pieces\shogi_Kb.png'
        self.__KingIco = PhotoImage(file=nomKingIco)
        nomLanceIco = 'pieces\shogi_lb.png'
        self.__LanceIco = PhotoImage(file=nomLanceIco)
        nomPionIco = 'pieces\shogi_Pb.png'
        self.__PionIco = PhotoImage(file=nomPionIco)
        nomKnightIco = 'pieces\shogi_nb.png'
        self.__KnightIco = PhotoImage(file=nomKnightIco)
        
        
        
        self.__Fou = PhotoImage(file='Fou.gif')
        self.__Gold = PhotoImage(file='Gold.gif')
        self.__Tour = PhotoImage(file='Tour.gif')
        self.__Knight = PhotoImage(file='Knight.gif')
        self.__King = PhotoImage(file='King.gif')
        self.__Silver = PhotoImage(file='Silver.gif')
        self.__Pion = PhotoImage(file='Pion.gif')
        self.__Lance = PhotoImage(file='Lance.gif')
        
        
        
    def menuTuto(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        bg = 'test.gif'
        photo = PhotoImage(file=bg)
        
        self.__background_label = Label(self, image=photo)
        self.__background_label.photo=photo
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.iconbitmap('shogi.ico')
        self.geometry("1200x800+200+100")
        self.__label = Label(self,text = 'Tutoriel', background = "#EED3A4")  # Titre
        font10 = "-family {DejaVu Sans} -size 22 -weight normal -underline 0 -overstrike 0" # Police
        self.__label.configure(font=font10)
        self.__label.place(x = 540, y = 280)
        #Style().configure("TButton", padding=6,relief = 'flat')
        
        self.__boutonBase = Button(self, text ='Base',width = 20,command = self.Base)
        self.__boutonBase.place(x = 520, y = 350)
        
        self.__boutonParachutage = Button(self, text ='Parachutage',width = 20,command = self.Parachutage)
        self.__boutonParachutage.place(x = 520, y = 390)
        
        self.__boutonPromotion = Button(self, text ='Promotion',width = 20,command = self.Promotion)
        self.__boutonPromotion.place(x = 520, y = 430)
        
        self.__boutonPieces = Button(self, text ='Pièces',width = 20,command = self.Pieces)
        self.__boutonPieces.place(x = 520, y = 470)
        
        self.__boutonQuitter = Button(self, text ='Quitter',width = 20, command = self.destroy)
        self.__boutonQuitter.place(x = 520, y = 510)
    def updateParachutage(self,delay=1000):  # Fonction nécessaire à l'affichage du gif
        global ind2
        ind2 += 1
        if ind2 == 4: ind2 = 0
        self.__parachutage.configure(format="gif -index " + str(ind2))
        self.after(delay, self.updateParachutage)
    def updatePromotion(self,delay=1500):  # Fonction nécessaire à l'affichage du gif
        global ind3
        ind3 += 1
        if ind3 == 4: ind3 = 0
        self.__promotion.configure(format="gif -index " + str(ind3))
        self.after(delay, self.updatePromotion)
    def updatePieces(self,delay=500):  # Fonction nécessaire à l'affichage du gif
        global ind4
        ind4 += 1
        if ind4 == 4: ind4 = 0
        self.__Fou.configure(format="gif -index " + str(ind4))
        self.__Tour.configure(format="gif -index " + str(ind4))
        self.__Lance.configure(format="gif -index " + str(ind4))
        self.__Pion.configure(format="gif -index " + str(ind4))
        self.__Knight.configure(format="gif -index " + str(ind4))
        self.__Silver.configure(format="gif -index " + str(ind4))
        global ind5
        ind5 += 1
        if ind5 == 2: ind5 = 0
        self.__Gold.configure(format="gif -index " + str(ind5))
        self.__King.configure(format="gif -index " + str(ind5))

        self.after(delay, self.updatePieces)
    def updatePlateau(self,delay=700):  # Fonction nécessaire à l'affichage du gif
        global ind6
        ind6 += 1
        if ind6 == 9: ind6 = 0
        self.__plateau.configure(format="gif -index " + str(ind6))
        self.after(delay, self.updatePlateau)
        
        
    def Base(self): # Affichage de la première page
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("1200x800+200+100")
        self.title('Base')
        self.__ftext = Frame(self)
        ### ScrollBar
        scrollbar = Scrollbar(self.__ftext)
        scrollbar.pack(side=RIGHT, fill=Y)
        ### Police
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -underline 0 -overstrike 0" 
        ### Configuration de la page
        text = Text(self.__ftext,wrap='word', yscrollcommand=scrollbar.set,font=font10,width=100,height=30,bg='#E7E7EB')
        text.pack()
        ### Contenu de la page
        with open('PAGE1.1.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                text.insert(END,line)
        text.insert(END,'                   ')
        text.image_create(8.19, image = self.__plateau)
        text.insert(END,'\n')
        with open('PAGE1.2.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                text.insert(END,line)

        scrollbar.config(command=text.yview)
        text.config(state='disabled') # On ne peut pas changer le texte
        self.__ftext.pack(side=TOP,padx=5,pady=5)
        #Boutons
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.menuTuto)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        

        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
        
    def Parachutage(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("1200x800+200+100")
        self.title('Parachutage')
        self.__ftext = Frame(self)
        ### ScrollBar
        scrollbar = Scrollbar(self.__ftext)
        scrollbar.pack(side=RIGHT, fill=Y)
        ### Police
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -underline 0 -overstrike 0" 
        ### Configuration de la page
        text = Text(self.__ftext,wrap='word', yscrollcommand=scrollbar.set,font=font10,width=100,height=30,bg='#E7E7EB')
        text.pack()
        with open('PAGE2.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                text.insert(END,line)
                
        text.insert(END,'                   ')
        text.image_create(8.19, image = self.__parachutage)
        text.insert(END,'\n')
        scrollbar.config(command=text.yview)
        text.config(state='disabled') # On ne peut pas changer le texte
        self.__ftext.pack(side=TOP,padx=5,pady=5)
        #Boutons
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.menuTuto)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Promotion(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("1200x800+200+100")
        self.title('Promotion')
        self.__ftext = Frame(self)
        ### ScrollBar
        scrollbar = Scrollbar(self.__ftext)
        scrollbar.pack(side=RIGHT, fill=Y)
        ### Police
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -underline 0 -overstrike 0" 
        ### Configuration de la page
        text = Text(self.__ftext,wrap='word', yscrollcommand=scrollbar.set,font=font10,width=100,height=30,bg='#E7E7EB')
        text.pack()
        text.insert(0.0,'                           ')
        text.image_create(20.0, image = self.__zone)
        text.insert(2.1,'\n')
        with open('PAGE3.txt','r',encoding='utf-8') as f:
            for line in f.readlines():
                text.insert(END,line)
                
        text.insert(END,'                                              ')
        text.image_create(20.30, image = self.__promotion)
        text.insert(END,'\n')
        scrollbar.config(command=text.yview)
        text.config(state='disabled') # On ne peut pas changer le texte
        self.__ftext.pack(side=TOP,padx=5,pady=5)
        #Boutons
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.menuTuto)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Pieces(self):
        ind4 = -1
        ind5 = -1
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("620x200+400+400")
        self.title('Pieces')
        self.__Label = Label(self,text = 'Veuillez choisir la pièce dont vous voulez connaître les déplacements : ')
        self.__Label.pack(side = TOP,padx=5,pady=20)
        
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.menuTuto)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        
        self.__boutonFou = Button(self, image=self.__FouIco,width = 20, command = self.Fou)
        self.__boutonFou.pack(side = LEFT,padx=5,pady=20)
        self.__boutonGold = Button(self, image=self.__GoldIco,width = 20, command = self.Gold)
        self.__boutonGold.pack(side = LEFT,padx=5,pady=20)
        self.__boutonSilver = Button(self, image=self.__SilverIco,width = 20, command = self.Silver)
        self.__boutonSilver.pack(side = LEFT,padx=5,pady=20)
        self.__boutonTour = Button(self, image=self.__TourIco,width = 20, command = self.Tour)
        self.__boutonTour.pack(side = LEFT,padx=5,pady=20)
        self.__boutonKing = Button(self, image=self.__KingIco,width = 20, command = self.King)
        self.__boutonKing.pack(side = LEFT,padx=5,pady=20)
        self.__boutonKnight = Button(self, image=self.__KnightIco,width = 20, command = self.Knight)
        self.__boutonKnight.pack(side = LEFT,padx=5,pady=20)
        self.__boutonLance = Button(self, image=self.__LanceIco,width = 20, command = self.Lance)
        self.__boutonLance.pack(side = LEFT,padx=5,pady=20)
        self.__boutonPion = Button(self, image=self.__PionIco,width = 20, command = self.Pion)
        self.__boutonPion.pack(side = LEFT,padx=5,pady=20)
    def Fou(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Fou')
        Label(self, image=self.__Fou).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Tour(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Tour')
        Label(self, image=self.__Tour).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Pion(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Pion')
        Label(self, image=self.__Pion).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Knight(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Knight')
        Label(self, image=self.__Knight).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Silver(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Silver')
        Label(self, image=self.__Silver).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Lance(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Lance')
        Label(self, image=self.__Lance).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def King(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('King')
        Label(self, image=self.__King).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    def Gold(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.geometry("500x500+400+400")
        self.title('Gold')
        Label(self, image=self.__Gold).pack()
        self.__boutonRetour = Button(self,image=self.__flocher, command = self.Pieces)
        self.__boutonRetour.pack(side=LEFT,padx = 5)
        self.transient(self.__main) 	  # Réduction popup impossible 
        self.grab_set()		  # Interaction avec fenetre jeu impossible
        self.__main.wait_window(self)   # Arrêt script principal
    
#End
fen = FenPrincipale()
fen.mainloop()