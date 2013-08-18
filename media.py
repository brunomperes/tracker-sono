#!/usr/bin/python
import numpy as np
import time
import calendar

# Definitions of the expect year and date to calculate sleep hours average
filePath = '/home/bruno/Dropbox/Projetos/PEP/Horas_sono/'
calcYear = 2013
calcMonth = int(raw_input('\nNumero mes de ' + str(calcYear) + ' a avaliar a media: '))
holidayStringIdentifier = 'F'

# Used Variables
sleepHoursWeekday = []
sleepHoursWeekend = []
lastRecordedDay = False
dateMonthday = None
dateMonth = None
holiday = False

# Import sleep data
print ('')
inputFile = open(filePath + 'track.txt', 'r')  # Open File
while True:
    line = inputFile.readline()     # Read content
    if len(line) == 0:
        inputFile.close()
        break   # EOF, stop reading
    line = line.split(',')
    date = line[0]
    # Fill data
    if (len(line) > 4 and line[4].find('F') > -1):
        holiday = True
    else:
        holiday = False
    dateFormated = time.strptime(date, "%Y-%m-%d")
    dateWeekday = time.strftime("%A", dateFormated)
    if (dateMonthday is None) is False:     # Check if variable is defined
        lastRecordedDay = dateMonthday
    dateMonthday = int(time.strftime("%d", dateFormated))
    if (dateMonthday is None) is False:     # Check if variable is defined
        lastRecordedMonth = dateMonth
    dateMonth = int(time.strftime("%m", dateFormated))
    dateYear = int(time.strftime("%Y", dateFormated))
    if dateYear == calcYear:
        if dateMonth == calcMonth:
            # Checks if duplicated data
            if lastRecordedDay == dateMonthday and lastRecordedMonth == dateMonth:
                print ('------Inconsistencia no dia ' + str(dateMonthday) + '/' + str(calcMonth) + ' checar se nao ha dados duplicados------\n')
            dateSleepHours = float(line[3].split()[0])  # Get the hours X.XX slept from format 'X.XX hrs'
            # Checks if weekend, holiday or weekday
            if (dateWeekday == 'Saturday' or dateWeekday == 'Sunday' or holiday is True):
                sleepHoursWeekend.append(dateSleepHours)
            else:
                sleepHoursWeekday.append(dateSleepHours)

# Check consistency of all data
countedDaysInMonth = len(sleepHoursWeekday) + len(sleepHoursWeekend)

if (countedDaysInMonth < 1):
    raise SystemExit('[ERRO] Nao houveram registros no mes ' + str(calcMonth) + '/' + str(calcYear) + '\n')

# Check consistency and outputs average
if (len(sleepHoursWeekday) < 1):
    print ('[AVISO] Nao houveram registros para calcular a media de horas em MEIO de semana no mes ' + str(calcMonth) + '/' + str(calcYear))
    averageWeekDay = 0
else:
    averageWeekDay = np.mean(sleepHoursWeekday)
    print ('Media horas de sono durante semana: ' + str("%.2f" % averageWeekDay) + ' hrs')

if (len(sleepHoursWeekend) < 1):
    print ('[AVISO] Nao houveram registros para calcular a media de horas em FINAIS de semana ou feriados do mes ' + str(calcMonth) + '/' + str(calcYear))
    averageWeekendDay = 0
else:
    averageWeekendDay = np.mean(sleepHoursWeekend)
    print ('Media horas de sono em finais de semana e feriados: ' + str("%.2f" % averageWeekendDay) + ' hrs')

averageOverall = float(sum(sleepHoursWeekend) + sum(sleepHoursWeekday)) / float(countedDaysInMonth)
print ('Media geral: ' + str("%.2f" % averageOverall))

# Accuracy check for number of tracked days and counted days
numDaysInMonth = calendar.monthrange(dateYear, calcMonth)[1]
countedDaysInMonthPercent = (float(countedDaysInMonth) / float(numDaysInMonth)) * 100.0

# Output checked accuracy
print ('')
print ('Dias trackeados no mes: ' + str(countedDaysInMonth) + '/' + str(numDaysInMonth) + ' - ' + str("%.2f" % countedDaysInMonthPercent) + '% trackeados')
print ('')
