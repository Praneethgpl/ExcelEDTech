
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("6181727089:AAHXx52Lwl_wtZQvLT2-ZLsxOO27aF81KXg",use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi..Let me help you with the tutorials..Please write /help to see the commands available.")
def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/html - To get html tutorial
    /css - To get the css tutorial
	/javascript- To get javascript tutorial
    /mongodb - To get the mongo db tutorial
	/mysql- To get the mysql tutorial
    /php - To get the php tutorial
    /pyhton - To get python tutorial
    /cpp - To get cpp tutorial
    /c - To get the c tutorial
    /java - To get the java tutorial""")
def html_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOOxqHgOzPyCzIl4AJjXbCYt")


def css_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOONc3kkuRmBOlj67YAG6jqo")


def javascript_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOMRMjHB_IEBjOW_ufr00yG1")


def mongodb_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZONbmOn3EsHac5u5_-Rue3ne")

def mysql_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOMskz6MdsMOgxzheIyjo-BZ")


def php_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOO6bGTY9jbLOyF_x6tgwcuB")


def python_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT")


def cpp_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOMHoXIcxze_lP97j2Ase2on")

def c_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOOzY_vR4zJM32SqsSInGMwe")


def java_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.youtube.com/playlist?list=PLZPZq0r_RZOMhCAyywfnYLlrjiVOkdAI1")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('html', html_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('css', css_url))
updater.dispatcher.add_handler(CommandHandler('javascript', javascript_url))
updater.dispatcher.add_handler(CommandHandler('mongodb', mongodb_url))
updater.dispatcher.add_handler(CommandHandler('mysql', mysql_url))
updater.dispatcher.add_handler(CommandHandler('php', php_url))
updater.dispatcher.add_handler(CommandHandler('python', python_url))
updater.dispatcher.add_handler(CommandHandler('cpp', cpp_url))
updater.dispatcher.add_handler(CommandHandler('c', c_url))
updater.dispatcher.add_handler(CommandHandler('java', java_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  
  

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
