from datetime import datetime
import pytz

#Hauptprogram
def lokale_zeit_erhalten(stadtname, info_typ):
    stadt_zeitzonen = {
        'san fransisko': 'America/Los_Angeles',
        'new york': 'America/New_York',
        'ottawa': 'America/Toronto',
        'st. helena': 'Atlantic/St_Helena',
        'kapstadt': 'Africa/Johannesburg',
        'berlin': 'Europe/Berlin',
        'warschau': 'Europe/Warsaw',
        'moskou': 'Europe/Moscow',
        'kalkutta': 'Asia/Kolkata',
        'peking': 'Asia/Shanghai',
        'tokio': 'Asia/Tokyo'
    }
    
    zeitzone = stadt_zeitzonen.get(stadtname.lower())
    if zeitzone:
        lokale_zeit = datetime.now(pytz.timezone(zeitzone))
        if info_typ == 'zeit':
            return lokale_zeit.strftime('%H:%M:%S')
        elif info_typ == 'datum':
            return lokale_zeit.strftime('%d.%m.%Y')
    else:
        return "Der eingegebene Stadtname ist ungültig."

 #Hauptschleife
while True:
    stadt_eingabe = input("Bitte geben Sie den Namen der Stadt ein, deren lokale Zeit oder Datum Sie wissen möchten: ")
    if stadt_eingabe.lower() == 'ende':
        print("Ups, es ist beendet:). ")
        break
    info_typ_eingabe = input("Möchten Sie die Zeit oder das Datum wissen? (zeit/datum): ")
    if info_typ_eingabe.lower() not in ['zeit', 'datum']:
        print("Ungültige Eingabe. Bitte geben Sie 'zeit' oder 'datum' ein.")
        continue
    print(f"{info_typ_eingabe.capitalize()} für {stadt_eingabe.title()}: {lokale_zeit_erhalten(stadt_eingabe, info_typ_eingabe.lower())}")



"""
Ziel des Programms ist es, 
die lokale Zeit für verschiedene Städte weltweit zu berechnen.

Bibliotheken: datetime, pytz

Funktion:(Hauptprogram) lokale_zeit_erhalten - '%d-%m-%Y' '%H:%M:%S'

Um das Programm laufen zu lassen, ohne es anzuhalten, 
wurde eine While-Schleife geschrieben.

Dieser Code fragt den Benutzer nach Eingabe des Ortsnamens, 
ob er "zeit" oder "datum" wünscht, und gibt die Informationen entsprechend zurück.
Der Benutzer kann die Schleife beenden, indem er "ende" eingibt. 

stadt_eingabe.lower() und info_typ_eingabe.lower() wurden verwendet, 
um die Nutzereingaben in Kleinbuchstaben umzuwandeln.
Durch die Verwendung der Funktionen capitalize() und 
title() wurde sichergestellt, dass die Ausgaben ordentlicher aussehen.

"""
