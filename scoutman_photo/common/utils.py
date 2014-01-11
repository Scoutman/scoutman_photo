# encoding: utf-8

from os import environ
from os.path import abspath, basename, dirname, join, normpath
from re import match, sub
import string

def read_env():
    # Liest evironment variables von .django_env/.SITE_NAME_env 

    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    SITE_NAME = basename(DJANGO_ROOT)

    path = string.replace(DJANGO_ROOT, SITE_NAME, '')
    path = string.rstrip(path, '/')
    path = ('%s/.django_env/.%s_env' % (path, SITE_NAME))
    
    try:
        with open(path) as f:
            content = f.read()
    except IOError:
        content = ''
        exit('Datei .django_env/.%s_env nicht gefunden.' % SITE_NAME)
  

    for line in content.splitlines():
        m1 = match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = match(r'\A"(.*)"\Z', val)
            if m3:
                val = sub(r'\\(.)', r'\1', m3.group(1))

            environ.setdefault(key, val)


def env_var(key, default=None):
    # Untersucht env vars und ersetzt boolean Werte
    val = environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val
            