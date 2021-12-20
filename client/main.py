from flux_led import WifiLedBulb
from websocket import WebSocketApp
# here you should put the private ip of your light
# so here is  the private ip of my light 
ip = "192.168.100.59"
bulb = WifiLedBulb(ip)
url="ws://localhost:8080/color"
def hex_to_rgb(hex):
    return int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)
def on_message(_, message):
    print(message)
    (r,g,b)=hex_to_rgb(message)
    bulb.set_levels(r,g,b)

def main():
    
    ws = WebSocketApp(url, on_message=on_message,on_open=lambda _: print("connected"))
    ws.run_forever()
    
if __name__ == "__main__":
    
    main()