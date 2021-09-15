<drac2>
cc = "Fores Magic"
spell = "Animal Messenger"
v = "Hedge" in character().race
if v:
   character().create_cc_nx(cc, 0, 1, 'long', 'bubble', reset_to="1")
   character().mod_cc(cc,-1)
   return f'cast "{spell}" -i -phrase "Using their {cc} trait." -f "{cc}|{character().cc_str(cc)}"'
else:
   return f'embed -title "You do not have the {cc} trait!" -desc "Better luck next life!" -color {color} -thumb {image}'
</drac2>