#!/usr/bin/python

import redis
import sys
import cgi, cgitb

myr=redis.Redis()

# total bets

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay Tote Board</title>"
print "</head><body>"

totbet=0
numbets=0
warns=[]
for horse in myr.keys('bet:*'):
	hn = horse.split(':')[1]
	if myr.sismember('derby:horses', hn):
		for bet in myr.hkeys(horse):
			numbets = numbets + 1
			totbet = totbet + int(myr.hget(horse, bet))
	else:
		warns.append(('warning,', hn, 'needs bets refunded.'))

print '<table border=1 style="font-size:20px;border-collapse:collapse;">'
print '<tr><th>Horse</th><th>Local Odds</th></tr>'
for horse in sorted(myr.smembers('derby:horses')):
	print "<tr><td>", horse, "</td>"
	hbet=0
	for bet in myr.hkeys(('bet:'+horse)):
		hbet=hbet + int(myr.hget(('bet:'+horse), bet))
	if hbet == 0:
		print "<td>", 'INF'," </td>"
	else:
		print "<td>", (totbet / hbet), 'to 1</td>'
	print "</tr>"
print "</table>"


print "<p>total pot $", totbet, "in", numbets, "bets.</p>"
if warns:
	print '==='
	print warns

print '<p>'
print '[<a href="placebet.cgi">Place Bet</a>]'
print '[<a href="listbets.cgi">List Bets</a>]'
print '</p>'
print "</body></html>"
