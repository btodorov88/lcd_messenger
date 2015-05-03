import RPi.GPIO as GPIO
from LCD1602.Adafruit_CharLCD import Adafruit_CharLCD
import time
import datetime

pin_buzzer = 21
pin_light = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_buzzer, GPIO.OUT)
GPIO.setup(pin_light, GPIO.OUT)

lcd = Adafruit_CharLCD()

def changeLight(isOn):
    GPIO.output(pin_light, isOn)
    
def light(delay=2):
    GPIO.output(pin_light, True)
    time.sleep(delay)
    GPIO.output(pin_light, False)
    
def beep(times = 2, interval = 0.14):
    GPIO.output(pin_buzzer, False)
    for x in range(times):
        GPIO.output(pin_buzzer, True)
        time.sleep(interval)
        GPIO.output(pin_buzzer, False)
        time.sleep(interval)
        
def printMsg(q):
    while True:
        msg = q.get()
        ts = time.time()
        
        if len(msg) <= 16:
            printWithTime(msg, ts)
        else:
            while True:
                printWithTime(msg, ts)
                msg = msg[1:] + msg[0]
                if q.empty():
                    time.sleep(0.65)
                else:
                    break

def printWithTime(msg, time):
    st = datetime.datetime.fromtimestamp(time).strftime('    %H:%M:%S')
    
    lcd.clear()
    lcd.message(msg + "\n" + st)
            
if __name__ == '__main__':
    beep()
    GPIO.cleanup()
        
