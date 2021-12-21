from asyncio import run
from pprint import pprint
from flux_led.aio import AIOWifiLedBulb
from websocket import create_connection
# here you should put the private ip of your light
# so here is  the private ip of my light 
ip = "192.168.100.59"
url="ws://ranon-bulb.herokuapp.com/color"

def hex_to_rgb(hex):
    try:
        if len(hex)!=7:
            return 255,255,255
        (r,g,b)=int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
    except:
        return 255,255,255
        
    return r,g,b


async def main():
    bulb = AIOWifiLedBulb(ip)

    await bulb.async_setup(lambda:pprint(["State Changed!", bulb.raw_state]))
    ws =create_connection(url)
    print("connected")
    while(True):
        try:
            result = ws.recv()
            print(result)
            (r,g,b)=hex_to_rgb(result)
            await bulb.async_set_levels(r,g,b)
        except:
            continue
    
    
if __name__ == "__main__":
    run(main())
