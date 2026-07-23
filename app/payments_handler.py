from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, SuccessfulPayment
import app.keyboard as kb
import logging

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command("test"))
async def test_command(message: Message):
    await message.answer("✅ /test работает! Если ты это видишь — бот работает.")

@router.message(Command('donate'))
async def send_donation_menu(message: Message):
    logger.info("🔴🔴🔴 /donate СРАБОТАЛ!")
    
    if message.from_user.is_bot:
        return
    
    if message.sender_chat and message.sender_chat.type == "channel":
        return
    
    await message.answer(
        "Поддержать проект\n\n"
        "Выберите способ оплаты:",
        reply_markup=kb.main_keyboard
    )

# ПОЖЕРТВОВАНИЕ ЧЕРЕЗ ЗВЕЗДЫ
@router.callback_query(F.data == 'donate_stars')
async def donate_stars(callback : CallbackQuery):
    await callback.answer()
    
    await callback.message.edit_text(
        "⭐ Оплата звёздами\n\n"
        "Выберите сумму доната:",
        reply_markup=kb.stars_keyboard,
    )
            
    
# КНОПКА НАЗАД
@router.callback_query(F.data == 'donate_back')
async def donate_back(callback: CallbackQuery):
    
    await callback.answer()
    
    await callback.message.edit_text(
        "Поддержать проект\n\n"
        "Выберите способ оплаты:",
        reply_markup=kb.main_keyboard
    )

# ОБРАБОТКА ПОДДЕРЖКИ В ЗВЕЗДАХ
@router.callback_query(F.data.startswith("stars_"))
async def process_stars_amount(callback: CallbackQuery):
    
    await callback.answer()
    
    amount = int(callback.data.split("_")[1])
    
    prices = [LabeledPrice(label="Поддержка проекта", amount=amount)]
    
    await callback.message.bot.send_invoice(
        chat_id=callback.message.chat.id,
        title="Поддержка создателя",
        description=f"Сумма: {amount} ⭐️",
        payload=f"donation_stars_{amount}",
        provider_token="",  # Для Stars оставляем пустым
        currency="XTR",
        prices=prices,
        start_parameter="donation_stars"
    )

@router.pre_checkout_query()
async def on_pre_checkout_query(query: PreCheckoutQuery):
    await query.answer(ok=True)
    
@router.message(F.successful_payment)
async def on_successful_payment(message: Message):
    
    payment: SuccessfulPayment = message.successful_payment
    user = message.from_user
    
    if payment.currency == "XTR":
        amount_text = f"{payment.total_amount} ⭐️"
    
    await message.answer(
        f"🌟 Спасибо за донат в размере {amount_text}!\n"
        "Ваша поддержка помогает проекту развиваться!"
    )
    


