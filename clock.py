import datetime
import time
from LCD1602.Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD()

while True:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('    %H:%M:%S')

    lcd.clear()
    lcd.message(st)
    time.sleep(1)