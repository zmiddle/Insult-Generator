#Takes the columns of words as one string and forms them into separate lists that will be used to randomly generate
#a Shakespeareanesque insult. This program is great to use for Vicious Mockery in Dungeons and Dragons!

##raw string can be found at http://www.pangloss.com/seidel/shake_rule.html##

import re
import random

#Raw string that contains the words
string ='''
artless             base-court          apple-john
bawdy               bat-fowling         baggage
beslubbering        beef-witted         barnacle
bootless            beetle-headed       bladder
churlish            boil-brained        boar-pig
cockered            clapper-clawed      bugbear
clouted             clay-brained        bum-bailey
craven              common-kissing      canker-blossom
currish             crook-pated         clack-dish
dankish             dismal-dreaming     clotpole
dissembling         dizzy-eyed          coxcomb
droning             doghearted          codpiece
errant              dread-bolted        death-token
fawning             earth-vexing        dewberry
fobbing             elf-skinned         flap-dragon
froward             fat-kidneyed        flax-wench
frothy              fen-sucked          flirt-gill
gleeking            flap-mouthed        foot-licker
goatish             fly-bitten          fustilarian
gorbellied          folly-fallen        giglet
impertinent         fool-born           gudgeon
infectious          full-gorged         haggard
jarring             guts-griping        harpy
loggerheaded        half-faced          hedge-pig
lumpish             hasty-witted        horn-beast
mammering           hedge-born          hugger-mugger
mangled             hell-hated          joithead
mewling             idle-headed         lewdster
paunchy             ill-breeding        lout
pribbling           ill-nurtured        maggot-pie
puking              knotty-pated        malt-worm
puny                milk-livered        mammet
qualling            motley-minded       measle
rank                onion-eyed          minnow
reeky               plume-plucked       miscreant
roguish             pottle-deep         moldwarp
ruttish             pox-marked          mumble-news
saucy               reeling-ripe        nut-hook
spleeny             rough-hewn          pigeon-egg
spongy              rude-growing        pignut
surly               rump-fed            puttock
tottering           shard-borne         pumpion
unmuzzled           sheep-biting        ratsbane
vain                spur-galled         scut
venomed             swag-bellied        skainsmate
villainous          tardy-gaited        strumpet
warped              tickle-brained      varlot
wayward             toad-spotted        vassal
weedy               unchin-snouted      whey-face
yeasty              weather-bitten      wagtail'''

#Removes the spaces inbetween the words and separates them with a newline
string2 = re.sub(r"\s+", "\n", string)

#Splits the string where the newline character is located
list = string2.split("\n")

#Lists used to makes the induvidual parts of the insult
l1 = []
l2 = []
l3 = []

#Variables used to off set each index, so the right word column matches the list order
e = 0
n1 = 0
n2 = 0
n3 = 0

#For loop that appends each word/element according to the list index
for i in list:
    if e == 0 + n1:
        l1.append(list[e])
        e = e + 1
        n1 = n1 + 3
    
    elif e == 1 + n2:
        l2.append(list[e])
        e = e + 1
        n2 = n2 + 3
    
    elif e == 2 + n3:
        l3.append(list[e])
        e = e + 1
        n3 = n3 + 3
        
    else:
        print("Error.")
        
#Variables that hold the randomly selected word from each list
w1 = l1[random.randint(0,49)]
w2 = l2[random.randint(0,49)]
w3 = l3[random.randint(0,49)]

#Prints the insult to system out
print('Thou ' + w1 +' '+ w2 +' '+ w3 + '!')
