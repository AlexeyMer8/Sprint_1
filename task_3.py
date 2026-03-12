world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Англия'

print(world_champions)

country = 'Италия'

for item in world_champions.values():
    if country != item:
        final_text = 'Италия не выигрывала чемпионат мира по футболу в 21 веке.'
    else:
        final_text = 'Италия cтановилась чемпионом мира по футболу в 21 веке!'
        break
    
print(final_text)