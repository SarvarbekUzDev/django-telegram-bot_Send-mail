from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from loader import dp
from .functions import user_data_
from states.states import Send_Mail_State, Add_State, Delete_State
from handlers.commands import commands
from handlers.sendmail import sendmail
from handlers.add_user import Add_user
from handlers.del_user import Del_user

# Create your views here.


# Dipatcher function
@csrf_exempt
def dispatch(request):
    if request.method == 'GET':
         return JsonResponse({'Ok':True}, status=200)

    get_json = dp.get_json(request)

    # ---------------- Commands ---------------
    start = dp.message_handler(request, command="/start")
    help = dp.message_handler(request, command="/help")
    if start or help:
        commands(request, get_json=get_json)


    if user_data_(get_json).get('user') or user_data_(get_json, True):
        # ------------  Send Mail -----------------
        send_mail_msg = dp.message_handler(request, command='/send_mail')
        send_mail_title = dp.message_handler(request, state=Send_Mail_State.title.is_())
        send_mail_description = dp.message_handler(request, state=Send_Mail_State.description.is_())
        send_mail_image = dp.message_handler(request, state=Send_Mail_State.image.is_())
        
        if send_mail_msg or send_mail_title or send_mail_description or send_mail_image:
            sendmail(request, get_json)


    if user_data_(get_json).get('is_admin')  or user_data_(get_json, True):
        # ----------------- Add user ---------------------
        add_user = dp.message_handler(request, command='/add_user')
        chat_id = dp.message_handler(request, state=Add_State.chat_id.is_())
        is_admin_ = dp.message_handler(request, state=Add_State.is_admin.is_())

        if add_user or chat_id or is_admin_:
            Add_user(request, get_json)

        # --------------------- Del user --------------
        del_user = dp.message_handler(request, command='/del_user')
        chat_id = dp.message_handler(request, state=Delete_State.chat_id.is_())

        if del_user or chat_id:
            Del_user(request, get_json)



    return JsonResponse({'Ok':True}, status=200)