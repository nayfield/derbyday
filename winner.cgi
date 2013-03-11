#!/usr/bin/python

import redis
import sys
import cgi, cgitb
from nicesort import nsorted

myr=redis.Redis()

# total bets

form = cgi.FieldStorage()
cgitb.enable()

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay Place Bet</title>"
print "</head><body>"

if "winner" not in form:
	print '<form action="winner.cgi" method="post" style="font-size:22px">'

	print 'Horse: <select name=winner>'
	print '<option value=""></option>'
	for horse in nsorted(myr.smembers('derby:horses')):
		print '<option', ('value="'+horse+'">')
		print horse, '</option>'
	print '</select>'

	print '<input type="submit" value="Show Payoffs">'

	print '</form>'

	print '<p>'
	print '[<a href="tote.cgi">Back to Tote</a>]'

else:
	print '<table border=1 style="font-size:22px">'
	winner = form.getfirst("winner")
	winkey = (('derby:bet:'+winner))
	totbet = 0
	winbet = 0
	paid = 0
	for horse in myr.keys('derby:bet:*'):
		hn = horse.split(':')[2]
		if myr.sismember('derby:horses', hn):
			for bet in myr.hkeys(horse):
				totbet = totbet + int(myr.hget(horse, bet))
	for bet in myr.hkeys(winkey):
		winbet=winbet + int(myr.hget(winkey, bet))
	vig = myr.get('derby:vig')
	if vig:
		vig = int(vig)
	else:
		vig = 0
	if winbet:
		payper = int(round((totbet - vig) / winbet))
	for bettor in myr.hkeys(winkey):
		print "<tr><td>", bettor, "</td>"
		payout = int(myr.hget(winkey, bettor)) * payper
		paid = paid + payout
		print "<td> $", payout, "</td></tr>"
	print "</table>"
	print "<p>Paid $", paid, "of total $", totbet, "</p>"
	print "<p>Helpers keep $", totbet-paid, "</p>"
	print '[<a href="tote.cgi">Back to Tote</a>]'
print '</p>'
print "</body></html>"
