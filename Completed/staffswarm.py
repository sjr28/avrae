<drac2>
uses = 1 if '%1%'=='cloud' else 4 if '%1%'=='giant' else 5 if '%1%'=='plague' else 0
cc = "Staff of Swarming Insects"
character().create_cc_nx(cc, 0, 10, 'long', 'bubble', reset_by='1d6+4')
character().set_cvar_nx('staffswarm_intact',"True")
v = character().get_cc(cc)>=uses>0
x = character().get_cc(cc)<uses
f = "Staff of Swarming Insects|This staff has 10 charges and regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll a d20. On a 1, a swarm of insects consumes and destroys the staff, then disperses."
s = "Spells|While holding the staff, you can use an action to expend some of its charges to cast one of the following spells from it, using your spell save DC: giant insect (4 charges) or insect plague (5 charges)."
c = "Insect Cloud|While holding the staff, you can use an action and expend 1 charge to cause a swarm of harmless flying insects to spread out in a 30-foot radius from you. The insects remain for 10 minutes, making the area heavily obscured for creatures other than you. The swarm moves with you, remaining centered on you. A wind of at least 10 miles per hour disperses the swarm and ends the effect."
g = "You've expended the staff's last charge and you rolled a "
live = "Congratulations, you get to keep your staff. For now."
die = "A swarm of insects consumes and destroys the staff, then disperses. Your staff is gone forever."


if '%1%' == 'reset':
	character().set_cvar('staffswarm_intact',"True")
	character().mod_cc(cc, character().get_cc_max(cc))
	return f'''embed -title "{cc} reset!" -desc "Did {name} find a new one? Did the DM handwave away its destruction? We may never know." '''
elif staffswarm_intact == "False":
	return f'''embed -title "{name}'s {cc} is nowhere to be found!" -desc "Did someone accidentally destroy their magic item by using all the charges and rolling a 1? Tsk tsk. If you found another one, try `!staffswarm reset`"'''
elif uses==0:
	return f'''embed -title "{name} quickly reads the instructions for their {cc}!" -desc "`!staffswarm cloud` or `!staffswarm giant` or `!staffswarm plague [-t target(s)]`" -f "{f}" -f "{s}" -f "{c}" '''
elif v:
	character().mod_cc(cc, -uses)
	if character().get_cc(cc)==0:
		theRoll = roll('1d20')
		if theRoll == 1:
			character().set_cvar('staffswarm_intact',"False")
		if uses == 1:
			return f'''embed -title "{name} calls forth an insect cloud" -desc "While holding the staff, you can use an action and expend 1 charge to cause a swarm of harmless flying insects to spread out in a 30-foot radius from you. The insects remain for 10 minutes, making the area heavily obscured for creatures other than you. The swarm moves with you, remaining centered on you. A wind of at least 10 miles per hour disperses the swarm and ends the effect." -f "{f}" -f "{g}{theRoll}|{die if theRoll == 1 else live}" '''
		elif uses == 4:
			return f'''cast "Giant Insect" -i -phrase "using the {cc}" -f "{s}" -f "{f}" -f "{g}{theRoll}|{die if theRoll == 1 else live}" '''
		elif uses == 5:
			return f'''cast "Insect Plague" -i -phrase "using the {cc}" -f "{s}" -f "{f}" -f "{g}{theRoll}|{die if theRoll == 1 else live}" '''
		else:
			return f'''-title "Where'd you find this?!" -desc "This code shouldn't be reachable. Something is fucked in line 37." '''
	else:
		if uses == 1:
			return f'''embed -title "{name} calls forth an insect cloud" -desc "While holding the staff, you can use an action and expend 1 charge to cause a swarm of harmless flying insects to spread out in a 30-foot radius from you. The insects remain for 10 minutes, making the area heavily obscured for creatures other than you. The swarm moves with you, remaining centered on you. A wind of at least 10 miles per hour disperses the swarm and ends the effect." -f "{f}" '''
		elif uses == 4:
			return f'''cast "Giant Insect" -i -phrase "using the {cc}" -f "{s}" -f "{f}" '''
		elif uses == 5:
			return f'''cast "Insect Plague" -i -phrase "using the {cc}" -f "{s}" -f "{f}" '''
		else:
			return f'''-title "Where'd you find this?!" -desc "This code shouldn't be reachable. Something is fucked in line 46." '''
elif x:
	return f'''embed -title "You do not have enough charges to use the {cc} for that." -f "Do something that needs fewer charges or wait until dawn" '''
else:
	return f'''-title "Where'd you find this?!" -desc "This code shouldn't be reachable. Something is fucked in line 50." '''
</drac2>
-f "{{cc}}{{f" (-{uses})" if v else ""}}|{{character().cc_str(cc)}}" 
-thumb https://media-waterdeep.cursecdn.com/avatars/thumbnails/7/418/1000/1000/636284769826755468.jpeg
-footer "!staffswarm cloud or !staffswarm giant or !staffswarm plague [-t target(s)]"