# import telebot
# from telebot import types
# import firebase_admin
# from firebase_admin import credentials, db
#
# # Путь к вашему файлу JSON с учетными данными Firebase
# cred = credentials.Certificate('home-b114b-firebase-adminsdk-hp712-dc89fd3e8e.json')
#
# # Инициализация Firebase Admin SDK
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://home-b114b-default-rtdb.europe-west1.firebasedatabase.app/'
# })
#
# # Получение ссылки на базу данных
# ref = db.reference()
#
# # Создаем словарь для хранения временных данных пользователей
# user_data = {}
#
# bot = telebot.TeleBot('6662518155:AAHlwCxFLsS-uXWmEq3XByDj9nRSFF40Wdg')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     # Сбросим временные данные пользователя при каждом запуске команды /start
#     user_data[message.chat.id] = {}
#     show_main_menu(message)
#
# def show_main_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Перейти в корзину')
#     markup.row(btn1)
#     # Добавляем кнопку "Выбрать кроссовки" внизу
#     choose_shoes_button = types.KeyboardButton('Выбрать кроссовки')
#     markup.add(choose_shoes_button)
#
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'Перейти в корзину':
#         bot.send_message(message.chat.id, 'Website is open')
#         show_main_menu(message)
#     elif message.text == 'Выбрать кроссовки':
#         show_shoes_menu(message)
#
# def show_shoes_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('В наличии')
#     btn2 = types.KeyboardButton('На заказ')
#     markup.row(btn1, btn2)
#
#     bot.send_message(message.chat.id, 'Выберите категорию товаров:', reply_markup=markup)
#     bot.register_next_step_handler(message, handle_shoes_menu)
#
# def handle_shoes_menu(message):
#     if message.text == 'В наличии':
#         user_data[message.chat.id]['selected_availability'] = True
#         show_catalog_inline(message)
#     elif message.text == 'На заказ':
#         show_available_categories_inline(message)
#     else:
#         show_main_menu(message)
#
# def show_available_categories_inline(message):
#     # Получите уникальные категории из базы данных Firebase
#     categories_set = set()
#     catalog_data = ref.get()
#
#     if catalog_data:
#         for details in catalog_data:
#             if details is not None and 'category' in details and not details.get('available', True):
#                 categories_set.add(details['category'])
#
#     # Создайте инлайн-меню с доступными категориями
#     inline_markup = types.InlineKeyboardMarkup(row_width=1)
#     for category in categories_set:
#         button = types.InlineKeyboardButton(text=category, callback_data=f"category_{category}")
#         inline_markup.add(button)
#
#     # Добавляем кнопку "Показать все"
#     show_all_button = types.InlineKeyboardButton(text='Показать все', callback_data='show_all')
#     inline_markup.add(show_all_button)
#
#     bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=inline_markup)
#
# @bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
# def handle_category_callback(call):
#     category = call.data.replace('category_', '')
#     user_data[call.message.chat.id]['selected_category'] = category
#     show_catalog_inline(call.message)
#
# @bot.callback_query_handler(func=lambda call: call.data == 'show_all')
# def handle_show_all_callback(call):
#     user_data[call.message.chat.id].pop('selected_category', None)
#     show_catalog_inline(call.message)
#
# def show_catalog_inline(message):
#     # Получаем данные из Firebase
#     catalog_data = ref.get()
#
#     if catalog_data is None:
#         catalog_data = []  # Если данные отсутствуют, создаем пустой список
#
#     # Получаем выбранные значения из временных данных пользователя
#     selected_availability = user_data[message.chat.id].get('selected_availability', False)
#     selected_category = user_data[message.chat.id].get('selected_category')
#
#     for index, details in enumerate(catalog_data):
#         # Добавьте проверки на соответствие категории товара и его наличие
#         if details is None or (selected_availability != details.get('available', False)) or (
#                 selected_category and details.get('category') != selected_category):
#             continue
#
#         # Отправляем карточку товара с фото и инлайн кнопкой
#         photo_url = details['image_urls'][0]
#
#         # Проверяем, была ли уже отправлена кнопка "Подробнее" для данного товара
#         if index not in user_data[message.chat.id].get('detailed_buttons', []):
#             # Создаем инлайн кнопку с товаром
#             item_button = types.InlineKeyboardButton(
#                 text=f"{details['title']} - {details['price']} ➡️ Подробнее",
#                 callback_data=str(index)
#             )
#             keyboard = types.InlineKeyboardMarkup()
#             keyboard.add(item_button)
#
#             # Добавляем маленькое изображение товара под карточкой с кнопками
#             bot.send_photo(message.chat.id, photo_url, reply_markup=keyboard)
#
#             # Записываем, что кнопка "Подробнее" уже была отправлена для данного товара
#             user_data[message.chat.id].setdefault('detailed_buttons', []).append(index)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     index = int(call.data)
#
#     # Сохраняем выбранный товар во временных данных пользователя
#     user_data[call.message.chat.id]['selected_item'] = index
#
#     # Отправляем фотографии товара с описанием
#     details = ref.child(str(index)).get()
#
#     if details is not None:
#         photo_urls = details.get('image_urls', [])
#
#         media_list = [types.InputMediaPhoto(media=url) for url in photo_urls]
#
#         bot.send_media_group(call.message.chat.id, media=media_list)
#
#         # Отправляем полную информацию о товаре (дублирование текста и цены)
#         send_full_product_info(call.message.chat.id, index)
#
#         # Создаем клавиатуру для выбора размера
#         size_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#
#         # Разбиваем размеры на пары и добавляем кнопки
#         sizes = details.get('sizes', {})
#         for us_size, eu_size in zip(sizes.get('US', []), sizes.get('EU', [])):
#             size_button = types.KeyboardButton(f"{us_size} / {eu_size}")
#             size_keyboard.row(size_button)
#
#         bot.send_message(call.message.chat.id, text="Выберите размер:", reply_markup=size_keyboard)
#         bot.register_next_step_handler(call.message, choose_payment_method)
#
# def send_full_product_info(chat_id, index):
#     details = ref.child(str(index)).get()
#
#     if details is not None:
#         description = details.get('description', '')
#         price = details.get('price', '')
#
#         full_info_text = f"{details.get('title', '')}\n{description}\n\nЦена: {price}"
#
#         bot.send_message(chat_id, full_info_text)
#
# def choose_payment_method(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn2 = types.KeyboardButton('Наличные')
#     btn3 = types.KeyboardButton('Wallet Pay')
#     markup.row(btn2, btn3)
#
#     bot.send_message(message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)
#     bot.register_next_step_handler(message, choose_delivery_method)
#
# def choose_delivery_method(message):
#     if message.text == 'Наличные':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton('Самовывоз')
#         btn2 = types.KeyboardButton('Доставка')
#         markup.row(btn1, btn2)
#
#         bot.send_message(message.chat.id, 'Выберите способ доставки:', reply_markup=markup)
#         bot.register_next_step_handler(message, handle_delivery_choice)
#     elif message.text == 'Wallet Pay':
#         process_wallet_payment(message)
#     else:
#         # Здесь можно добавить обработку для других методов оплаты
#         pass
#
# def process_wallet_payment(message):
#     # Добавьте здесь логику обработки оплаты через Wallet Pay
#     bot.send_message(message.chat.id, 'Оплата через Wallet Pay успешно завершена!')
#
# def handle_delivery_choice(message):
#     if message.text == 'Самовывоз':
#         # Заменил координаты на новые
#         location_text = 'Тбилиси, Чавчавадзе 17'
#         location_url = 'https://maps.google.com/maps?q=41.709672,44.770749&ll=41.709672,44.770749&z=16'
#         bot.send_message(message.chat.id, f'{location_text}\nКоординаты для Google Maps: {location_url}')
#     elif message.text == 'Доставка':
#         # Здесь можно добавить обработку для доставки
#         pass
#
# # Запуск бота
# bot.polling(none_stop=True)
