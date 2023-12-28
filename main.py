import telebot
from telebot import types
from js_mess import *

api = api_set
bot = telebot.TeleBot(api)

users_ids = {}
nusers_ids = {}
ids_s = {}
dars = "درس مورد نظرت رو انتخاب کن"
ostad = "استاد مورد نظرت رو انتخاب کن"
jozve = "جزوه"
power = "پاورپوینت"
mess_choose_power = "."
mess_choose_mabhas = "مبحث مورد نظرت رو انتخاب کن"
nothing = "Nothing!"
mess_warn = """ 
    
            *همه فایلای این درس یکجا مخصوص چاپ*

            این فایلا ممکنه اضافه یا کم باشن و هیچ دسته بندی صورت نگرفته
            
            """




# ایدی فایل ها
@bot.channel_post_handler(content_types=["photo"])
def aks(m):
    ids = m.json["photo"][-1]["file_id"]
    bot.send_message(chat_id(m), ids)


@bot.channel_post_handler(content_types=["document"])
def aks(m):
    ids = m.json["document"]["file_id"]
    bot.send_message(chat_id(m), ids)


@bot.channel_post_handler(content_types=["audio"])
def aks(m):
    ids = m.json["audio"]["file_id"]
    bot.send_message(chat_id(m), ids)


@bot.channel_post_handler(content_types=["video"])
def aks(m):
    ids = m.json["video"]["file_id"]
    bot.send_message(chat_id(m), ids)


@bot.channel_post_handler(content_types=["video_note"])
def aks(m):
    ids = m.json["video_note"]["file_id"]
    bot.send_message(chat_id(m), ids)


@bot.channel_post_handler(content_types=["voice"])
def aks(m):
    ids = m.json["voice"]["file_id"]
    bot.send_message(chat_id(m), ids)





# فرستادن پیام به همه
@bot.message_handler(func=lambda m: text(m) == "/send" and (user_id(m) == 245633649 or user_id(m) == 6019680947))
def send_to_all(m):
    msg = bot.send_message(user_id(m), "پیامت رو بنویس")
    bot.register_next_step_handler(msg, sending)
def sending(m):
    all_users = []
    for x in users_ids:
        all_users.append(x)
    for all_user in all_users:
        bot.send_message(all_user, text(m))

# لیست افراد بات
@bot.message_handler(func=lambda m: text(m) == "/save" and (user_id(m) == 245633649 or user_id(m) == 6019680947))
def strat(m):
    all_users = []
    for x in users_ids:
        all_users.append(x)
    bot.send_message(user_id(m), len(all_users))

    bot.send_message(user_id(m), str(list(users_ids.items())))
    bot.send_message(user_id(m), str(list(nusers_ids.items())))


# ایدی افراد بات
@bot.message_handler(func=lambda m: text(m) == "/ids" and (user_id(m) == 245633649 or user_id(m) == 6019680947))
def ids(m):
    all_useranme = []
    for x in ids_s:
        all_useranme.append(f"@{x}")
    bot.send_message(user_id(m), str(all_useranme))


# هر فرد چند بار تو بات بوده
@bot.message_handler(func=lambda m: text(m) == "/who" and (user_id(m) == 245633649 or user_id(m) == 6019680947))
def who(m):
    bot.send_message(user_id(m), str(list(ids_s.items())))


# شروع

@bot.message_handler(
    func=lambda m: text(m) == "/start"
)
def start(m):
    users_ids[user_id(m)] = "first"
    nusers_ids[user_id(m)] = "first"
    try:
        if ids_s.get(user_name(m)) == None:
            ids_s[user_name(m)] = 1
    except Exception:
        pass


    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("ترم ۱", "ترم ۲")

    bot.send_message(chat_id(m), "خوش اومدی⛄️", reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "term")
    or (users_ids.get(user_id(m)) == None)
)
def start(m):
    try:
        if ids_s.get(user_name(m)) == None:
            ids_s[user_name(m)] = 1
        else:
            ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "first"
    nusers_ids[user_id(m)] = "first"


    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("ترم ۱", "ترم ۲")

    bot.send_message(chat_id(m), "ترم مورد نظرت رو انتخاب کن", reply_markup=re)



# لیست دروس ترم ۱
@bot.message_handler(
    func=lambda m: (text(m) == "ترم ۱" and nusers_ids.get(user_id(m)) == "first")
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "dars_term1")
)
def term1(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "term"
    nusers_ids[user_id(m)] = "term1"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("اصول و فنون پرستاری")
    re.row("بیوشیمی")
    re.row("میکروب شناسی")
    re.row("فیزیولوژی")
    re.row("انگل شناسی")
    re.row("تشریح")
    re.row("بازگشت")

    bot.send_message(chat_id(m), dars, reply_markup=re)


# اصول و فنون
@bot.message_handler(
    func=lambda m: (
        text(m) == "اصول و فنون پرستاری"
        and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_nurse")
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "p_nurse")
)
def nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "nurse"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر خواجه", "خانم فدایی")
    re.row("خانم ایمانی", "آقای میرحسینی")
    re.row("پراتیک")
    re.row("منبع اصول و فنون پرستاری")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: text(m) == "منبع اصول و فنون پرستاری"
    and nusers_ids.get(user_id(m)) == "nurse"
)
def book_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAU9lA_4OPHMLlDA1Nn3b9IC_moewNgAC8AoAAgfZIFIxhpulwXZ7jTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAVNlA_5R5F2WH3VTC2LcKZ4wOGHvXQAClA0AAvxmsFOBv6Ud0GLWCTAE",
    )


@bot.message_handler(
    func=lambda m: text(m) == "دکتر خواجه" and nusers_ids.get(user_id(m)) == "nurse"
)
def os_kh_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAVZlA_8DdGkXRfmPZQx1Vg_uj8EdWwAChQwAAoDcgVO5apUpIkjxgzAE",
        caption="مراقبت های قبل، حین و بعد از جراحی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAVhlA_8dpgWgph4JhWwjE4-iCsEPgwACEw8AAnSY6VPktZEup8LW5jAE",
        caption="تجویز دارو و محاسبات دارویی پارت 1",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAVplA_80O6qCq1bZiT7UbobJojBtlAACFA8AAnSY6VNiK-Adbfy0rjAE",
        caption="تجویز دارو و محاسبات دارویی پارت 2",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAVxlA_9MNnTNfwggaYc3Pgf07lIQ3gACFQ8AAnSY6VOCtL8J-tqwrjAE",
        caption="تجویز دارو و محاسبات دارویی پارت 3",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAV5lA_9m9kH_k7MxVkF1ptwIg1oqDwACOg8AAlAocVEAATG_GWofaTIwBA",
        caption="حرکت و بی حرکتی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXNlBAABqAMucwvm5IUk2eA75rHGn80AAigOAAK5sxhTZm8s8g39HP8wBA",
        caption="کنترل درد",
    )


