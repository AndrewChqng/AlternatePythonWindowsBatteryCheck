class FONT:
    BLACK = '\033[30m'
    RED = '\033[31;1m'
    GREEN = '\033[32;1m'
    YELLOW = '\033[33;1m'
    BLUE = '\033[34;1m'
    MAGENTA = '\033[45;1m'
    CYAN = '\033[36;1m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95;1m'

def returncolour(val):
    if val >= 80:
        return highbat[ran(0,len(highbat)-1)] + FONT.GREEN
    elif val >= 25:
        return medbat[ran(0,len(medbat)-1)] + FONT.YELLOW
    elif val >= 0:
        return lowbat[ran(0,len(lowbat)-1)] + FONT.RED

def ripsyntax(cmd):
    return run(["powershell", "-Command", "WMIC PATH Win32_Battery Get " + cmd], capture_output=True, text=True).stdout
    
def returnint(string):
    return search(r'\d+', string).group()

def writedyn(tmp):
    sys.stdout.write(u"\u001b[600D" + tmp + (100-len(tmp))*" ")
    sys.stdout.flush()

def newclearline(tmp):
    sys.stdout.write("\n" + " "*355)*tmp
    sys.stdout.flush()

from re import search
from subprocess import run
from random import randint as ran
import sys, time

lowbat=["Watch out!!! ", "Duh duh duhhh ", "PANIC!!! ", "I'm dying ", "Low Battery! "]
medbat=["Relaxxx ", "Breathe ", "Things are fine ", "You're kinda okay "]
highbat=["Phew You're safe ", "I'm feeling great ", "Everyone's Happy"]
batval = int(returnint(ripsyntax("EstimatedChargeRemaining"))) #Why does this have to be here??? Colours don't work at school until this is set

print('\033[?25l', end="")
print(FONT.HEADER + FONT.BOLD + "Let's try not do anything stupid with this please - Andrew Chang\nSuggestions for additional stuff/comments welcome\n\n" + FONT.END + FONT.UNDERLINE + FONT.CYAN + "Welcome to my magicness (version: I've lost count but for future reference this is a million) \n\n" + FONT.END + FONT.BLUE + "Press enter to update" + FONT.END)
sys.stdout.write(u"\u001b[H" + u"\u001b[8B")
while True:
    writedyn(returncolour(batval) + str(batval) + "%" + FONT.END)
    newclearline(1)
    writedyn(returncolour(batval) + str(returnint(ripsyntax("EstimatedRunTime"))) + " mins left according to da laptop (but don't believe it! - very half glass full)" + FONT.END)
    newclearline(2)
    width = int((batval + 1)/2)
    bar = "[" + "#"*width + " " *(50 - width) + "]"
    writedyn(bar)
    input()
    sys.stdout.write(u"\u001b[H" + u"\u001b[8B")
    writedyn(FONT.MAGENTA + "Updating..." + FONT.END)
    batval = int(returnint(ripsyntax("EstimatedChargeRemaining")))
