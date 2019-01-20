from dhooks import Webhook
import requests
from proxymanager import ProxyManager
import time
import discord
import json


print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  "------------------------------")
print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  '--------AMNotify Stock--------')
print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  '--------@PerceptionIO---------')
print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  '-----------@navrxo------------')
print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  '------------------------------')

false = False
true = True

availability = true
#Headers for the requests
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

#Initializes the ProxyManager, proxies.txt is the file with proxies in it
proxylist = ProxyManager('proxies.txt')

#URL Bot will be requesting
url = 'https://amnotify.com/api/stock/available'

#Define the monitor function
def monitor():
    proxy = proxylist.next_proxy() #Gets next proxy from the proxy list, this way it cycles in order
    proxies = proxy.get_dict() #Makes the 'Proxy Object(proxy) usable for an HTTP Request
    
    '''proxies are always stored like this in a dictionary
    {
        'http' : proxy,
        'https' : proxy,
    }
    '''

    #Prints out the proxy being used
    print(' [ '+ time.strftime('%H:%M:%S') + ' ] ' +  proxies['http'])

    #opens stock json, and checks what stock is
    file = open('stock.json', 'r')
    data = json.loads(file.read())
    stockold = data["available"]

    response = requests.get(url, headers=headers, proxies=proxies) #Gets the url specified and stores response in a variable
    
    #Since the response is in JSON format, you can call the json method on it. 
    #If the response is not in JSON format, this will return an error 
    res = response.json()

    #checks if availability is not same as old stock
    if res["available"] != stockold:
        if stockold == true and res['available'] == false:
            const_emb('Out of Stock')
            #changes stock value
            stockold = false
            with open('stock.json', 'w') as outfile:
                json.dump(data, outfile)

        else:
            const_emb('In stock')
            stockold = true
            with open('stock.json', 'w') as outfile:
                json.dump(data, outfile)

#Makes the embed function, so i can easily call it later
def const_emb(status):
    #opens the config.json file to get the Webhook
    file = open('config.json', 'r')
    data = json.loads(file.read())

    webhook = data["webhook"]

    embed = discord.Embed(
        title = 'AM Notify Stock Monitor',
        color = 0xEB414C
    )
    embed.add_field(name = 'Stock Status', value = status, inline = False)
    embed.set_footer(text='@PerceptionIO | @navrxo | ' + time.strftime('%H:%M:%S'), icon_url = 'https://cdn.discordapp.com/attachments/508733744249700353/518241988546396161/big_perception-01.png')

    if status == 'In Stock':
        embed.add_field(name = 'Link', value = '[Click Here](https://amnotify.com)', inline = False)
        hook = Webhook(webhook)
        hook.send(embeds=embed)
    else:
        hook = Webhook(webhook)
        hook.send(embeds=embed)

while True:
    monitor()
    time.sleep(5)