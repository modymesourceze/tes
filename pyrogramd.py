from pyrogram import Client, filters

bot_token = "6635986173:AAH0Veius7B7-o6m4_lxWiMeW1ahqZqZ-o4"

api_id = 25281175
api_hash = "6d99cb2b60a2c519fc1f99bd19565730"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

