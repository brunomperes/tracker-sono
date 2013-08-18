#!/usr/bin/python
from datetime import datetime, date

# Config
filepath = '/home/bruno/Dropbox/Projetos/PEP/Horas_sono/'

# Used variables
holiday = False

# Input sleep data
while True:
    t1 = raw_input('Que horas voce dormiu? ')
    if not ':' in t1:
        t1 = datetime.strptime(t1, '%H')
    else:
        t1 = datetime.strptime(t1, '%H:%M')
    if t1.hour > 8 and t1.hour < 20:  # Checks if input hour is during the day
        resposta = raw_input('Esse e um horario durante o dia. Esta correto [s/n]? ')
        if resposta == 's':
            break
        else:
            pass
    else:
        break
t2 = raw_input('Que horas voce acordou? ')
if 'F' in t2:
    holiday = True
    t2 = t2.split(' ')[0]   # Remove string holiday from input
    print 'Feriado detectado'
if not ':' in t2:
    t2 = datetime.strptime(t2, '%H')
else:
    t2 = datetime.strptime(t2, '%H:%M')

# File opening as append
f = open(filepath + 'track.txt', 'a')

# Get time differences as decimal value
delta = (t2 - t1)
delta = float(delta.seconds) / 3600

# Echo result
print str("%.2f" % delta) + ' hrs de sono'
f.write(str(date.today()) + ', ' + str(t1.strftime("%H:%M")) + ', ' + str(t2.strftime("%H:%M")) + ', ' + str("%.2f" % delta) + ' hrs')
if holiday is True:
    f.write(', F')
f.write('\n')
f.close()
