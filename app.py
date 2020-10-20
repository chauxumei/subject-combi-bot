print("subject combi quiz:O")
print()
print("helluu pls ans the questions and we'll suggest a subject combi for you??")
print()
print("kayy so firstly, let's find out about your grades; please respond with a number from 1 to 5, where 1 is C+ and below, 2 is B, 3 is B+, 4 is A and 5 is A+!!!")
print()

hist = input("your history grade ")

geog = input("your geography grade ")

lit = input("your english literature grade ")

bio = input("your biology grade (take percentage of bio component) ")

phys = input("your physics grade (take percentage of physics component) ")

clit = input("your Chinese grade ")

print()
print("okie let's consider your strengths now ooo; please respond with a number from 1 to 5, where 1 is strongly disagree and 5 is strongly agree!!!")
print()

geog1 = input("you're observant ")

bio2 = input("you can handle unfamiliar concepts ")

clit1 = input("you're familiar with Chinese culture ")

hist1 = input("you have the ability to weigh an argument in a logical and persuasive manner ")

lit1 = input("you hvae good vocab skills ")

clit2 = input("you have proficient Chinese speaking skills (???) ")

hist2 = input("you have intellectual rigour and independence ")

bio1 = input("you can notice fine details better than most ")

phys1 = input("you're good at math lol ")

lit2 = input("you are open minded ")
  
geog2 = input("you tend to think of logical reasons that lead to a certain outcome??? ")

phys2 = input("you're highly logical ")

print()
print("now let's consider your interest wooo")
print()

lit3 = input("you find looking at different perspectives interesting ")

geog3 = input("you're like handling facts and figures lol ")

hist3 = input("you actually give a (care) about the past ")

clit4 = input("you feel an inclination to Chinese culture ")

hist4 = input("you feel the need to know about the past to progress into the future ")

phys3 = input("you want to find out abt random phenomenons ")

bio4 = input("you find the creation of life intriguing ha ha ha ! ")

clit3 = input("you like Chinese ")

phys4 = input("you want to know more about theory of the world (?????????) ")

bio3 = input("you enjoy studying more about your characteristics (??) ")

lit4 = input("you like incorporating perswonal experiences into your ideas ")
  
geog4 = input("you like finding trends which lead to logical deductions ")

geog_final = int(geog)+ int(geog1) + int(geog2)+ int(geog3)+ int(geog4)
hist_final = int(hist)+ int(hist1) + int(hist2)+ int(hist3)+ int(hist3)
lit_final = int(lit)+ int(lit1)+ int(lit2)+ int(lit3)+ int(lit3)
clit_final = int(clit)+ int(clit1)+ int(clit2)+ int(clit3)+ int(clit3)
humans_final = ((geog_final + hist_final + lit_final + clit_final)/4)*100
bio_final = int(bio)+ int(bio1)+ int(bio2)+ int(bio3)+ int(bio3)
phys_final = int(phys)+ int(phys1)+ int(phys2)+ int(phys3)+ int(phys3)
sciences_final = ((bio_final + phys_final)/2)*100

print()

if sciences_final > humans_final:
  print("you might be suitable for trip sci!1!1!")
if humans_final > sciences_final:
  print("you might be suitable for double humans!1!1!")
print()
print("here are your indiv sub results lol")
print("geography:",geog_final, "history:", hist_final, "literature:", lit_final, "cliterature:", clit_final, "biology:", bio_final, "physics:", phys_final)
