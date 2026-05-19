#registratie website voor sporten

from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#maak arrays voor de verschillende categorieën dieren
KATACHTIGEN = ["Leeuw", "Amoertijger", "Jaguar", "Amoerluipaard"]
MENSAPEN = ["Gorilla", "Chimpansee", "Uilenkopmeerkat"]
BEREN = ["Brilbeer"]
KLEINE_ROOFDIEREN = ["Rode panda", "Stokstaartje", "Neusbeer", "Vosmangoest", "Wasbeer"]
ZEEDIEREN = ["Californische zeeleeuw", "Gewone zeehond"]
HOEFDIEREN = ["Giraffe", "Okapi", "Kaapse buffel", "Anoa", "Nijlpaard", "Olifant"]
VOGELS = ["Pinguïn", "Afrikaanse vogelsoorten"]
REPTIELEN = ["Krokodil", "Alligator", "Slang", "Hagedis"]
AQUARIUMDIEREN = ["Tripische rifvissen", "Koralen", "Zoet- en zoutwatervissen"]
#route voor de indexpagina met categorieën
@app.route("/")
def index():
    return render_template("index.html", katachtigen=KATACHTIGEN, mensapen=MENSAPEN, beren=BEREN, kleine_roofdieren=KLEINE_ROOFDIEREN, zeedieren=ZEEDIEREN, hoefdieren=HOEFDIEREN , vogels=VOGELS, reptielen=REPTIELEN, aquariumdieren=AQUARIUMDIEREN)
#route voor verschillende categorieën 
#route voor katachtigen
@app.route("/katachtigen")
def katachtigen():
    return render_template("katachtigen.html", katachtigen=KATACHTIGEN)
#route voor mensapen
@app.route("/mensapen")
def mensapen():
    return render_template("mensapen.html", mensapen=MENSAPEN)