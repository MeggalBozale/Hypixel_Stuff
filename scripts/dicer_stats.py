drops = {
    'Uncommon': 341,
    'Rare': 99,
    'Crazy Rare': 14,
    'RNGesus': 2
}

loot = {
    'Uncommon': 1 * 160,
    'Rare': 5 * 160,
    'Crazy Rare': 59 * 160,
    'RNGesus': 2 * 160 * 160
}
rows = 694 * 324 # amount of melon blocks in 1 row

bonus = 0
for key in drops:
    value = drops[key]
    print(f"{key}: {value}/{rows} | ~{round(value/rows*100,8)}%")
    bonus += (value/rows) * loot[key]
print(bonus)

# Proposed drop rates as 0-1 float
drops['Uncommon'] = 0.0015
drops['Rare'] = 0.0005
drops['Crazy Rare'] = 0.00005
drops['RNGesus'] = 0.00001

bonus = 0
print('Proposed drop rates:')
for key in drops:
    print(f"{key}: {drops[key]*100}%")
    bonus += drops[key] * loot[key]
print(f"This has a bonus of {bonus}")
