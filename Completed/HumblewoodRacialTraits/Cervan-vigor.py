<drac2>
cc = "Surge of Vigor"
desc = "All cervans possess a great tenacity and will to survive, which allows them to bounce back from even the most devastating blows. If an attack deals over half of your current remaining hit points in damage, (even if your hit points are reduced to 0 by the attack) you immediately regain hit points equal to 1d12 + your Constitution Modifier. You can’t use this feature again until you have completed a long rest."
hdg = 'Cervan' in character().race
if not hdg:
	return f'''embed -title "You are not a Cervan!" -desc "You don't surge, and it surely isn't vigorous." '''
else:
	character().create_cc_nx(cc, 0, 1, 'short', 'bubble', reset_to="1")
	if character().get_cc(cc)<1:
  		return f'''embed -title "{name} is all out of Vigor!" -desc "Rest up and try again." '''
	character().mod_cc(cc, -1)
	heal = vroll('1d12') + constitutionMod
	character.modify_hp(heal,overflow=False)
	return f'''embed -title "{name} uses {cc}" -desc "{desc}" -f "Heal:{heal}|{name}: {character().hp_str()} -footer "{cc}\n{character().cc_str(cc)}"'''
</drac2>
-thumb "<image>"