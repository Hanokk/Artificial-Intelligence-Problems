rules=[(['hello','hi'],["hi there how may i help you"]),
	(["headache","cold",""],["anything other than"]),
	(["mad","angry","crazy","sick","bad","mean"],["why do you think"]),
	(["yes"],["are u sure"]),
	(["what","when","where","how"],["Seriously,Do u really need to know?"]),
	(["thanks"],["you are welcome :)"])]
replace=[("you","me"),
	("your","my"),
	("i","you"),
	("my","your"),
	("am","are"),
	("are","am")]

def join(split):
    new=""
    for word in split:
        new=new+" "+word
    return new


while True:
    flag=""
    input=raw_input()
    split=input.split()
    count=0
    for word in split:
        rulecount=0
        for rule in rules:
            for key in rule[0]:
		for rep in replace:
		    if word==rep[0]:
			split[count]=rep[1]
		        flag2=1
			break
                if word == key:
                    flag="found"
                    result=rule[1]
		    if rulecount==2:
                        print result[0]+join(split)
                        break
		    elif rulecount==4:
			print result[0]+join(split)
                        break
		    else:
			print result[0]
            if flag=="found":
                break
	    rulecount=rulecount+1  
        if flag=="found":
                break
        count=count+1
        

