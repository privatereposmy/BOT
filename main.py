from pyrogram import Client


BOT = Client(
    "BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5545165624:AAGWkOcageIuHa7Ola0LDA-kBOXWElSrbNw",
    plugins=dict(root="plugins")
)


BOT.run
