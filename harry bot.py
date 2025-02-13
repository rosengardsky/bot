from telethon import TelegramClient, events, utils, sync, types
from random import choice
from datetime import datetime, timedelta
from asyncio import sleep
import time
import re
import requests
import sys
from bs4 import BeautifulSoup
import os
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.types import Channel
from telethon.tl.functions.messages import ImportChatInviteRequest
from urllib.parse import urlparse
from telethon.errors import ChatAdminRequiredError
import asyncio
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
import psutil
from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest

menutext = "<b>{}</b>\nвторой хелп - <code>.меню</code>\n\n остальные команды:\n<code>.лист</code> + медия — список работы бота.\n<code>.меню</code> + медия — mеnю\n<code>.хелп</code> — второе меню\n<code>.слова</code> + репл — количество слов в сообщении.\n<code>.сменить</code> + репл — смена шаблов бота.\n<code>.основа</code> — основной шаблон бота.\n<code>.зайти</code> + линк — зайти в чат.\n<code>.выйти</code> + линк — лив с чата\n<code>.аптайм</code> — аптайм.\n<code>.пинг</code> — пинг.\n<code>.афк</code> + 1(on)/2(off) \ медия \ причина — управление afk.\n<code>.айди</code> — узнать чат /юз айди\n<code>.x0</code> + репл — загрузить медию на хостинг\n\nthis chat id: <code>{}</code>\nyour user id: <code>{}</code>\nyour name: <code>{}</code>\nyour username: @{}</b>\nbot owner — <a href='.'>@oxpio</a></b>\nbot coder —<a href='.'>@requimforadreaml</a>  "
shablon = ["перекручу твоє ригалище в цій конференції", "ти єбаний син хуйні всіма виєбаний тут", "нікому не відомий раб хуя закрий піздак свій", "я мамашу різав твою синулька хуйні єбаний слабкий", "ригало твоє я єбав синуля гівна пучеглазий", "вузькі твої очі натягну тобі на жопу якщо ще раз рило відкриєш син хуйні єбаний", "ти тут не більше чим пузатий хуєсос нікому не відомий а ну по тапкам дав бігом нахуй", "я твою мамашу в рильник єбав синуля повії єбучий кривозубий", "алоу циган косоокий, я що тобі сказав? закрий рило своє придурок єбучий інакше зараз пізди втричі сильніше отримаєш", "єбали тебе між іншим клоуна єбаного", "давай синуля гівна єбаний намагайся протистояти моєму членіксу придурок блять хахвхп", "надутий єбанат ти справді спеціально для того щоб смоктанути мій хуяк призвав його з моїх штанів наче демона з пекла?", "давай тужся придурок єбаний ще трішки і я залишу твою рожицю єбучу в спокої назавжди бо ти помреш нахуй !!", "мамаша твоя шалава єбуча і що ти мені скажеш тепер слабкий син хуйні?", "ну і терпи придурок єбаний, все одно я твою сестру вже трахнув.", "лови лящину бомжара єбуча аби не спав поки трахають тебе", "до речі на ура твою мамашу трахав", "я різав горло твоєї матері", "ти єбаний син хуйні русопідарасний", "о да давай помирай єбаний син хуйні слабкий на мозок", "а ну русня єбуча закрила піздак свій кривий нахуй", "ти синок шалави полеглий від мого хуя яка тобі витримка взагалі", "починай мені хуя смоктати я тобі мамашку шалаву все рівно виєбу", "не намагайся давати якогось виду відпіру всі вже знають що ти терпінь єбаний", "сруснявий синок шалави ти там не думай що ти на щось то і здатен", "всі твої мрії я знищу нахуй бо ясен хуй ти ніколи не переможеш мене", "захаркаю все рівно тебе синка шалавки різаного", "дивись не налякайся моєї залупи синок шалави відсосний", "русосвиню єбану тебе ріжу бо така померша одноразка мені нахуй не потрібна", "прям тут я твою мамашку в рило єбав", "свинка єбана сруснява ти там в свої сили повірила чи як я це повинен розуміти ?", "дивись за тиждень не помри на своєму копроботі синок блядухи", "твою мамашку повію тут з легкістю натягну на свій хуяк", "на нон стопі ти мені хуй сосав", "до речі мамашку твою на ура швілив", "русоблядську мамашку шалашовку різану тут на фарш пустимо", "і шо ти мені вкинув синок шалави єбаний котрий свої говнотекста зі швидкістю равлика пише а ну пішов нахуй звідси", "бігом починай мою залупу до свіркання шліфувати своїм рилом русоблядотним", "ти померший хряк дивись не відсмокчи знову", "копротроль єбаний мамашку твою всією конференцією в зад трахали", "почуй мене та зрозумій що ти на справді не більше ніж насадка для хуя", "равлика єбаного по лезу пущу", "я тобі горловину нахуй вскрою синачело слабачки наївної", "єбали тобі свинорило синку русоблядоти єбаної", "мамашку тобі різали хуями якщо ти не знав", "ти синок шалашовки бомжеватий котрий всім давно вже хуй відсмоктав", "ти як був захарканим слабаком таким і лишився", "твою кривозубу циганськоподібну мамашку свиню закидали цеглою", "на гідранти насаджували твою матір її натягнутою виєбаною піздою", "ти не більше ніж насадка на хуяк всіма відпізжена", "мамашку твою єбали без зайвих слів", "трахали тобі рило дегенерату єбаному сука", "без проблем тобі єбальник переломаю синочку свині сруснявої", "бомжонок єбаний мамашку тобі виєбемо", "зуби тобі вирвемо як би ти не чинив опір", "цеглою переломаю тобі бошку нахуй", "докажи що ти на щось здатен єбаний ротовиєбаний слабак", "ти ні в якому разі не зможеш протидіяти мені бо всі вже бачили кожен твій відсос мого хуя", "дивись там не помри раніше чим планував", "спробуй відбитись від мене один хуй моментально по єбалу получиш", "ти тільки там не сильно надійся що твої сили тебе не залишуть коли побачуть справжню швидкість мого письма", "від рук ти хуй смоктав ось й впав на бота", "мамашку твою натовпом забили", "криворилий найслабший свиноруснявий синачело блядоруснявої циганськоподібної шалашовки відсосний тобі в ніякому разі не можна з'являтись тут бо тебе просто напросто чекає смерть", "переломаємо копита твоїй жирнішій свиноподібній шалашоматері за всі вчинки котрі вона вчинила", "покажи свою фантазію русноблядський полумертвий орк котрому єбальник не переломав тільки той кому було впадлу", "всюди ти мій хуй смоктав та тягав його з собою", "краще б ти тренував вміння тролитись чим тренував вміння мінету", "получивши по рилу ти один раз і назавжди зрозумієш що я одночасно з тим як давав тобі піздонів ще й вчив тебе не лізти на українські пеніси без потреби", "ти голозадий та відпізжений синок шалавки єбаний закрий своє срусняве свинорило нахуй та терпи плевки", "померлому на пенісі синку шалави я ні шансу не залишу та вб'ю до останнього свинорила єбаного", "не вихрюкуй більше слабачок свиноруснявий котрий получив по єбалу на перших хвилинах свого говнотролінгу", "я тобі тут мати повію рильну єбашу без співчуття до тебе", "нахуй ти руснявий син шалашовки помер тут то", "свиня блядоруснява я тебе тут так то захаркую, покажи свої сили поки не вмер знову", "завали єбало своє свиня чорнозуба нахуй та навіть не думай писати сюди щось", "не трусись від мого хуя безнадіжний говнотроль котрий б ніколи від українського хуя не відмовився", "не помирай тут слабак єбаний, продовжуй тужитись щоб показати щось моєму хую", "твої маневри язиком на пенісі ніколи не були та не будуть актуальними для нормального роду тролів котрі не рипаються на мій хуй", "який тобі нон стоп слабіший сруснявий син хуйні котрий получає піздонів від мене весь час поки знаходиться в конференції та намагається давити з себе 30 впм", "сиди та бійся мене так і надалі слабачок свиноблядський котрий вже побачив мою силу", "якщо ти так і будеш мовчати я без шансів для тебе порву рилище твоїй свиноподібній мамашці шалаві", "во славу України твою русоблядську матір відсосницю за шкіру підвішаємо на ланцюгах та почнемо знущатись поки вона в свідомості", "один хуй ти слабіший ротовиєбаний циган до того ще й чорнозубий обожнюючий українські пеніси навіть близько зі мною не стоїш", "не відривайся від хуя, я ж бачу що ти ловиш кайф від нього", "твою мамашенцію трахнемо у любому випадку", "русоблядоті тут матір повію в рило виєбемо поки ніхто не бачить", "ну так як тобі на смак український хуй синуля шалави свинорилий котрий при любому розкладі мене не переможе?", "камінцями закидали твою тупішу мамашку шалавенцію", "між іншим твоя мамашка шалава жирна", "шо ти мені зробиш я тобі мамашку єбав", "терпи так і надалі ти ж не здатний синок шалави блядоруснявий", "один хуй в терпнях залишишся", "син хуйні блядський не втикай сука копита тобі виламаю", "я тобі щелепу твою криву до кінця вирву шалава єбуча", "руснява насадка на хуй ти попросту не здатен на тролінг давай засмокчуй хуїну", "я твою мамашу єбав поки ти терпів сруснявий слабак піздец нахуй з'єбався звідси", "збирайся з силами щоб мені щось відписати син хуйні єбаний", "твою мамашку пустимо по лезу та всю кров вип'ємо", "ти нічого не вартий син шалави давай там ще втечи з хуя", "прискорюйся син хуйні єбаний копита тобі вирвемо", "рильце твоє блядське тут напросто в кашу перемолотимо", "досить терпіти блядорус єбучий дай відпір мені", "реневаловським пенісом тобі піздак пірву нахуй", "вкачай фантазію синок шалави єбаний ти куди помер", "швидше пиши виєбастий син хуйні криворукий", "ти там щось взагалі в паніку вирішила впасти криворука сволота", "дай відпір син шалави блядський скільки разів тобі ще сказати тупішому синку шалави", "чисто на шматки тебе нахуйницю розріжемо", "блядоруснявий син хуйні циганський почни вже по клавіатурі попадати хулі ти як теля криволапе", "де твоя агресія синяра шалавні терпіжний", "поки ти терпів тобі сраку виєбали ну думаю ти не проти досихпір", "скільки часу пройшло, а ти досихпір не набрався сміливості відписати мені щось", "ну звісно ти синок хуйні потішний", "твою шалавоблядоматір на хуяк накрутимо вона більше встати не зможе", "копита тобі відріжемо почуй мене син блядоти єбучий", "ну так що, ти досихпір терпиш як син шалави слабкий ?", "русопідарасу копита нахуй відрізали членами", "ти як син хуйні досихпір фанатієш від реневаловського хуя", "синку шалави єбальник перекрутили і він стерпів всі знущання", "ну чисто тебе тут єбашити продовжимо тому не сподівайся на порятунок слабак єбаний", "не глохни раб підарас ", "ти руснявий слабак дивись по тапкам не дай", "синяра повії єбучий ти на що рохраховувати вирішив придурок сука", "да я мамашу твою єбав що далі", "не мовчати на члені дурочка єбана інакше пізди нахапаєш", "ти бомжара єбуча не смій писати в чат щось", "рабопідарас свиноруснявий а ну піздак свій підбий там нахуй", "рабиня хуя я тобі сказав закрий рилище нахуй ти що не зрозумів ", "придурок єбучий закрий рилище нахуй", "слабак єбучий алоу не спати тут", "ти чому тут помер придурок виєбаний", "не думай реалізовувати революцію проти мого члена слабак єбаний", "звикай до того що я твою мамашу в піздак єбу коли захочу", "ну ти піздец терпінь єбаний русопідарський сидиш харчу ловиш слабак нахуй", "твою мамашу роздягну членом", "придурок нікому не відомий хто тобі дав дозвіл писати в чат нахуй а ну рилище втопив русопідарас лісний", "твоя мамаша шалава єбуча нахуй", "не пиши нічого сюди бомжонок блядський", "виєбали твою мамашу да так щоб ніхто не бачив", "вирву твої нирки паскудниця єбуча", "кістки твоєї рідні переламаю не залишаючи жодних цілих місць ти зрозумів мене підарас?", "ти повільний рабопідарас не смій тут копита відкинути", "затиснув зубами твоєї матері свій хуй", "тільки спробуй померти насадка для хуя блядська", "ти свин руснявий саме тут хуя заглатуй ", "не думай що ти сильний придурок сука не здатний на щось", "мамашу твою поєбу зараз нахуй", "рилище закрий нахуй своє", "підбий рилище синяра хуйні", "я на твоє рилище срав синяра повії ", "нахуярив рилище твоєї мамаши гівном", "рило тобі поєбу в будь якому випадку", "без шансів твоє рило єбу сволота єбуча", "в рило тебе трахаю не терпи ноунейм криворукий", "паскудниця давай відпір нахуй чому ти мовчиш", "мамашу твою напізжу", "напіздячу рилище твоїй матері ", "переломаю нахуй п'яти твоєї матері ", "ти копитний рабопідарас пиши швидше нахуй", "копита твої виламаю ", "ти чорний синок хуйні свинорилий закрийся нахуй там", "підбий хрюкало своє жирний синок хуйні", "я мамашу твою єбав в рот нахуй", "ти чому терпіти вирішила бомжиха блядська", "всім відомо хто твою мамашу єбав, а саме Реневал!", "ти циган єбучий закрий сосало своє нахуй", "твою циганську мамашу бомжиху нахуярю", "твого батька цигана заб'ю нахуй ", "піздили тебе членами чисто ноунейма сруснявого", "ти бомжонок єбучий дивись не злітай з хуя", "твого сразербайджанського батька підараса на членах вертіли", "закрий єбало своє бомжиха сука відстала", "я твою мамашу в піздак єбу тільки спробуй про це розповісти комусь нахуй", "ти бомж єбучий тільки спробуй тут ще раз щось написати я точно тобі свинорилище переламаю придурок нахуй", "ти нікому не відомий раб підарас закрий нахуй рилище ти чому там ще хрюкаєш то свинота нахуй", "твоя мамаша шалава блять", "піздец твоя матір хуй смокче", "тебе піздили лошка єбаного", "пізжу тебе бомжа сука", "по рилу з ноги приймай придурок сука", "в пізду твоєї матері незаконно хуї провозив", "прорвався на територію пізди твоєї матері", "хуйом проводив шоу талантів на рилищі твоєї матері", "пропіздили тебе точно в анус", "зарейдив пізду твоєї матері", "протаранив пенісом тобі дупу", "в прямому сенсі тебе гівном полив", "запіздили тебе бомжа єбаного"]

