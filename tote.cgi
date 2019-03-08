#!/usr/bin/python

import redis
import sys
from nicesort import nsorted
import ht
import cgi, cgitb
cgitb.enable()


myr=redis.Redis()

# total bets

ht.header("Derby Day Tote Board")

totbet=0
numbets=0
warns=[]
for horse in myr.keys('derby:bet:*'):
    hn = horse.split(':')[2]
    if myr.sismember('derby:horses', hn):
        for bet in myr.hkeys(horse):
            numbets = numbets + 1
            totbet = totbet + int(myr.hget(horse, bet))
    else:
        warns.append(('warning:'+ hn+ ' needs bets refunded.'))
vig = myr.get('derby:vig')
if vig:
    vig = int(vig)
else:
    vig = 0
totbet = totbet - vig

totetable=[ ['Horse', 'Local Odds', 'w'] ]
for horse in nsorted(myr.smembers('derby:horses')):
    hbet=0
    for bet in myr.hkeys(('derby:bet:'+horse)):
        hbet=hbet + int(myr.hget(('derby:bet:'+horse), bet))
    if hbet == 0:
        odds="INF"
    else:
        odds  = "{} to 1".format((totbet / hbet))
    hlink='<a href="winner.cgi?winner='+horse+'">W</a>'
    totetable.append([horse, hbet, hlink])
ht.table(totetable)


print "<p>total pot $", totbet, "in", numbets, "bets.</p>"
for warning in warns:
    print '<p><b>'
    print warning
    print '</b></p>'

print '<p>'
print '[<a href="placebet.cgi">Place Bet</a>]'
print '[<a href="listbets.cgi">List Bets</a>]'
ht.footer()
