from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(
              text='Звёздами',
              callback_data='donate_stars',
          )
        ]
    ]
)

stars_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10 ⭐️", callback_data="stars_10"),
            InlineKeyboardButton(text="25 ⭐️", callback_data="stars_25")
        ],
        [
            InlineKeyboardButton(text="50 ⭐️", callback_data="stars_50"),
            InlineKeyboardButton(text="75 ⭐️", callback_data="stars_75")
        ],
        [
            InlineKeyboardButton(text="100 ⭐️", callback_data="stars_100"),
            InlineKeyboardButton(text="200 ⭐️", callback_data="stars_200"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="donate_back")
        ]
    ]
)


