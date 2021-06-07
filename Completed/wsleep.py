<drac2>
uses = int('%1%') if '%1%'.isdigit() else 0
lvl = int("%1%")+2 if '%1%'.isdigit() else 0
cc = "Wand of Sleep"
character().create_cc_nx(cc, 0, 5, 'long', 'bubble', reset_by='1d4+1')
character().set_cvar_nx('wsleep_intact',"True")
v = character().get_cc(cc)>=uses and lvl!=0
x = character().get_cc(cc)>0
f = "Wand of Sleep|This wand has 5 charges and regains 3 (1d4+1) charges daily at dawn. If you expend the wand’s last charge, roll a d20. On a 1, the wand crumbles into dust and is destroyed. While holding the wand, you can use an action to expend 1 charge to cast sleep. You can expend an additional charge to cast this spell at a higher level."
g = "You've expended the wand's last charge and you rolled a "
live = "Congratulations, you get to keep your wand. For now."
die = "The wand crumbles into dust, gone forever."


if '%1%' == 'reset':
	character().set_cvar('wsleep_intact',"True")
	character().mod_cc(cc, character().get_cc_max(cc))
	return f'''embed -title "{cc} reset!" -desc "Did {name} find a new one? Did the DM handwave the disintegration away? We may never know." '''
elif wsleep_intact == "False":
	return f'''embed -title "{name}'s {cc} is nowhere to be found!" -desc "Did someone accidentally disintegrate their magic item? Tsk tsk. If you found another one, try `!wsleep reset`"'''
elif lvl==0:
	return f'''embed -title "{name} quickly reads the instructions for their {cc}!" -desc "`!wsleep [charges used] [-t target(s)]`" '''
elif v:
	character().mod_cc(cc, -uses)
	if character().get_cc(cc)==0:
		theRoll = roll('1d20')
		if theRoll == 1:
			character().set_cvar('wsleep_intact',"False")
		return f'''cast "sleep" -i -l {lvl} -phrase "at level {lvl} using the {cc}" -f "{f}" -f "{g}{theRoll}|{die if theRoll == 1 else live}" '''
	else:
		return f'''cast "sleep" -i -l {lvl} -phrase "at level {lvl} using the {cc}" -f "{f}" '''
elif x:
	return f'''embed -title "You do not have enough charges to use the {cc} at level {lvl}." -f "Cast at a lower level or wait until dawn." '''
else:
	return f'''embed -title "All of the charges are gone from the {cc}!" -desc "If all the charges are used from the wand, roll a d20.  On a one, the wand turns to dust and is destroyed." '''
</drac2>
-f "{{cc}}{{f" (-{uses})" if v else ""}}|{{character().cc_str(cc)}}" 
-thumb https://static.wikia.nocookie.net/dnd-campaign/images/7/74/Wax_wand.png/revision/latest/scale-to-width-down/680?cb=20171115033506
-footer "!wsleep [charges used] [-t target(s)]"