from dp.keyboards.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup



cancel = InlineKeyboardButton(text="Cancel❌", callback_data="cancel")

Ok = InlineKeyboardButton(text="Ha✅", callback_data="ok")
No = InlineKeyboardButton(text="Yo'q❌", callback_data="no")
inline_keyboard1 = InlineKeyboardMarkup(variable_name="inline_keyboard1").add(Ok, True, No,
																				cancel)




# Cancel
cancel_keyboard = InlineKeyboardMarkup(variable_name="cancel_keyboard").add(cancel)