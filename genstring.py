#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nخلي الاييبي الايدي]\n > ")
API_HASH = input("\nخلي الايبي هاش \n > ")

print("\n\n خلي رقمك حبيب كلبي  \n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nهاي جلستك خلصت دربالك تشاركها تره ينيجوك ويهددوك بيها \n")
    print(f"\nسييييييي\n")


asyncio.run(main())
