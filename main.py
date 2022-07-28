from pyrogram import Client


BOT = Client(
    "BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5545165624:AAGUHPgUtwrBTh7IKnVMcFzI0Rk-KY4I1cw",
    plugins=dict(root="Plugins")
)


BOT.run
