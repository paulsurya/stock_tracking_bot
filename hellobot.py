from telegram import Update,Bot
from telegram.ext import Application,filters,CommandHandler,MessageHandler,ContextTypes
import stock as s

token = '7533063538:AAFn6U86nZM5GaS-nBodFODdxZba14zvHq4'
botName = 'emfseofbot'
bot = Bot(token=token)
watchlist={}

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await bot.sendMessage(chat_id=update.message.chat. id,text='Welcome to *Trackify* ! I\'m your go-to bot for real-time stock and forex market updates. Want to track a specific stock or currency? Just send me its name or ticker symbol. Need help? Type \'/help\' for a list of commands',parse_mode='Markdown')

async def wallpaper_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("Sending Wallpaper")
    await bot.send_photo(update.message.chat.id,"\myPNG.png")

# async def document_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
#     await bot.send_document(update.message.chat.id,"C:\\Users\\pauls\\OneDrive\\Documents\\ARTIFICIAL INTELLIGENCE-mod.pdf")

async def watchlist_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if len(watchlist)==0:
        await bot.sendMessage(chat_id=update.message.chat.id,text="Sorry, But the watchlist is empty right now.But you can add stocks to the watchlist by using the /add command.",parse_mode="Markdown")
    else:
        processed_str = ""
        counter = 0
        for i in watchlist[update.message.chat.id]:
            counter += 1
            processed_str += f"\n1:({i["Type"]}):-\n**Name**: {i["Name"]}\n**Purchase Price**: {i["Purchase Price"]}\n**Date Of Purchase**: {i["DOP"]}\n**Profit%**: {i["Forecast"]}"
        await bot.sendMessage(chat_id=update.message.chat.id,text="Here are the stocks in your watchlist:"+processed_str,parse_mode="Markdown")


async def add_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if context.args:
        symbol = context.args[0]
        if s.get_type(symbol):
            watchlist+={update.message.chat.id:s.format_currency(symbol)}
        else:
            watchlist+={update.message.chat.id:s.format_stock(symbol)}
        await bot.sendMessage(chat_id=update.message.chat.id,text=symbol+" has been added to your watchlist",parse_mode="Markdown")
    else:
        await bot.sendMessage(chat_id=update.message.chat.id,text="Please a valid Ticker symbol.If you dont know what it is,then please visit [Yhaoo Finance](https://finance.yahoo.com/) to know more about Ticker symbol.",parse_mode="Markdown")

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update:{update} caused error:{context.error}')

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await bot.sendMessage(chat_id=update.message.chat.id,text="Here are some commands that i can perform:-\n1./portfolio\n2./watchlist\n3./add\n4./remove\n5./compare\n6./status",parse_mode="Markdown")

def handle_response()->str:
    text:str = update.message.text # type: ignore
    processed:str = text.lower()
    if 'fuck' in processed:
        return text+" u too"

async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    msg:str = update.message.chat.type
    text:str = update.message.text

    print(f'User({update.message.chat.id}) in {msg}:{text}')

if __name__ == '__main__':
    print('Starting: Hello Bot')
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('wallpaper',wallpaper_command))
    # app.add_handler(CommandHandler('document',document_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('watchlist',watchlist_command))
    app.add_handler(CommandHandler('add',add_command))


    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print('Polling.......')
    app.run_polling(poll_interval=3)