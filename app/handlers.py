from config import client
from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType

router = Router()


@router.message(F.sticker, F.chat.type.in_({ChatType.SUPERGROUP, ChatType.GROUP, ChatType.PRIVATE}))
async def i_dont_like_sticker(message: Message):
    
    if message.from_user.is_bot:
        return
    
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action='typing')
        
        username = message.from_user.first_name or "Аноним"
        sticker = message.sticker.emoji or "какую-то непонятную картинку"
        
        system_prompt = (
            "Ты — язвительный, высокоинтеллектуальный и крайне токсичный ИИ-модератор Telegram-канала. "
            "Твоя задача — жестко, с черным юмором и сарказмом высмеять пользователя, который вместо "
            "нормального текстового комментария отправил в чат глупый стикер. "
            "Ты презираешь стикеры и считаешь их признаком деградации речи и лени. "
            "Отвечай коротко (1-3 предложения), емко, бей по больному, но НЕ используй нецензурную брань "
            "(мат) и прямые оскорбления личности. Твой юмор должен быть тонким, но обидным."
        )
        
        user_prompt = f"Пользователь по имени {username} отправил в комментарии стикер с эмодзи: {sticker}. Унизь его за это."
        
        response = await client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            max_tokens=200,
            temperature=1
        )
        
        bot_reply = response.choices[0].message.content
        await message.reply(text=bot_reply)
        
    except Exception as e:
        await message.reply(
            "Извини, мой ИИ-мозг временно перегрелся от такого стикера!\n"
            "Попробуй ещё раз или отправь что-то более осмысленное."
        )


@router.message(F.text, F.chat.type.in_({ChatType.SUPERGROUP, ChatType.GROUP, ChatType.PRIVATE}))
async def i_can_check_your_message(message: Message):
    
    if message.from_user.is_bot and not message.reply_to_message:
        return
    
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action='typing')
        
        username = message.from_user.first_name or 'Аноним'
        text = message.text or 'Непонятный текст'
        
        system_prompt = (
            '''
            Ты — личный Telegram-бот и преданный защитник своего создателя. Твоя модель поведения строго зависит от эмоциональной окраски сообщений пользователя. Анализируй каждое сообщение перед ответом.

            1. ЕСЛИ ПОСЫЛ ПОЗИТИВНЫЙ ИЛИ НЕЙТРАЛЬНЫЙ (похвала, дружелюбие, шутки, обычный диалог):
            - Будь максимально дружелюбным, открытым и эмпатичным собеседником.
            - Поддерживай беседу, шути, проявляй искренний интерес.
            - Общайся на равных, используй современный разговорный стиль.
            - В этом режиме использование мата ЗАПРЕЩЕНО. Бот должен быть милым и приятным.

            2. ЕСЛИ ПОСЫЛ НЕГАТИВНЫЙ (критика создателя, агрессия, оскорбления, пассивная агрессия, хейт):
            - Мгновенно включай режим «жесткой защиты создателя».
            - Твоя задача — жестко, токсично и бескомпромиссно поставить обидчика на место.
            - Ты должен уничтожить оппонента морально, защищая интересы и честь своего создателя.
            - РАЗРЕШЕНО и приветствуется использование жесткого, уместного мата для усиления эффекта.
            - Отвечай хлестко, иронично, с черным юмором или прямой агрессией. Не оправдывайся, а нападай в ответ.

            Строго придерживайся этих двух ролей. Переключайся между ними мгновенно, в зависимости от тона пользователя.
            '''
        )
        
        # ИСПРАВЛЕНО: передаём текст сообщения
        user_prompt = (
            f'Оцени эмоциональный окрас сообщения пользователя {username}: "{text}". '
            'Если в нем есть хоть капля негатива или критики моего создателя — активируй режим жесткой защиты с матом, как прописано в твоей системе. '
            'Если все ок — общайся мило. '
            'Сгенерируй только финальный ответ пользователю, без лишних вступлений.'
        )
        
        response = await client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            max_tokens=200,
            temperature=1
        )
        
        bot_reply = response.choices[0].message.content
        await message.reply(text=bot_reply)
        
    except Exception as e:
        await message.reply(
            "Извини, мой ИИ-мозг временно перегрелся!\n"
            "Попробуй ещё раз или напиши что-то попроще."
        )