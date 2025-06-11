from model import MonsterSpecies, session
import json

monsters = [
    {
        "name": "Zivra",
        "type": "Air",
        "base_stats": {
            "base_hp": 35, "base_attack": 80, "base_defense": 25,
            "scaling": {"hp": 2, "attack": 6, "defense": 1}
        },
        "rarity": 0.1,
        "tier": "Legendary",
        "abilities": [
            {"name": "Zephyr Strike", "type": "Air", "power": 100, "effect": "speed_up"},
            {"name": "Whisper Cloak", "type": "Air", "power": 0, "effect": "evade"}
        ],
        "description": "Banned from competitive battles after sweeping three consecutive world cups with one wing.",
        "strengths": ["Earth"],
        "weaknesses": ["Fire"],
        "evolves_to": None,
        "evolution_level": None,
        "battle_style": "Speedster"
    },
    {
        "name": "Terrosu",
        "type": "Earth",
        "base_stats": {
            "base_hp": 90, "base_attack": 30, "base_defense": 95,
            "scaling": {"hp": 6, "attack": 2, "defense": 5}
        },
        "rarity": 0.35,
        "tier": "Common",
        "abilities": [
            {"name": "Soil Armor", "type": "Earth", "power": 0, "effect": "defense_up"},
            {"name": "Pebble Shot", "type": "Earth", "power": 25}
        ],
        "description": "Common in the Mistlands, Terrosu are favored by novice trainers for their patience and personality.",
        "strengths": ["Air"],
        "weaknesses": ["Water"],
        "evolves_to": "Gaianox",
        "evolution_level": 18,
        "battle_style": "Defensive"
    },
    {
        "name": "Kawa",
        "type": "Water",
        "base_stats": {
            "base_hp": 60, "base_attack": 45, "base_defense": 40,
            "scaling": {"hp": 5, "attack": 3, "defense": 3}
        },
        "rarity": 0.25,
        "tier": "Uncommon",
        "abilities": [
            {"name": "Wave Dance", "type": "Water", "power": 40},
            {"name": "Tide Pull", "type": "Water", "power": 0, "effect": "disable"}
        ],
        "description": "In Eastern folklore, a Kawa that jumps over a waterfall becomes a raincaller.",
        "strengths": ["Fire"],
        "weaknesses": ["Earth"],
        "evolves_to": "Namiyasha",
        "evolution_level": None,
        "battle_style": "Trickster"
    },
    {
        "name": "Ignis Pup",
        "type": "Fire",
        "base_stats": {
            "base_hp": 40, "base_attack": 55, "base_defense": 35,
            "scaling": {"hp": 4, "attack": 4, "defense": 2}
        },
        "rarity": 0.4,
        "tier": "Common",
        "abilities": [
            {"name": "Bark Burn", "type": "Fire", "power": 45},
            {"name": "Ember Sniff", "type": "Fire", "power": 0, "effect": "reveal_enemy"}
        ],
        "description": "Often gifted to children by retired Gym Leaders, but known to chew firewood.",
        "strengths": ["Earth"],
        "weaknesses": ["Water"],
        "evolves_to": "Pyrohound",
        "evolution_level": 12,
        "battle_style": "Loyal"
    },
    {
        "name": "Umbloom",
        "type": "Earth",
        "base_stats": {
            "base_hp": 55, "base_attack": 45, "base_defense": 55,
            "scaling": {"hp": 5, "attack": 3, "defense": 4}
        },
        "rarity": 0.2,
        "tier": "Rare",
        "abilities": [
            {"name": "Spore Cloud", "type": "Earth", "power": 0, "effect": "sleep"},
            {"name": "Petal Slash", "type": "Earth", "power": 50}
        ],
        "description": "Said to bloom only under moonlight. Rangers in the Bloomshade Forest guard them fiercely.",
        "strengths": ["Water"],
        "weaknesses": ["Fire"],
        "evolves_to": None,
        "evolution_level": None,
        "battle_style": "Disabler"
    }
]

for m in monsters:
    monster = MonsterSpecies(
        name=m["name"],
        type=m["type"],
        base_stats=json.dumps(m["base_stats"]),
        rarity=m["rarity"],
        tier=m["tier"],
        abilities=json.dumps(m["abilities"]),
        description=m["description"],
        strengths=json.dumps(m["strengths"]),
        weaknesses=json.dumps(m["weaknesses"]),
        evolves_to=m["evolves_to"],
        evolution_level=m["evolution_level"],
        battle_style=m["battle_style"]
    )
    session.add(monster)

session.commit()
print("🌟 Human-touched monster seed complete.")
