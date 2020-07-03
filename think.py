from PIL import Image

import cv2






Image1 = Image.open(r'C:\Users\KIIT\Documents\hell.png')

Image1copy = Image1.copy()


a = 24
b = 38
i=0

word = 'The quick brown fox jumps over the lazy dog My school is closed for summer vacation.'

def split(word):
    return [ char for char in word]


def line():
    global a
    global b

    Image2copy = Image2.copy()

    Image1copy.paste(Image2copy , (a , b))

    if (a>=500):
        a=24
        b=b+38
    elif (a<500):
        a = a +24

def small():
    global a
    global b

    outputcopy = Image2.copy()

    Image1copy.paste(outputcopy , (a , b+10))

    if (a>=500):
        a=24
        b=b+38
    elif (a<500):
        a = a + 14


def under():
    global a
    global b

    outputcopy = Image2.copy()

    Image1copy.paste(outputcopy , (a , b+10))

    if (a>=500):
        a=24
        b=b+38
    elif (a<500):
        a = a + 14






alparr = split(word)

while (i<len(word)):

    alp = alparr[i]

    if alp =='A':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha268.png')

      #Image2copy = Image2.copy()

      line()

      print('A')


    if alp =='B':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha452.png')

      #Image2copy = Image2.copy()

      line()

      print('B')

    if alp =='C':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha539.png')

      #Image2copy = Image2.copy()

      line()

      print('C')

    if alp =='D':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha584.png')

      #Image2copy = Image2.copy()

      line()

      print('D')

    if alp =='E':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha630.png')

      #Image2copy = Image2.copy()

      line()

      print('E')

    if alp =='F':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha646.png')

      #Image2copy = Image2.copy()

      line()

      print('F')

    if alp =='G':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha653.png')

      #Image2copy = Image2.copy()

      line()

      print('G')

    if alp =='H':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha657.png')

      #Image2copy = Image2.copy()

      line()

      print('H')

    if alp =='I':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha662.png')

      #Image2copy = Image2.copy()

      line()

      print('I')

    if alp =='J':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha666.png')

      #Image2copy = Image2.copy()

      line()

      print('J')

    if alp =='K':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha672.png')

      #Image2copy = Image2.copy()

      line()

      print('K')


    if alp =='L':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha676.png')

      #Image2copy = Image2.copy()

      line()

      print('L')

    if alp =='M':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha680.png')

      #Image2copy = Image2.copy()

      line()

      print('M')

    if alp =='N':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha682.png')

      #Image2copy = Image2.copy()

      line()

      print('N')

    if alp =='O':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha572.png')

      #Image2copy = Image2.copy()

      line()

      print('O')

    if alp =='P':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha622.png')

      #Image2copy = Image2.copy()

      line()

      print('P')

    if alp =='Q':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha252.png')

      #Image2copy = Image2.copy()

      line()

      print('Q')

    if alp =='R':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha459.png')

      #Image2copy = Image2.copy()

      line()

      print('R')

    if alp =='S':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha551.png')

      #Image2copy = Image2.copy()

      line()

      print('S')

    if alp =='T':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha585.png')

      #Image2copy = Image2.copy()

      line()

      print('T')


    if alp =='U':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha673.png')

      #Image2copy = Image2.copy()

      line()

      print('U')

    if alp =='V':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha648.png')

      #Image2copy = Image2.copy()

      line()

      print('V')

    if alp =='W':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha681.png')

      #Image2copy = Image2.copy()

      line()

      print('W')

    if alp =='X':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha416.png')

      #Image2copy = Image2.copy()

      line()

      print('X')


    if alp =='Y':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha663.png')

      #Image2copy = Image2.copy()

      line()

      print('Y')


    if alp =='Z':

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha668.png')

      #Image2copy = Image2.copy()

      line()

      print('Z')


    if alp =='a':

      img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha398.png', cv2.IMREAD_UNCHANGED)

      dsize = (14, 14)

      output = cv2.resize(img, dsize)

      cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha398.png', output)

      Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha398.png')

      small()

      print('a')

    if alp == 'b':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha497.png')

        #Image2copy = Image2.copy()

        line()

        print('b')


    if alp is 'c':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha560.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha560.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha560.png')

       #Image2copy = Image2.copy()

        small()

    if alp is 'd':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha608.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'e':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha647.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha647.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha647.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'f':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha655.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'g':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha660.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 24)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha660.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha660.png')

        #Image2copy = Image2.copy()

        under()

    if alp is 'h':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha664.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'i':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha3.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha3.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha3.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'j':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha674.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 24)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha674.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha674.png')

        #Image2copy = Image2.copy()

        under()

    if alp is 'k':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha679.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'l':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha683.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'm':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha403.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha403.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha403.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'n':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha506.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha506.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha506.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'o':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha685.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha685.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha685.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'p':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha622.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 24)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha622.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha622.png')

        #Image2copy = Image2.copy()

        under()

    if alp is 'q':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha649.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 24)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha649.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha649.png')

        #Image2copy = Image2.copy()

        under()

    if alp is 'r':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha656.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha656.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha656.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 's':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha661.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha661.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha661.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 't':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha667.png')

        #Image2copy = Image2.copy()

        line()

    if alp is 'u':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha673.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha673.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha673.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'v':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha678.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha678.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha678.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'w':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha681.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha681.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha681.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'x':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha659.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha659.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha659.png')

        #Image2copy = Image2.copy()

        small()

    if alp is 'y':


        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha518.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 24)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha518.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha518.png')

        #Image2copy = Image2.copy()

        under()

    if alp is 'z':

        img = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha576.png', cv2.IMREAD_UNCHANGED)

        dsize = (14, 14)

        output = cv2.resize(img, dsize)

        cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha576.png', output)

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha576.png')

        #Image2copy = Image2.copy()

        small()

    if alp is ' ':

        if (a >= 500):
            a = 24
            b = b + 38
        elif (a < 500):
            a = a + 24

    if alp is '.':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha666.png')

        #Image2copy = Image2.copy()

        line()

    if alp is ',':

        Image2 = Image.open(r'C:\Users\KIIT\Desktop\Writer\alpha666.png')

        #Image2copy = Image2.copy()

        line()

    i+=1



Image1copy.save(r'C:\Users\KIIT\Desktop\Writer\f.png')
