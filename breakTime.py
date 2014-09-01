import time
import webbrowser

breaks = 3
breakCount = 0
print 'Program started on %s' % time.ctime()
while breakCount < breaks:
    time.sleep(10)
    webbrowser.open(r'http://www.youtube.com/watch?v=D5Y11hwjMNs')
    breakCount+=1
    
