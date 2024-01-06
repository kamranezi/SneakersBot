# import firebase_admin
# from firebase_admin import credentials, db
#
# # Загрузите файл конфигурации Firebase Admin SDK
# cred = credentials.Certificate('home-b114b-firebase-adminsdk-hp712-dc89fd3e8e.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://home-b114b-default-rtdb.europe-west1.firebasedatabase.app/'
# })
#
# # Получите ссылку на базу данных
# ref = db.reference()
#
# # Пример записи данных в базу данных
#
# data_to_add={
#     '5': {
#         'id': '5',
#         'category': "Men's Sportswear",
#         'title': 'X_PLRBOOST Shoes',
#         'main': 'https://assets.adidas.com/images/w_383,h_383,f_auto,q_auto,fl_lossy,c_fill,g_auto/fba27d9497e44d9dbf7889f33a21fba9_9366/x_plrboost-shoes.jpg',
#         'description': 'City life and versatility are quite the pair, and these adidas shoes give them both a starring role. Inspired by designs built for an active lifestyle, they offer a modern take on best-in-class comfort and style. The neoprene collar and mesh upper are key for breathability, while the BOOST midsole meets your every step with energy and support. It all comes together on a rubber outsole that gives you traction whenever you need it.\nMade with a series of recycled materials, this upper features at least 50% recycled content. This product represents just one of our solutions to help end plastic waste.',
#         'price': '$64',
#         'image_urls': [
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/e2fb982485d54637bf9f9691aa8997dc_9366/X_PLRBOOST_Shoes_Black_IF2921_01_standard.jpg',
#             'https://videos.adidas.com/videos/w_600,f_auto,q_auto/6055bcfa39d2438181ce4cb8ba80e55b_d98c/X_PLRBOOST_Shoes_Black_IF2921_video.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/9639e76423894ecd961cd0d1cb6be802_9366/X_PLRBOOST_Shoes_Black_IF2921_02_standard_hover.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/31954c9cb1dc4715a92fdda4342d9c4c_9366/X_PLRBOOST_Shoes_Black_IF2921_03_standard.jpg'
#              ],
#         'sizes': {'US': [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5],
#                   'EU': [40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5]},
#         'available': False
#     },
#     '6': {
#         'id': '6',
#         'category': "Men's Sportswear",
#         'title': 'X_PLRBOOST Shoes',
#         'main': 'https://assets.adidas.com/images/w_383,h_383,f_auto,q_auto,fl_lossy,c_fill,g_auto/36377fa931a14b0b988caf9c0164f6ea_9366/x_plrboost-shoes.jpg',
#         'description': 'Up the style. Up the energy. These BOOST sneakers are responsive and stylish. The soft upper is lined for comfort. It sits atop a BOOST midsole that gives you ultimate comfort with each step. Made with a series of recycled materials, this upper features at least 50% recycled content. This product represents just one of our solutions to help end plastic waste.',
#         'price': '$64',
#         'image_urls': [
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/5890b3c785bb4f5bb347af9c016491eb_9366/X_PLRBOOST_Shoes_White_ID9436_01_standard.jpg',
#             'https://videos.adidas.com/videos/w_600,f_auto,q_auto/018637b249914247bea9afb600c5c952_d98c/X_PLRBOOST_Shoes_White_ID9436_video.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/92b49cc2643b4d1b8350af9c0164a92e_9366/X_PLRBOOST_Shoes_White_ID9436_02_standard_hover.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/575e79b3f8ce408da25aaf9c0164b1d5_9366/X_PLRBOOST_Shoes_White_ID9436_03_standard.jpg'
#              ],
#         'sizes': {'US': [7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5],
#                   'EU': [40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5]},
#         'available': False
#     },
#     '7': {
#         'id': '7',
#         'category': 'Originals',
#         'title': 'Gazelle Indoor Shoes',
#         'main': 'https://assets.adidas.com/images/w_383,h_383,f_auto,q_auto,fl_lossy,c_fill,g_auto/0edaed2c73a5419c84d6a036db695aad_9366/gazelle-indoor-shoes.jpg',
#         'description': 'Shake up the iconic adidas Gazelle shoes with some playful colors. Originally released as an indoor soccer trainer, this stylish silhouette has gone on to shine in the fashion world. This pair shows off bold colors offset by the white laces, eyestay, tongue and lining.',
#         'price': '$90',
#         'image_urls': [
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/0643354eec9945edb92c800a064146ab_9366/Gazelle_Indoor_Shoes_Burgundy_IG4996_01_standard.jpg',
#             'https://videos.adidas.com/videos/w_600,f_auto,q_auto/e6e7cc15458f403a8d051e083073f148_d98c/Gazelle_Indoor_Shoes_Burgundy_IG4996_video.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/5b447865fa5c44e48c2a5ed371cf7846_9366/Gazelle_Indoor_Shoes_Burgundy_IG4996_010_hover_standard.jpg',
#             'https://assets.adidas.com/images/w_600,f_auto,q_auto/f87604ebde1b4d6d9247350ed412f968_9366/Gazelle_Indoor_Shoes_Burgundy_IG4996_02_standard.jpg'
#         ],
#         'sizes': {'US': [9.5], 'EU': [42.5]},
#         'available': True
#
#     }
# }
# # Записываем данные в базу данных Firebase
# ref.update(data_to_add)