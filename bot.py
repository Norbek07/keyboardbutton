import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F #new
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboardbutton import main_button,computer_button,computers,computers_info, phones_info, phone_button, phones

TOKEN = "7083075969:AAGXj8oUQ_PVxwONVZ47chbiA4xlg-bYtgE"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Kompyuter va telefonlar botiga hush kelibsiz"
    await message.answer(text,reply_markup=main_button)


@dp.message(F.text=="💁🏻‍♂️ About us")
async def about_as_handler(message:Message):
    about = "      🎉 Welcom       \nWe are The Best Company. Mr Norbek"
    photo_link = "https://picjumbo.com/wp-content/uploads/entrepreneur-working-in-the-office-2210x1473.jpg"
    await message.answer_photo(photo=photo_link,caption=about)

@dp.message(F.text=="☎️ Contact admin")
async def about_as_handler(message:Message):
    about = "Admin info: \nTel: +998 (99)0113618 \nAdmin: https://t.me/Norbek_111" 
    await message.answer(text= about)

@dp.message(F.text == "📍 Location")
async def company_location(message:Message):
    lat = 40.102296
    long = 65.37345
    await message.answer("📍Norbek company location ")
    await message.reply_location(latitude=lat,longitude=long)


@dp.message(F.text=="💻 Computers")
async def my_computers(message:Message):
    await message.answer("Our computers",reply_markup=computer_button)

@dp.message(F.text.func(lambda computer:computer in computers))
async def computer_info(message:Message):
    info = computers_info.get(message.text)

    photo = info.get("photo")
    price = info.get("price")
    color = info.get("color")

    text = f"{message.text}\nprice: {price}$ \ncolor:{color} and ..."

    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="📱 Phones")
async def my_computers(message:Message):
    await message.answer("Our computers",reply_markup=phone_button)

@dp.message(F.text.func(lambda phone:phone in phones))
async def computer_info(message:Message):
    info = phones_info.get(message.text)

    photo = info.get("photo")
    price = info.get("price")
    color = info.get("color")

    text = f"{message.text}\nprice: {price}$\ncolor:{color} and ..."

    await message.answer_photo(photo=photo,caption=text)


@dp.message(F.text=="🔙 ortga")
async def computer_func(message:Message):
    text = "Asosiy menu"
    await message.answer(text=text, reply_markup=main_button)

@dp.startup()
async def bot_start():
    await bot.send_message(1245143580, "Botimiz ishga tushdi !")

@dp.shutdown()
async def bot_start():
    await bot.send_message(1245143580, "Bot to'xtadi !")
        
# @dp.message(F.location)
# async def get_location(message:Message):
#     lat = message.location.latitude
#     long = message.location.longitude
#     text = f"latitude:<code>{lat}</code>\n"
#     text += f"longitude:<code>{long}</code>"
#     await message.answer(text)

async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())