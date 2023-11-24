#
# includes
#

import io
import datetime
import sys





#
# set parameters
#

path_birthday_list = "birthday_list.txt"




#
# read birthdays
#

birthday_file = io.open(path_birthday_list, "r", encoding="utf-8")
list_of_birthdays = birthday_file.read().split("\n")




#
# build list of pending birthdays
#

# aktuelles Datum ermitteln
today = datetime.datetime.now()
today_day = today.day
today_month = today.month

# Datum in 8 Tagen ermitteln
today_plus_8 = datetime.datetime.now() + datetime.timedelta(days=8)
today_plus_8_day = today_plus_8.day
today_plus_8_month = today_plus_8.month

# Finden von Geburtstagen in den kommenden 8 Tagen
result_list = []
for row in list_of_birthdays:

    # day
    idx = row.find(".")
    day = int(row[:idx])

    # month
    idx2 = row[idx+1:].find(".")
    month = row[idx+1:idx+idx2+1]
    
    # TRICKY

    # vielleicht wäre es hier gut, wenn man den Vergleich der Datumswerte
    # direkt über das datetime-Objekt macht. Also: nicht mit den Einzelwerten
    # wie "today_day" arbeiten, sondern eher die Werte des aktuellen
    # Geburtstags-Elements (Zeile) in ein datetime-Objekt wandeln und dann
    # einen Größer- / Kleiner-Vergleich anstellen. Das klappt 100%.

    if month >= today_month and month <= today_plus_8_month:
        if day >= today_day and day <= today_plus_8_day:

            # append current row to positive results list
            result_list.append(row)




#
# determine email addresses
#

# soll es eine einheitliche Nachricht für ALLE Personen geben (inklusive der
# Geburtstag-habenden Person), oder soll für jeden eine individuelle
# Benachrichtigung versandt werden, in der er selbst nicht vorkommt?




#
# send emails
#


