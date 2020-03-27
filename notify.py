from nsetools import Nse
import time,requests

x = requests.get('https://maker.ifttt.com/trigger/notify/with/key/pl1VWQ5BWRHXona1uvQ7c9ZjuhhMX0-A-G0lXqg70gX')

while(True):
    quote1 = float(Nse().get_quote("RCOM")['lastPrice'])
    quote2 = float(Nse().get_quote("YESBANK")['lastPrice'])
    print("RCOM: ",quote1,"YESBANK:", quote2)
    if quote1<10 or quote2<0.26:
        y = requests.get('https://maker.ifttt.com/trigger/price_dropped/with/key/pl1VWQ5BWRHXona1uvQ7c9ZjuhhMX0-A-G0lXqg70gX') #This is my key! Everytime this request I send get your key from IFTTT Webhooks API Documentation.
    time.sleep(1)
    

