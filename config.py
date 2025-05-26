#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "22272180"))
    API_HASH = os.environ.get("API_HASH", "c1ca68108649edb2fb0b1e78fe03e780")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5096393058")
