import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup():
	markup = InlineKeyboardMarkup()
	markup.row_width = 4
	markup.add(InlineKeyboardButton("Нет", callback_data="cb_no"),
               InlineKeyboardButton("Скорее нет", callback_data="cb_mbno"),
               InlineKeyboardButton("Скорее да", callback_data="cb_mbyes"),
               InlineKeyboardButton("Да", callback_data="cb_yes"))
	return markup

def gen_markup_start():
	markup = InlineKeyboardMarkup()
	markup.row_width = 1
	markup.add(InlineKeyboardButton("Я все понял, давай начинать!", callback_data="cb_start"))
	return markup