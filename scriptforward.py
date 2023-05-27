from telethon.sync import TelegramClient

# Replace the placeholders below with your own values
api_id = '24546246'
api_hash = 'f4701f42fe603625427a6fb6d2c9eebc'
phone_number = '+12015784790'

# Create an instance of the telegram client
with TelegramClient('anon', api_id, api_hash) as client:
    message = "i am blue dabadee"

    # Find the groups
    for group in ['cMj8BZ8dmjdiN2Vh', '9iEkY-LaBERmNDQ5', 'fukuuVUqhc9lOTlh']:
        try:
            entity = client.get_input_entity(group)

            # Send the message
            client.send_message(entity, message)
            print(f"Message sent to the {group} group")
        except ValueError:
            print(f"Couldn't find the {group} group")
# popazhopa
