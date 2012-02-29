#!/usr/bin/python
from Utils import removeCookies, redirect

removeCookies(['uid', 'username'])
redirect("index.cgi?logged=out")
