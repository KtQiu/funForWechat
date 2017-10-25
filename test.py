#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : Kt Qiu
# @Time     : 17/10/25 22:25
# @Contact  : kitty666ball@gmail.com
# @GitHub   : https://github.com/KtQiu

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    return 'Auto reply:' + msg['Text']

itchat.auto_login(hotReload=True)
# itchat.send('Message Content', '几点')

itchat.run()