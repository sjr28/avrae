<drac2>
cc = "Volgar's Rapier"
character().create_cc_nx(cc, 0, 1, 'long', 'bubble', reset_to="1")
args,c=argparse(&ARGS&),combat()
dmg=vroll("4d6[necrotic]")
halfdmg = floor(dmg.total/2)
tgt=args.get('t')
combatants=[c.get_combatant(x) for x in tgt] if c else []
target = combatants[0]
v = character().get_cc(cc)==1
save = target.save("con")
didSave = save.total>=16
savestatus = "Success!" if didSave else "Failure!"
damage = target.damage("4d6[necrotic]/2") if didSave else target.damage("4d6[necrotic]")
totaldmg = damage['total']

if character().get_cc(cc)<1:
  return f'''embed -title "{cc} is all out of charges!" -desc "Good try though {name}." '''

else:
  character().mod_cc(cc, -1)
  target.set_maxhp(target.max_hp-totaldmg)
  character().modify_hp(totaldmg,overflow=False)
  return f'''embed -title "{name} strikes with exceptional force with {cc}" -f "Meta|**DC**: 16" -f "**{target.name}**|**CON Save**: {save}; {savestatus}\n {damage['damage']}\n **Effect**: {target.name} max HP reduced by {totaldmg}!\n **Lifesteal**: {name} regains {totaldmg} HP! \n {name}: {character().hp_str()}" '''

#-title "Nissa's Cannon used Protect!" -desc  "It gave the targets {{thp}} temp hp!" -f "Given to:|{{'\n'.join([x.name for x in combatants]) or "*None*" if c else "This channel is not in combat."}}" -footer "{{'\n'.join([str(x) for x in combatants])}}"
</drac2>
-f "{{cc}}|{{character().cc_str(cc)}}" 
-thumb https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c65576f6-89f4-424e-b027-0d4b70c2f3b1/d4a3of-47cfa1fc-a214-47b6-8e8d-6ad29e7ab3bf.jpg/v1/fill/w_966,h_568,q_75,strp/vapiric_rapier_by_aslyrogue_d4a3of-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTY4IiwicGF0aCI6IlwvZlwvYzY1NTc2ZjYtODlmNC00MjRlLWIwMjctMGQ0YjcwYzJmM2IxXC9kNGEzb2YtNDdjZmExZmMtYTIxNC00N2I2LThlOGQtNmFkMjllN2FiM2JmLmpwZyIsIndpZHRoIjoiPD05NjYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.WDlsh24s6OUaZJdugaT0ITr_wN3joDGsmOSZ8ewlsSw
-footer "!volgars -t target"
