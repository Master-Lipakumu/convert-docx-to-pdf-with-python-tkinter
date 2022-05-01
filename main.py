#coding:UTF-8


import img2pdf

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path

from docx2pdf import convert

from pdf2docx import Converter, parse



from tkinter import *


import json 




pdf_doc = "data/MON CV.pdf"

word_doc = "data/MON CV.docx"



#convert(word_doc, "output.pdf")



class Convert:
    #initialisation de l'écran
    def __init__(self, App):
        self.window = App
        #titre de l'application
        self.window.title("Master Lipakumu Convert Docx to Pdf")
        #taille de l'écran
        self.window.geometry("500x300")
        #couleur de fond ou background
        self.window.configure(bg="#0040ff")
        #interdiction de pouvoir redimentionner avec la souris
        self.window.resizable(False, False)

       #menu de notre application phrase d'affiche de notre app
        Label(App, text="Enter the path to files",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
        #champ d'etre de notre app
        self.path = Entry(App, width=16, font=("Arial", 15), relief="flat")
        #boutton 1 de nottre app 
        self.convert_button = Button(App, text="Convert", bg="#22c1c3", relief="sunken")
        #création des phrases a afficher sur notre app
        self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")

        #positionnement de tout nos éléments précedemment crée 
        self.path.place(x=170, y=120)

        self.convert_button.place(x=200, y=200)

        #lier nos boutton a une fonction bien précis
        self.convert_button.bind("<Button-1>", self.convert_location)


         #1er fonction d'excution evenementiel
    def convert_location(self,event):
        #récuperation du numero inscrit dans le champs précedament crée 
        path = self.path.get()
        if path:
            convert(path, "version-convertis.pdf")



#lancement de l'app
Doc_Convert = Tk()

MyApp = Convert(Doc_Convert)

Doc_Convert.mainloop()
# MASTER LIPAKUMU

