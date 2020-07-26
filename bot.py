import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TELEGRAM_API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)


# Constants
MARKUP_REQUESTS = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('Мотивация'))\
    .add(KeyboardButton('Эрдеш'))\
    .add(KeyboardButton('Кастрация'))
QUOTES = {
    "Мотивация": [
        "Если Вы хотите добиться успеха, избегайте 6-ти пороков: сонливости, лени, страха, гнева, праздности и "
        "нерешительности.\n\nДжеки Чан",
        "Если ты простил человеку все, значит с ним покончено.",
        "Человек, который радуется счастью других людей, всегда будет счастлив сам.\n\nГеше Джампа Тинлей",
        "Не ждите, что станет легче, проще, лучше. Не станет. Трудности будут всегда. Учитесь быть счастливыми "
        "прямо сейчас. Иначе не успеете. ",
        "Возможно все. На невозможное просто требуется больше времени.",
        "В течение 72 часов после принятия решения вы должны сделать первый шаг к его реализации. Если вы этого не "
        "сделали. то тогда девяносто шансов из ста, что вы так никогда и не начнете.\n\nБодо Шефер",
    ],
    "Эрдеш": [
        "В нашей судьбе пессимистично только одно: человек живёт недолго и надолго умирает.",
        "У меня всего лишь два недостатка.. Плохая память и ещё что то!",
        "Признав реальность - не пытайся ее оправдать...",
        "Красота спасет Мир, если она добра. Но добра ли она? Не красота спасет Мир, а светлые помыслы. Ибо какой "
        "прок от надменной и безбожной красоты? ",
        "Слабый всегда уступает дорогу сильному и только самый сильный уступает дорогу всем.",
        "Желая стать свободным, нужно ли освободиться и от этого желания?"
    ],
    "Кастрация": [
        "Девушка в автобусе держит на коленях котёнка и нежно его гладит.\nСидящий напротив мужчина говорит с "
        "намёком: — Хотел бы я оказаться на месте вашего котёнка!\n— Ну это вряд ли: я везу его к ветеринару на "
        "кастрацию. ",
        "Вот такая, мой милый друг, ситуация…\nИзменишь — ждет тебя кастрация!)))",
        "Манипуляция — чужих мозгов частичная кастрация!"
    ]
}


@dp.message_handler(commands='start')
async def send_start(message: types.Message):
    await message.reply("Hi!!!!", reply_markup=MARKUP_REQUESTS)


@dp.callback_query_handler(text='Мотивация')
@dp.callback_query_handler(text='Эрдеш')
@dp.callback_query_handler(text='Кастрация')
async def send_quote(query: types.CallbackQuery):
    answer_data = query.data
    logger.info(answer_data)
    text = QUOTES[answer_data][0]
    await bot.send_message(query.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
