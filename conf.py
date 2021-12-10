# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "1uci3n/weilantian.net@gh-pages"
}

# 站点设置
site_name = "搞点儿技术总结"
site_logo = "${static_prefix}logo.png"
site_build_date = "2021-12-31T16:51+08:00"
author = "魏蓝天"
email = "lantian.wei.it@gmail.com"
author_homepage = "https://www.weilantian.net"
description = "就搞点儿研究吧,您叻"
key_words = ['Maverick', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
    # {
    #     "name": "三無計劃",
    #     "url": "https://www.imalan.cn",
    #     "brief": "熊猫小A的主页。"
    # }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    # {
    #     "name": "Twitter",
    #     "url": "https://twitter.com/AlanDecode",
    #     "icon": "gi gi-twitter"
    # },
    {
        "name": "GitHub",
        "url": "https://github.com/1uci3n",
        "icon": "gi gi-github"
    },
    {
        "name": "Google Scholar",
        "url": "https://scholar.google.com/citations?hl=ja&user=I5PJIJ4AAAAJ",
        "icon": "gi gi-google-scholar"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="shortcut icon" href="${static_prefix}favicon.ico" type="image/vnd.microsoft.icon" />
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
