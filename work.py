from telethon import TelegramClient, sync
import edit_our_bid

import time


def work(client, bank_id, random_meaning):
    first_cycle = True
    while True:
        message = client.get_messages('@sky_btc_bot')  # get message from server
        messages = str(message).split("KeyboardButtonCallback(text='")
        if len(messages) == 4:  # checking that we have received the right message
            messages = messages[1]
            if messages[0] == '📈':
                break
        if first_cycle:
            first_cycle = False
            client.send_message('@sky_btc_bot', '🔄 Обмен BTC')
    message[0].click(text='📈 Купить')  # click to button buy
    time.sleep(1)
    message = client.get_messages('@sky_btc_bot')
    messages = str(message).split("Callback(text='")

    if bank_id == 1:
        identificator_symbol = 'б'  # sber
    elif bank_id == 2:
        identificator_symbol = 'и'  # tink
    elif bank_id == 3:
        identificator_symbol = ' '  # С карты на карту
    elif bank_id == 4:
        identificator_symbol = 'ю'  # Любой банк РФ
    elif bank_id == 5:
        identificator_symbol = 'I'  # Visa
    elif bank_id == 6:
        identificator_symbol = 'a'  # Mastercard
    elif bank_id == 7:
        identificator_symbol = 'л'  # Альфа-Банк

    for i in range(1, 11):
        element = messages[i].split("'")
        if (element[0])[1] == identificator_symbol:
            message[0].click(text=element[0])  # click for button name bank
            break
    time.sleep(1)
    message = client.get_messages('@sky_btc_bot')
    messages = str(message).split("Callback(text='")
    button = []
    for i in range(1, 14):  # add name banks to list button
        element = messages[i].split("'")
        button.append(element[0])
    value_users = 0
    for i in range(0, 11):
        if button[i][0] == "🔵":  # we reached our position
            if value_users:  # if we  searched a value interrupt
                message[0].click(text=button[i])  # click to our position
                print("we edit our bid\n")
                edit_our_bid.edit_our_bid(client, value_users, random_meaning)
            else:
                print("we favorite\n")
                return  # whell then we favorite and exit from function
        if value_users == 0 and button[i][0] == "✅":  # if we don't search a value interrupt and search user with ✅
            element = button[i].split('- ')  # split to search a value users
            min_balance = element[1].split(' ')  # cut to end number
            if int(min_balance[0]) >= 10000:  # if balance user >10000 it our useful competitor
                value_users = element[0].split('.')  # take him value int form
                value_users = (value_users[0])[2:]
                print("The search the value is succesessful\n")
