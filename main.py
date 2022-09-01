from telethon import TelegramClient, sync

import account
import work



def main():
    client = TelegramClient(account.pc_name, account.api_id, account.api_hash)  # values from account.py
    client.start()
    
    messages = str(client.get_messages('@marinopowns'))  # get message
    messages = messages.split(",")
    messages = list(messages[9])  # transform 9th element to list symbol
    if messages[10:17] == ['C', 'r', 'y', 'p', 't', 'e', 'x']:
        bank_list = input("""Choose banks for work:\n1.Sberbank\n2.Tinkoff\n3.С карты на карту\n4.Любой банк РФ\n
5.Visa\n6.Mastercard\n7.ALPHA\n""")
        random_meaning = input("Choose the value for lower the rate: ")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for bank_Id in bank_list:
            work.work(client, int(bank_Id), int(random_meaning))  # if key word is true


if __name__ == '__main__':
    main()
