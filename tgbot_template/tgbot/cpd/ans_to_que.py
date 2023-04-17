from aiogram import types, Dispatcher

#ID чатов цпд, в которых пишут ответ
# cpd = [742287623, 1541621229]
cpd = [482131625]

async def asdsad(message: types.Message):
    if message.from_user.id in cpd:
        '''
        Попытка сделать reply ответ

        mess = types.Message()
        chat: types.Chat = message.chat
        
        s = message.text[::-1]
        k = -1
        for i in range(len(s)):
            if i == '/':
                if k == -1:
                    chat.id = int(s[:i-1][::-1])
                    k = i + 1
                else:
                    mess.message_id = int(s[k:i-1][::-1])

        mess.chat = chat

        await mess.reply(message.text)
        
        '''
        chat_id = 0
        s = message.reply_to_message.text[::-1]
        for i in range(len(s)):
            if s[i] == '/':
                chat_id = int((s[:i])[::-1])
                break
        await message.bot.send_message(chat_id, "Ответ от сотрудника ЦПД:\n" + message.text)

        await message.reply("Ответ доставлен")

        
        

async def chat_id(mes: types.Message):
    await mes.answer(str(mes.chat.id))



def register_acc(dp: Dispatcher):
    
    dp.register_message_handler(chat_id, commands= "send_my_chatid")
    # dp.register_message_handler(asdsad)