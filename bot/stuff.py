#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🔥Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A Bot  Which Can Encode Videos.\nReduce Size of Videos in 480p or 720p As The Case May Be\nU can Generate Samples/screenshots too.",
        buttons=[
            [
                Button.url(
                    "Repo (Source Code)",
                    url="https://github.com/Rick-and-Roll/Light-Queue",
                )
            ],
            [Button.url("📢 AD", url="t.me/RsTvMarvel")],
            [
                Button.url("Channel", url="t.me/RS_Community"),
                Button.url("Maintainer", url="t.me/itsjust_r"),
            ],
        ],
    )
