duration = int(input('Введите кол-во секунд '))
days = 0
hours = 0
minutes = 0
seconds = 0


if duration < 60:
    print(str(duration)+' сек')
elif 60 <= duration < 3600:
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print(str(minutes) + ' мин ' + str(seconds) + ' сек')
elif 3600 <=duration < 86400:
    hours = duration // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print(str(hours)+' час '+str(minutes)+' мин '+str(seconds)+' сек')
else:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print(str(days)+' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')





