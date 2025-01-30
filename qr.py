# import qrcode; data = 'https://vkvideo.ru/video444500969_456239142?t=47m35s'; filename = "site.png"; img = qrcode.make(data); img.save(filename)

import qrcode
data = input('Введите ссылку: ')
filename = "site.png"
img = qrcode.make(data)
img.save(filename)