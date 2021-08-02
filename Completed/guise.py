<drac2>
cc = "Tasha's Otherworldly Guise"
char = combat().get_combatant(character().name)

if '%1%' == 'upper' or '%1%' == 'Upper':
	char.add_effect('Immunity (Necrotic, Radiant, Charmed Condition)','-immune radiant -immune necrotic')
	return f'''cast "Tasha's Otherworldly Guise" -phrase "Drawing on the magic of the Upper Planes" -f "Upper Planes|Immune to Radiant Damage\nImmune to Necrotic Damage\nImmune to the Charmed Condition"'''
elif '%1%' == 'lower' or '%1%' == 'Lower':
	char.add_effect('Immunity (Fire, Poison, Poisoned Condition)','-immune fire -immune poison')
	return f'''cast "Tasha's Otherworldly Guise" -phrase "Drawing on the magic of the Lower Planes" -f "Lower Planes|Immune to Fire Damage\nImmune to Poison Damage\nImmune to the Poisoned Condition"'''
elif '%1%' == 'drop' or '%1%' == 'Drop':
	char.remove_effect("Immunity (Necrotic, Radiant, Charmed Condition)")
	char.remove_effect("Immunity (Fire, Poison, Poisoned Condition)")
	return f'''embed -title "{name} drops concentraion!" -desc "Immunity effects removed" '''
else:
	return f'''spell "Tasha's Otherworldly Guise"'''
</drac2>
-footer "!guise upper or !guise lower, !guise drop when you lose concentration"