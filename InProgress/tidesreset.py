<drac2>
character().set_cvar_nx('tidesReset','0')
f = "Wand of Sleep|This wand has 5 charges and regains 3 (1d4+1) charges daily at dawn. If you expend the wand’s last charge, roll a d20. On a 1, the wand crumbles into dust and is destroyed. While holding the wand, you can use an action to expend 1 charge to cast sleep. You can expend an additional charge to cast this spell at a higher level."
g = "You've expended the wand's last charge and you rolled a "
live = "Congratulations, you get to keep your wand. For now."
die = "The wand crumbles into dust, gone forever."

diceTable = {'0':'1d4', '1':'1d3', '2':'1d2'}
currentDie = diceTable[tidesReset]
theRoll = roll(diceTable[tidesReset])
tryCounter = int(tidesReset)

if theRoll==1:
	character().set_cvar('tidesReset','0')
	return f'''embed -title "Tides of Chaos reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. Run !wmsurge tides now." '''
else:
	character().set_cvar('tidesReset',str(tryCounter+=1))
	return f'''embed -title "Tides of Chaos does not reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. This was attempt {tidesReeset}." '''
</drac2>
-footer "!tides"