@bot.message_handler(
    func=lambda m: text(m) == "خانم فدایی" and nusers_ids.get(user_id(m)) == "nurse"
)
def os_fa_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWBlA__Px91Lg3H6nZeaKJzgY9ojAgACpw0AAgTjAVDegqAYzWERLTAE",
        caption="مفهوم تغذیه در مددجویان\nپسورد فایل: FADAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWJlA__oPUQNhZC8Wv1stn5LoBDsewACHw8AAkVMkFCC9KAPyJHOqDAE",
        caption="خواب و ریتم ها",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWRlA__2hBEsOWArHf_ONlb1NA_cNAAC0Q4AAhFzsFEg9kJ9k9-IJjAE",
        caption="گزارش نویسی",
    )


@bot.message_handler(
    func=lambda m: text(m) == "آقای میرحسینی" and nusers_ids.get(user_id(m)) == "nurse"
)
def os_mi_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWZlBAABHkn8-dhPQHnx6XXH_rYN57YAAk0NAAKH11BQ5Djq3cd2KT8wBA",
        caption="ماهیت پرستاری",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWhlBAABLneVL6qh12v0QzZtewIfrtUAAk4NAAKH11BQ04eB6bA2pDwwBA",
        caption="نیاز های انسان",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWplBAABQYGvRNntcdgpuZjdyknPbrYAAkwNAAKH11BQpxB8VCyU44QwBA",
        caption="سلامت و بیماری",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAWxlBAABWrLcL10PseA4IAJkuxlqOyoAAj8NAAKH11BQX_buWbT9XqowBA",
        caption="پذیرش، ترخیص و انتقال",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAW5lBAABa_MJdLkVGE_GneUIU0B16oMAApoNAAK5sxhTonOImvFXqeYwBA",
        caption="فرایند پرستاری",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXFlBAABiC7neseHIxWHmoXMxiqdn6UAApsNAAK5sxhT5rjiEtbG1vQwBA",
        caption="مراقبت از زخم",
    )


@bot.message_handler(
    func=lambda m: text(m) == "خانم ایمانی" and nusers_ids.get(user_id(m)) == "nurse"
)
def os_im_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXVlBAJUl8JMPhs99LTI_cmQFWaw8QACHg8AAkVMkFCZnWjyAAGlMSkwBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXdlBAJftgFPuZPe70CX8EkT4z3v9wACVRAAAqH-kFL6sW5OT3vdNjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXllBAKAUaJxRimWP-EuhJcfErewxAACVhAAAqH-kFJJcz_0ug0HgzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAXtlBAKi6Wa69t76mkdVjJFmc2eecwACVxAAAqH-kFLcYiNSYnGgiTAE",
    )


# پراتیک اصول و فنون
@bot.message_handler(
    func=lambda m: (text(m) == "پراتیک" and nusers_ids.get(user_id(m)) == "nurse")
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_p_nurse")
)
def p_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "p_nurse"
    nusers_ids[user_id(m)] = "p_nurse"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر خواجه", "خانم فدایی")
    re.row("خانم ایمانی")
    re.row("چک لیست ها")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: text(m) == "چک لیست ها" and nusers_ids.get(user_id(m)) == "p_nurse"
)
def check_list(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAX1lBALtUm2TNjFTPXTZqY19Jm0-MQACPBAAAoSqWFOKgPOF4usTozAE",
        caption="چک لیست های امتحان پراتیک",
    )


@bot.message_handler(
    func=lambda m: text(m) == "دکتر خواجه" and nusers_ids.get(user_id(m)) == "p_nurse"
)
def os_p_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAX9lBAMNsV6jzTBBY9geGUBDs2XT2QAC7xAAAs3JsVF04f65p-uHyDAE",
        caption="محاسبات دارویی",
    )
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAYFlBAMnuoSiQScErzkMoctHkv1GYAAC8RAAAs3JsVE7zTKMwKxiejAE",
        caption="تزریقات\nhttps://b2n.ir/257619",
    )


@bot.message_handler(
    func=lambda m: text(m) == "خانم فدایی" and nusers_ids.get(user_id(m)) == "p_nurse"
)
def os_p_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAYNlBANvSH06lnY2GKtwhGFnXqu7dQAC5wwAAlhuAAFQVEEhvQ5YHe0wBA",
        caption="فیلم اموزشی عملی اکسیژن تراپی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAYVlBAOFpCssFU2MF6i6xX09jz42VwAC6wwAAlhuAAFQJ4EWMAs0miYwBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAYdlBAOWj8UImry2NqlmaEtVQI8xaAAC7AwAAlhuAAFQv50hBhBd_TcwBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAYllBAOqNtgFjdXDB5C5AqCA4BBnZAAC7QwAAlhuAAFQaStpPUjYpJkwBA",
        caption="فیلم ساکشن راه هوایی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAYtlBAO9hS_QLQH91HQenc0dW-lfmQAC7gwAAlhuAAFQpT2gB6SB0tMwBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAY1lBAPN9TnFsj-y-K2A6hkeiM6r_QAC7wwAAlhuAAFQdrDQlzYWQNAwBA",
        caption="سند گذاری بینی معده ای - دهانی معده ای",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAY9lBAPor3KCQcOayNmehROh2ajoYwAC8AwAAlhuAAFQ74P_fR9nrDAwBA",
        caption="سند گذاری بینی معده ای - دهانی معده ای",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAZFlBAP-yrxb5EzPi7mLeqtVlG42YAAC8QwAAlhuAAFQMpTmyte0T4QwBA",
        caption="گاواژ",
    )


@bot.message_handler(
    func=lambda m: text(m) == "خانم ایمانی" and nusers_ids.get(user_id(m)) == "p_nurse"
)
def os_p_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "os_p_nurse"
    nusers_ids[user_id(m)] = "nurse_p_imani"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("شستن دست و پوشیدن دستکش", "علائم حیاتی")
    re.row("گرما و سرما درمانی", "انما")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_mabhas, reply_markup=re)


@bot.message_handler(
    func=lambda m: text(m) == "شستن دست و پوشیدن دستکش"
    and nusers_ids.get(user_id(m)) == "nurse_p_imani"
)
def os_p_im_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZNlBAQe7sJtiVr5fcOYe0J2UrP2qwACWRAAAqH-kFKEkFxWg35rGjAE",
        caption="پوشیدن دستکش و گان",
    )
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZVlBAQwBv9dIYMXfaMkNpXnOzSYcAACWhAAAqH-kFJziB6jtHUy3zAE",
        caption="شستن جراحی دست",
    )
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZdlBARHHz9U4ohMGbGQ9B2OnW0DBgACWxAAAqH-kFLQrJpglHE81jAE",
        caption="شستن جراحی دست و پوشیدن دستکش و گان",
    )


