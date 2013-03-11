#!/usr/bin/python

import redis
import sys
import cgi, cgitb

myr=redis.Redis()

# total bets

form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay Place Bet</title>"
print "</head><body>"

if "bettor" not in form:
	print '<form action="placebet.cgi" method="post" style="font-size:22px">'
	print 'Bettor: <select name=bettor>'
	print '<option value=""></option>'
	for bettor in sorted(myr.smembers('derby:bettors')):
		print '<option', ('value="'+bettor+'">')
		print bettor, '</option>'
	print '</select>'

	print 'Horse: <select name=horse>'
	print '<option value=""></option>'
	for horse in sorted(myr.smembers('derby:horses')):
		print '<option', ('value="'+horse+'">')
		print horse, '</option>'
	print '</select>'

	print 'Bet: <select name=amount>'
	for amount in 1, 2, 3, 4, 5:
		print '<option', ('value="'+str(amount)+'">')
		print '$', amount, '</option>'
	print '</select>'

	print '<input type="submit" value="Place Bet">'

	print '</form>'

	print '<p>'
	print '[<a href="addbettor.cgi">Add a new bettor</a>]'
	print '[<a href="tote.cgi">Back to Tote</a>]'

else:
	bettor = form.getfirst("bettor")
	horse = form.getfirst("horse")
	amount = int(form.getfirst("amount"))
	myr.hincrby(('bet:'+horse),bettor,amount)
	print '<p style="font-size:22px">'
	print "took bet for", bettor, " - $", amount, "on", horse
	#print ticket
	print '</p><p>'
	print '[<a href="tote.cgi">Back to Tote</a>]'
print '</p>'
print "</body></html>"
