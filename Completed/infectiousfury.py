<drac2>
cc = "Infectious Fury"
character().create_cc_nx(cc, 0, constitutionMod if constitutionMod>0 else 1, 'long', 'bubble') 
args,c=argparse(&ARGS&),combat()
v = character().get_cc(cc)>0
dc = 8+constitutionMod+proficiencyBonus
subclass = load_json(get("subclass", "{}")).get("BarbarianLevel", "")
hdg = "Beast" in subclass and BarbarianLevel>9

if not hdg:
	return f'''embed -title "{name} isn't the right level to use Infectious Fury!" -desc "make sure you're up to date on `.level`"'''

#if character().get_cc(cc)<1:
elif character().get_cc(cc)<1:
	return f'''embed -title "{name} has no more {cc} remaining!" -desc "Sleep it off, champ." '''

elif not c:
	return f'''embed -title "{name} isn't in combat" -f "{cc}|At 10th level, when you hit a creature with your natural weapons while you are raging, the spirit within you can curse your target with rabid fury. The target must succeed on a Wisdom saving throw (DC equal to 8 + your Constitution modifier + your proficiency bonus) or suffer one of the following effects (your choice):\n-The target must use its reaction to make a melee attack against another creature of your choice that you can see.\n-Target takes 2d12 psychic damage.\nYou can use this feature a number of times equal to your Constitution modifier (a minimum of once). You regain all expended uses when you finish a long rest." '''

elif "react" in &ARGS&:
	tgt=args.get('t')
	combatants=[c.get_combatant(x) for x in tgt] if c else []
	target = combatants[0]
	save = target.save("wis")
	didSave = save.total>=dc
	savestatus = "Success!" if didSave else "Failure!"
	character().mod_cc(cc, -1)
	return f'''embed -title "{name} strikes with {cc}!" -f "Meta|**DC**: {dc}" -f "**{target.name}**|**WIS Save**: {save}; {savestatus}\n **Effect**: {target.name} must use its reaction to make a melee attack against another creature of your choice that you can see." '''

elif "damage" in &ARGS&:
	tgt=args.get('t')
	combatants=[c.get_combatant(x) for x in tgt] if c else []
	target = combatants[0]
	save = target.save("wis")
	didSave = save.total>=dc
	savestatus = "Success!" if didSave else "Failure!"
	if not didSave:
		if "crit" in &ARGS&:
			damage = target.damage("4d12[psychic]")
		else:
			damage = target.damage("2d12[psychic]")
		totaldmg = damage['total']
		target.modify_hp(-totaldmg)
		totaldmg = 0 if didSave else damage['total']
		target.modify_hp(-totaldmg)
	character().mod_cc(cc, -1)
	return f'''embed -title "{name} strikes with {cc}!" -f "Meta|**DC**: {dc}" -f "**{target.name}**|**WIS Save**: {save}; {savestatus}\n {damage['damage'] if not didSave else 'No Damage!'}\n{target.name}: {target.hp_str()}"'''

else:
	return f'''embed -title "{name} ponders the meaning of their fury" -f "{cc}|At 10th level, when you hit a creature with your natural weapons while you are raging, the spirit within you can curse your target with rabid fury. The target must succeed on a Wisdom saving throw (DC equal to 8 + your Constitution modifier + your proficiency bonus) or suffer one of the following effects (your choice):\n-The target must use its reaction to make a melee attack against another creature of your choice that you can see.\n-Target takes 2d12 psychic damage.\nYou can use this feature a number of times equal to your Constitution modifier (a minimum of once). You regain all expended uses when you finish a long rest." '''
</drac2>
-f "{{cc}}|{{character().cc_str(cc)}}" 
-footer "!fury [react|damage] -t target"