@bot.message_handler(
    func=lambda m: text(m) == "علائم حیاتی"
    and nusers_ids.get(user_id(m)) == "nurse_p_imani"
)
def os_p_im_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZllBARcXwR8zn7uv1dsPjMyYAlL1AACXBAAAqH-kFKrEDaLl7EIIDAE",
        caption="علائم حیاتی، نبض و فشار",
    )
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZtlBARwipU_UCw08v15NSP4tCq1iAACXRAAAqH-kFItybm1gtPoizAE",
        caption="علائم حیاتی، فشار خون",
    )
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZ1lBASCe8Fr0zL5atIe1WD5o3psYwACXxAAAqH-kFI_XmQWyDCT1jAE",
        caption="علائم حیاتی، دما و تنفس",
    )


@bot.message_handler(
    func=lambda m: text(m) == "گرما و سرما درمانی"
    and nusers_ids.get(user_id(m)) == "nurse_p_imani"
)
def os_p_im_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAZ9lBAUt5tccoVavDisRj4k3oaqE0wACYBAAAqH-kFJjjw-uVcSUcDAE",
        caption="گرما و سرما درمانی",
    )


@bot.message_handler(
    func=lambda m: text(m) == "انما" and nusers_ids.get(user_id(m)) == "nurse_p_imani"
)
def os_p_im_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_video(
        chat_id(m),
        "BAACAgQAAx0Cbu8Z0gACAaFlBAVErg-zVLocHEfyQTffcWwJ_QACYRAAAqH-kFKW6TgXMjlULzAE",
        caption="انما",
    )


# بیوشیمی
@bot.message_handler(
    func=lambda m: (
        text(m) == "بیوشیمی" and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_bio")
)
def biochemistery(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "os_bio"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("خانم عباسیان")
    re.row("🔬 آزمایشگاه بیوشیمی🔬")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "خانم عباسیان" and nusers_ids.get(user_id(m)) == "os_bio"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "bio_abb")
)
def abasian(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "os_bio"
    nusers_ids[user_id(m)] = "bio_abb"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "bio_abb")
)
def power_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "bio_abb"
    nusers_ids[user_id(m)] = "power_bio_abb"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("مبحث ph و قند")
    re.row("مبحث آنزیم و آنزیم بالینی")
    re.row("مبحث های باقیمانده")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_mabhas, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث ph و قند" and nusers_ids.get(user_id(m)) == "power_bio_abb"
    )
)
def power_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAbdlBDVDbfZfWRNeKQXwPv0BnNtxzgACJw8AAmGWgFO_5uUvLBqN0jAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAbllBDVSC9D0q4DEItN55nEXzsCwYwACKA8AAmGWgFMzpgdfy8_-eTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAbtlBDVj8a43RGuJKij65d2FfFdMNQACKQ8AAmGWgFPbpbB-PNBQuDAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث آنزیم و آنزیم بالینی"
        and nusers_ids.get(user_id(m)) == "power_bio_abb"
    )
)
def power_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAb1lBDV_q71fNeCyAcn79wzDgtPAIgAC6RAAApvVSVBJcd9Kx6tfNDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAb9lBDWPrMwvcy9djOXZzG1BO2YrYQAC5xAAApvVSVBKlRM3KjxIGjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAcFlBDWdLLGKJrLF5w4F1JuknSOpIgAC6BAAApvVSVDlLaJiXtgxoTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAcNlBDWuZ34YpM_CrfdBalhsXBkgJAAC0g4AAuYlgVLshZHTW-dEtTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAcVlBDW9so9U-lFAQJqV1xDJ1VbTfAAC1A4AAuYlgVJtc5SIltg-SjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAcdlBDXaf6BJXETnKtBKrMsmuMzPbAAC1Q4AAuYlgVKbmZHRlnySqDAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث های باقیمانده"
        and nusers_ids.get(user_id(m)) == "power_bio_abb"
    )
)
def power_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAcllBDX809WQpjM2USTyMmJWRr67gwAC1g4AAuYlgVIpGNbO5Bjr3TAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACActlBDYNG6jDsLT0bjbZvxOPJ_a5cAAC2g4AAuYlgVL1cjbM6eN94zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAc1lBDYfiwPJxmxuhSk-fqmhmqIitQAC2w4AAuYlgVI7JnY7BggHLzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAc9lBDY3rl1YhLW-A-mqU2hjoL3MmgAC3Q4AAuYlgVLCCs4SygRTXDAE",
    )


@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "bio_abb")
)
def power_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "bio_abb"
    nusers_ids[user_id(m)] = "jozve_bio_abb"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("مبحث ph و قند")
    re.row("مبحث آنزیم و آنزیم بالینی")
    re.row("مبحث های باقیمانده")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_mabhas, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث ph و قند" and nusers_ids.get(user_id(m)) == "jozve_bio_abb"
    )
)
def jozve_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAdFlBDZ4AxrGW0nRWOnZx5iK8VYp4QACWhEAAmjheVMGiJMjdnLjTTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAdNlBDaKMnwPyNehSsEo3okVOGp0_wACXBEAAmjheVOEQ1UvbVadHjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAdVlBDblMq7h_uDA7_XOzsayxvMHaQACXxEAAmjheVO35nryKpWB2jAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAddlBDb77Tm9_JEMmigAAWEQ2AABEfqHAAJgEQACaOF5U7PYIxeXw5u1MAQ",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAdllBDcFbfEJ0jeEp9eNHdlMLRlztgACXhEAAmjheVNR1NUJCa8edDAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث آنزیم و آنزیم بالینی"
        and nusers_ids.get(user_id(m)) == "jozve_bio_abb"
    )
)
def jozve_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAdtlBDch-yRqBoF2bbIabVuaW708OAACAQ8AAuYlgVIexJXT91Ft6zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAd1lBDct2vSBdYnz2RSunYZ-6Pg3VQACAg8AAuYlgVLx2rSNA5dc6zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAd9lBDdEHNlQigbtqxhjM8fDQq8QcQACBA8AAuYlgVKf-LfpmNrFVjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAeFlBDdR0H_4ZHR7jSqRtEn6n6vkoAACBg8AAuYlgVJWpX69hJap4DAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "مبحث های باقیمانده"
        and nusers_ids.get(user_id(m)) == "jozve_bio_abb"
    )
)
def jozve_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAeNlBDdixknpo6JVHIbUS64xtwUgxAACCQ8AAuYlgVLZRE39NFAZYTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAeVlBDdtugmnB8NiV4MrImo-_xLVvQACCg8AAuYlgVJ-QyGKlZeZcTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAedlBDd-N6DpY0_wHDudDknjmRpShwACCw8AAuYlgVKgVJo_MAwIiDAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "🔬 آزمایشگاه بیوشیمی🔬" and nusers_ids.get(user_id(m)) == "os_bio"
    )
)
def abasian(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "os_bio"
    nusers_ids[user_id(m)] = "bio_az"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "bio_az")
)
def power_bio_az(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAellBDegnQ2rWmOdN67X69yFwrdbngAC0AwAAhqFqVIdT9PVDH6whTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAetlBDeyNgROPQNIVIVfZB2iJBHAOwAC0QwAAhqFqVIpHXFSF69YPjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAe1lBDfwRnB9JbgCnF5VmMW4x-NPpAAC0gwAAhqFqVKgaIZRFj_zhDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAe9lBDgB25EeJ6f3s6hO7UGS0nTx6wACjw8AAkhWQVNy9RdTCOBlzjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAfFlBDgSdhP-4bqmGJt6op_sypXQ_wACkA8AAkhWQVPSDnl8i8RNEDAE",
    )


