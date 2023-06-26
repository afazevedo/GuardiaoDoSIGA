import requests
from bs4 import BeautifulSoup
import re
import datetime
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def scrape_date_ranges():
    # Fetch the webpage
    url = "https://www.cos.ufrj.br/index.php/pt-BR/pos-graduacao/calendario-academico-graduacao-3/5910-calendario-academico-2023"
    response = requests.get(url)
    html = response.text

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table
    table = soup.find('table')

    # Get all text from the table
    table_text = table.get_text()

    # Find the position of "Inscrição em Disciplinas" in the text
    inscricao_pos = table_text.find("em Disciplinas")

    # Extract the subsequent text and dates
    dates = []
    if inscricao_pos != -1:
        subsequent_text = table_text[inscricao_pos:].replace('\n', ' ')
        # Extract the dates
        dates = re.findall(r'\d{2}/\d{2}/\d{4}', subsequent_text)
        # Only take the first 8 dates (4 pairs)
        dates = dates[:8]

    # Convert to datetime objects and pair them as ranges
    date_objects = [datetime.datetime.strptime(date, '%d/%m/%Y') for date in dates]
    date_ranges = [(date_objects[i], date_objects[i + 1]) for i in range(0, len(date_objects), 2)]

    return date_ranges

async def send_reminder(context: ContextTypes.DEFAULT_TYPE, chat_id):
    message = "Não se esqueça de se inscrever no SIGA!"
    await context.bot.send_message(chat_id=chat_id, text=message)

async def schedule_reminder(context: ContextTypes.DEFAULT_TYPE, chat_id, run_datetime):
    delay = (run_datetime - datetime.datetime.now()).total_seconds()
    await asyncio.sleep(delay)
    await send_reminder(context, chat_id)

async def start(update: Update, _: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id

    # Here we call the scrape_date_ranges function to get the dates
    date_ranges = await scrape_date_ranges()

    # Loop through each date range and set reminders
    for start_date, end_date in date_ranges:
        current_date = start_date
        while current_date <= end_date:
            # Set reminder time to 16:45
            run_datetime = datetime.datetime(current_date.year, current_date.month, current_date.day, 17, 30)
            if datetime.datetime.now() < run_datetime:
                asyncio.create_task(schedule_reminder(_, user_id, run_datetime))
            # Increment by one day
            current_date += datetime.timedelta(days=1)

    await update.message.reply_text("Lembretes configurados!")

async def help_command(update: Update, _: CallbackContext) -> None:
    help_message = (
        "🤖 Bem-vindo ao SIGA Lembretes Bot! 🤖\n\n"
        "Este bot foi criado para ajudar você a acompanhar os prazos de inscrição no SIGA.\n\n"
        "📅 Como funciona:\n"
        "O bot enviará lembretes automáticos todos os dias às 17:30 durante os períodos de inscrição.\n\n"
        "🔧 Comandos disponíveis:\n"
        "/start - Ativa os lembretes do bot.\n"
        "/help - Mostra esta mensagem de ajuda.\n\n"
        "🔔 Lembre-se de ativar as notificações para este bot para receber os lembretes.\n\n"
        "🚀 Comece agora mesmo usando o comando /start e fique por dentro dos prazos do SIGA!"
    )
    await update.message.reply_text(help_message)

if __name__ == "__main__":
    # Configuração do bot
    app = ApplicationBuilder().token("6056583080:AAHIsZLDerkg-nVhZ-iS0aYjvwHf3G0xbC0").build()

    # Adiciona o handler para o comando /start
    app.add_handler(CommandHandler("start", start))

    # Adiciona o handler para o comando /help
    app.add_handler(CommandHandler("help", help_command))

    # Inicia o bot
    app.run_polling()