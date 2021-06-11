!alias tides embed
<drac2>
cc = "Tides Tracker"
character().create_cc_nx(cc,0,reset='long',reset_to='0',dispType=None)
diceTable = {0:'1d4', 1:'1d3', 2:'1d2'}
tryCounter = character().get_cc(cc)
currentDie = diceTable[tryCounter] if tryCounter<3 else '1d2'
theRoll = roll(currentDie)


if '%1%' == 'reset':
	character().set_cc(cc,0)
	return f'''embed -title "Tides of Chaos reset!" -desc "Counter manually reset" '''
elif theRoll==1:
	character().set_cc(cc,0)
	return f'''embed -title "Tides of Chaos reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. Run !wmsurge tide now." '''
else:
	tryCounter+=1
	character().mod_cc(cc,+1)
	return f'''embed -title "Tides of Chaos does not reset!" -desc "{name} rolled a {theRoll} on a {currentDie}. This was attempt {tryCounter}." '''
</drac2>
-footer "!tides"