!alias whiteydrink embed
<drac2>
#Define variables for later use
cc = "Relentless Endurance"
desc = "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead."
rest = "You can’t use this feature again until you finish a long rest."
hasHP = "You have not been reduced to 0 hit points."
noCC = "You do not have this ability."
ch=character()

#Create the counter if it should exist but doesn't already
if ch.race.lower() == "half-orc":
    ch.create_cc_nx(cc, 0, 1, "long", "bubble", None, None, cc, desc+" "+rest)

#Logic of the alias. Check for all the necessary conditions
succ = "tries to use"
if ch.cc_exists(cc) and ch.get_cc(cc) and not ch.hp:
    succ = "uses"
    D = desc
    ch.mod_cc(cc, -1)
    ch.set_hp(1)
elif ch.hp:
    D = hasHP
elif ch.cc_exists(cc):
    D = rest
else:
    D = noCC

#Prepare the output
T = f"{name} {succ} {cc}!"
F = f"{cc}|{ch.cc_str(cc) if ch.cc_exists(cc) else '*None*'}"
</drac2>
-title "{{T}}"
-desc "{{D}}"
-f "{{F}}"
-color <color>
-thumb <image>