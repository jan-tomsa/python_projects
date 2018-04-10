import urllib.request
from bs4 import BeautifulSoup

try:
    orig_file = open("szr_marquee.txt", "r")
    orig_text = orig_file.read()
    orig_file.close()
except FileNotFoundError:
    orig_text = ""

soup = BeautifulSoup(urllib.request.urlopen('http://www.szrcr.cz/'), "lxml")
new_tag = soup.find('marquee')
#new_tag = soup.find(id="hp-text-scroll")
new_text = str(new_tag)

if orig_text == new_text:
    print('Marquee unchanged.')
else:
    print('Marquee changed!')
    print('Original text:')
    print(orig_text)
    print('New text:')
    print(new_text)
    file = open("szr_marquee.txt","w")
    file.write(new_text)
    file.close()
    script = open("display_warning.vbs","w")
    script.write('Set WshShell = WScript.CreateObject("WScript.Shell")\n')
    script.write('WshShell.Run("http://www.szrcr.cz/")\n')
    script.write('WScript.Sleep 1500\n')
    script.write('WScript.Echo "SZR warning changed."\n')
    script.close()
