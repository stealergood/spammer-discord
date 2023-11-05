import requests as r
import time

# URL untuk mengirim pesan ke Discord
URL = "https://discordapp.com/api/v9/channels/737344491526029384/messages"

# Pesan spam yang akan dikirim
MESSAGE = "SELL FLOUR 20/1 AT BUMVFLOUR\nSELL FLOUR 20/1 AT BUMVFLOUR\nSELL FLOUR 20/1 AT BUMVFLOUR"

# Buat header HTTP
headers = {
    "Authorization": "NzI1MzI5MTE2NTQ2NzI4MDM3.GUyELv.SNarNxbm-yFapzJXYBuEREYpEmkR02vNYEU_oA",
}

# Kirim pesan spam
while True:
    response = r.post(URL, headers=headers, json={"content": MESSAGE})
    if response.status_code == 200:
        print("Pesan berhasil dikirim")
    else:
        print("Pesan gagal dikirim") 

    time.sleep(7300)
