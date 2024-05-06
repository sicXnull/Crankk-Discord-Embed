# Crankk Discord Embed
![image](https://github.com/sicXnull/Crankk-Discord-Embed/assets/31908995/feef4bd6-e644-4042-ab89-2bce643619a0)



## Installation


### Edit the following variables

1. `discord_webhook_url` - Add discord webhook link
2. `url` change URL to the IP of your Crankk Node
3. `authorization_key` Use chrome dev tools to grab authorization cookie for your login

## Run 

Run as cronjob. Example, every 6 hours. 

```
0 */6 * * * python3 /opt/scripts/crankk.py
```
