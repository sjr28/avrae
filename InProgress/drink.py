<drac2>
this = load_json(get_gvar("ac8a5d23-8715-46d8-882e-60b29417347c"))
args = &ARGS&
help = args[0].lower() in '?help' if args else True
cc = "Intoxication"
status = this[cc]
drinks = this["Beverages"]
statlist = ["sober","tipsy","merry","drunk","hammered","plastered","unconscious"]
au = 0
d = None
character().create_cc_nx(cc, 0, constitution*6, 'long', reset_to="0")
#return f'''embed -title "Test" -desc "{character().resistances}" '''

if help:
	return f'''embed -title "{name} considers getting another drink" -desc "What's one more, right?\n\n**Intoxication**\n{character().get_cc(cc)}/{character().get_cc_max(cc)}\n\n**Stage**\n{floor(character().get_cc(cc)/constitution)}/6"'''

else:
	for x in drinks:
		if args[0].lower() in x.lower():
			au += drinks[x]
			d = x
	if not d:
		return f'''embed -title "{name} drinks...something we don't sell here" -desc "Check your spelling of the drink!" '''
	au = int(au/2) if "poison" in str(character().resistances.resist) else au
	#return f'''embed -title "Test" -desc "{au}" '''
	au = int(au*2) if get('size','Medium') == "Small" or get('size','Medium') == "Tiny" else au
	#return f'''embed -title "Test" -desc "{au}" '''
	character().mod_cc(cc, au)
	cs = floor(character().get_cc(cc)/constitution)
	drunk = statlist[cs]
	if d == "Phoenix Fire":
		beakRoll = roll("1d4")
		beakd = this["Beak"][str(beakRoll)]
		if beakRoll == 1:
			dmg = vroll("1d4[fire]")
			totaldmg = dmg.total
			character().modify_hp(-totaldmg)
			return f'''embed -title "{name} drinks {d} and is {drunk}!" -desc "{status[drunk]}\n\n**Talon of the Phoenix**\nYou take {dmg} fire damage as the drink burns your stomach internally\n\n**Intoxication**\n{character().get_cc(cc)}/{character().get_cc_max(cc)}\n\n**Stage**\n{cs}/6\n\n**{name}**\n{character().hp_str()}" '''
		return f'''embed -title "{name} drinks {d} and is {drunk}!" -desc "{status[drunk]}\n\n**Talon of the Phoenix**\n{beakd}\n\n**Intoxication**\n{character().get_cc(cc)}/{character().get_cc_max(cc)}\n\n**Stage**\n{cs}/6" '''
	return f'''embed -title "{name} drinks {d} and is {drunk}!" -desc "{status[drunk]}\n\n**Intoxication**\n{character().get_cc(cc)}/{character().get_cc_max(cc)}\n\n**Stage**\n{cs}/6" '''
</drac2>
-thumb "<image>"
-footer "!drink [ale|wine|mead|spirits|phoenix fire]"