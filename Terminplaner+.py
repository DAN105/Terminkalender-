import os

pfad_ordner = 'Datei'

if os.path.isfile(pfad_ordner):
    os.remove(pfad_ordner)
    print(f'Datei "{pfad_ordner}" wurde als Datei gefunden und gelöscht.')

if not os.path.isdir(pfad_ordner):
    os.makedirs(pfad_ordner)
    print(f'Ordner "{pfad_ordner}" wurde erfolgreich erstellt.')



def lade_termine(pfad):
    termine=[]
    try:
        with open(pfad, 'r', encoding='utf-8') as datei:
            termine=[zeile.strip() for zeile in datei.readlines()]
    except FileNotFoundError:
        termine = ['Kein Termin'] * 24
    return termine

def speichere_termine(pfad, termine):
    try:
        with open(pfad, 'w',encoding='utf-8') as datei:
            for termin in termine:
                datei.write(termin + '\n')
    except FileNotFoundError:
        print('FileNotFoundError')
def ausgabe(termine):
    print('\nTermine für heute:')

    for i, termin in enumerate(termine):
        print(f'{i} Uhr: {termin}')

pfad_ordner = 'Datei'
pfad_datei = pfad_ordner + '/Inhalt.txt'


pfad = 'Datei/Inhalt.txt'
termine = lade_termine(pfad)

while True:
    print('\nTerminkalender\n--------------')
    print('1: Neuer Eintrag')
    print('2: Termine ausgeben')
    print('3: Programm beenden')
    auswahl = input('Auswahl: ')

    if auswahl == '1':
        try:
            hour = int(input('Uhrzeit (0 bis 23 Uhr): '))
            if 0 <= hour <= 23:
                termine[hour] = input('Eintrag: ')
                speichere_termine(pfad, termine)
            else:
                print('Ungültige Zeitangabe!')
        except ValueError:
            print('Bitte eine gültige Zahl eingeben!')

    elif auswahl == '2':
        ausgabe(termine)

    elif auswahl == '3':
        print('Programm ENDE!')
        break

    else:
        print('Eingabe nicht akzeptiert!')