@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "bio_az")
)
def jozve_bio_abb(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAfNlBDgn2RCZnX0BL2iFKSl-64FwUQACGQ4AAmjhgVP21RdSAAGKKsYwBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAfVlBDg2CB6Rp3SpMpUis7q7UsbFsgACGA4AAmjhgVOWDnstdH3S9DAE"
    )


# میکروب شناسی
@bot.message_handler(
    func=lambda m: (
        text(m) == "میکروب شناسی"
        and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_micro")
)
def biochemistery(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "os_micro"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر نوشک")
    re.row("🔬 آزمایشگاه میکروب شناسی🔬")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == "دکتر نوشک" and nusers_ids.get(user_id(m)) == "os_micro")
)
def power_noosh(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAfdlBDjjDS6-cKuP-UjVbli3sglQ2gACLA8AAhKDAVKHpsvPYO7ZEzAE",
        caption="طبقه بندی و ساختار",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAfllBDjzo5hItE4QU07gOBDlNkpNGgAC9BcAAuMtkFLyRaUGyeT9ujAE",
        caption="استافیلوکوک ها",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAftlBDkF6AqZkVDF65UPSZHWCDcOsQAC9hcAAuMtkFKYIPqMs8GTijAE",
        caption="استرپتوکوک ها",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAf1lBDkdjrLQkS6P7uxIzh8rxSvRHQAC9xcAAuMtkFKwV42iOigILTAE",
        caption="ویروس شناسی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAf9lBDkrkIhYwBPSE1l2KfRYh5E5egAC-BcAAuMtkFLDLuvWJXD8cTAE",
        caption="آنتی بیوتیک ها",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "🔬 آزمایشگاه میکروب شناسی🔬"
        and nusers_ids.get(user_id(m)) == "os_micro"
    )
)
def power_bio_az(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgFlBDlLhC0-7-vtqi8E-kmwsHc3owACwxAAApvVSVCxhdD6pt5J6TAE",
        caption="پی دی اف استاد فضلی",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgNlBDlYmh8uR-Kypu1aJNquCa4J_QAC-xcAAuMtkFKZtanKIW8bxjAE",
        caption="خلاصه همراه با عکس",
    )


# فیزیولوژی
@bot.message_handler(
    func=lambda m: (
        text(m) == "فیزیولوژی" and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_phisio")
)
def phisiology(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "os_phisio"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر گرمابی", "دکتر خاکساری")
    re.row("🔬 آزمایشگاه فیزیولوژی 🔬")
    re.row("📔 فیزیولوژی گایتون 📔")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "🔬 آزمایشگاه فیزیولوژی 🔬"
        and nusers_ids.get(user_id(m)) == "os_phisio"
    )
)
def phisio_lab(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgVlBDmutQGpFvW5x18wB4bk6waiTwAClAwAAgjSqVNkZ0BD_ZF1SjAE"
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "📔 فیزیولوژی گایتون 📔" and nusers_ids.get(user_id(m)) == "os_phisio"
    )
)
def phisio_gaiton(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgdlBDnGB_lP2HwUf1ZOhnX6n7mtagACWREAAmjheVPlzi2UcKHV5TAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر گرمابی" and nusers_ids.get(user_id(m)) == "os_phisio"
    )
)
def phisio_gar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "os_phisio"
    nusers_ids[user_id(m)] = "phisio_gar"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "phisio_gar")
)
def power_phisio_gar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgllBDoWVSpL8WxYUqJUWWdL2izFKgAC3g4AAtpM4VGBoJTy02j3bjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAgtlBDoo09_rt-HRcl7ZjyJeu9tHIwACbRgAAuMtkFL_JYra-sxApDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAg1lBDo1y3p1QsojYL78P4eoNzTBXgACcBgAAuMtkFKy6IPwl1-PZzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAg9lBDpDUYj1kl7HECA9NE6wZhwFmwACcRgAAuMtkFKb1aTN4y_H3zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhFlBDpViRgGEm_bOYkdkYXc5vsZxwACdRgAAuMtkFJ-zcvlxij4pDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhNlBDpl_rT3PU1G0AlKC81qeeiYkwACdhgAAuMtkFIusCjlq9EyATAE",
    )


@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "phisio_gar")
)
def jozve_phisio_gar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhVlBDp3K2R7w4qnMIpgXtbqzc_LxQACVhEAAmjheVPjRlqpdj0nRTAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر خاکساری" and nusers_ids.get(user_id(m)) == "os_phisio"
    )
)
def power_phisio_khak(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhdlBDqUeZ_PWK1-xRe8VWUSbQO7HwACLg8AAmGWgFONEYnnGzismDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhllBDqja9t4q8UHxTU8rkwcEmP5tgACRA0AAgTjCVAK9l1vpYnY0TAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAhtlBDq0DQ_VHuAP0dshgDnlUtiA4AACRQ0AAgTjCVB1lhBAGUYMZjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAh1lBDrBNVKsrUXRXnmHSX9ILhLP3gAC5A8AAsC_cFAoe2pCGj2b7DAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAh9lBDrQPbV2chuJBT5FhKbwoA7Z4gAC5Q8AAsC_cFCr7EVNFob53zAE",
    )




