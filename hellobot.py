from telegram import Update,Bot
from telegram.ext import Application,filters,CommandHandler,MessageHandler,ContextTypes

token = '7533063538:AAFn6U86nZM5GaS-nBodFODdxZba14zvHq4'
botName = 'emfseofbot'
bot = Bot(token=token)

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await bot.sendMessage(chat_id=update.message.chat. id,text='Welcome to *Trackify* ! I\'m your go-to bot for real-time stock and forex market updates. Want to track a specific stock or currency? Just send me its name or ticker symbol. Need help? Type \'/help\' for a list of commands',parse_mode='Markdown')

async def wallpaper_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("Sending Wallpaper")
    await bot.send_photo(update.message.chat.id,"\myPNG.png")

async def document_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await bot.send_document(update.message.chat.id,"C:\\Users\\pauls\\OneDrive\\Documents\\ARTIFICIAL INTELLIGENCE-mod.pdf")

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update:{update} caused error:{context.error}')

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
    app.add_handler(CommandHandler('document',document_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print('Polling.......')
    app.run_polling(poll_interval=3)