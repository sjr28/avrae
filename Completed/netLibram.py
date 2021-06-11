!alias netlibram embed
<drac2>
theRoll = roll("1d10000")
kQ = get_gvar("1569f7e0-a4e8-4014-9ce8-769ad12b71aa")
kQ = get_gvar("142b0ac9-b33e-4b35-828d-4794a1370c3d") if (theRoll > 1000 and theRoll < 2001) else kQ
kQ = get_gvar("be6b4291-2f23-4028-adec-3184c73b0e29") if (theRoll > 2000 and theRoll < 3001) else kQ
kQ = get_gvar("93b6415e-dd8c-44ff-bd0b-2af6554f5a52") if (theRoll > 3000 and theRoll < 4001) else kQ
kQ = get_gvar("eda61c92-fc3a-4935-9e2c-af086b318c3f") if (theRoll > 4000 and theRoll < 5001) else kQ
kQ = get_gvar("1a14a50e-ca6d-4e67-9bf9-260a87390155") if (theRoll > 5000 and theRoll < 6001) else kQ
kQ = get_gvar("920b5d52-f481-4d40-9f03-b7d460581dd5") if (theRoll > 6000 and theRoll < 7001) else kQ
kQ = get_gvar("1494aa28-b023-4948-9b22-b7dcf9ffe75f") if (theRoll > 7000 and theRoll < 8001) else kQ
kQ = get_gvar("bc879196-1233-495a-a476-b7fbf24729e1") if (theRoll > 8000 and theRoll < 9001) else kQ
kQ = get_gvar("7f6140f9-66e5-4408-8057-f6b7f168c1c6") if (theRoll > 9000 and theRoll < 10001) else kQ
x1 = kQ.split("\n")
x2 = int(theRoll / 100)
x3 = x1[x2][5:]

return f'''embed -title "{name} rolls a {theRoll} on the Net Libram of Random Magical Effects!" -desc "{str(x3)}" '''

</drac2>
-footer "!netlibram"