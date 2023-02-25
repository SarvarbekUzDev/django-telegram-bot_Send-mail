from loader import dp
from Bot.functions import save_image, custom_send_mail
from states.states import Send_Mail_State
from keyboards.reply_keyboards import reply_markup_admin, reply_markup_user
from keyboards.inline_keyboards import cancel_keyboard


# Send mail
def sendmail(request, get_json):
    # start
    if dp.callback_data(request, text="cancel"):
        dp.send_message(
            chat_id=get_json["callback_query"]['from']["id"],
            text="Cancel❌",
        )
        Send_Mail_State.title.finish()
        Send_Mail_State.description.finish()
        Send_Mail_State.image.finish()

    elif dp.message_handler(request, command='/send_mail'):
        message = "Emailga ma'lumot yuborish xizmati\n\nMatn sarlavhasini kiriting: "
        key_b = dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
            reply_markup=cancel_keyboard,
            variable_name="cancel_keyboard"
        )
        Send_Mail_State.title.set()

    elif dp.message_handler(request, state=Send_Mail_State.title.is_()):
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text="Yaxshi endi matnni kiritng: ",
            reply_markup=cancel_keyboard,
            variable_name="cancel_keyboard"

        )
        # Title finish
        Send_Mail_State.title.update(text=get_json["message"]["text"])
        Send_Mail_State.title.finish()

        Send_Mail_State.description.set()

    elif dp.message_handler(request, state=Send_Mail_State.description.is_()):
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text="Endi rasm kiriting: ",
            reply_markup=cancel_keyboard,
            variable_name="cancel_keyboard"
        )
        Send_Mail_State.description.update(text=get_json["message"]["text"])
        Send_Mail_State.description.finish()

        Send_Mail_State.image.set()
    

    elif dp.message_handler(request, state=Send_Mail_State.image.is_()) and dp.message_handler(request, content_types='photo'):
        Send_Mail_State.image.update(text=get_json["message"]["photo"][0]['file_id'])
        Send_Mail_State.image.finish()

        # Send data
        msg = f"<b>Title:</b> {Send_Mail_State.title.get('title')}\n"
        msg += f"<b>Description:</b> {Send_Mail_State.description.get('description')}\n"

        image = Send_Mail_State.image.get('image')
        chat_id = get_json["message"]["chat"]["id"]
        send_pht = dp.send_photo(
            chat_id=chat_id,
            photo=image,
            caption=msg,
            )

        # Save Image
        image_path = save_image(image, chat_id)
        # Send Mail 
        custom_send_mail(
            image=image_path,
            title=Send_Mail_State.title.get('title'),
            description=Send_Mail_State.description.get('description')
        )