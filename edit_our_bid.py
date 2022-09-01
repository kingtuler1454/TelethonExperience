def edit_our_bid(client, value_users, random_meaning):
    time.sleep(1)
    client.send_message('@sky_btc_bot', value_users - randint(1, random_meaning))  # start client
