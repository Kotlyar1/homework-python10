from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from random import randint


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Привет! Здесь можно выполнять разные арифметические действия с рациональными и комплексными числами! ) ")
    update.message.reply_text(main_menu_message(), reply_markup=main_menu_keyboard())


def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=main_menu_message(),
        reply_markup=main_menu_keyboard())


def first_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=first_menu_message(),
        reply_markup=first_menu_keyboard())


def second_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=second_menu_message(),
        reply_markup=second_menu_keyboard())


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Рациональные числа', callback_data='m1')],
                [InlineKeyboardButton('Комплексные числа', callback_data='m2')]]
    return InlineKeyboardMarkup(keyboard)


def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Складывать', callback_data='m1_1')],
                [InlineKeyboardButton('Вычитать', callback_data='m1_2')],
                [InlineKeyboardButton('Умножать', callback_data='m1_3')],
                [InlineKeyboardButton('Делить', callback_data='m1_4')]]
    return InlineKeyboardMarkup(keyboard)


def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Складывать', callback_data='m2_1')],
                [InlineKeyboardButton('Вычитать', callback_data='m2_2')],
                [InlineKeyboardButton('Умножать', callback_data='m2_3')],
                [InlineKeyboardButton('Делить', callback_data='m2_4')]]
    return InlineKeyboardMarkup(keyboard)


def main_menu_message():
    return 'Выберите действие:'


def first_menu_message():
    return 'Что будем делать с рациональными числами? '


def second_menu_message():
    return 'Что будем делать с комплексными числами? '


def first_submenu(bot, update):
    return "Введите первое число: "


def second_submenu(bot, update):
    pass


bot_token = "5622628765:AAGo3P8MTi4cRRK5KEDiIH8WlJ7Or2JlkRI"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_3'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_4'))

updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_2'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_3'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_4'))

updater.start_polling()