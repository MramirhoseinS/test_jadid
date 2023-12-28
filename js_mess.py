api_set = "6124548441:AAFg49l11HsWoKjQkWAlXuhmb9BTAxRNoHM"


# message


def message_id(m):
    return m.json["message_id"]


def user_id(m):
    return m.json["from"]["id"]

def user_name(m):
    return m.json["from"]["username"]

def chat_id(m):
    return m.json["chat"]["id"]


def text(m):
    return m.json["text"]


def reply_text(m):
    return m.json["reply_to_message"]["text"]


def reply_message_id(m):
    return m.json["reply_to_message"]["message_id"]


def reply_from_id(m):
    return m.json["reply_to_message"]["from"]["id"]


def reply_first_name(m):
    return m.json["reply_to_message"]["from"]["first_name"]


# callback


def callback_id_c(c):
    return c.json["id"]


def chat_id_c(c):
    return c.json["message"]["chat"]["id"]


def user_id_c(c):
    return c.json["from"]["id"]


def data_c(c):
    return c.json["data"]


def message_id_c(c):
    return c.json["message"]["message_id"]


def text_c(c):
    return c.json["message"]["text"]


def inline_message_id_c(c):
    return c.json["inline_message_id"]

# inline
def id_i(i):
    return i.id


def user_id_i(i):
    return i.from_user.id


def query_i(i):
    return i.query
