art=["a","an","the"]
pro=["he","she","it","they"]
nou=["elephant","cat","dog"]
verb=["eats","eating"]
adj=["old","young"]
auxverb=["is","was",""]
prep=["on","in","under"]
Noutable=[[0,art,(pro,nou)],[0,0,nou]]

strg=raw_input("Enter the sentence ")
strItem=strg.split()
strlen=len(strItem)
i=0
result=""
result2=""
result3=""
strg=strItem
for arti in art:
    if strg[i]==arti:
	i=i+1
	for noun in nou:
	    if strg[i]==noun:
		result="success"
		i=i+1
		break
	if result!="success":
	    print "not accepted"
        break
if result!="success":
    for pron in pro:
        if strg[i]==pron:
	    result="success"
	    i=i+1
	    break
    if result!="success":    
	for noun in nou:
	    if strg[i]==noun:
		i=i+1
		result="success"
		print result
		break
if result=="success":
    for aux in auxverb:
	if strg[i]==aux:
	    i=i+1
    for ver in verb:
	if strg[i]==ver:
	    i=i+1
	    for adje in adj:
		if strg[i]==adje:
		    i=i+1
	    for noun in nou:
		if strg[i]==noun:
		    result2="success"
		    i=i+1
		    break
	    for prepo in prep:
		print strg[i]
		if strg[i]==prepo:
		    i=i+1
		    print strg[i]
		    for noun in nou:
			if strg[i]==noun:
			    result3="success"
			    break
	    break
    if result2=="success" and result3=="success":
	print "accepted"
    else:
	print "not accepted"
