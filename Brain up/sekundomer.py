import time

def sekundomer(sekund):
    while sekund:
        mins, secs = divmod(sekund, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        sekund -= 1
    print("Boshlang!")
    
