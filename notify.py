from nsetools import Nse
import time,requests

x = requests.get('https://maker.ifttt.com/trigger/notify/with/key/pl1VWQ5BWRHXona1uvQ7c9ZjuhhMX0-A-G0lXqg70gX')

while(True):
    quote1 = float(Nse().get_quote("YESBANK")['lastPrice'])
    quote2 = float(Nse().get_quote("RCOM")['lastPrice'])
    quote3 = float(Nse().get_quote("IDEA")['lastPrice'])
    print("YESBANK: ",quote1,"RCOM:", quote2, "IDEA: ", quote3)
    if quote1<10 or quote2<0.26 or quote3<3:
        y = requests.get('https://maker.ifttt.com/trigger/price_dropped/with/key/pl1VWQ5BWRHXona1uvQ7c9ZjuhhMX0-A-G0lXqg70gX')
    time.sleep(1)
    

