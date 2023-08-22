import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site não está acessível no momento\033[m')
else:
    print('\033[33mConsegui acessar o site do Pudim com sucesso!\033[m')
    print(site.read())
