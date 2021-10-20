.alias tokecheck embed
<drac2>
name = "&1&"
namelower = name.lower()
nametitle = name.title()
G = load_json(get_gvar("51bee7f1-c3d0-41e4-af9c-fe0d1e69c981"))

if namelower in G.Monsters:
  token = G.Monsters[namelower].Token if "Token" in G.Monsters[namelower] else "N/A"
  size = G.Monsters[namelower].Size if "Size" in G.Monsters[namelower] else "N/A"
  return f'''embed -title "Found {name}" -desc "Token: {token}. Size: {size}" '''
elif nametitle in G.Monsters:
  token = G.Monsters[nametitle].Token if "Token" in G.Monsters[nametitle] else "N/A"
  size = G.Monsters[nametitle].Size if "Size" in G.Monsters[nametitle] else "N/A"
  return f'''embed -title "Found {name}" -desc "Token: {token}. Size: {size}" '''
else:
  return f'''embed -title "Did not find {name}" -desc "Get better at spelling or something I dunno" '''

</drac2>