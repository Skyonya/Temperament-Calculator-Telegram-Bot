import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
import calc_result
import calc_answer
import load_db
import inline_buttons

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	if call.data:
		calc_answer.add_answer(call.from_user.id, call.data)
		if calc_answer.get_len_answer(call.from_user.id) == calc_answer.get_max_len_answer():
			bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text=calc_result.calc_final_result(call.from_user.id))
			calc_answer.clear_answers(call.from_user.id)
		else:
			bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, 
                                  text=load_db.questionsText[calc_answer.get_len_answer(call.from_user.id)], 
                                  reply_markup=inline_buttons.gen_markup())

@bot.message_handler(commands = ['start'])
def start(message, res = False):
	calc_answer.add_user(message.from_user.id)
	calc_answer.clear_answers(message.from_user.id)
	bot.send_message(message.chat.id, load_db.textOnStart, reply_markup=inline_buttons.gen_markup_start())

bot.infinity_polling()