# انگل شناسی
@bot.message_handler(
    func=lambda m: (
        text(m) == "انگل شناسی"
        and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_parasi")
)
def parasaitology(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "os_parasi"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر عسگریان")
    re.row("🔬 آزمایشگاه انگل شناسی 🔬")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر عسگریان" and nusers_ids.get(user_id(m)) == "os_parasi"
    )
)
def power_para_asgar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAiFlBDtYIEO-JToO-6xgjBQveNU2qAACLQ8AAmGWgFNZ3SulUARLxjAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAiNlBDtm3rWLRin2PAOkCr_bh2j0ywACEg4AAmF8mVNWQwhXzlkOdTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAiVlBDt1I6SVbWgNPj3KhZA7L2_syAAC6hAAApvVSVALrRXvIrQujzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAidlBDuCYRswBy-wJGS6z5-d0IehlAAC3w4AAtpM4VEHqd1ZO2cQ-zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAillBDuPlBaY3mbhtiFVDZXOYY7N_AAC7hcAAuMtkFJ5T_LIK0dijTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAitlBDud35Uu1ORAhFM9jvb6zLvgUgAC7xcAAuMtkFL07uOM7rvh5DAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAi1lBDurJ8rgo-jThOvBuY4gTqEzRQACVREAAq_W2FCl35CltOicyDAE",
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "🔬 آزمایشگاه انگل شناسی 🔬"
        and nusers_ids.get(user_id(m)) == "os_parasi"
    )
)
def az_para(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAi9lBDvEqGaiyIRNz-kdqQM0JRN3ewACDg4AAmF8mVNGHpnEulmedTAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjFlBDvbo-ZKMSdyBGyuBYPjCymjZAACYA4AAnLz4FNL36enNPLDXzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjNlBDvnnW1ZMFyy1lY_binzdhRBTQAC6xAAApvVSVAPrrd7ipkH_jAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjVlBDvzph4pKFJxLVuL8dDacN5cKgAC4A4AAtpM4VGj0P8_v0953zAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjdlBDwCRUzVU16gzBNjUBr1OutZuwAC4Q4AAtpM4VEwOJI62hINETAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjllBDwRYdHZ1QI2Qxj_VZl6yg11WgAC8hcAAuMtkFIkqEzbMU-LYzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAjtlBDwjessikBaUpYgAAXVyKSoC2OIAArQPAALKfQhQFqAuFxS5pfgwBA",
        caption="جزوه انگل شناسی",
    )


# آناتومی
@bot.message_handler(
    func=lambda m: (
        text(m) == "تشریح" and nusers_ids.get(user_id(m)) == "term1"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "os_ana")
)
def anatomy(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term1"
    nusers_ids[user_id(m)] = "os_ana"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر تولی")
    re.row("منبع تشریح")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)


@bot.message_handler(
    func=lambda m: (
        text(m) == "منبع تشریح" and nusers_ids.get(user_id(m)) == "os_ana"
    )
)
def jozve_ana_tol(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAj1lBDxhI7AzvBWnqAJbUM6UGMMFUAACwhAAApvVSVDUbFxnPqNi_jAE",
    )


@bot.message_handler(
    func=lambda m: (text(m) == "دکتر تولی" and nusers_ids.get(user_id(m)) == "os_ana")
)
def ana_tol(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "os_ana"
    nusers_ids[user_id(m)] = "ana_tol"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "ana_tol")
)
def power_ana_tol(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAj9lBDx4yGejTfZK7JWl77r1osj42wACKg8AAmGWgFNluWxC3fEFszAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAkFlBDyKI2ZPrdLzGb3UcVPKMYYKSQACKw8AAmGWgFN3cFAJLDhZDzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAkNlBDyWb0c3FkdyY5e9MOlJaHjMpwAC5hAAApvVSVCXBAEAAdziIrIwBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAkVlBDypENqYwLLAuMv3GVIreqi8JwACEw4AArcF6FNjFpaOc1RfzDAE",
        caption="مفصل",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAkdlBDy6STI23OdxAh4Tkz6WuzfpiwAC4A8AAqgWqFJzydLWDzq1pDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAkllBDzEJH4AAS63qjum2EeD678li_kAAuEPAAKoFqhSFYaYl0OYR8swBA",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAktlBDzg3rJ-crbqmSX0hQkj8ZoLqAAC4g8AAqgWqFIRngWwSelXDzAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAk1lBDz5MhUj_661f_PJEbqrOzHJwAAC5Q8AAqgWqFLUiX3TMSEUYDAE",
    )
    bot.send_message(chat_id(m), "عصب")
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAk9lBD0NO52mxHapq2RmCM3ylC9mawAC5A8AAqgWqFLS7VDuGl2poDAE",
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAlFlBD0a-O-XUJvW-EJiWCzqWG5gdwAC5g8AAqgWqFJp__AYk5cv6zAE",
    )
    bot.send_message(chat_id(m), "ادراری تناسلی")


@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "ana_tol")
)
def jozve_ana_tol(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAlNlBD0u_A7vH2Hy-x6AYua7gD8RlQACVxEAAmjheVOZEUruOs-wZzAE",
    )



# ترم ۲
@bot.message_handler(
    func=lambda m: (text(m) == "ترم ۲"  and nusers_ids.get(user_id(m)) == "first")
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "dars_term2")
)
def term1(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "term"
    nusers_ids[user_id(m)] = "term2"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("مفاهیم پایه پرستاری")
    re.row("ژنتیک و ایمونولوژی")
    re.row("داروشناسی")
    re.row("پرستاری سلامت جامعه")
    re.row("تغذیه")
    re.row("فناوری اطلاعات در پرستاری")
    re.row("روانشناسی فردی و اجتماعی")
    re.row("اخلاق پرستاری")
    re.row("زبان عمومی")
    re.row("بازگشت")

    bot.send_message(chat_id(m), dars, reply_markup=re)


# مفاهیم پایه پرستاری
@bot.message_handler(
    func=lambda m: (
        text(m) == "مفاهیم پایه پرستاری"
        and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "mafahim_nurse")
)
def mafahim_nurse(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "mafahim_nurse"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر خواجه", "دکتر عباسی")
    re.row("آقای خطیبی", "آقای بخشی عرب")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر خواجه" and nusers_ids.get(user_id(m)) == "mafahim_nurse"
    )
)
def mafa_nurse_khaje(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "mafahim_nurse"
    nusers_ids[user_id(m)] = "mafa_nurse_khaje"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "mafa_nurse_khaje")
)
def power_mafa_nurse_khaje(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACApdlJwS3saIeAAGgLgyDqAoSAffEk1UAAjMTAAIjjDhRSY4_73OL35AwBA"
    )

    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAlllJpLiHeh0LJPV_h-1JpIW3reusgACoRIAAiOMOFHM2bzbYf8OFzAE"
    )

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "mafa_nurse_khaje")
)
def jozve_mafa_nurse_khaje(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAqFlKTfahFMmECUL7nBYX2_zKJjxlwAC5RIAA3tRUXtOcdAPqWSsMAQ"
    )



