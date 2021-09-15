<drac2>
cc = "Appraising Eye"
desc = "You have an almost supernatural ability to appraise objects. By spending an action examining any object, you can determine any magical properties the item has, how they might be used or activated, as well as a fair estimation of market price. Using this skill strains the eyes, and you must complete a long or short rest before you can use it again."
hdg = 'Corvum' in character().race
if not hdg:
	return f'''embed -title "You are not a Corvum!" -desc "Your eye doesn\'t see shit." '''
else:
	character().create_cc_nx(cc, 0, 1, 'short', 'bubble', reset_to="1")
	if character().get_cc(cc)<1:
  		return f'''embed -title "{name}\'s eye is tired!" -desc "Rest up and try again." '''
	character().mod_cc(cc, -1)
	return f'''embed -title "{name} uses {cc}" -desc "{desc}" -footer "{cc}\n{character().cc_str(cc)}"'''
</drac2>
-thumb "<image>"