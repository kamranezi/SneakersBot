# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
#
# # Ваш новый список ID
# ids = [
#     "IE8605", "H01512", "ID3739", "IE2948", "ID3189", "IE3239",
#     "IE2946", "ID7006", "BB5498", "IE5130", "CQ2809", "FX6563",
#     "IG4996", "IE0420", "IG4994", "IE0429", "IE5597", "IG0360",
#     "IE0421", "IG4028", "IF0881", "ID1105", "B41645", "IE0428",
#     "IF0877", "IE0876", "BB5478", "IG6200", "BB5476", "IF1016",
#     "ID6983", "H06260", "ID7026", "H06126", "BB5480", "H06259",
#     "ID7990", "IG6434", "H06261", "IG4998", "IE8674", "FZ5593",
#     "GY2529", "ID7004", "IG4999", "GY2531", "ID6982", "ID6984"
# ]
#
#
# def get_adidas_product_details(url):
#     service = ChromeService(executable_path='C:/Users/Maibenben/PycharmProjects/chromedriver-win64/chromedriver.exe')
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(service=service, options=options)
#
#     try:
#         driver.get(url)
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#         images = [img['src'] for img in
#                   soup.select('#pdp-gallery-desktop-grid-container .view-cell-container___aqB7e .content___3m-ue img')]
#         description_container = soup.find(class_='description___29WFI')
#         if description_container:
#             description = description_container.find(class_='text-content___13aRm').text
#         else:
#             description = "Описание не найдено"
#
#         price_element = soup.find(class_='gl-price-item notranslate')
#         if price_element:
#             price = price_element.text
#         else:
#             price = "Цена не найдена"
#
#         sizes = [span.text for span in soup.select('.sizes___2jQjF .gl-label span')]
#         unavailable_sizes = [span.text for span in soup.select('.gl-label.size___2lbev.size-selector__size--unavailable___1EibR.size-selector__size--unavailable-crossed___3zV2f')]
#
#         color_images = [img['src'] for img in soup.select('.color-chooser-grid___1ZBx_ img')]
#
#         return {
#             'images': images,
#             'description': description,
#             'price': price,
#             'sizes': sizes,
#             'unavailable_sizes': unavailable_sizes,
#             'color_images': color_images
#         }
#     finally:
#         driver.quit()
#
#
# # Создадим пустой DataFrame для сохранения данных
# data = {
#     'images': [],
#     'description': [],
#     'price': [],
#     'sizes': [],
#     'unavailable_sizes': [],  # Добавляем новое поле для недоступных размеров
#     'color_images': []
# }
#
# for id in ids:
#     url = f'https://www.adidas.com/us/gazelle-bold-shoes/{id}.html'
#     product_details = get_adidas_product_details(url)
#
#     # Добавляем данные в DataFrame
#     for key, value in product_details.items():
#         data[key].append(value)
#
# # Создаем DataFrame
# df = pd.DataFrame(data)
#
# # Сохраняем в Excel
# df.to_excel('detail.xlsx', index=False)
#
# print("Данные сохранены в deе.xlsx")