afk_photo = "https://i.pinimg.com/736x/31/e7/36/31e736ca8e35c55454b76f0bce009048.jpg"
state = None
spam_state = {}
spam_state1 = {}
user_list = []
chatreply_list = []
start_time = time.time()
chats_to_greet = []
chats = {}
active_forwards = {} 
autoreply_list = []
autoreply_time = {}
last_reply_time = {}
autoreply_photo = {}
autoreply_shpk = {}
autoreply_shpk_chat = {}
autoreply_time_chat = {}
autoreply_list_chat = []
autoreply_photo_chat = {}
start = 10
tagger_chats = {}
tag_chats = {}
reason = "бот"
start1 = datetime.now()
lists = {}
mid = 'https://media.giphy.com/media/QLCWubleeNppS/giphy.gif?cid=790b7611zf4tugxusknnota9p3tg3x2x86m5oui0i8ldrdxh&ep=v1_gifs_search&rid=giphy.gif&ct=g'
name = " harry bot "
menu = "первый хелп -  <code>.хелп</code>\n\n команды спам:\n<code>.спамм</code> + время + скорость + реплай — спам в чат.\n<code>.спам</code> + время + скорость — спам в чат.\n<code>.стоп</code> / <code>.zstop</code> + чат_айди — остановка спама\n<code>.теггер</code> + айди + время + скорость + реплай — спам-теггер.\n<code>.тег</code> + чат_айди + юз_айди + время + скорость — спам-теггер.\n<code>.офф</code> / <code>.тегофф</code> + айди — остановка теггера.\n<code>.клд</code> + время + скорость + реплай — календарь.\n<code>.клдд</code> + чат_айди + время + скорость — календарь.\n<code>.нт</code> + айди + время + скорость // реплай  — автоответчик.\n<code>.нтт</code> + юз_айди / реплай — off автоответчик.\n<code>.арг</code> + [shapka,скорость,вреmя] + юз_айди — смена аргументов автоответчика.\n<code>.лз</code> — off автоответчик на всех."
mh = 'https://i.pinimg.com/736x/4e/84/9c/4e849c4caa86f06363de8cc6f077de66.jpg'
mm = 'https://media.giphy.com/media/QLCWubleeNppS/giphy.gif?cid=790b7611zf4tugxusknnota9p3tg3x2x86m5oui0i8ldrdxh&ep=v1_gifs_search&rid=giphy.gif&ct=g'
mlist = 'https://i.pinimg.com/736x/4b/7f/ed/4b7fed6a5633e05e3d7de73eba12d794.jpg'
State = {}

