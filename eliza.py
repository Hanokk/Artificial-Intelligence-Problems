rules=[(['hello','hi'],["hi there how may i help you"]),
	(["sick"],["can u tell me what are u suffering from"]),
	(["headache"],["take rest"]),
	(["mad","angry","crazy"],["why do you think"]),
	(["yes"],["are u sure"]),
	(["thanks"],["you are welcome :)"])]

while True:
    flag=""
    input=raw_input()
    split=input.split()
    for word in split:
        for rule in rules:
            for key in rule[0]:
                if word == key:
                    flag="found"
                    result=rule[1]
                    print result[0]
                    break
            if flag=="found":
                break
        if flag=="found":
                break
        
            
