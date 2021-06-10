!alias tides embed
<drac2>
character().set_cvar_nx('tidesReset','0')
diceTable = {'0':'1d4', '1':'1d3', '2':'1d2'}
currentDie = diceTable[tidesReset] if int(tidesReset)<3 else '1d2'
theRoll = roll(currentDie)
tryCounter = int(tidesReset)

if '%1%' == 'reset':
	character().set_cvar('tidesReset',"0")
	return f'''embed -title "Tides of Chaos reset!" -desc "{name} manually reset the " '''
elif theRoll==1:
	character().set_cvar('tidesReset','0')
	return f'''embed -title "Tides of Chaos reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. Run !wmsurge tides now." '''
else:
	tryCounter+=1
	character().set_cvar('tidesReset',str(tryCounter))
	return f'''embed -title "Tides of Chaos does not reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. This was attempt {tidesReset}." '''
</drac2>
-footer "!tides"