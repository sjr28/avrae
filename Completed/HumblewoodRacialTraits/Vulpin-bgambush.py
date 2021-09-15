<drac2>
cc = "Bewitching Guile - Ambush Prey"
spell = "Ambush Prey"
v = 'Vulpin' in character().race and level>2
if not v:
   return f'embed -title "You do not have the {cc} trait!" -desc "Better luck next life!" -color {color} -thumb {image}'
else:
   character().create_cc_nx(cc, 0, 1, 'long', 'bubble', reset_to="1")
   if character().get_cc(cc)<1:
      return f'embed -title "{name} tries to cast {spell} using {cc}!" -desc "You must complete a long rest before using this trait again." -f "{cc}|{character().cc_str(cc)}" -color {color} -thumb {image}'
   character().mod_cc(cc,-1)
   return f'cast "{spell}" -i -dc {intelligenceMod+proficiencyBonus+8} -phrase "Using their {cc} trait." -f "{cc}|{character().cc_str(cc)}"'
</drac2>