@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر عباسی" and nusers_ids.get(user_id(m)) == "mafahim_nurse"
    )
)
def mafa_nurse_abbasi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "mafahim_nurse"
    nusers_ids[user_id(m)] = "mafa_nurse_abbasi"
    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    # re.row("همه فایل ها")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


# @bot.message_handler(
#     func=lambda m: (text(m) == "همه فایل ها" and nusers_ids.get(user_id(m)) == "mafa_nurse_abbasi")
# )
# def hame_mafa_nurse_abbasi(m):
#     try:
#         ids_s[user_name(m)] += 1
#     except Exception:
#         pass
#     bot.send_message(chat_id(m), mess_warn, parse_mode= "MarkdownV2")
#     bot.send_document(
#         chat_id(m),
#         "BQACAgQAAx0Cbu8Z0gACAm5lJphFCuK5V48scCFv87sTVsa2BgACrRIAAiOMOFFN59AWQyjf6TAE"
#     )


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "mafa_nurse_abbasi")
)
def power_mafa_nurse_abbasi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAl5lJpUX1eIXeQhWx-vDUmdMu95HoAACpBIAAiOMOFECxgocF5PQDjAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmBlJpUuRwlQ1lMRvhLaOeCnT2NrNAACpRIAAiOMOFE5Z3jA2xsxmDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAqplLC8lnoYQDHhKwgzC2DBHINMpiwAC0REAAkAJYFE7Dv23yfN99TAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArJlNqIg7sJ_UkwLMjHjHi2GxfGAKAAC6RMAArZDsVEB1PazvFdVfTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArplPTmNd5iFyEgCkCONIlO-OZ6wpAAC3BAAAroE6VFMjdBKtMwC4jAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArxlPTsj27qz4ry6oWDM6ulebDhidQAC4BAAAroE6VF51mrEydA4aTAE"
    )

@bot.message_handler( 
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "mafa_nurse_abbasi")
)
def jozve_mafa_nurse_abbasi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)


@bot.message_handler(
    func=lambda m: (
        text(m) == "آقای خطیبی" and nusers_ids.get(user_id(m)) == "mafahim_nurse"
    )
)
def mafa_nurse_khatibi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "mafahim_nurse"
    nusers_ids[user_id(m)] = "mafa_nurse_khatibi"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)


@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "mafa_nurse_khatibi")
)
def power_mafa_nurse_khatibi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "mafa_nurse_khatibi")
)
def jozve_mafa_nurse_khatibi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAp9lKTdAfHCg8cJEAAF3bHA1vvp5QDcAAuMSAAN7UVEtVMzm0ShsUDAE"
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "آقای بخشی عرب" and nusers_ids.get(user_id(m)) == "mafahim_nurse"
    )
)
def mafa_nurse_bakhshi(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass

    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmJlJpY0Kpqr82CVNrL2bHCR5ptT1wACpxIAAiOMOFG4MqK9_K0-zTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmVlJpZnTFOhSeWpJR4kj2MTMxDLRAACqBIAAiOMOFFgSmbo7ReMUTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmdlJpZ8Id4aSEavHBHkE13YXTr8uQACqRIAAiOMOFFTUxu287FxmDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmllJpaL3NtLCcVTj1VPbWUIb1OPNQACqhIAAiOMOFHl0Q-NtcRvhDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAmtlJpaa3zUhJPu_gR6HPZmfahJT1gACqxIAAiOMOFHEWbJnaJJ-mjAE"
    )



# اخلاق پرستاری
@bot.message_handler(
    func=lambda m: (
        text(m) == "اخلاق پرستاری" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "akhlagh")
)
def akhlagh(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "akhlagh"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("آقای بازقلعه")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "آقای بازقلعه" and nusers_ids.get(user_id(m)) == "akhlagh"
    )
)
def akhlagh_bazgh(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAlVlJYlMCNFxuimMqiVp1NXy1vIwfgACsRAAAhedMVHo57_bfutvATAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAwdliZGKSsLArdAyZGtPyGwtOd8_twACYRMAAnXJUVAWpq5-gUUCyDME"
    )


# تغذیه
@bot.message_handler(
    func=lambda m: (
        text(m) == "تغذیه" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "taghzie")
)
def taghzie(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "taghzie"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر دلوریان‌زاده")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر دلوریان‌زاده" and nusers_ids.get(user_id(m)) == "taghzie"
    )
)
def taghzie_del(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "taghzie"
    nusers_ids[user_id(m)] = "taghzie_del"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("مخصوص پرینت")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == "مخصوص پرینت" and nusers_ids.get(user_id(m)) == "taghzie_del")
)
def hame_taghzie_del(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    # bot.send_message(chat_id(m), mess_warn, parse_mode= "MarkdownV2")
    # bot.send_document(
    #     chat_id(m),
    #     "BQACAgQAAx0Cbu8Z0gACAp1lJ67yArWqt5lv5AABu6qKk0YPKawAAksQAAIjjEBRJRtKscWeFmEwBA"
    # )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAr5lPmg6dvTk9I-iB1ks5Bpjju6gfAACFRAAAroE-VGFgLnJzFVv3DAE",
        caption="فایل pure شده و آماده پرینت"
    )

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "taghzie_del")
)
def power_taghzie_del(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAnNlJpk2Nqrl4HLiVjgWdLFb0W61UQACsBIAAiOMOFEBGiv_auYNDDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArRlNqM5qWiDj44VgFnLP_zEbGl8MgAC7xMAArZDsVHBkQsubu6O_zAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAsBlPnAhFBu4GymZHpQgKVEzO-yCwgACIBAAAroE-VEOFoWuN9CUiTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAtJlURPPR575wi9RHNatuIzQjEv7qAACvxEAArxmiFJiA5lBSuK_qjME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAtZlWmePC-E7N5nvSTxggdQXKct0uwAC3xAAAmSy0FLucTF1A55zbzME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvtliJkzAAHDaAud2CAXnmX5VjqNWr4AAk0WAAJ1yUlQlIQw6eFI0zYzBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAv1liJ4EbXhmC3V6es4qFJvzjeG8ZwACUBYAAnXJSVBvTdVf6C1sGzME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAv9liJ9iOTKKgZDr1iDERd_1KZ03ogACURYAAnXJSVAFA4L1b8SO1jME"
    )

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "taghzie_del")
)
def jozve_taghzie_del(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAqhlKTi4LDYfdcExwaUIXvdZGDIFzQAC6BIAA3tRUdd24eQrG5RZMAQ"
    )


