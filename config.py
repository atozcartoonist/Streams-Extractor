#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6198560504:AAFqL7kPGgGj0EBFENyONR0Dsk5gOZHhG-Q")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "8755370"))
    API_HASH = os.environ.get("API_HASH", "54261233493bbc5bbf489146dd2909dc")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1463744219").split())
    
