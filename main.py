import requests
import win32com.client
import threading
import time
import speech_recognition as  spr
import webbrowser
import os
import telebot
ozvuk = win32com.client.Dispatch('SAPI.SpVoice')
ozvuk.Rate = 5
name = ''
api_comet = ''
api_groq = ''
action_micro = False
token = 'ваш токен @BotFather'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Привет! Я aksa, твоя помощница для твоего пк. /info')
@bot.message_handler(commands=['info'])
def info(m):
    bot.send_message(m.chat.id, '1. /open https://your.url.com - открыть ссылку в браузере\n2. /pc_off - выключить пк сейчас.\n3. /pc_offtime (секунды) - выключить пк через n секунд. (/pc_anti - отмена)\n3. /close_all - закроет все вкладки.\nВсе, что вы делаете выполняется на вашем пк.')
@bot.message_handler(commands=['open'])
def open(m):
    txt = m.text.replace('/open').strip()
    try:
        webbrowser.open(txt)
    except:
        bot.send_message(m.chat.id, 'Ой. Не получилось открыть эту страницу. Проверь валидность ссылки.')
@bot.message_handler(commands=['pc_off'])
def pcoff(m):
    try:
        os.system('shutdown /s /f /t 0')
    except:
        bot.send_message(m.chat.id, 'Ой. Не получилось.')
@bot.message_handler(commands=['pc_offtime'])
def pcoft(m):
    time = m.text.replace('/pc_offtime', '').strip()
    num = 60
    try:
        num = int(time)
    except:
        bot.send_message(m.chat.id, 'Введи число')
    os.system(f'shutdown /s /f /t {num}')
@bot.message_handler(commands=['pc_anti'])
def pctimanti(m):
    try:
        os.system('shutdown /a')
    except:
        bot.send_message(m.chat.id, 'Ой! Ошибка.')
@bot.message_handler(commands=['close_all'])
def clall(m):
    try:
        os.system('powershell -c "Get-Process | Where-Object {$_.MainWindowTitle} | Stop-Process -Force"')
    except:
        bot.send_message(m.chat.id, 'Ой! Ошибка')
if token:
    try:
        th2 = threading.Thread(target=bot.polling)
        th2.daemon = True
        th2.start()
    except:
        print('Ой! Не получилось запустить телеграм бота')
while True:
    ac = input('Ваше имя: ')
    if ac:
        name = str(ac)
        ozvuk.speak(f'Приятно познакомиться, {name}! Введи мне скорость речи.')
        while True:
            spd = input('Скорость речи: ')
            if spd.lower() != 'pass':
                try:
                    if 0 < int(spd) <= 10:
                        sped = int(spd)
                        ozvuk.Rate = sped
                        ozvuk.speak(f'Поняла, {name}! Буду говорить со скоростью {spd}. Выбери способ управления.')
                        break
                    else:
                        ozvuk.speak(f'{name}, я не поняла число. Но я готова продолжить работу. Введи установи скорость для смены скорости. Выбери способ управления.')
                        break
                except:
                    ozvuk.speak(f'{name}, введи скорость цифрой.')
                    pass
            else:
                ozvuk.speak(f'{name}, поняла! Оставляю скорость по умолчанию. Выбери способ управления.')
                break
        ugl = input('Использовать микрофон для команд? ')
        if 'да' in ugl.lower() or 'yes' in ugl.lower():
            ozvuk.speak(f'{name}, поняла. Буду слушать.')
            action_micro = True
        else:
            ozvuk.speak(f'{name}, поняла. Оставлю вам ввод через консоль.')
        break
    else:
        ozvuk.speak('Введите имя, пожалуйста...')