# ژنتیک و ایمونولوژی
@bot.message_handler(
    func=lambda m: (
        text(m) == "ژنتیک و ایمونولوژی" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "zhenet")
)
def zhenet(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "zhenet"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر یوسفی")
    re.row("دکتر جعفری")
    re.row("آزمایشگاه")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == "آزمایشگاه" and nusers_ids.get(user_id(m)) == "zhenet")
)
def jozve_zhenet_jefer(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACApFlJq6IOfJNGwhlULrBgr1r-qTJjwACwxIAAiOMOFFLEi4C6XEBkjAE"
    )


@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر یوسفی" and nusers_ids.get(user_id(m)) == "zhenet"
    ) or
    (
        text(m) == "بازگشت" and users_ids.get(user_id(m)) == "zhenet_juseph"
    )
)
def zhenet_juseph(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "zhenet"
    nusers_ids[user_id(m)] = "zhenet_juseph"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    # re.row("همه فایل ها")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

# @bot.message_handler(
#     func=lambda m: (text(m) == "همه فایل ها" and nusers_ids.get(user_id(m)) == "zhenet_juseph")
# )
# def hame_zhenet_juseph(m):
#     try:
#         ids_s[user_name(m)] += 1
#     except Exception:
#         pass
#     bot.send_message(chat_id(m), mess_warn, parse_mode= "MarkdownV2")
#     bot.send_document(
#         chat_id(m),
#         "BQACAgQAAx0Cbu8Z0gACAnVlJptixk90bq-dYBdzKa7oO-a7TQACsRIAAiOMOFEHxra7raM5IDAE"
#     )

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "zhenet_juseph")
)
def power_zhenet_juseph(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAndlJp6CtGk85bW8yCbDM3pa8YhXWAACvBIAAiOMOFEWNry8Tw6UczAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAnllJp6oC9A2DWz14z-JFWQwkMqssAACvRIAAiOMOFGxyG-xx0fmdDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAq5lNp2JsCr5Xx_OYjy5XJhg6tzWIwAC2hMAArZDsVFjqVOLdtAKDDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArBlNp38ygXLNWSOn9T2AAGIrxqYAnMAAt0TAAK2Q7FRedRFkSelkHEwBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAsRlSO40c5Z7HS54b2C42e2UaPcEKgACzBQAAj88SVKn3sG13qk_WzME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAtRlUlSHp9bjtMwULMxRkGFvO6NylAACFA8AArxmmFKPQI0S60bztzME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAt9lXhikpAgIFfUImRUiC9TIeKWa1QACEBIAApvR8FIGeIZBToBwzjME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAuFlXhi6snMz-QWl0CBMRm4KjNAZtwACERIAApvR8FIhfhQ40E4GFDME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAulliH3TQWmrn71GhT-pUBfzx62dPgAC-BUAAnXJSVCi23qFKZhFtTME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAutliH3gaVqibY1YWYBYfZSG4tJA0gAC-hUAAnXJSVCkkFmlbxs6xDME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAu1liIE0BhiAbEdLoTcKSSxorOqsIgACBRYAAnXJSVCAjigu6pv78TME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAu9liIZ11MeKBMGAPiHiAQ8fmNEBNgACERYAAnXJSVBp690Mw_W0UTME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvFliIbjKXDK6qLzEc5zkzDdNGTZeAACEhYAAnXJSVDDrubMYVuBejME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvNliIiWX9qLIML1L5Jl5_-JTXHHZAACFBYAAnXJSVAHam2VyGnlXzME"
    )

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "zhenet_juseph")
)
def jozve_zhenet_juseph(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "zhenet_juseph"
    nusers_ids[user_id(m)] = "zhenet_juseph_jozve"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("جزوه نوع یک")
    re.row("جزوه نوع دو")
    re.row("بازگشت")

    bot.send_message(chat_id(m), "نوع جزوه رو انتخاب کن", reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == "جزوه نوع یک" and nusers_ids.get(user_id(m)) == "zhenet_juseph_jozve")
)
def jozve_one_zhenet_juseph(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(
        chat_id(m),
            """

                این جزوه *دست نویس* و *جدیده* و تطبیق بیشتری با تدریس استاد داره

            """,
        parse_mode= "MarkdownV2"
    )
    bot.send_message(
        chat_id(m),
        "به زودی..."
    )
    
@bot.message_handler(
    func=lambda m: (text(m) == "جزوه نوع دو" and nusers_ids.get(user_id(m)) == "zhenet_juseph_jozve")
)
def jozve_two_zhenet_juseph(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(
        chat_id(m),
            """
        
                این جزوات *تایپ شده* و *قدیمی* هستن و ممکنه نسبت به تدریس استاد مطالب بیشتری داشته باشن

            """,
        parse_mode= "MarkdownV2"
    )

    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAntlJqmFQMGrCN2PMQuLDa6zLFLqUAACJgcAAkOhSVDWvYKN4tB3hTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAn1lJqmpLlYlQ2HlxptW748P1KNUowACIwcAAkOhSVABqIlyd5JF-jAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAn9lJqnCRWPMoJfK2phizvQx2bROmgACJQcAAkOhSVCeHcX5avINsTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAoFlJqn2qjmc0htM75c11X5y7vMyowACJAcAAkOhSVCqJTcCp0RpFDAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAoNlJqoNqCe1IW8n2n5XtF7dmtO94QACtgcAAjc4MFBvhKR2gX0P-jAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAoVlJqoeuOVxpTx7pMkBh6apt4Xc3QACwAkAAgvZqFHwiqg_jF4Q9jAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAodlJqoyxxX6m27aAvhzu7qsovIAAc0AAsEJAAIL2ahRz_pskZDDV1cwBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAollJqpKP_DBGwEHujbkZdeJzzCmZwAC-gkAAjJJ6VGNPueuuqaFKTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAotlJqpax0Jh5ZayX_OzM7AfTjj33gACkwgAAocHIFII6xJ9OQnbkjAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAo1lJqpuFT3XkqJ001YNYwvF2XOCPgACcgwAAhvSuFEHLMFGa3NGDjAE"
    )




@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر جعفری" and nusers_ids.get(user_id(m)) == "zhenet"
    )
)
def zhenet_jefer(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "zhenet"
    nusers_ids[user_id(m)] = "zhenet_jefer"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "zhenet_jefer")
)
def power_zhenet_jefer(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAo9lJq20GSUqEiQhJ7CqyrlKbaxTWAACwRIAAiOMOFF0El_0LI5FjjAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvVliIldlA-T9MVhUkQEc2UL4NFcAwACGRYAAnXJSVD8sxTQ8L2PFDME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvdliImHF7K_zgdDhHdxqxZ7xa8rxwACGhYAAnXJSVCAVkv2NqTNZjME"
    )
    

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "zhenet_jefer")
)
def jozve_zhenet_jefer(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)


