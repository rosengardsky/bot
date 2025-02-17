# Name: RequimSpam
# Author: разрушая мечты
# Commands:
# .rspam
# .rstop
# scope: hikka_only
# meta developer: @requimforadreaml

import asyncio
from .. import loader, utils
from telethon.tl.types import Message  # type: ignore

@loader.tds
class RequimSpamMod(loader.Module):
    """Module for mailing messages"""

    strings = {
        "name": "RequimSpam",
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>Рассылка успешно завершена, все сообщения были доставлены.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Ошибка! Неправильно введено значение конфига или его не существует.",
        "cfg_group_id": "Введите индификатор группы в формате ChatID, ChatID",
        "cfg_custom_text": "Введите кастомный текст для рассылки",
        "cfg_photo_url": "Введите ссылку для отправки медиа с текстом.",
        "cfg_message_count": "Введите количество сообщений для рассылки (1-100)",
        "cfg_delay_minutes": "Введите задержку между сообщениями в минутах (1-60)"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "group_id",
                None,
                lambda: self.strings["cfg_group_id"],
                validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("[0-9]"),
                    ),
                ),
            ),
            loader.ConfigValue(
                "custom_text",
                "Это тестовое сообщение.",
                lambda: self.strings["cfg_custom_text"],
            ),
            loader.ConfigValue(
                "photo_url",
                None,
                lambda: self.strings["cfg_photo_url"],
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "message_count",
                1,
                lambda: self.strings["cfg_message_count"],
            ),
            loader.ConfigValue(
                "delay_minutes",
                1,
                lambda: self.strings["cfg_delay_minutes"],
            ),
        )
        self.spamming = False  # Флаг для отслеживания статуса рассылки

    @loader.command(
        ru_doc="Начать рассылку сообщений.",
    )
    async def rspam(self, message: Message):
        """Start sending messages."""
        self.spamming = True  # Установить флаг спама в True
        ccid = self.config["group_id"]
        text = self.config["custom_text"]
        photo = self.config["photo_url"]
        message_count = self.config["message_count"]
        delay_minutes = self.config["delay_minutes"]

        # Проверка на корректность количества сообщений
        if not (1 <= message_count <= 100):
            await utils.answer(message, "Количество сообщений должно быть от 1 до 100.")
            return

        # Проверка на корректность задержки
        if not (1 <= delay_minutes <= 60):
            await utils.answer(message, "Задержка должна быть от 1 до 60 минут.")
            return

        if ccid is None or ccid == []:
            await utils.answer(message, self.strings["error_cfg_group_id"])
            return

        for i in ccid:
            for j in range(message_count):
                if not self.spamming:  # Проверка флага перед отправкой
                    await utils.answer(message, "Рассылка остановлена.")
                    return
                
                if photo is None:
                    await self.client.send_message(i, text)
                else:
                    await self.client.send_file(i, photo, caption=text)
                    
                await asyncio.sleep(delay_minutes * 60)  # Задержка в секундах (минуты в секунды)

        await utils.answer(message, self.strings["successfully_spam"])

    @loader.command(
        ru_doc="Остановить рассылку сообщений.",
    )
    async def rstop(self, message: Message):
        """Stop sending messages."""
        self.spamming = False  # Установить флаг спама в False
        await utils.answer(message, "Рассылка остановлена.")
