from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
import time
import csv



def main():
    heroDict = {
"":0,
"Abaddon":102,
"Alchemist":73,
"Ancient Apparition":68,
"Anti-Mage":1,
"Arc Warden":113,
"Axe":2,
"Bane":3,
"Batrider":65,
"Beastmaster":38,
"Bloodseeker":4,
"Bounty Hunter":62,
"Brewmaster":78,
"Bristleback":99,
"Broodmother":61,
"Centaur Warrunner":96,
"Chaos Knight":81,
"Chen":66,
"Clinkz":56,
"Clockwerk":51,
"Crystal Maiden":5,
"Dark Seer":55,
"Dark Willow":119,
"Dazzle":50,
"Death Prophet":43,
"Disruptor":87,
"Doom":69,
"Dragon Knight":49,
"Drow Ranger":6,
"Earth Spirit":107,
"Earthshaker":7,
"Elder Titan":103,
"Ember Spirit":106,
"Enchantress":58,
"Enigma":33,
"Faceless Void":41,
"Grimstroke":121,
"Gyrocopter":72,
"Huskar":59,
"Invoker":74,
"Io":91,
"Jakiro":64,
"Juggernaut":8,
"Keeper of the Light":90,
"Kunkka":23,
"Legion Commander":104,
"Leshrac":52,
"Lich":31,
"Lifestealer":54,
"Lina":25,
"Lion":26,
"Lone Druid":80,
"Luna":48,
"Lycan":77,
"Magnus":97,
"Mars":129,
"Medusa":94,
"Meepo":82,
"Mirana":9,
"Monkey King":114,
"Morphling":10,
"Naga Siren":89,
"Nature's Prophet":53,
"Necrophos":36,
"Night Stalker":60,
"Nyx Assassin":88,
"Ogre Magi":84,
"Omniknight":57,
"Oracle":111,
"Outworld Devourer":76,
"Pangolier":120,
"Phantom Assassin":44,
"Phantom Lancer":12,
"Phoenix":110,
"Puck":13,
"Pudge":14,
"Pugna":45,
"Queen of Pain":39,
"Razor":15,
"Riki":32,
"Rubick":86,
"Sand King":16,
"Shadow Demon":79,
"Shadow Fiend":11,
"Shadow Shaman":27,
"Silencer":75,
"Skywrath Mage":101,
"Slardar":28,
"Slark":93,
"Snapfire":128,
"Sniper":35,
"Spectre":67,
"Spirit Breaker":71,
"Storm Spirit":17,
"Sven":18,
"Techies":105,
"Templar Assassin":46,
"Terrorblade":109,
"Tidehunter":29,
"Timbersaw":98,
"Tinker":34,
"Tiny":19,
"Treant Protector":83,
"Troll Warlord":95,
"Tusk":100,
"Underlord":108,
"Undying":85,
"Ursa":70,
"Vengeful Spirit":20,
"Venomancer":40,
"Viper":47,
"Visage":92,
"Void Spirit":126,
"Warlock":37,
"Weaver":63,
"Windranger":21,
"Winter Wyvern":112,
"Witch Doctor":30,
"Wraith King":42,
"Zeus":22}
    driver = webdriver.Chrome()
    listOfUrls = ["https://hawkbets.com/matches/recent/2020-05-16",
                  "https://hawkbets.com/matches/recent/2020-05-15",
                  "https://hawkbets.com/matches/recent/2020-05-14",
                  "https://hawkbets.com/matches/recent/2020-05-13",
                  "https://hawkbets.com/matches/recent/2020-05-12",
                  "https://hawkbets.com/matches/recent/2020-05-11",
                  "https://hawkbets.com/matches/recent/2020-05-10",
                  "https://hawkbets.com/matches/recent/2020-05-09",
                  "https://hawkbets.com/matches/recent/2020-05-08",
                  "https://hawkbets.com/matches/recent/2020-05-07",
                  "https://hawkbets.com/matches/recent/2020-05-06",
                  "https://hawkbets.com/matches/recent/2020-05-05",
                  "https://hawkbets.com/matches/recent/2020-05-04",
                  "https://hawkbets.com/matches/recent/2020-05-03",
                  "https://hawkbets.com/matches/recent/2020-05-02"]
    heroesWoEmpty = []
    winWoEmpty = []
    for date in listOfUrls:
        driver.get(date)
        time.sleep(2)
        winner= driver.find_elements_by_class_name("live-series__winner")
        winner1=[v for k,v in enumerate(winner) if not k%2]
        heroes = driver.find_elements_by_class_name("live-series__heroes")
        heroes1=[v for k,v in enumerate(heroes) if not k%2]
        heroes2=[v for k,v in enumerate(heroes) if k%2]
        win = []
        hero1 = []
        hero2 = []
        for elem in winner1:
            try: elem.find_element_by_tag_name("img")
            except Exception:
                win.append(2) # win 2 team
            else:
                win.append(1) # win 1 team
        for elem in heroes1:
            imgs = elem.find_elements_by_tag_name("img")
            for el in imgs:
                try: el.get_attribute("alt")
                except Exception:
                    hero1.append(0)
                else:
                    hero1.append(el.get_attribute("alt"))
        for elem in heroes2:
            imgs = elem.find_elements_by_tag_name("img")
            for el in imgs:
                try: el.get_attribute("alt")
                except Exception:
                    hero2.append(0)
                else:
                    hero2.append(el.get_attribute("alt"))
        heroes = []
        for n in range(0,len(hero1),5):
            heroes.append([heroDict[hero1[n]],heroDict[hero1[n+1]],heroDict[hero1[n+2]],heroDict[hero1[n+3]],heroDict[hero1[n+4]],heroDict[hero2[n]],heroDict[hero2[n+1]],heroDict[hero2[n+2]],heroDict[hero2[n+3]],heroDict[hero2[n+4]]])
        iterator = 0
        for team in heroes:
            if 0 not in team:
                heroesWoEmpty.append(heroes[iterator])
                winWoEmpty.append(win[iterator])
            iterator+=1
            
    FILENAME = "inHeroes.csv"
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(heroesWoEmpty)
    FILENAME = "outResults.csv"
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(winWoEmpty)
    print("foo")  
    
   # for elem in matchElements:

if __name__ == "__main__":
    main()