class Userbot():
    def __init__(self):
        self.api_id = 23825950
        self.api_hash = "270fa73cf300dfcf9d131745869b31c0"
        self.client = TelegramClient('Narcissist', self.api_id, self.api_hash, system_version="4.16.30-vxCUSTOM")
        self.client.start()
        
        
        
        
    async def start(self):
        await self.client.start()

    async def get_args(self, msg):
        try:
            args = msg.message.message.split(maxsplit=1)[1]
            return args
        except IndexError:
            return None
    
    async def watcher(self, client, msg):
        if state is True:
            global user_list
            user_id = msg.sender_id
            if user_id not in user_list:
                if msg.is_private:
                    user_list.append(user_id)
                    time_now = datetime.now()
                    timing = time_now - start
                    time_string = str(timing)
                    time_result = time_string.split('.')[0]
                    await msg.reply(
                        "я в AFK режиmе <code>{}</code>\nпричина: <code>{}</code>".format(time_result, reason),
                        file=afk_photo,
                        parse_mode='html'
                    )
                else:
                    pass
        
        user_id = msg.sender_id
        if user_id in autoreply_list:
            if user_id not in last_reply_time or time.time() - last_reply_time[user_id] >= autoreply_time[user_id]:
                last_reply_time[user_id] = time.time()
                await sleep(autoreply_time[user_id])
                if autoreply_shpk.get(user_id, ''):
                    await msg.reply(
                        autoreply_shpk[user_id] + " " + choice(shablon),
                        file=autoreply_photo[user_id]
                    )
                else:
                    await msg.reply(
                        choice(shablon),
                        file=autoreply_photo[user_id]
                    )
            else:
                pass
        else:
            pass
        

    async def afk_handler(self, client, msg):  
        try:
            global state, user_list, start, reason, afk_photo
            me = await self.client.get_me()  
            if msg.sender_id == me.id:  
                args = msg.text.split()[1:] 
                if not args:  
                    if state:  
                        status = "включен" 
                    else:  
                        status = "выключен" 
                    if afk_photo:  
                        media = f"установлено медиа: <code>{afk_photo}</code>" 
                    else:  
                        media = "медиа не было установлено" 
                    return await msg.edit(f"статус афк: <code>{status}</code>\n{media}\nпричина нахождения в АФК: <code>{reason}</code>", parse_mode='html')  
            
                if args[0] == '1':  
                    state = True  
                    start = datetime.now()
                    me = await self.client.get_me()  
                    user_list.append(
                        int(
                            me.id
                        )
                    )
                    return await msg.edit("<b>afk включен.</b>", parse_mode='html')  
                    b
            
                elif args[0] == '2':  
                    state = False  
                    start = 10  
                    user_list = []  
                    return await msg.edit("<b>афк выключен</b>", parse_mode='html')  
            
                elif 'https' in args[0]:   
                    afk_photo = args[0]   
                    return await msg.edit("<b>фото для афк успешно было изменено</b>", parse_mode='html')   
                     
                reason = ' '.join(args[0:])   
                return await msg.edit(f'причина нахождения в АФК изменина на: <code>{reason}</code>', parse_mode='html')   
        
            async def reason(msg): 
                try: 
                    global reason 
                    args = msg.text.split()[1:] 
                    if not args: 
                        return await msg.edit("причина нахождения в АФК: <code>{}</code>".format(reason), parse_mode='html') 
        
                    reason = ' '.join(args) 
                    await msg.edit('причина нахождения в АФК изменена на: <code>{}</code>'.format(reason), parse_mode='html') 
        
                except Exception as e: 
                    print(e) 
        
            async def set_photo(msg): 
                try: 
                    global afk_photo 
                    args = msg.text.split()[1:] 
                    if not args: 
                        return await msg.edit("<b>укажи аргумент <code>сыллка на медиа</code></b>", parse_mode='html') 
        
                    afk_photo = args[0] 
                    await msg.edit("<b>фото для афк установлено</b>", parse_mode='html') 
        
                except Exception as e: 
                    print(e)

        except Exception as e: 
            print(e)


    async def kalendar_handler(self, client, msg):
        try:
            reply = await msg.get_reply_message()
            args = await self.get_args(msg)
            if args is None:
                return await msg.edit(
                    "<b>ты ввел команду без аргументов.\nиспользуй znr {time} {media}.</b>",
                    parse_mode='html'
                )
            time = int(args.split()[0])
            photo = str(args.split()[1])
            shapka = ' '.join(args.split()[2:])
            reply_id = None
            chat_id = msg.chat_id
            if not reply and 'https' not in photo:
                photo = None
            elif not reply and 'https' in photo:
                reply_id = None
            elif reply and 'https' not in photo:
                reply_id = reply.id
                photo = None
            elif reply and 'https' in photo:
                reply_id = reply.id

            orig_time = time
            await msg.edit(
                "{} {}".format(shapka, choice(shablon)),
                parse_mode='html'
            )
            for i in range(99):
                schedule_date = datetime.now() + timedelta(minutes=time)
                await msg.respond(
                    f"{shapka} {choice(shablon)}",
                    file=photo,
                    reply_to=reply_id,
                    schedule=schedule_date.timestamp()
                )
                time += orig_time
                await sleep(0)

            last_schedule_date = datetime.now() + timedelta(minutes=time)
            await msg.respond(
                f"{msg.text}",
                file=photo,
                reply_to=reply_id,
                schedule=last_schedule_date.timestamp()
            )
        except Exception as e:
            print(e)


    async def renewal_handler(self, client, msg):
        try:
            global spam_state
            args = await self.get_args(msg)
            if args is None:
                return await msg.edit("<b>аргументы не указаны</b>", parse_mode='html')
    
            reply = await msg.get_reply_message()
            chat_id = msg.chat_id
            time = int(args.split()[0])
    
            if time < 3:
                return await msg.edit("<b>задержка слuшкоm малеnькая, мuнuмальnое значеnuе - 3</b>", parse_mode='html')
    
            photo = str(args.split()[1]) if len(args.split()) > 1 else None
            shapka = ' '.join(args.split()[2:]) if len(args.split()) > 2 else ''
            spam_state[chat_id] = True
            await msg.edit('<b>включен\nчтобы выключить пиши <code>.стоп {}</code></b>'.format(chat_id), parse_mode='html')
    
            if chat_id in spam_state and spam_state[chat_id] is True:
                while True:
                    if chat_id not in spam_state or not spam_state[chat_id]:
                        del spam_state[chat_id]
                        break
                    if chat_id in spam_state:
                        if reply:
                            if photo:
                                try:
                                    await msg.respond(shapka + " " + choice(shablon), file=photo, reply_to=reply.id)
                                except Exception as e:
                                    await msg.respond(shapka + " " + choice(shablon), reply_to=reply.id)
                            else:
                                await msg.respond(shapka + " " + choice(shablon), reply_to=reply.id)
                        else:
                            if photo:
                                try:
                                    await msg.respond(shapka + " " + choice(shablon), file=photo)
                                except Exception as e:
                                    await msg.respond(shapka + " " + choice(shablon))
                            else:
                                await msg.respond(shapka + " " + choice(shablon))
                    
                    await asyncio.sleep(time)
        except Exception as e:
            print(e)


    async def spam_handler(self, client, msg): 
        try: 
            global spam_state1 
            args = msg.message.message.split(maxsplit=1) 
            if args is None:  
                return await msg.edit("<b>укажи аргументы</b>",  
                    parse_mode='html') 
            chat_id = int(args[1].split()[0]) 
            time = int(args[1].split()[1]) 
            if time < 3: 
                return await msg.edit( 
                    "<b>задержка слишком маленькая, минимальное значение - 3</b>", 
                    parse_mode='html' 
                ) 
                
            if len(args) < 2: 
                return await msg.edit(  
                    "<b>недостаточно аргументов</b>",  
                    parse_mode='html'  
                )  
                
            photo = args[1].split()[2] if len(args[1].split()) > 2 and 'https' in args[1].split()[2] else None 
            shapka = ' '.join(args[1].split()[3:]) if len(args[1].split()) > 3 else ''
            
            spam_state1[chat_id] = True 
            await msg.edit( 
                '<b>включил в чате {}\nчтобы выключить zstop <code>.rstop {}</code></b>'.format(chat_id, chat_id), 
                parse_mode='html' 
            ) 
            if spam_state1.get(chat_id) is True: 
                while True: 
                    if spam_state1.get(chat_id) is False: 
                        del spam_state1[chat_id] 
                        break 
                    if chat_id in spam_state1: 
                        if photo: 
                            await self.client.send_file( 
                                chat_id, 
                                file=photo, 
                                caption=shapka + " " + choice(shablon) 
                            ) 
                        else: 
                            await self.client.send_message(chat_id, shapka + " " + choice(shablon)) 
                    await sleep(time) 
        except Exception as e: 
            print(e)


    async def autoreply_handler(self, client, msg):
        try:
            global autoreply_photo, autoreply_list, autoreply_time, autoreply_shpk
            args = msg.message.message.split(maxsplit=0)[0]
            
            if str(args.split()[0]) == '.нт':
                if msg.is_reply:
                    user_id = (await msg.get_reply_message()).sender_id
                    autoreply_list.append(user_id)
                    autoreply_shpk[user_id] = ' '.join(args.split()[1:]) 
                    autoreply_time[user_id] = 1
                    autoreply_photo[user_id] = None
                    await msg.edit(
                        '<b>включил<code>{}</code>\nчтобы выключить <code>.нтт </code></b>'.format(user_id),
                        parse_mode='html'
                    )
                else:
                    user_id = int(args.split()[1])
                    autoreply_list.append(user_id)
                    autoreply_time[user_id] = int(args.split()[2])
                    autoreply_photo[user_id] = str(args.split()[3]) if 'https' in args.split()[3] else None
                    autoreply_shpk[user_id] = ' '.join(args.split()[4:]) 
                    await msg.edit(
                        '<b>включил\nчтобы off <code>.нтт {}</code></b>'.format(user_id),
                        parse_mode='html'
                    )
        
            elif str(args.split()[0]) == '.нтт':
                if msg.is_reply:
                    reply_msg = await msg.get_reply_message() 
                    user_id = reply_msg.sender_id 
                    if user_id in autoreply_list:
                        autoreply_list.remove(user_id)
                        del autoreply_time[user_id]
                        del autoreply_photo[user_id]
                        await msg.edit(
                            f'<b>автоответчик выключен на пользователя <code>{user_id}</code></b>',
                            parse_mode='html'
                        )
                    else:
                        await msg.edit('<b>пользователь<code>{}</code> не был обнаружен</b>'.format(user_id), parse_mode='html')
                else:
                    args = msg.message.message
                    if args.startswith('.нтт'):
                        if len(args.split()) > 1:
                            user_id = int(args.split()[1])
                            autoreply_list.remove(user_id)
                            del autoreply_time[user_id]
                            del autoreply_photo[user_id]
                            await msg.edit(
                                f'<b>автоответчик был выключен на пользователя <code>{user_id}</code></b>',
                                parse_mode='html'
                            )
                            del autoreply_shpk[user_id]
        
            elif str(args.split()[0]) == '.setshpk':
                user_id = int(args.split()[1])
                if user_id in autoreply_list:
                    autoreply_shpk[user_id] = ' '.join(args.split()[2:])
                else:
                    autoreply_shpk[user_id] = ' '.join(args.split()[2:])
                await msg.edit('<b>установлена шапка<code>{}</code> для пользователя с айди<code>{}</code>'.format(autoreply_shpk[user_id], user_id), parse_mode='html')

        except KeyError as e: 
            print(f"KeyError occurred: {e}")
        
        except ValueError as e:
            print(f"ValueError occurred: {e}")



    async def kalend_handler(self, event, msg):       
        try:    
            args = await self.get_args(msg)  
            chat_id = int(args.split()[0])   
            time = int(args.split()[1])  
            photo = str(args.split()[2]) if len(args) > 2 else None   
            shapka = ' '.join(args.split()[3:])  
            orig_time = time 
            if 'https' not in photo:
                photo = None
            await msg.edit(  
                "{} {}".format(shapka, choice(shablon)),  
                parse_mode='html'  
            )  
            for i in range(100):       
                schedule_date = datetime.now() + timedelta(minutes=time)     
                if photo is not None:  
                    await self.client.send_file(chat_id, photo, caption=shapka+" "+choice(shablon), schedule=schedule_date.timestamp())
                    time += orig_time 
                    await sleep(0) 
                else:   
                    await self.client.send_message(chat_id, shapka+" "+choice(shablon), schedule=schedule_date.timestamp())
                    time += orig_time 
                    await sleep(0) 
            for i in range(1): 
                schedule_date = datetime.now() + timedelta(minutes=time)   
                await msg.respond( 
                    f"{msg.text}", 
                    file=photo, 
                    schedule=schedule_date.timestamp()
                ) 
        except Exception as e:       
            print(e)



    async def rchange_handler(self, client, msg):
        try:
            global autoreply_photo, autoreply_list, autoreply_time, autoreply_shpk
            args = msg.message.message.split(maxsplit=0)[0]
            
            if str(args.split()[0]) == '.rchange':
                action = str(args.split()[1])
                user_id = int(args.split()[2])
    
                if action == 'shapka':
                    autoreply_shpk[user_id] = ' '.join(args.split()[3:])
                    await msg.edit(
                        f'<b>шапка для поользователя {user_id} изменена</b>',
                        parse_mode='html'
                    )
    
                elif action == 'media':
                    autoreply_photo[user_id] = str(args.split()[3]) if 'https' in args.split()[3] else None
                    await msg.edit(
                        f'<b>медиа для пользователя {user_id} изменена на: {autoreply_photo[user_id]}</b>',
                        parse_mode='html'
                    )
    
                elif action == 'time':
                    autoreply_time[user_id] = int(args.split()[3])
                    await msg.edit(
                        f'<b>задержка для пользователя {user_id} изменена на: {autoreply_time[user_id]} секунд</b>',
                        parse_mode='html'
                    )
    
        except KeyError as e:
            print(f"KeyError occurred: {e}")
    
        except ValueError as e:
            print(f"ValueError occurred: {e}")


    def run(self):
        @self.client.on(events.NewMessage(pattern=r'\.клдд')) 
        async def kalend_handler_event(msg): 
            me = await self.client.get_me() 
            if msg.sender_id == me.id: 
                await self.kalend_handler(self.client, msg)
        
        @self.client.on(events.NewMessage(pattern=r'\.афк'))  
        async def afk_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.afk_handler(self.client, msg)

        @self.client.on(events.NewMessage(pattern=r'\.спам'))
        async def renewalspam_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.renewal_handler(self.client, msg)
                
        @self.client.on(events.NewMessage(pattern=r'\.ыыы'))
        async def spam_rhandler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.spam_handler(self.client, msg)
            

        @self.client.on(events.NewMessage(pattern=r'\.клд'))
        async def kalendar_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.kalendar_handler(self.client, msg)

        @self.client.on(events.NewMessage(pattern=r'\.нт|.нтт|.setshpk'))
        async def autoreply_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.autoreply_handler(self.client, msg)

        @self.client.on(events.NewMessage(pattern=r'\.rchange'))
        async def rchange_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                await self.rchange_handler(self.client, msg)

        @self.client.on(events.NewMessage(pattern=r'.стоп'))
        async def stop_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                global spam_state
                args = await self.get_args(msg)
                if args:
                    chat_id = int(args.split()[0])
                else:
                    chat_id = msg.chat_id
                if chat_id in spam_state:
                    spam_state[chat_id] = False
                    del spam_state[chat_id]
                    await msg.edit(
                        "<b>остановлено в чате<code>{}</code></b>".format(chat_id),
                        parse_mode='html'
                    )
                else:
                    await msg.edit(
                        "<b>чат с айди<code>{}</code> не был найден</b>".format(chat_id),
                        parse_mode='html'
                    )


        @self.client.on(events.NewMessage(pattern=r'\.офф'))
        async def off_handler(msg): 
            me = await self.client.get_me() 
            if msg.sender_id == me.id: 
                global tagger_chats 
                args = await self.get_args(msg) 
                if args:
                    chat_id = int(args.split()[0]) 
                else:
                    chat_id = msg.chat_id
                if chat_id in tagger_chats: 
                    del tagger_chats[chat_id] 
                    await msg.edit( 
                        "<b>остановлено в чате<code>{}</code></b>".format(chat_id), 
                        parse_mode='html' 
                    ) 
                else: 
                    await msg.edit( 
                        "<b>чат с айди<code>{}</code> не был обнаружен</b>".format(chat_id), 
                        parse_mode='html' 
                    )
        
        @self.client.on(events.NewMessage(pattern=r'\.zstop')) 
        async def stop_handler(msg): 
            me = await self.client.get_me() 
            if msg.sender_id == me.id: 
                global spam_state1 
                args = await self.get_args(msg) 
                if args:
                    chat_id = int(args.split()[0]) 
                else:
                    chat_id = msg.chat_id
                if chat_id in spam_state1: 
                    del spam_state1[chat_id] 
                    await msg.edit( 
                        "<b>остановлено в чате <code>{}</code></b>".format(chat_id), 
                        parse_mode='html' 
                    ) 
                else: 
                    await msg.edit( 
                        "<b>чат с айди <code>{}</code> не был обнаружен</b>".format(chat_id), 
                        parse_mode='html' 
                    )


        @self.client.on(events.NewMessage(pattern='\.меню'))      
        async def command_menu_commands(event):      
            me = await self.client.get_me()      
            msg = event.message     
            if msg.sender_id == me.id:      
                chat_id = event.chat_id      
                args = await self.get_args(event)     
                if len(event.raw_text.split()) > 1:   
                    args = event.raw_text.split(maxsplit=1)[1]   
                    global mm
                    if args.lower() == "None":   
                        mm = None   
                    else:   
                        mm = args   
                    await event.edit("<b>медиа установлено</b>", parse_mode='html')   
                    return   
                reply_msg = await msg.get_reply_message()        
                if reply_msg:  
                    reply_to = reply_msg.id      
                    try:
                        await self.client.send_file(chat_id, mm, caption=menu, reply_to=reply_to, parse_mode='html')
                        await msg.delete()
                    except:
                        await event.edit(menu, parse_mode='html')
                else:  
                    if mm is not None:
                        try:
                            await self.client.send_file(chat_id, mm, caption=menu, parse_mode='html')
                            await msg.delete()
                        except:
                            await event.edit(menu, parse_mode='html')
                    else:
                        await event.edit(menu, parse_mode='html')

        @self.client.on(events.NewMessage(pattern=r'\.айди')) 
        async def id_handler(event): 
            global mid   
            me = await self.client.get_me() 
            msg = event.message 
            if msg.sender_id == me.id: 
                try: 
                    if msg.is_reply: 
                        reply_msg = await msg.get_reply_message() 
                        user_id = reply_msg.sender_id 
                        reply_id = reply_msg.id 
                        reply_to = reply_msg.id 
                        reply_msg.id = None 
                        caption = '<b>user id: <code>{}</code></b>'.format(user_id) 
                    elif len(msg.text.split()) > 1 and msg.text.split()[1].startswith('@'):  
                        entity = await self.client.get_entity(msg.text.split()[1])  
                        user_id = entity.id  
                        caption = '<b>user id: <code>{}</code></b>'.format(user_id)  
                    elif len(msg.text.split()) > 1 and msg.text.split()[1].startswith('t.me/'):  
                        entity = await self.client.get_entity(msg.text.split()[1])  
                        chat_id = entity.id
                        caption = '<b>chat id: <code>-100{}</code></b>'.format(chat_id)  
                    elif len(msg.text.split()) > 1 and msg.text.split()[1].startswith('https://t.me/'):  
                        entity = await self.client.get_entity(msg.text.split()[1])  
                        chat_id = entity.id
                        caption = '<b>chat id: <code>-100{}</code></b>'.format(chat_id)  
                    else:  
                        chat_id = msg.chat_id  
                        caption = '<b>chat id: <code>{}</code></b>'.format(chat_id)  
        
                    if msg.is_reply: 
                        if mid is not None:   
                            try: 
                                await self.client.send_file( 
                                    msg.chat_id, 
                                    file=mid, 
                                    caption=caption, 
                                    reply_to=reply_to, 
                                    parse_mode='html' 
                                ) 
                                await self.client.delete_messages(msg.chat_id, msg.id) 
                            except: 
                                sent_msg = await self.client.edit_message( 
                                    msg.chat_id, 
                                    msg.id, 
                                    text=caption, 
                                    parse_mode='html' 
                                ) 
                        else: 
                            sent_msg = await self.client.edit_message( 
                                msg.chat_id, 
                                msg.id, 
                                text=caption, 
                                parse_mode='html' 
                            ) 
                    elif len(msg.text.split()) > 1 and not any(link in msg.text.split()[1] for link in ['@', 'https://t.me/', 't.me/']):  
                        mid = msg.text.split()[1]   
                        await self.client.edit_message(  
                            msg.chat_id,  
                            msg.id,  
                            text="<b>медиа установлено</b>",  
                            parse_mode='html'  
                        )
                        return 
                    if mid is not None and not msg.is_reply:   
                        await self.client.send_file(                
                            msg.chat_id,                
                            file=mid,              
                            caption=caption,             
                            parse_mode='html'                
                        )          
                        await self.client.delete_messages(msg.chat_id, msg.id)          
                    else:   
                        sent_msg = await self.client.edit_message( 
                            msg.chat_id,            
                            msg.id,           
                            text=caption,        
                            parse_mode='html'        
                        )   
                except Exception as e:   
                    sent_msg = await self.client.edit_message(
                        msg.chat_id,            
                        msg.id,           
                        text=caption,
                        parse_mode='html'        
                    )



        @self.client.on(events.NewMessage(pattern=r'\.contacts'))  
        async def add_contacts(event):  
            chat = await event.get_chat()  
            async for user in self.client.iter_participants(chat, aggressive=True, search=""):  
                if user.phone:
                    contact = InputPhoneContact(client_id=user.id, phone=user.phone, first_name=f"user", last_name=str(user.id))  
                    await self.client(ImportContactsRequest([contact]))
                    await asyncio.sleep(1) 

        @self.client.on(events.NewMessage(pattern=r'\.аптайм'))    
        async def times(msg): 
            me = await self.client.get_me()    
            if msg.sender_id == me.id:    
                bot_runtime = int(time.time() - start_time) 
                bot_runtime_formatted = str(timedelta(seconds=bot_runtime))
                try:
                    pc_runtime = int(time.time() - psutil.boot_time()) 
                    pc_runtime_formatted = str(timedelta(seconds=pc_runtime)) 
                    await msg.edit( 
                        f'\nаптайм бота: <code>{bot_runtime_formatted}</code>' 
                        f'\nаптайм ПК: <code>{pc_runtime_formatted}</code>', parse_mode='html')  
                except:
                    await msg.edit(
                        f'\nаптайм бота: <code>{bot_runtime_formatted}</code>', parse_mode='html')  

        @self.client.on(events.NewMessage(pattern=r'\.теггер'))
        async def tagger_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                text = msg.message.message.split(maxsplit=1)[1]
                args = text.split()
                if args is None: 
                    return await msg.edit("<b>аргументы не указаны</b>", 
                    parse_mode='html')
                chat_id = msg.chat_id
                user_id = int(args[0])
                time_sleep = int(args[1])
                
                if time_sleep <= 2:
                    return await msg.edit("<b>задержка слишком маленькая, минимальное значение - 3</b>", parse_mode='html')
                
                photo = args[2] if len(args) > 2 and 'https' in args[2] else None
                caption = ' '.join(args[3:]) if len(args) > 3 else ''
                reply_to_msg = await msg.get_reply_message()
                if reply_to_msg:
                    chat_id = reply_to_msg.chat_id
                
                await msg.edit('<b>включил\nчтобы выключить пиши <code>.офф {}</code></b>'.format(chat_id), parse_mode='html')
                
                tagger_chats[chat_id] = True
                while chat_id in tagger_chats:
                    if photo:
                        await self.client.send_file(
                            chat_id,
                            file=photo,
                            caption=f"{caption} <a href='tg://user?id={user_id}'>{choice(shablon)}</a>",
                            parse_mode='html',
                            reply_to=reply_to_msg.id if reply_to_msg else None
                        )
                        await sleep(int(time_sleep))
                    else:
                        await self.client.send_message(
                            chat_id,
                            f"{caption} <a href='tg://user?id={user_id}'>{choice(shablon)}</a>",
                            parse_mode='html',
                            reply_to=reply_to_msg.id if reply_to_msg else None
                        )
                        await sleep(int(time_sleep))
        
        @self.client.on(events.NewMessage(pattern=r'\.тег'))
        async def tag_handler(msg):
            me = await self.client.get_me()
            if msg.sender_id == me.id:
                text = msg.message.message.split(maxsplit=1)[1]
                args = text.split()
                if args is None: 
                    return await msg.edit("<b>аргументы не указаны</b>", 
                    parse_mode='html')
                
                chat_id = int(args[0])
                user_id = int(args[1])
                time_sleep = int(args[2])
                
                if time_sleep < 3:
                    return await msg.edit("<b>задержка слишком маленькая, минимальное значение - 3</b>", parse_mode='html')
                
                photo = args[3] if 'https' in args[3] else None
                caption = ' '.join(args[4:]) if len(args) > 4 else ''
                
                await msg.edit('<b>включил\nчтобы выключить пиши <code>.тегофф {}</code></b>'.format(chat_id), parse_mode='html')
                
                tag_chats[chat_id] = True
                while chat_id in tag_chats:
                    if photo:
                        await self.client.send_file(
                            chat_id,
                            file=photo,
                            caption=f"{caption} <a href='tg://user?id={user_id}'>{choice(shablon)}</a>",
                            parse_mode='html'
                        )
                        await sleep(int(time_sleep))
                    else:
                        await self.client.send_message(
                            chat_id,
                            f"{caption} <a href='tg://user?id={user_id}'>{choice(shablon)}</a>",
                            parse_mode='html'
                        )
                        await sleep(int(time_sleep))


        @self.client.on(events.NewMessage(pattern=r'\.тегофф')) 
        async def off_handler(msg): 
            me = await self.client.get_me() 
            if msg.sender_id == me.id: 
                global tag_chats 
                args = await self.get_args(msg) 
                if args:
                    chat_id = int(args.split()[0]) 
                else:
                    chat_id = msg.chat_id
                if chat_id in tag_chats: 
                    del tag_chats[chat_id] 
                    await msg.edit( 
                        "<b>остановлено в чате <code>{}</code></b>".format(chat_id), 
                        parse_mode='html' 
                    ) 
                else: 
                    await msg.edit( 
                        "<b>чат с айди <code>{}</code> не был обнаружен</b>".format(chat_id), 
                        parse_mode='html' 
                    )


        @self.client.on(events.NewMessage(pattern=r'\.лз'))
        async def clear_autoreply_list_handler(event):
            me = await self.client.get_me()
            msg = event.message
            if msg.sender_id == me.id:  
                autoreply_list.clear()
                autoreply_time.clear()
                autoreply_photo.clear()
                autoreply_shpk.clear()
                await msg.edit("успешно очищено")
            else:
                pass


        @self.client.on(events.NewMessage(pattern=r'\.с_флуд'))
        async def clear_autoreply_list_handler(event):
            me = await self.client.get_me()
            msg = event.message
            if msg.sender_id == me.id:  
                spam_state.clear()
                spam_state1.clear()
                tag_chats.clear()
                tagger_chats.clear()
                await msg.edit("все флудилки были оффнуты")
            else:
                pass
    

        @self.client.on(events.NewMessage(pattern=r'\.лист'))
        async def show_lists_handler(event):
            me = await self.client.get_me()
            if event.sender_id == me.id:
                args = event.raw_text.split(' ')
                if len(event.raw_text.split()) > 1:   
                    args = event.raw_text.split(maxsplit=1)[1]   
                    global mlist
                    if args.lower() == "None":   
                        mlist = None   
                    else:   
                        mlist = args   
                    await event.edit("<b>медиа изменено</b>", parse_mode='html')   
                    return   
                else:
                    reply_to = None
                    reply_msg = await event.get_reply_message()
                    if reply_msg:
                        reply_to = reply_msg.id
                    response = "чаты в которых работает rayzen:\n"
                    response += str(spam_state) + "\n\n"
                    response += "чаты в которых работает  спам:\n"
                    response += str(spam_state1) + "\n\n"
                    response += "пользователи на которых работает нт:\n"
                    response += str(autoreply_list) + "\n\n"
                    response += "чаты в которых работает теггер:\n"
                    response += str(tagger_chats) + "\n\n"
                    response += "чаты в которых работает тег:\n"
                    response += str(tag_chats) 
                try:
                    await event.respond(response, file=mlist, reply_to=reply_to)
                    await event.delete()
                except:
                    await event.edit(response)
            else:
                if mlist is not None:
                    await event.edit(response, file=mlist)
                    await event.delete()
                else:
                    await event.edit(response)


        @self.client.on(events.NewMessage(pattern=r'\.пинг'))
        async def ping_handler(msg):
            me = await self.client.get_me() 
            if msg.sender_id == me.id: 
                ping_now = time.perf_counter_ns()
                await msg.edit(
                    '<b>пинг бот: <code>{}</code> ms</b>'.format(round((time.perf_counter_ns() - ping_now) / 10**2, 2)),
                    parse_mode='html')


        @self.client.on(events.NewMessage(pattern='\.хелп'))      
        async def command_help_commands(event):      
            me = await self.client.get_me()      
            msg = event.message     
            namee = name 
            if msg.sender_id == me.id:      
                chat_id = event.chat_id      
                args = await self.get_args(event)     
                if len(event.raw_text.split()) > 1:   
                    args = event.raw_text.split(maxsplit=1)[1]   
                    global mh   
                    if args.lower() == "None":   
                        mh = None   
                    else:   
                        mh = args   
                    await event.edit("<b>медиа установлено</b>", parse_mode='html')   
                    return   
                reply_msg = await msg.get_reply_message()        
                if reply_msg:  
                    reply_to = reply_msg.id      
                    try:
                        await self.client.send_file(chat_id, mh, caption=menutext.format(namee, chat_id, me.id, me.first_name, me.username), reply_to=reply_to, parse_mode='html')  
                        await msg.delete()
                    except:
                        await event.edit(menutext.format(namee, chat_id, me.id, me.first_name, me.username), parse_mode='html')
                else:  
                    if mh is not None:
                        try:
                            await self.client.send_file(chat_id, mh, caption=menutext.format(namee, chat_id, me.id, me.first_name, me.username), parse_mode='html')
                            await msg.delete()
                        except:
                            await event.edit(menutext.format(namee, chat_id, me.id, me.first_name, me.username), parse_mode='html')
                    else:
                        await event.edit(menutext.format(namee, chat_id, me.id, me.first_name, me.username), parse_mode='html')



        async def upload_to_imgur_http(file_path): 
            url = 'https://t.me/bb_imgur_bot' 
            files = {'file': open(file_path, 'rb')} 
        
            try: 
                response = requests.post(url, files=files) 
                if response.status_code == 200:
                    os.remove(file_path) 
                    return response.text   
                else: 
                    return f"ошибка загрузки: {response.status_code} {response.reason}" 
            except Exception as e: 
                return str(e) 
        
        
        @self.client.on(events.NewMessage(pattern='\.медиа'))
        async def handle_imgur_command(event):
            me = await self.client.get_me()
            msg = event.message
        
            if msg.sender_id == me.id:
                if event.is_reply:
                    reply_msg = await event.get_reply_message()
                    if reply_msg.media:
                        await event.edit("<b>начинаю загружать данное медиа:</b>", parse_mode='html')
                        media = reply_msg.media
                        file = await self.client.download_media(media)
                        imgur_link = await upload_to_imgur_http(file)
                        reply_id = reply_msg.id
                        try:
                            await event.client.send_file(event.chat_id, media, caption=f"<code>{imgur_link}</code>", reply_to=reply_id, parse_mode='html')
                            await event.delete()
                        except Exception as e:
                            await event.edit(f"<code>{picloud_link}</code>", parse_mode='html')
                    else:
                        await event.edit("<b>ошибка: сообщение не имеет медиа файл</b>", parse_mode='html')
                else:
                    await event.edit("<b>ошибка: нужен реплай</b>", parse_mode='html')


    

        @self.client.on(events.NewMessage(pattern=r'\.слова'))  
        async def count_handler(msg):  
            if msg.is_reply:  
                try: 
                    reply_msg = await msg.get_reply_message()
                    words = reply_msg.message.split()  
                    total_words = len(words)  
                    total_chars = len(reply_msg.message)  
                    total_lines = reply_msg.message.count('\n') + 1  
                    result_message = (  
                        f"<b>результат:</b>\n"  
                        f"количество слов: {total_words}\n"  
                        f"количество символов: {total_chars}\n"  
                        f"количество строк: {total_lines}"  
                    )  
                    await msg.edit(result_message, parse_mode='html') 
                except Exception as e: 
                    print(e)

        @self.client.on(events.NewMessage(pattern=r'\.сменить'))  
        async def change_handler(msg):  
            me = await self.client.get_me()  
            if msg.sender_id == me.id:  
                if msg.is_reply:  
                    reply_msg = await msg.get_reply_message()  
                    if reply_msg.file:  
                        try:  
                            file = await reply_msg.download_media()  
                            with open(file, 'r', encoding='utf-8') as f:  
                                lines = f.readlines()  
                                shablon.clear()  
                                for line in lines:  
                                    shablon.append(line.strip())  
                            os.remove(file) 
                            await msg.edit("шаблоны изменены") 
                        except Exception as e: 
                            print(f"Помилка: {e}") 
                            await msg.delete() 
                        finally:
                            os.remove(file)
                    else: 
                        await msg.edit("нужен реплай на файл") 
                else: 
                    await msg.edit("укажи реплай на файл") 
                    
                    
        @self.client.on(events.NewMessage(pattern=r'\.основа'))  
        async def file_handler(msg):  
            me = await self.client.get_me()  
            if msg.sender_id == me.id:  
                try:  
                    with open('texts.txt', 'w', encoding='utf-8') as f:  
                        for line in shablon:  
                            f.write(line + '\n')  
                    await self.client.send_file(msg.chat_id, 'texts.txt') 
                    os.remove('texts.txt') 
                    await msg.delete()
                except Exception as e: 
                    print(f"ошибка: {e}") 

        @self.client.on(events.NewMessage(pattern=r'\.name'))
        async def name_handler(msg):
            me = await self.client.get_me()  
            if msg.sender_id == me.id:  
                text = msg.message.message.split(maxsplit=1)[1]
                global name
                name = str(text)
                await msg.edit('<b>имя бота изменено {}</b>'.format(text), parse_mode='html')


        @self.client.on(events.NewMessage(pattern=r'\.зайти'))    
        async def join_handler(event):    
            me = await self.client.get_me()    
            if event.sender_id == me.id:    
                args = await self.get_args(event) 
                if args:
                    chat_link = args.split()[0]   
                    chat_entity = await self.client.get_entity(chat_link)  
                    await self.client(JoinChannelRequest(chat_entity))  
                else:
                    await event.edit("нужна ссылка")
                          
                          
        @self.client.on(events.NewMessage(pattern=r'\.выйти'))    
        async def leave_handler(event):    
            me = await self.client.get_me()    
            if event.sender_id == me.id:    
                args = await self.get_args(event) 
                if args:
                    chat_link = args.split()[0]  
                    chat_entity = await self.client.get_entity(chat_link)  
                    await self.client(LeaveChannelRequest(chat_entity)) 
                else:
                    chat_id = event.to_id.chat_id
                    await self.client(LeaveChannelRequest(chat_id))



        @self.client.on(events.NewMessage())
        async def watcher_handler(msg):
            await self.watcher(self.client, msg)
            


    def start(self):
        self.client.run_until_disconnected()



if __name__ == "__main__":
    bot = Userbot()
    bot.run()
    bot.start()
    client.run()


