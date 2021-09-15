<drac2>
c = combat()
ch = character()
hdg = 'Hedge' in character().race
a = argparse(&ARGS&)
n = '\n'
text='-desc "You can use your action to curl up, exposing attackers to a wall of your toughened quills. While curled up you cannot move, attack, or cast spells with somatic components, and your base armor class becomes 19. You cannot benefit from any Dexterity bonus to armor class while curled up, but you can still use shields. Any creature that misses you with a melee attack while you are curled up takes 2d4 points of piercing damage from your sharp quills. If a creature hits you while you are curled up, you are knocked prone in your space at the end of the turn. You may uncurl yourself at any point during your turn." '
targ = a.get('t')
combatants = [c.get_combatant(x) for x in targ] if c else []

if not hdg:
	text='-title "You are not a Hedge!" -desc "Only Hedges are able to use this ability!" '
elif 'shield' in "&*&".lower():
	c.me.add_effect('Curled Up',f"-ac 21") if c else ''
	text=text+f'-title "{ch.name} curls up with a shield!" '
	text=text+f'-f "AC|21" '
elif 'up' in "&*&".lower():
	c.me.add_effect('Curled Up',f"-ac 19") if c else ''
	text=text+f'-title "{ch.name} curls up!" '
	text=text+f'-f "AC|19" '
elif 'uncurl' in "&*&".lower():
	c.me.remove_effect('Curled Up') if c else ''
	text=text+f'-title "{ch.name} uncurls!" '
	text=text+f'-f "AC|{c.me.ac if c and c.me else ch.ac}" '
elif '-t' in "&*&".lower():
	text=text+f'-title "{ch.name} is curled up and pokey!" '
	for x in combatants:
		spine = vroll('2d4')
		dmg = ((f'{spine.total}')+'[piercing]')
		x.damage(dmg).damage 
		text=text+f'-f "Damage: {spine.result} [piercing]|{str(x)}" '
elif 'hit' in "&*&".lower():
	c.me.add_effect('Prone',f"dis")
	text=text+f'-title "{ch.name} is curled up and prone!" '
	text=text+f'-f "Prone|You are forcibly knocked prone by being hit while curled up." '
elif not "&*&" or 'help' in "&*&".lower() or 'h' in "&*&".lower():
	text=text+f'-title "Hedge Curl Help" '
return f'''embed {text}'''
</drac2>
-thumb "<image>"
-footer "!curl [up|shield|uncurl|hit] or !curl -t Target"