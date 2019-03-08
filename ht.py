#!/usr/bin/python

def header(title="fixme"):
    print "Content-type:text/html\r\n\r\n"
    print "<html><head>"
    print "<title>", title, "</title>"
    print "</head><body>"

def footer():
    print '</p>'
    print "</body></html>"


def table(tdata):
    print '<table border=1 style="font-size:22px">'

    print '<tr>'
    for i in tdata.pop():
        print '<th>', i, '</th>'
    print '</tr>'

    for r in tdata:
        print '<tr>'
        for i in r:
            print '<td>', i, '</td>'
        print '</tr>'
    print '</table>'
#print '<p>'
#print '[<a href="placebet.cgi">Place Bet</a>]'
#print '[<a href="tote.cgi">Tote Board</a>]'
