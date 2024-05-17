
from typing  import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN : Final = '6947461946:AAFNoU8xyXugkGGhYEZ8JMJB1yJFFISiagQ'
BOT_USERNAME: Final = '@mentalhealthbot_bot'

# commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello ! thanks for seeking help . I am mentalhealth_bot')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('how may i help you')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is custom command')

# Responses 

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return ' hello ! hope your doing well . what is the concern ?'
    
    if 'i am feeling depressed' in processed:
        return '  i am really sorry to hear that you are feeling depressed . priortizing mental wellbeing is very important. Try reaching out to the person you trust like a friend , family member or mental gealth professionals'
    
    if 'i am suffering from adhd' in processed:
        return 'Oh, I see! Living with ADHD can have its challenges, but remember that you are unique and amazing just the way you are. Is there anything specific you would like to talk about or share?'
    
    if 'i am priya' in processed:
        return ' hello priya ! how is it going . what is the concern ?'
    
    return 'Thanks for choosing me ! stay positive . I will help you out '
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot ....')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))



    app.add_handler(MessageHandler(filters.TEXT, handle_message))



    app.add_error_handler(error)
    print('polling...')
    app.run_polling(poll_interval=3)