import time
import LCD_Ext as Ext
from multiprocessing import Pool, Queue, Manager

light_pool = Pool(1)
beeper_pool = Pool(1)
msg_pool = Pool(1)

q = Manager().Queue()
msg_pool.apply_async(Ext.printMsg, [q]) 

messages = ["Hi!", "Kak si?", "Kakvo shte kaje6? ", "Chao!"]

for x in messages:
    light_pool.apply_async(Ext.light, [9]) 
    beeper_pool.apply_async(Ext.beep, []) 
    q.put(x);
    
    time.sleep(10)
    