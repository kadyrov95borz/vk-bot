# -*- coding: utf-8 -*-
import os
import bot as vk_bot
# Чтобы получить токен, нужно перейти по ссылке https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 нажать "разрешить" и скопировать в адресной строке все, что идёт после access_token= до &
bot = vk_bot.Bot("2e370e62fe8e8f84398c418e410aa27d2f1a4fda471854e33bd117397183dfbb14b2850969c4b287633bc", anticaptcha_key = "")
with open(__file__[:-7] + "templates.txt", "r", encoding="utf-8") as file:
	bot.set_template_list(file.read().split("\n"))
bot.conversation_photos = os.listdir(__file__[:-7] + "photos")
bot.set_attachment_list(["wall531170160_4", "photo530941218_457262715"]) # Список вложений. Сюда нужно добавлять идентификаторы вложений. Чтобы получить идентификатор вложения, нужно скопировать ссылку на него (пример: https://vk.com/photo530941218_457262715) и убрать https://vk.com/
bot.set_voice_message_list(["doc599521094_554607859 {sticker_ids: [20012, 21148]} {delay: 10}", "doc599521094_554607973"]) # Список голосовых сообщений. Сюда нужно добавлять идентификатооы голосовых сообщений. О том, как их получить можно прочитать в файле README.txt (пункт 3.1)
bot.set_response_chance_in_chats(100) # Шанс ответа на сообщение в беседе
bot.set_response_chance_in_private_messages(100) # Шанс ответа на личное сообщение
bot.set_attachment_response_chance(0) # Шанс того, что в случае ответа бот отправит вложение (фотографию, аудиофайл, видеофайл)
bot.set_voice_message_response_chance(0) # Шанс того, что бот в случае ответа отправит голосовое сообщение
bot.sticker_sending_chance = 0 # Шанс отправки стикера
bot.text_message_delay = 5 # Задержка при отправке текстового сообщения
bot.attachment_message_delay = 5 # Задержка при отправке сообщения с вложением
bot.audio_message_delay = 5 # Задержка при отправке голосового сообщения
bot.set_sticker_sending_delay(0.5) # Задержка перед отправкой стикера
bot.set_ignore_list([210055087, 586570854, 465292380, 549742518, 576355200, 530941218]) # Список id пользователей, на чьи сообщения бот отвечать не будет
bot.set_ignore_chat_list([64, 81, 92]) # Список id бесед, в которые бот не будет отправлять сообщения
bot.set_ignore_message_list(["vto.pe", "vkbot.ru"]) # При наличии в сообщении любого слова из этого списка бот не будет на него отвечать (сюда нужно добавить ссылки, за отправку которых можно получить бан)
bot.conversation_titles = ["Название 1", "Название 2"] # Названия для бесед
bot.sticker_ids = [60, 19657] # id стикеров
bot.msg_show()
bot.wrappers = ["{name}, {template}", "Ауе, {template}"] # Обёртки для шаблонов
bot.join_chat_by_link_in_private_messages = True # True: бот будет заходить в беседы по ссылкам, которые ему отправляют в личных сообщениях, False: бот будет игнорировать ссылки, которые ему отправляют в личных сообщениях
bot.join_chat_by_link_in_chats = True # True: бот будет заходить в беседы по ссылкам, которые ему отправляют в других беседах, False: бот будет игнорировать ссылки, которые ему отправляют в беседах
bot.messages_forwarding = True # True: в случае ответа бот будет пересылать сообщение пользователя, на которое он отвечает, False: бот не будет пересылать сообщения
bot.messages_forwarding_when_sticker_sent = False # True: в случае отправки стикера бот будет пересылать сообщение пользователя, на которое он отвечает, False: бот не будет пересылать сообщения, когда отправляет стикер
bot.attachment_with_message = False # True: в случае отправки ботом вложения оно будет добавленно к текстовому сообщению, Flase: бот отправит только вложение
bot.message_pinning = False # True: бот будет закреплять свои сообщения при возможности
bot.conversation_title_changing = False # True: бот будет менять названия бесед
bot.conversation_photo_changing = False # True: бот будет менять фотографии бесед
bot.wrapping = False # True: при отправке сообщения шаблон будет добавлен к одной из обёртке
if __name__ == "__main__":
	bot.run()
