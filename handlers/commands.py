from loader import dp
from Bot.functions import user_data_
from keyboards.reply_keyboards import reply_markup_admin, reply_markup_user



# bot commands function
def commands(request, get_json):
    user = user_data_(get_json).get('user')
    # command start
    if dp.message_handler(request, command="/start"):
        # not user
        if user is False:
            dp.send_message(
                chat_id=get_json["message"]["chat"]["id"],
                text=f"Assalomu alaykum {get_json['message']['chat']['first_name']}"
            )
        # user
        elif not user.is_admin:
            message = f"Assalomu alaykum hurmatli foydalanuvchi {get_json['message']['chat']['first_name']}"
            dp.send_message(
                chat_id=get_json["message"]["chat"]["id"],
                text=message,
                reply_markup=reply_markup_user,
                variable_name="reply_markup_user"
            )
        # Admin
        elif user.is_admin:
                message = f"Assalomu alaykum hurmatli admin {get_json['message']['chat']['first_name']}"
                dp.send_message(
                    chat_id=get_json["message"]["chat"]["id"],
                    text=message,
                    reply_markup=reply_markup_admin,
                    variable_name="reply_markup_admin"
                )

    # command help
    if dp.message_handler(request, command="/help"):
        message = "Assalomu alaykum.\nBu bot emailga xabar yuboruvchi bot"
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
        )
