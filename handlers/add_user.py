from Bot.models import Users

from loader import dp
from states.states import Add_State
from keyboards.inline_keyboards import inline_keyboard1, cancel_keyboard



# Add user
def Add_user(request, get_json):
    data = {}

    if dp.callback_data(request, text="cancel"):
        Add_State.chat_id.finish()
        Add_State.is_admin.finish()
        dp.send_message(
            chat_id=get_json["callback_query"]["from"]["id"],
            text="Cancel❌",
        )

    # add user
    if dp.message_handler(request, command='/add_user'):
        message = "Admin kiritish xizmati\n\nAdmin chat idsini kiritng: "
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
            reply_markup=cancel_keyboard,
            variable_name="cancel_keyboard"
        )
        # State start
        Add_State.chat_id.set()

    # Chat id
    elif dp.message_handler(request, state=Add_State.chat_id.is_()):
        message = "Admin bo'lsinmi: "
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
            reply_markup=inline_keyboard1,
            variable_name="inline_keyboard1"
        )
        # State finish
        Add_State.chat_id.update(text=get_json["message"]["text"])
        Add_State.chat_id.finish()

        Add_State.is_admin.set()



    # User create
    elif Add_State.is_admin.set() and dp.callback_data(request, text="ok") or dp.callback_data(request, text="no"):
        data['is_admin'] = True if dp.callback_data(request, text="ok") else False

        chat_id = Add_State.chat_id.get("chat_id")
        Users.objects.create(
            chat_id=chat_id,
            is_admin=data['is_admin']
        )
        dp.send_message(
            chat_id=get_json["callback_query"]["from"]["id"],
            text=f"<strong>{chat_id}</strong> chat idda gi foydalanuvchi qo'shildi✅",
        )

        Add_State.is_admin.finish()