import os
import sys
import platform

def getFileList(p):
    
    p = str(p)
    
    if p == "":
        return []
        
    if p[-1] != "/":
        p = p + "/"
    
    a = os.listdir(p)     
    
    b = []
    
    for x in a:
        if os.path.isfile(p + x) and ( os.path.splitext(x)[-1] == ".png" or os.path.splitext(x)[-1] == ".PNG"):
            b.append(p + x)
    return b

# ---- main ----

if ( platform.system() != "Windows" and platform.system() != "Darwin" ):
    print "Only support Windows and Darwin"
    exit()

if len(sys.argv) < 2:
    print "Need Path"
    exit()
    
os.chdir(platform.system())

path = sys.argv[1]

option = ""
if len(sys.argv) > 2:
    option = sys.argv[2]

b = getFileList(path)

for f in b:
    a , b = os.path.splitext(f)
    
    print "Encoding " + f + " to " + a + ".webp"
    
    if( platform.system() == "Darwin" ):
        os.system("./cwebp " + option + " -quiet " + f + " -o " + a + ".webp")
    elif( platform.system() == "Windows" ):
        os.system("cwebp " + option + " -quiet " + f + " -o " + a + ".webp")
    


        