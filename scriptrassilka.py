import asyncio
from telethon import TelegramClient, events, errors

api_id = input("Enter your API ID: ")
api_hash = input("Enter your API Hash: ")
source_group_link = input("Enter the link to the source group: ")

client = TelegramClient('anon', api_id, api_hash, flood_sleep_threshold=0)

async def main():
    source_group = await client.get_entity(source_group_link)
    
    dialogs = await client.get_dialogs()
    target_groups = [dialog.id for dialog in dialogs if dialog.is_group]
    
    success_count = 0
    total_groups = len(target_groups)
    
    @client.on(events.NewMessage(chats=source_group.id))
    async def handler(event):
        nonlocal success_count
        for group in target_groups:
            try:
                await client.forward_messages(group, event.message)
                success_count += 1
                print(f"Message forwarded to group {group}. ({success_count} of {total_groups})")
                await asyncio.sleep(7) # Add delay
            except errors.FloodWaitError as e:
                print(f"FloodWaitError. Must wait for {e.seconds} seconds.")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Could not forward message to group {group}. Error: {e}")
    
    await client.run_until_disconnected()

with client:
    client.start()
    client.loop.run_until_complete(main())
# popazhopa
