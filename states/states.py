from dp.states.states import State


# Send mail State
class Send_Mail_State:
	title = State(variable_name="title")
	description = State(variable_name="description")
	image = State(variable_name="image")



# Add State
class Add_State:
	chat_id = State(variable_name="chat_id")
	is_admin = State(variable_name="is_admin")


# Delete State
class Delete_State:
	chat_id = State(variable_name="chat_id")
