import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('O site não está disponível no momento.')
else:
    print('Consegui acessar o site com sucesso.')