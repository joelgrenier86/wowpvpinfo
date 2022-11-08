from blizzardapi import BlizzardApi
import dload

CLIENTSECRET = ""
def GetUrl(spell_id):
    try:
        r = api_client.wow.game_data.get_spell_media( "us", "en_US", spell_id)
        print(r)
        spellMedia = r['assets'][0]['value']
        return spellMedia
    except r.exceptions.HTTPError as e:
        return print(spell_id)

api_client = BlizzardApi("263d29b290b5433cade43113f901dc03",CLIENTSECRET)

def add_retail_skill_icons():
    textFile = open(r'C:\Users\Joel\Documents\projects\WowPvpInfo\wowpvpinfo\retaildr\static\retailDrInfoNoSpaces.txt', 'r')
    byLine = textFile.readlines()
    for line in byLine:
        print(line)
        data = line.split(',')
        spell_id = data[0]
        print(spell_id)
        iconLink = GetUrl(spell_id)
        target = f"C:\\Users\\Joel\\Documents\\projects\WowPvpInfo\\wowpvpfront\\wowpvpinfo\\quasar-project\\src\\assets\\icons\\{data[2]}.jpg"
        dload.save(iconLink, target)


add_retail_skill_icons()
