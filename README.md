# AMNotify-Stock-Monitor
Monitors the AMNotify site for restocks

[@PerceptionIO Twitter](https://twitter.com/PerceptionIO)
     
[@navrxo](https://twitter.com/navrxo)

Requirements:
- Python 3

To Set Up:
1. Create a Webhook for your Discord Channel
2. Go to `config.json` and put your webhook where it says "INSERT WEBHOOK HERE", make sure to leave it in double quotes.
3. Put your proxies in `proxies.txt`, one on each line
2. cd the directory
3. Run `pip3 install -r requirements.txt` or `pip install -r requirements.txt`

To Run:
- If you are on Windows, run `python3 ammonitor_windows.py` or `python ammonitor_windows.py`
- If you are on a UNIX Based system, run `python3 ammonitor_unix.py` or `python3 ammonitor_unix.py`

When a restock is found, the notification will look like this - 
![AM-Stock](https://cdn.discordapp.com/attachments/530617706504912916/536652347493974026/unknown.png)
