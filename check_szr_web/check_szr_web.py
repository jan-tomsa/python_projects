import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

URL = "http://www.szrcr.cz/"

try:
    orig_file = open("szr_marquee.txt", "r")
    orig_text = orig_file.read()
    orig_file.close()
except FileNotFoundError:
    orig_text = ""

soup = BeautifulSoup(urllib.request.urlopen(URL), "html.parser")
div_scroll = soup.find_all("div", id="scroll")
#new_tag = soup.find('marquee')
#new_tag = soup.find(id="hp-text-scroll")

p_text = ""
for tag in div_scroll:
    p_element = tag.find('p')
    if(not p_element is None):
        p_text = p_element.get_text()

new_text = p_text

if orig_text == new_text:
    print('Marquee unchanged.')
else:
    print('Marquee changed!')
    print('Original text:')
    print(orig_text)
    print('New text:')
    print(new_text)

    with open("szr_marquee.csv","a") as f:
        sNow= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("{0};{1}\n".format(sNow, new_text))
        f.close()
        print('Marquee changed!')
        print(new_text)

    with open("szr_marquee.txt","w") as file:
        file.write(new_text)
        file.close()

    with open("display_warning.vbs","w") as script:
        script.write('Set WshShell = WScript.CreateObject("WScript.Shell")\n')
        script.write('WshShell.Run("http://www.szrcr.cz/")\n')
        script.write('WScript.Sleep 1500\n')
        script.write('WScript.Echo "SZR warning changed."\n')
        script.close()
