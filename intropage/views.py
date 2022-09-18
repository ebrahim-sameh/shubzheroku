import json

from django.shortcuts import render, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def mainpage(request):
    return render(request, 'intropage/main.html')


def audio(request):
    return render(request, 'index.html')

#
# def scrape(request):
#     http_proxy = "http://65.21.141.242:10100"
#     https_proxy = "https://65.21.141.242:10100"
#     ftp_proxy = "ftp://10.10.1.10:3128"
#
#     proxies = {
#         "http": http_proxy,
#         "https": https_proxy,
#         "ftp": ftp_proxy
#     }
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         'authority': 'mobile.fmcsa.dot.gov',
#         'method': 'GET',
#         'scheme': 'http',
#         'upgrade-insecure-requests': '1',
#         'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#
#     }
#     url = 'http://mobile.fmcsa.dot.gov/qc/services/carriers/name/greyhound?webKey=f9d9a84990f7f4a5b72ebba8ccdb7bb861a44eff'
#
#     r = requests.get(url, proxies=proxies)
#     print(r)
#     if r.status_code == 200:
#         return HttpResponse('Yay, it worked')
#     return HttpResponse('Could not save data')
