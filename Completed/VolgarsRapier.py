<drac2>
cc = "Volgar's Rapier"
cc2 = "Volgar's Rapier - Root Strike"
character().create_cc_nx(cc, 0, 1, 'long', 'bubble', reset_to="1")
character().create_cc_nx(cc2, 0, 2, 'long', 'bubble', reset_to="2")
args = &ARGS&
a,c=argparse(&ARGS&),combat()
dmg=vroll("4d6[necrotic]")
halfdmg = floor(dmg.total/2)
tgt=a.get('t') if a.get('t') else None
#return f'''embed -title "{tgt}"'''
combatants=[c.get_combatant(x) for x in tgt] if c else []
target = combatants[0] if c else None

if args[0].lower() in 'root strike':
  if character().get_cc(cc2)<1:
    return f'''embed -title "{cc2} is all out of charges!" -desc "Good try though {name}." '''
  elif not target:
    return f'''embed -title "{name} examines their {cc2}" -desc "Twice per day, your rapier is now able to also cast Root Strike. You plunge the sword tip into the ground and summon roots to constrict up to 2 foes within 120 ft. On failure, they are restrained and take 3d8 + 8 magical bludgeoning. Each turn they fail to escape is another 3d8 + 8. The DC is equal to a nature check you make when you cast it, contested by a DEX save, then athletics to break free. Lasts for one minute." '''
  elif c:
    damage = vroll("3d8+8[magical bludgeoning]")
    if a.get('t'):
      character().mod_cc(cc2, -1)
      dc = vroll(character().skills.nature.d20())
      out = [f''' -f "Meta|**Damage**:\n{damage}\n**DC**:\n{dc}"''']
      targets, targetArgs = [], {}
      for targ in a.get('t'):
        targName, targArgs = (targ.split("|")+[""])[:2]
        targArgs = argparse(targArgs)
        if curTarg := c.get_combatant(targName):
          targets.append(curTarg)
          a.add_context(curTarg.name, argparse(targArgs))
          targetArgs[curTarg.name] = targArgs
        elif curTarg := c.get_group(targName):
          for gTarg in curTarg.combatants:
            targets.append(gTarg)
            a.add_context(gTarg.name, argparse(targArgs))
            targetArgs[gTarg.name] = targArgs
      for target in targets:
        targName = target.name
        targBonus = targetArgs[targName].get('sb')
        dice = target.saves.get("dex").d20(targetArgs[targName].adv(boolwise=True, custom={'adv': 'sadv', 'dis': 'sdis'}))
        saveRoll = vroll(f'{dice} {"+"+"+".join(targBonus) if targBonus else ""}')
        out.append(f''' -f "{targName}|**DEX Save:** {saveRoll}; {['Failure!', target.damage(damage.consolidated()), target.add_effect('Restrained - Root Strike','',10,end=True)][0] if saveRoll.total<dc.total else 'Success!'} \n {f"""**Effect:** {target.get_effect('Restrained - Root Strike')}""" if saveRoll.total<dc.total else ''} \n {f"""**{targName}:** {target.hp_str()}""" if saveRoll.total<dc.total else ''}"''')
      return f'''embed -title "{name} uses {cc2}!" {' '.join(out)} -f "Volgar's Rapier - Root Strike|Twice per day, your rapier is now able to also cast Root Strike. You plunge the sword tip into the ground and summon roots to constrict up to 2 foes within 120 ft. On failure, they are restrained and take 3d8 + 8 magical bludgeoning. Each turn they fail to escape is another 3d8 + 8. The DC is equal to a nature check you make when you cast it, contested by a DEX save, then athletics to break free. Lasts for one minute."'''
    else:
      return f'''embed -title "No targets"'''
  else:
    return f'''embed -title "Not in combat"'''

elif character().get_cc(cc)<1:
  return f'''embed -title "{cc} is all out of charges!" -desc "Good try though {name}." '''

elif not target:
  return f'''embed -title "{name} examines their {cc}" -desc "You gain a +1 bonus to attack and damage rolls made with this magic weapon. \n \n When you hit a creature with this weapon, you may channel the rapier's energy to strike with exceptional force. The target must make a DC 16 constitution saving throw or take 4d6 necrotic damage, half damage on a success. The target’s hit point maximum is reduced by an amount equal to the necrotic damage taken, and you regain hit points equal to that amount. The rapier can't be used this way again until the next dawn.\n \nYou feel a certain uneasiness, but you can't quite place it. You have disadvantage on charisma saving throws and can speak abyssal. You are unable to remove the rapier from your person or break your attunement to it." '''

else:
  save = target.save("con")
  didSave = save.total>=16
  savestatus = "Success!" if didSave else "Failure!"
  damage = target.damage("4d6[necrotic]/2") if didSave else target.damage("4d6[necrotic]")
  totaldmg = damage['total']
  character().mod_cc(cc, -1)
  target.set_maxhp(target.max_hp-totaldmg)
  character().modify_hp(totaldmg,overflow=False)
  return f'''embed -title "{name} strikes with exceptional force with {cc}" -f "Meta|**DC**: 16" -f "**{target.name}**|**CON Save**: {save}; {savestatus}\n {damage['damage']}\n **Effect**: {target.name} max HP reduced by {totaldmg}!\n **Lifesteal**: {name} regains {totaldmg} HP! \n {name}: {character().hp_str()}" '''

</drac2>
-f "{{cc}}|{{character().cc_str(cc)}}" 
-f "{{cc2}}|{{character().cc_str(cc2)}}" 
-thumb https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c65576f6-89f4-424e-b027-0d4b70c2f3b1/d4a3of-47cfa1fc-a214-47b6-8e8d-6ad29e7ab3bf.jpg/v1/fill/w_966,h_568,q_75,strp/vapiric_rapier_by_aslyrogue_d4a3of-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTY4IiwicGF0aCI6IlwvZlwvYzY1NTc2ZjYtODlmNC00MjRlLWIwMjctMGQ0YjcwYzJmM2IxXC9kNGEzb2YtNDdjZmExZmMtYTIxNC00N2I2LThlOGQtNmFkMjllN2FiM2JmLmpwZyIsIndpZHRoIjoiPD05NjYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.WDlsh24s6OUaZJdugaT0ITr_wN3joDGsmOSZ8ewlsSw
-footer "!volgars -t target or !volgars root -t target1 -t target2"