while True:
    txt = ''
    a = ''
    if action_micro == True:
        try:
            mic = spr.Recognizer()
            with spr.Microphone() as aud_total:
                aud = mic.listen(aud_total)
                text = mic.recognize_google(aud, language='ru-RU')
                a = text
        except:
            txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
    else:
        a = input('')
    if 'открой' in a.lower() or 'jnrhjq' in a.lower():
        try:
            a = a.replace('открой', '').strip()
            a = a.replace('jnrhjq', '').strip()
            a = a.split(',')[0]
            url = f'https://{a}.com'
            b = requests.get(url)
            if b.status_code == 200:
                txt = f'Окей, {name}, открываю {a}'
                webbrowser.open(url)
            else:
                url = f'https://{a}.org'
                n = requests.get(url)
                if n.status_code == 200:
                    txt = f'Окей, {name}, открываю {a}'
                    webbrowser.open(url)
                else:
                    url = f'https://{a}.ru'
                    n = requests.get(url)
                    if n.status_code == 200:
                        txt = f'Окей, {name}, открываю {a}'
                        webbrowser.open(url)
                    else:
                        url = f'https://www.{a}.com'
                        b = requests.get(url)
                        if b.status_code == 200:
                            txt = f'Окей, {name}, открываю {a}'
                            webbrowser.open(url)
                        else:
                            url = f'https://www.{a}.org'
                            b = requests.get(url)
                            if b.status_code == 200:
                                txt = f'Окей, {name}, открываю {a}'
                                webbrowser.open(url)
                            else:
                                url = f'https://www.{a}.ru'
                                b = requests.get(url)
                                if b.status_code == 200:
                                    txt = f'Окей, {name}, открываю {a}'
                                    webbrowser.open(url)
                                else:
                                    txt = f'{name}, ой. Произошла ошибка. Кажется такого адреса нету.'
        except:
            txt = f'Ой, {name} простите! Произошла ошибка при откртии {a}. Попробуйте еще раз! Проверь адрес или интернет-соединение.'
    elif 'хочу музыку' in a.lower() or 'послушать музыку' in a.lower() or 'музыку' in a.lower():
        ozvuk.speak(f'{name}, что пожелаете? VK музыка или Яндекс музыка? Или может зайцев net?')
        bc = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    bc = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            bc = input()
        try:
            if 'vk' in bc.lower() or 'вк' in bc.lower():
                url = 'https://vk.com/audio'
                one = requests.get(url)
                if one.status_code == 200:
                    txt = f'{name}, ваше желание сбылось! Включаю вам VK музыку!'
                    webbrowser.open(url)
                else:
                    url = 'https://music.yandex.ru/'
                    kd = requests.get(url)
                    if kd.status_code == 200:
                        txt = f'{name}, VK музыка не открылась. Но я открыла вам яндекс музыку. Приятного прослушивания песен!'
                        webbrowser.open(url)
                    else:
                        url = 'https://zaycev.net/'
                        kd = requests.get(url)
                        if kd.status_code == 200:
                            txt = f'{name}, VK музыка не открылась. Но я открыла вам зайцев net. Приятного прослушивания песен!'
                            webbrowser.open(url)
                        else:
                            txt = f'{name}, ни один из сервисов не работает. Может, надо чуть чуть подождать?'
            elif 'yandex' in bc.lower() or 'яндекс' in bc.lower():
                url = 'https://music.yandex.ru/'
                one = requests.get(url)
                if one.status_code == 200:
                    txt = f'{name}, ваше желание сбылось! Включаю вам яндекс музыку!'
                    webbrowser.open(url)
                else:
                    url = 'https://vk.com/audio'
                    kd = requests.get(url)
                    if kd.status_code == 200:
                        txt = f'{name}, Яндекс музыка не открылась. Но я открыла вам VK музыку. Приятного прослушивания песен!'
                        webbrowser.open(url)
                    else:
                        rl = 'https://zaycev.net/'
                        kd = requests.get(url)
                        if kd.status_code == 200:
                            txt = f'{name}, яндекс музыка не открылась. Но я открыла вам зайцев net. Приятного прослушивания песен!'
                            webbrowser.open(url)
                        else:
                            txt = f'{name}, ни один из сервисов не работает. Может, надо чуть чуть подождать?'
            elif 'зайцев' in bc.lower() or 'zaycev' in bc.lower():
                url = 'https://zaycev.net/'
                one = requests.get(url)
                if one.status_code == 200:
                    txt = f'{name}, ваше желание сбылось! Включаю вам зайцев net!'
                    webbrowser.open(url)
                else:
                    url = 'https://vk.com/audio'
                    kd = requests.get(url)
                    if kd.status_code == 200:
                        txt = f'{name}, зайцев net не открылась. Но я открыла вам VK музыку. Приятного прослушивания песен!'
                        webbrowser.open(url)
                    else:
                        rl = 'https://music.yandex.ru/'
                        kd = requests.get(url)
                        if kd.status_code == 200:
                            txt = f'{name}, зайцев net не открылась. Но я открыла вам яндекс музыку. Приятного прослушивания песен!'
                            webbrowser.open(url)
                        else:
                            txt = f'{name}, ни один из сервисов не работает. Может, надо чуть чуть подождать?'
        except:
            txt = f'Ой, {name} простите! Произошла ошибка при откртии {a}. Попробуйте еще раз! Проверь адрес или интернет-соединение.'
    elif 'удали файл' in a.lower() or 'elfkb afqk' in a.lower():
        ozvuk.speak(f'{name}, откуда удалить файл? Я могу удалить с загрузок, если файл не там, то укажи путь для него.')
        gr = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    gr = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            gr = input()
        if 'загрузки' in gr.lower() or 'загрузок' in gr.lower():
            ozvuk.speak(f'Окей, {name}! Укажи название файла.')
            hh = input()
            if hh:
                try:
                    os.remove(f'C:\\Users\\{name}\\Downloads\\{hh}')
                    txt = f'{name}, успешно удалила файл {gr}'
                except:
                    txt = f'{name}, не получилось удалить файл. Проверь, есть ли такой файл?'
        else:
            try:
                os.remove(hh)
                txt = f'{name}, успешно удалила файл {gr}'
            except:
                txt = f'{name}, не получилось удалить файл. Проверь, есть ли такой файл?'
    elif 'найди видео' in a.lower() or 'yfqlb dbltj' in a.lower() or 'поищи видео' in a.lower() or 'хочу посмотреть видео' in a.lower() or 'хочу видео' in a.lower() or 'включи видео' in a.lower():
        ozvuk.speak(f'Окей, {name}! Я найду вам видео, но уточните, пожалуйста, где искать видео? В VK видео или в Rutube?')
        h = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    h = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            h = input()
        if 'вк видео' in h.lower() or 'vk видео' in h.lower() or 'vk dbltj' in h.lower() or 'vk video' in h.lower() or 'вк' in h.lower() or 'vk' in h.lower():
            ozvuk.speak(f'Поняла, {name}! Буду искать в VK видео. Пожалуйста, укажи название видео.')
            k = ''
            if action_micro == True:
                try:
                    mic = spr.Recognizer()
                    with spr.Microphone() as aud_total:
                        aud = mic.listen(aud_total)
                        text = mic.recognize_google(aud, language='ru-RU')
                        k = text
                except:
                    txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
            else:
                k = input()
            if k:
                try:
                    vlsrjhn = requests.get('https://m.vkvideo.ru')
                    if vlsrjhn.status_code == 200:
                        try:
                            webbrowser.open(f'https://m.vkvideo.ru/?q={k}&action=search')
                            txt = f'{name}, нашла вам видео {k}. Приятного просмотра!'
                        except:
                            txt = f'{name}, произошла ошибка при поиске видео {k}. Извините, пожалуйста!'
                    else:
                        vlsrjhn = requests.get('https://rutube.ru')
                        if vlsrjhn.status_code == 200:
                            try:
                                webbrowser.open(f'https://rutube.ru/search/?query={k}')
                                txt = f'{name}, нашла вам видео {k}. Приятного просмотра!'
                            except:
                                txt = f'{name}, произошла ошибка при поиске видео {k}. Извините, пожалуйста!'
                        else:
                            txt = f'{name}, я искала вам видео, но не получилось. Простите, пожалуйста!'
                except:
                    txt = f'{name}, произошла ошибка. Простите меня, {name}!'
        elif 'на рутубе' in h.lower() or 'в рутубчике' in h.lower() or 'на рутуб' in h.lower() or 'рутубе' in h.lower() or 'рутуб' in h.lower():
            ozvuk.speak(f'Поняла, {name}! Буду искать в рутубе. Пожалуйста, укажи название видео.')
            k = ''
            if action_micro == True:
                try:
                    mic = spr.Recognizer()
                    with spr.Microphone() as aud_total:
                        aud = mic.listen(aud_total)
                        text = mic.recognize_google(aud, language='ru-RU')
                        k = text
                except:
                    txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
            else:
                k = input()
            if k:
                try:
                    vlsrjhn = requests.get('https://rutube.ru')
                    if vlsrjhn.status_code == 200:
                        try:
                            webbrowser.open(f'https://rutube.ru/search/?query={k}')
                            txt = f'{name}, нашла вам видео {k}. Приятного просмотра!'
                        except:
                            txt = f'{name}, произошла ошибка при поиске видео {k}. Извините, пожалуйста!'
                    else:
                        vlsrjhn = requests.get('https://m.vkvideo.ru')
                        if vlsrjhn.status_code == 200:
                            try:
                                webbrowser.open(f'https://m.vkvideo.ru/?q={k}&action=search')
                                txt = f'{name}, нашла вам видео {k}. Приятного просмотра!'
                            except:
                                txt = f'{name}, произошла ошибка при поиске видео {k}. Извините, пожалуйста!'
                        else:
                            txt = f'{name}, я искала вам видео, но не получилось. Простите, пожалуйста!'
                except:
                    txt = f'{name}, произошла ошибка. Простите меня, {name}!'
    elif 'установи скорость' in a.lower():
        a = a.lower().replace('установи скорость', '').strip()
        try:
            v = int(a)
        except:
            v = 5
        if 0 < v <= 10:
            try:
                ozvuk.Rate = v
                txt = f'{name}, поняла вас! Установила скорость {v}'
            except:
                txt = f'{name}, проверь, точно ли ты ввел число от 1 до 10.'
        else:
            txt = f'{name}, введи число от одного до десяти.'
    elif 'найди песню' in a.lower() or 'yfqlb gtcy.' in a.lower() or 'включи песню' in a.lower() or 'найди музыку' in a.lower() or 'песню' in a.lower() or 'музыку' in a.lower():
        ozvuk.speak(f'{name}, поняла! У вас музыкальное настроение! Могу предложить вам VK музыку или Зайцев net.')
        vybor = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    vybor = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            vybor = input()
        if 'vk' in vybor.lower() or 'вк' in vybor.lower():
            ozvuk.speak(f'Поняла, {name}! Вы хотите использовать ВК музыку. Напишите мне название песни.') 
            fgj = ''
            if action_micro == True:
                try:
                    mic = spr.Recognizer()
                    with spr.Microphone() as aud_total:
                        aud = mic.listen(aud_total)
                        text = mic.recognize_google(aud, language='ru-RU')
                        fgj = text
                except:
                    txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
            else:
                fgj = input()
            if fgj:
                try:
                    trn = requests.get('https://vk.com/audio')
                    if trn.status_code == 200:
                        try:
                            webbrowser.open(f'https://vk.com/audio?q={fgj}') 
                            txt = f'{name}, я открыла вам песню. Приятного прослушивания!'
                        except:
                            txt = f'{name}, кажется, произошла ошибка. Пожалуйста, простите меня!' 
                    else:
                        kh = requests.get('https://zaycev.net')  
                        if kh.status_code == 200:
                            try:
                                webbrowser.open(f'https://zaycev.net/search?query_search={fgj}&type=all')       
                                txt = f'{name}, я открыла вам песню. Приятного прослушивания!'        
                            except:
                                txt = f'{name}, кажется, произошла ошибка. Пожалуйста, простите меня!' 
                        else:
                            txt = f'{name}, простите! Я не смогла открыть эту песню.'
                except:
                    txt = f'{name}, произошла ошибка. Простите, пожалуйста!'
        elif 'зайцев' in vybor.lower() or 'zaycev' in vybor.lower():
            ozvuk.speak(f'Поняла, {name}! Вы хотите использовать зайцев net. Напишите мне название песни.') 
            fgj = ''
            if action_micro == True:
                try:
                    mic = spr.Recognizer()
                    with spr.Microphone() as aud_total:
                        aud = mic.listen(aud_total)
                        text = mic.recognize_google(aud, language='ru-RU')
                        fgj = text
                except:
                    txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
            else:
                fgj = input()
            if fgj:
                try:
                    trn = requests.get('https://zaycev.net')
                    if trn.status_code == 200:
                        try:
                            webbrowser.open(f' https://zaycev.net/search?query_search={fgj}&type=all') 
                            txt = f'{name}, я открыла вам песню. Приятного прослушивания!'
                        except:
                            txt = f'{name}, кажется, произошла ошибка. Пожалуйста, простите меня!' 
                    else:
                        kh = requests.get('https://vk.com/audio')  
                        if kh.status_code == 200:
                            try:
                                webbrowser.open(f'https://vk.com/audio?q={fgj}')       
                                txt = f'{name}, я открыла вам песню. Приятного прослушивания!'        
                            except:
                                txt = f'{name}, кажется, произошла ошибка. Пожалуйста, простите меня!' 
                        else:
                            txt = f'{name}, простите! Я не смогла открыть эту песню.'
                except:
                    txt = f'{name}, произошла ошибка. Простите, пожалуйста!'
    elif 'найди фото' in a.lower() or 'yfqlb ajnj' in a.lower() or 'найди фотки' in a.lower() or 'yfqlb ajnrb' in a.lower() or 'фото' in a.lower():
        ozvuk.speak(f'{name}, уточни, какие фото искть?')
        og = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    og = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            og = input()
        if og:
            try:
                d = requests.get('https://google.com')
                if d.status_code == 200:
                    try:
                        webbrowser.open(f'https://www.google.com/search?q={og}&sca_esv=4efc6c15b1c21641&udm=2&ei=BsFQabaAMo_JwPAP6O-SKQ&ved=0ahUKEwi2m-mqx9-RAxWPJBAIHei3JAUQ4dUDCBI&uact=5&oq=%D0%B2&gs_lp=Egtnd3Mtd2l6LWltZyIC0LIyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMg4QABiABBixAxiDARiKBTILEAAYgAQYsQMYgwEyChAAGIAEGEMYigUyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwFIxAlQygVYygVwAXgAkAEAmAFQoAFQqgEBMbgBA8gBAPgBAZgCAaACVqgCAJgDAZIHATGgB78FsgcBMbgHVsIHAzItMcgHBYAIAA&sclient=gws-wiz-img')
                        txt = f'{name}, нашла вам фото. Открыла в браузере.'
                    except:
                        txt = f'{name}, простите, я не смогла найти вам фото.'
                else:
                    h = requests.get('https://yandex.ru')
                    if h.status_code == 200:
                        try:
                            webbrowser.open(f'https://ya.ru/images/search?from=tabbar&text={og}')
                            txt = f'{name}, нашла вам фото. Открыла в браузере.'
                        except:
                            txt = f'{name}, простите, я не смогла найти вам фото.'
                    else:
                        txt = f'{name}, не смогла найти вам фото. Простите!'
            except:
                txt = f'{name}, простите, произошла ошибка.'
    elif 'найди в поиске' in a.lower() or 'выполни поиск' in a.lower() or 'найди в интернете' in a.lower() or 'найди' in a.lower():
        ozvuk.speak(f'{name}, поняла вас. Уточните, что вам надо найти?')
        ghe = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    ghe = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            ghe = input()
        if ghe:
            try:
                fs = requests.get('https://google.com')
                if fs.status_code == 200:
                    try:
                        webbrowser.open(f'https://www.google.com/search?q={ghe}&sca_esv=4efc6c15b1c21641&biw=1511&bih=828&ei=isRQadm-HcvZwPAPtMuUoQU&ved=0ahUKEwjZq-jXyt-RAxXLLBAIHbQlJVQQ4dUDCBE&uact=5&oq=gjbcr&gs_lp=Egxnd3Mtd2l6LXNlcnAiBWdqYmNyMg4QABiABBixAxgKGCoYCzIPEAAYgAQYsQMYgwEYChgLMgkQABiABBgKGAsyDBAAGIAEGLEDGAoYCzIJEAAYgAQYChgLMgkQABiABBgKGAsyCRAAGIAEGAoYCzIJEAAYgAQYChgLMg8QABiABBixAxiDARgKGAsyCRAAGIAEGAoYC0ivHVDuCFi6GnABeAKQAQCYAfwEoAGgD6oBCzAuMS4xLjAuMi4xuAEDyAEA-AEBmAIHoALGD6gCFMICBBAAGEfCAhYQABiABBhDGLQCGOcGGIoFGOoC2AEBwgIWEC4YgAQYQxi0AhjnBhiKBRjqAtgBAcICEBAAGAMYtAIY6gIYjwHYAQLCAhAQLhgDGLQCGOoCGI8B2AECwgILEAAYgAQYsQMYgwHCAggQABiABBixA8ICDhAAGIAEGLEDGIMBGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAgUQABiABMICCxAuGIAEGLEDGIMBwgIMEAAYgAQYARixAxgKwgIJEAAYgAQYARgKwgILEAAYgAQYARgKGCrCAgsQABiABBiSAxiKBcICDBAAGIAEGAEYyQMYCpgDC_EFyCM9vYbVTiaIBgGQBgi6BgQIARgHugYGCAIQARgKkgcLMi4xLjEuMC4yLjGgB8w3sgcLMC4xLjEuMC4yLjG4B7cPwgcHMC4yLjQuMcgHHoAIAA&sclient=gws-wiz-serp')
                        txt = f'{name}, нашла вам контент. Открыла в браузере'
                    except:
                        txt = f'{name}, простите. Произошла ошибка.'
                else:
                    woh = requests.get('https://yandex.ru')
                    if woh.status_code == 200:
                        try:
                            webbrowser.open(f'https://ya.ru/search/?text={ghe}&lr=141085')
                            txt = f'{name}, нашла вам контент. Открыла в браузере'
                        except:
                            txt = f'{name}, простите. Произошла ошибка.'
                    else:
                        txt = f'{name}, простите. Ни один из сервисов не работает.'
            except:
                txt = f'Простите, {name}! Я пыталась, но произошла ошибка.'
    elif 'включи мой плейлист' in a.lower() or 'включи мои песни' in a.lower() or 'мои песни' in a.lower() or 'мой плейлист' in a.lower() or 'мои любимые' in a.lower():
        try:
            hf = requests.get('https://vk.com/audio')
            if hf.status_code == 200:
                try:
                    webbrowser.open('https://vk.com/audios') #ссылка на ваш плейлист
                    txt = f'{name}, включила твой плейлист в VK музыке. Приятного прослушивания!'
                except:
                    txt = f'Ой, {name}! Кажется, произошла ошибка. Простите, пожалуйста!'
            else:
                try:
                    qf = requests.get('https://music.yandex.ru')
                    if qf.status_code == 200:
                        try:
                            webbrowser.open('https://music.yandex.ru/playlists/') #ссылка на ваш плейлист
                            txt = f'{name}, включила твой плейлист в Яндекс музыке. Приятного прослушивания!'
                        except:
                            txt = f'Ой, {name}! Кажется, произошла ошибка. Простите, пожалуйста!'
                    else:
                        txt = f'Прости, {name}! Я не хотела, но произошла ошибка. Проверь интернет соединение!'
                except:
                    txt = f'{name}, произошла ошибка. Простите, пожалуйста!'
        except:
            txt = f'{name}, извини.. Произошла ошибка, и я не смогла открыть тебе твой плейлист. Проверь интернет-соединение.'
    elif 'выполни код' in a.lower() or 'dsgjkyb rjl' in a.lower():
        ozvuk.speak(f'{name}, поняла. Напиши свой код, а когда будет готов, введи run')
        code = '''
print('Выполняю код...')'''
        while True:
            dwb = input()
            if dwb:
                if dwb.lower() == 'run':
                    try:
                        exec(code)
                        txt = f'{name}, успешно выполнила ваш код. Удачи!'
                        break
                    except:
                        txt = f'{name}, произошла ошибка. Простите'
                        break
                else:
                    code = code + '\n' + dwb
            else:
                pass
    elif 'сделай код' in a.lower() or 'cltkfq rjl' in a.lower() or 'сделай проект' in a.lower() or 'напиши код' in a.lower() or 'создай код' in a.lower():
        ozvuk.speak(f'{name}, поняла. Вам нужен проект. Скажите, какой проект вам нужен? Добавьте все API токены и ключи.')
        gjh = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    gjh = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            gjh = input()
        if gjh:
            try:
                post1 = {
                        'Authorization': f'Bearer {api_groq},
                        'Content-Type': 'application/json'
                    }
                post2 = {
                    'model': 'openai/gpt-oss-120b',
                    'messages': [
                        {
                            'role': 'system',
                            'content': '''

You are a Python code generator. Your task is to create safe, working code.
давай только чистый, правильный код без пояснений и символов, которые нарушают синтаксис
 '''
                        },
                        {
                            'role': 'user',
                            'content': gjh
                        }
                    ],
                    'temperature': 0.7,
                    'max_tokens': 200
                }
                api_post = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=post1, json=post2, timeout=30)
                if api_post.status_code == 200:
                    otv = api_post.json()
                    otvai = otv['choices'][0]['message']['content']
                    otvai = otvai.replace('python', '').strip()
                    otvai = otvai.replace('`', '').strip()
                    try:
                        th1 = threading.Thread(target=lambda: exec(otvai))
                        th1.start()
                        th1.join()
                        txt = f'{name}, успешно создала проект! Можете проверять.'
                    except:
                        txt = f'{name}, не смогла создать проект. Простите!'
                else:
                    try:
                        post1 = {
                                'Authorization': f'Bearer {api_comet}',
                                'Content-Type': 'application/json'
                            }
                        post2 = {
                            'model': 'gpt-3.5-turbo',
                            'messages': [
                                {
                                    'role': 'system',
                                    'content': '''

        You are a Python code generator. Your task is to create safe, working code.
'''
                                },
                                {
                                    'role': 'user',
                                    'content': gjh
                                }
                            ],
                            'temperature': 0.7,
                            'max_tokens': 200
                        }
                        api_post = requests.post('https://api.cometapi.com/v1/chat/completions', headers=post1, json=post2, timeout=30)
                        if api_post.status_code == 200:
                            otv = api_post.json()
                            otvai = otv['choices'][0]['message']['content']
                            otvai = otvai.replace('python', '').strip()
                            otvai = otvai.replace('`', '').strip()
                            try:
                                th1 = threading.Thread(target=lambda: exec(otvai))
                                th1.start()
                                th1.join()
                                txt = f'{name}, успешно создала проект! Можете проверять.'
                            except:
                                txt = f'{name}, не смогла создать проект. Простите!'
                        else:
                            txt = f'{name}, простите. Получила ошибку. Попробуйте проверить интернет-соединение.'
                    except:
                        txt = f'{name}, простите! Я не смогла сделать вам проект. Проверьте интернет соединение'
            except:
                try:
                    post1 = {
                            'Authorization': f'Bearer {api_comet}',
                            'Content-Type': 'application/json'
                        }
                    post2 = {
                        'model': 'gpt-3.5-turbo',
                        'messages': [
                            {
                                'role': 'system',
                                'content': '''
    You are a Python code generator. Your task is to create safe, working code.
'''
                            },
                            {
                                'role': 'user',
                                'content': gjh
                            }
                        ],
                        'temperature': 0.7,
                        'max_tokens': 200
                    }
                    api_post = requests.post('https://api.cometapi.com/v1/chat/completions', headers=post1, json=post2, timeout=30)
                    if api_post.status_code == 200:
                        otv = api_post.json()
                        otvai = otv['choices'][0]['message']['content']
                        otvai = otvai.replace('python', '').strip()
                        otvai = otvai.replace('`', '').strip()
                        try:
                            th1 = threading.Thread(target=lambda: exec(otvai))
                            th1.start()
                            th1.join()
                            txt = f'{name}, успешно создала проект! Можете проверять.'
                        except:
                            txt = f'{name}, не смогла создать проект. Простите!'
                    else:
                        txt = f'{name}, простите. Получила ошибку. Попробуйте проверить интернет-соединение.'
                except:
                    txt = f'{name}, простите! Я не смогла сделать вам проект. Проверьте интернет соединение'
    elif 'выключи' in a.lower() and 'сейчас' in a.lower():
        ozvuk.speak(f'{name}, я выключю твой компьютер. Ты уверен?')
        uy = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    uy = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            uy = input()
        if 'да' in uy.lower() or 'yes' in uy.lower():
            ozvuk.speak(f'{name}, выключаю ваш компьтер. Возвращайтесь!')
            os.system('shutdown /s /f /t 0')
        else:
            txt = f'{name}, поняла. Не буду выключать пк.'
    elif 'закрой' in a.lower() and 'вкладк' in a.lower():
        ozvuk.speak(f'{name}, вы уверены? Это закроет все ваши вкладки.')
        ig = ''
        if action_micro == True:
            try:
                mic = spr.Recognizer()
                with spr.Microphone() as aud_total:
                    aud = mic.listen(aud_total)
                    text = mic.recognize_google(aud, language='ru-RU')
                    ig = text
            except:
                txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
        else:
            ig = input()
        if 'да' in ig.lower() or 'yes' in ig.lower():
            ozvuk.speak(f'{name}, поняла. Закрываю все вкладки.')
            os.system('powershell -c "Get-Process | Where-Object {$_.MainWindowTitle} | Stop-Process -Force"')
        else:
            txt = f'{name}, поняла. Не буду закрывать все вкладки.'
    elif 'выключ' in a.lower() and 'микро' in a.lower():
        txt = f'{name}, поняла. Выключила прослушку микрофона. Теперь общение со мной через консоль.'
        action_micro = False
    elif 'включ' in a.lower() and 'микро' in a.lower():
        txt = f'{name}, поняла. Включила микрофон для прослушки команд.'
        action_micro = True
    elif 'выключи' in a.lower() and 'потом' in a.lower():
        ozvuk.speak(f'{name}, поняла. Выключю ваш компьютер через время. Укажи в секундах, через сколько мне его выключить?')
        while True:
            bu = ''
            if action_micro == True:
                try:
                    mic = spr.Recognizer()
                    with spr.Microphone() as aud_total:
                        aud = mic.listen(aud_total)
                        text = mic.recognize_google(aud, language='ru-RU')
                        bu = text
                except:
                    txt = f'{name}, извините. Не расслышала. Повторите, пожалуйста.'
            else:
                bu = input()
            if 'отмена' in bu.lower() or 'отме' in bu.lower():
                txt = f'{name}, поняла. Отменила это действие.'
                break
            else:
                try:
                    ec = int(bu)
                    os.system(f'shutdown /s /t {ec}')
                    txt = f'{name}, запланировала отключение вашего компьютера. Приятного отдыха!'
                    break
                except:
                    txt = f'{name}, введи число, пожалуйста.'
                    pass
    elif 'отм' in a.lower() and 'выключе' in a.lower():
        txt = f'{name}, отменила отключение пк. Приятной работы!'
        os.system('shutdown /a')
    else:
        try:
            post1 = {
                'Authorization': f'Bearer {api_groq}',
                'Content-Type': 'application/json'
                    }
            post2 = {
                'model': 'llama-3.1-8b-instant',
                'messages': [
                    {
                        'role': 'system',
                        'content': 'Тебя зовут Акса, ты очень добрая.'
                    },
                    {
                        'role': 'user',
                        'content': a.lower()
                    }
                ],
                'temperature': 0.7,
                'max_tokens': 25
            }
            postai = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=post1, json=post2, timeout=30)
            if postai.status_code == 200:
                otv = postai.json()
                txt = otv['choices'][0]['message']['content']
            else:
                try:
                    post1 = {
                            'Authorization': f'Bearer {api_comet}',
                            'Content-Type': 'application/json'
                        }
                    post2 = {
                        'model': 'gpt-3.5-turbo',
                        'messages': [
                            {
                                'role': 'system',
                                'content': 'Тебя зовут Акса, ты очень добрая.'
                            },
                            {
                                'role': 'user',
                                'content': a.lower()
                            }
                        ],
                        'temperature': 0.7,
                        'max_tokens': 25
                    }
                    api_post = requests.post('https://api.cometapi.com/v1/chat/completions', headers=post1, json=post2, timeout=30)
                    if api_post.status_code == 200:
                        otv = api_post.json()
                        txt = otv['choices'][0]['message']['content']
                    else:
                        txt = f'{name}, простите. Произошла ошибка, и я не смогла вам ответить. Проверьте интернет соединение'
                except:
                    txt = f'{name}, простите! Я не смогла вам ответить. Проверьте интернет соединение.'
        except:
            txt = f'Простите, {name}! Произошла ошибка, и я не смогла вам ответить. Проверьте интернет соединение.'
    ozvuk.speak(txt)
