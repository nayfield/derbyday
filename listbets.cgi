#!/usr/bin/python

import redis
import sys
import cgi, cgitb
cgitb.enable()

myr=redis.Redis()

# total bets

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay Bets</title>"
print "</head><body>"

print '<table border=1 style="font-size:22px">'
print '<tr><th>Horse</th><th>Bettor</th><th>Amount</th></tr>'
for horse in sorted(myr.keys('bet:*')):
	for bettor in myr.hkeys(horse):
		print "<tr><td>", horse.split(':')[1], "</td>"
		print "<td>", bettor, "</td>"
		print "<td> $", myr.hget(horse, bettor), "</td>"
print "</table>"

print '<p>'
print '[<a href="placebet.cgi">Place Bet</a>]'
print '[<a href="tote.cgi">Tote Board</a>]'
print '</p>'
print "</body></html>"