# فناوری اطلاعات در پرستاری
@bot.message_handler(
    func=lambda m: (
        text(m) == "فناوری اطلاعات در پرستاری" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "fanavar")
)
def fanavar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "fanavar"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر دلدار")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر دلدار" and nusers_ids.get(user_id(m)) == "fanavar"
    )
)
def fanavar_deldar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "fanavar"
    nusers_ids[user_id(m)] = "fanavar_deldar"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "fanavar_deldar")
)
def power_fanavar_deldar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "fanavar_deldar")
)
def jozve_fanavar_deldar(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)


# پرستاری سلامت جامعه
@bot.message_handler(
    func=lambda m: (
        text(m) == "پرستاری سلامت جامعه" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "salamtjame")
)
def salamtjame(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "salamtjame"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("خانم خیری")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "خانم خیری" and nusers_ids.get(user_id(m)) == "salamtjame"
    )
)
def salamtjame_kheyr(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "salamtjame"
    nusers_ids[user_id(m)] = "salamtjame_kheyr"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    # re.row("همه فایل ها")
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

# @bot.message_handler(
#     func=lambda m: (text(m) == "همه فایل ها" and nusers_ids.get(user_id(m)) == "salamtjame_kheyr")
# )
# def hame_salamtjame_kheyr(m):
#     try:
#         ids_s[user_name(m)] += 1
#     except Exception:
#         pass
#     bot.send_message(chat_id(m), mess_warn, parse_mode= "MarkdownV2")
#     bot.send_document(
#         chat_id(m),
#         "BQACAgQAAx0Cbu8Z0gACApNlJrMdNz2jGqSqB17P_SJkv7l5OAAC2BIAAiOMOFFWT-q8R85H7zAE"
#     )



@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "salamtjame_kheyr")
)
def power_salamtjame_kheyr(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACApVlJrU0yYd-6i42bpdDCAVJFvk_VwAC2xIAAiOMOFHxB6f1M2bfCjAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAqxlMQidtzo-B_R5JcfoJO39CP7yZQAC-Q8AAh4LiVEHoBhPhimhjTAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACArhlOmKuzPGBxFMf6tKHLlaEmaOQ4wACWRIAAnkP2VFaWaK42r02HjAE"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAsZlSnHAQ659Jy7NKrgoncyKsGMtDgACaBAAAj88UVLJQuP-4t6ZXzME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAshlSnK1nvY_cU8fEhKkc5EZL0XkvAACbRAAAj88UVJcC-GUbKXg4DME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAsplSnLzyzAS042troKvxUr78kKHgwACbhAAAj88UVLM10DdtT9i0TME"
    )
    bot.send_audio(
        chat_id(m),
        "CQACAgQAAx0Cbu8Z0gACAsxlSnQbSOMUaK7oW6LQpOLn6wABwr4AAnQQAAI_PFFSdOvDcJlDChMzBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAs5lSnRM45FJByUv0n2jh0BU9wU_ygACdhAAAj88UVKxqorBo3yDLzME"
    )
    bot.send_audio(
        chat_id(m),
        "CQACAgQAAx0Cbu8Z0gACAtBlSnUSx3G-EV4Fj-A7kavVvGjwoQACeBAAAj88UVIMVlxc1gzEQTME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAuNlXhkdzvVToUiHy6QmN1jrmAdGrgACExIAApvR8FJ6QWacAAE-7A8zBA"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAuVlXhmJMK1YjgLHfiLhoaM7Qx3uRQACBBIAArFx-FLHwr8YxOv2iTME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAudlXhnDn_FbZ88BBMP-L2dsOVJLCQACFRIAApvR8FKQF_tjL1EckTME"
    )
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAvlliJCwTHcHNkox6d76-QxJsmxAWwACNxYAAnXJSVDgfMCRvgIEtjME"
    )


@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "salamtjame_kheyr")
)
def jozve_salamtjame_kheyr(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)


# داروشناسی
@bot.message_handler(
    func=lambda m: (
        text(m) == "داروشناسی" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "medicine")
)
def medicine(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass

    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "medicine"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("دکتر بزرگی")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "دکتر بزرگی" and nusers_ids.get(user_id(m)) == "medicine"
    )
)
def medicine_boz(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass

    users_ids[user_id(m)] = "medicine"
    nusers_ids[user_id(m)] = "medicine_boz"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "medicine_boz")
)
def power_medicine_boz(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass

    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAwtlib4OrMOdWLtk6REeonWPItugPwACbQ8AAkXSSFCFefnNSZzZUDME"
    )

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "medicine_boz")
)
def jozve_medicine_mas(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass

    bot.send_message(chat_id(m), nothing)


# روانشناسی فردی و اجتماعی
@bot.message_handler(
    func=lambda m: (
        text(m) == "روانشناسی فردی و اجتماعی" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "ravanfard")
)
def ravanfard(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "ravanfard"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("خانم گرزین")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "خانم گرزین" and nusers_ids.get(user_id(m)) == "ravanfard"
    )
)
def ravanfard_gorz(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "ravanfard"
    nusers_ids[user_id(m)] = "ravanfard_gorz"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row(power)
    re.row(jozve)
    re.row("بازگشت")

    bot.send_message(chat_id(m), mess_choose_power, reply_markup=re)

@bot.message_handler(
    func=lambda m: (text(m) == power and nusers_ids.get(user_id(m)) == "ravanfard_gorz")
)
def power_ravanfard_gorz(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_document(
        chat_id(m),
        "BQACAgQAAx0Cbu8Z0gACAwlliZJeSRWyhqVSvCm5d4LrkX8P_QACYxMAAnXJUVDzSdLZS4UxizME"
    )

@bot.message_handler(
    func=lambda m: (text(m) == jozve and nusers_ids.get(user_id(m)) == "ravanfard_gorz")
)
def jozve_ravanfard_gorz(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)


# زبان عمومی
@bot.message_handler(
    func=lambda m: (
        text(m) == "زبان عمومی" and nusers_ids.get(user_id(m)) == "term2"
    )
    or (text(m) == "بازگشت" and users_ids.get(user_id(m)) == "zabanomoo")
)
def zabanomoo(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    users_ids[user_id(m)] = "dars_term2"
    nusers_ids[user_id(m)] = "zabanomoo"

    re = types.ReplyKeyboardMarkup(resize_keyboard=True)
    re.row("خانم مهدویان")
    re.row("بازگشت")

    bot.send_message(chat_id(m), ostad, reply_markup=re)

@bot.message_handler(
    func=lambda m: (
        text(m) == "خانم مهدویان" and nusers_ids.get(user_id(m)) == "zabanomoo"
    )
)
def zabanomoo_mahdav(m):
    try:
        ids_s[user_name(m)] += 1
    except Exception:
        pass
    bot.send_message(chat_id(m), nothing)















bot.infinity_polling()
