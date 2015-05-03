import time
import LCD_Ext as Ext
from multiprocessing import Pool, Queue, Manager

def init():
    global light_pool, beeper_pool, msg_queue
    light_pool = Pool(1)
    beeper_pool = Pool(1)
    msg_pool = Pool(1)

    msg_queue = Manager().Queue()
    msg_pool.apply_async(Ext.printMsg, [msg_queue]) 

def message(msg): 
    light_pool.apply_async(Ext.light, [9]) 
    beeper_pool.apply_async(Ext.beep, []) 
    msg_queue.put(msg);

if __name__ == '__main__':
    messages = ["Hi!", "Kak si?", "Kakvo shte kaje6? ", "Chao!"]
    init()
    for x in messages:
        message(x)
        time.sleep(10)
    