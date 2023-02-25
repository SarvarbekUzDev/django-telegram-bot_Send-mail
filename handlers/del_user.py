from Bot.models import Users

from loader import dp
from states.states import Delete_State
from keyboards.inline_keyboards import inline_keyboard1, cancel_keyboard



# Delete user
def Del_user(request, get_json):
    data = {}

    if dp.callback_data(request, text="cancel"):
        Delete_State.chat_id.finish()
        dp.send_message(
            chat_id=get_json["callback_query"]["from"]["id"],
            text="Cancel❌",
        )

    # Delete admin
    if dp.message_handler(request, command='/del_user'):
        message = "Foydalanuvchi o'chirish xizmati\n\nFoydalanuvchi chat idsini kiritng: "
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
            reply_markup=cancel_keyboard,
            variable_name="cancel_keyboard"
        )
        # State start
        Delete_State.chat_id.set()

    elif dp.message_handler(request, state=Delete_State.chat_id.is_()):
        # State finish
        Delete_State.chat_id.update(text=get_json["message"]["text"])
        Delete_State.chat_id.finish()

        # Delete user
        chat_id = Delete_State.chat_id.get("chat_id")
        message = f"{chat_id} chat idsidagi foydalanuvchi o'chirildi✅"
        try:
            Users.objects.get(chat_id=chat_id).delete()
        except Exception as e:
            message = "Bunday foydalanuvchi mavjud emas❌"
        
        dp.send_message(
            chat_id=get_json["message"]["chat"]["id"],
            text=message,
        )