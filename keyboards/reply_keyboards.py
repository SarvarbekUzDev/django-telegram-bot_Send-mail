from dp.keyboards.reply_keyboard import ReplyKeyboardButton, ReplyKeyboardMarkup


# Buttons
send_mail_button = ReplyKeyboardButton(text="/send_mail")
add_admin_button = ReplyKeyboardButton(text="/add_user")
delete_admin_button = ReplyKeyboardButton(text="/del_user")

# Admin reply markup
reply_markup_admin = ReplyKeyboardMarkup(resize_keyboard=True, 
				variable_name="reply_markup_admin").add(
							send_mail_button,
							add_admin_button, True, delete_admin_button)


# User reply markup
reply_markup_user = ReplyKeyboardMarkup(resize_keyboard=True, 
				variable_name="reply_markup_user").add(send_mail_button)


