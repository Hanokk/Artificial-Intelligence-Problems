rules=[(['hello','hi'],["hi there how may i help you"]),
	(["sick"],["can u tell me what are u suffering from"]),
	(["headache"],["take rest"]),
	(["mad","angry","crazy"],["why do you think"]),
	(["yes"],["are u sure"]),
	(["Thanks"],[])]

while True:
    f=open(data,"r")
    input=raw_input()
    split=input.split()
    for word in split:
        for rule in rules:
            for key in rule:
                if word == key:
                    result="found"
        if result=="found":
            print rule[1]

        
            
