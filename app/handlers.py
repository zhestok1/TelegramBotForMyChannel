from config import client
from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatType


router = Router()

@router.message(F.sticker, F.chat.type.in_({ChatType.SUPERGROUP, ChatType.GROUP, ChatType.PRIVATE}))
async def i_dont_like_sticker(message: Message):
    # Логируем получение стикера
   
    try:
        # Показываем, что бот печатает
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
        
        # Отправляем пользователю сообщение об ошибке
        await message.reply(
            "Извини, мой ИИ-мозг временно перегрелся от такого стикера!\n"
            "Попробуй ещё раз или отправь что-то более осмысленное."
        )