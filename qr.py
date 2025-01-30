import qrcode; data = 'https://vkvideo.ru/video444500969_456239142?t=47m35s'; filename = "site.png"; img = qrcode.make(data); img.save(filename)

# import qrcode
# # пример данных
# data = "Сюда ссылку"
# # имя конечного файла
# filename = "site.png"
# # генерируем qr-код
# img = qrcode.make(data)
# # сохраняем img в файл
# img.save(filename)