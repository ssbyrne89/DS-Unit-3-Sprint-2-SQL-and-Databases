import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dictionaries

cursor = connection.cursor()



	
cursor.execute('''SELECT 
	count(distinct name) as NumberOfCharacters

FROM charactercreator_character''')



print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT(
                SELECT 
                COUNT(charactercreator_cleric.character_ptr_id)
                	FROM charactercreator_cleric)
                	as ClericCount,
                (SELECT COUNT(charactercreator_mage.character_ptr_id)
                	FROM charactercreator_mage)
                	as MageCount,
                (SELECT COUNT(charactercreator_fighter.character_ptr_id)
                	FROM charactercreator_fighter)
                	as FighterCount,
                (SELECT COUNT(charactercreator_thief.character_ptr_id)
                	FROM charactercreator_thief)
                	as ThiefCount;
            """)


print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT
                COUNT(item_id) AS ItemCount
                FROM armory_item;
              """)

print(dict(cursor.fetchall()[0]))


cursor.execute("""
                SELECT
                COUNT(item_ptr_id) AS NumberOfWeapons
                FROM armory_weapon;
                """)

print(dict(cursor.fetchall()[0]))

cursor.execute("""
                SELECT COUNT(item_id) - COUNT(item_ptr_id) AS nonweapons
                FROM armory_item
                LEFT JOIN armory_weapon
                ON armory_weapon.item_ptr_id = armory_item.item_id;
                """)

print(dict(cursor.fetchall()[0]))

cursor.execute("""
                SELECT charactercreator_character_inventory.character_id, COUNT(charactercreator_character_inventory.item_id) AS item_count FROM charactercreator_character_inventory
                JOIN armory_item
                ON charactercreator_character_inventory.item_id = armory_item.item_id
                GROUP BY character_id
                LIMIT 20;
                """)
print(dict(cursor.fetchall()[0:20]))

cursor.execute("""
                SELECT charactercreator_character_inventory.character_id, COUNT(charactercreator_character_inventory.item_id) AS item_count FROM charactercreator_character_inventory
                JOIN armory_weapon
                ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
                GROUP BY character_id
                LIMIT 20;
                """)
print(dict(cursor.fetchall()[0:20]))

cursor.execute("""
                SELECT AVG(count) AS inventory_avg_items
                FROM
                (SELECT COUNT(charactercreator_character_inventory.item_id) AS count
                FROM charactercreator_character_inventory
                GROUP BY charactercreator_character_inventory.character_id)
                """)

print(dict(cursor.fetchall()[0]))

connection.close()