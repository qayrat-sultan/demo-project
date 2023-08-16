from aiogram import types, Dispatcher
from tgbot.db.queries import Database


async def bot_echo_all(message: types.Message, db: Database):
    if message.content_type == "text":
        _resp, status = await db.send_token_to_server(message.from_user.id, message.text)
        if status not in [200, 201]:
            await message.answer("Ошибка сервера, попробуйте позже")
        else:
            await message.answer("Успешно соединен с сервером")
    else:
        await message.answer("Отправьте только токен, другие типы данных не поддерживаются")


# state_name = await state.get_state()
# text = [
#     f'Эхо в состоянии {hcode(state_name)}',
#     'Содержание сообщения:',
#     hcode(message.text)
# ]
# await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
