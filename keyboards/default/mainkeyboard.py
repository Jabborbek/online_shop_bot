from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

mainkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Buyurtma berish")
        ],
        [
            KeyboardButton(text='📦 Buyurtmalarim'),
            KeyboardButton(text='⚙️Sozlamalar'),
        ],
        [
            KeyboardButton(text="ℹ️Biz haqimizda"),
            KeyboardButton(text="✍️Fikr qoldirish"),
        ]
    ],
    resize_keyboard=True
)