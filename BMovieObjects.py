#!/usr/bin/env python

from itertools import chain

from BMovieConstants import *
from WeightedTuple import WeightedTuple


objectWordLists = {

    nameVehicleSingular : WeightedTuple ( [
        "Battleship",       1,
        "Fighter Jet",      1,
        "Flying Saucer",    1,
        "Hovercraft",       1,
        "Rocket",           1,
        "Ship",             1,
        "Spaceship",        2,
        "Starship",         2,
        "Submarine",        1,
    ] ),

    nameWeaponSingular : WeightedTuple( [
        "Bomb",             1,
        "Cannon",           1,
        "Laser",            1,
        "Machine Gun",      1,
        "Ray Gun",          2,
        "Spear",            1,
        "Sword",            2,
        "Trident",          1,
        "Weapon",           2,
        "Whip",             1,
    ] ),

    nameTechnologySingular : WeightedTuple( [
        "Computer",             1,
        "Electronic Brain",     1,
        "Laser",                1,
        "Magnet",               1,
        "Magnetron",            1,
        "Radar",                1,
        "Radio",                1,
        "Satellite",            1,
        "Transistor",           1,
        "Vacuum Tube",          1,
        "Video",                1,
    ] ),

    nameObjectSingularCommon : WeightedTuple( [
        nameObjectSingularCommon1,      15,
        [
            nameModifier,
            nameObjectSingularCommon1,
        ],                              1,
    ] ),

    nameObjectSingularCommon1 : (
        WeightedTuple( [
            "Android",      2,
            "Book",         1,
            "Clue",         1,
            "Code",         1,
            "Codex",        1,
            "Coffin",       1,
            "Computer",     2,
            "Dream",        1,
            "Ectoplasm",    1,
            "Eye",          1,
            "Mechanoid",    1,
            "Moon",         1,
            "Nightmare",    1,
            "Planet",       1,
            "Robot",        2,
            "Scroll",       1,
            "Secret",       2,
            "Skull",        1,
            "Spell",        1,
            "Star",         1,
            "Tomb",         1,
            "Treasure",     2,
        ] ),
        nameVehicleSingular,
        nameWeaponSingular,
    ),

    nameObjectPluralCommon : WeightedTuple( [
        nameObjectPluralCommon1,        15,
        [
            nameModifier,
            nameObjectPluralCommon1,
        ],                              1,
    ] ),

    nameObjectPluralCommon1 : (
        WeightedTuple( [
            "Androids",     1,
            "Books",        1,
            "Clues",        1,
            "Codes",        1,
            "Coffins",      1,
            "Computers",    1,
            "Dreams",       1,
            "Eyes",         1,
            "Jewels",       1,
            "Mechanoids",   1,
            "Mysteries",    2,
            "Nightmares",   1,
            "Planets",      1,
            "Robots",       1,
            "Secrets",      1,
            "Skulls",       1,
            "Stars",        1,
            "Tombs",        1,
            "Treasures",    1,
        ] ),
        nameVehiclePlural,
        nameWeaponPlural,
    ),

    nameVehiclePlural : WeightedTuple( [
        "Battleships",  1,
        "Fighter Jets", 1,
        "Rockets",      1,
        "Ships",        1,
        "Spaceships",   2,
        "Starships",    1,
        "Submarines",   1,
        "Tanks",        1,
    ] ),

    nameWeaponPlural : WeightedTuple( [
        "Bombs",        1,
        "Cannons",      1,
        "Guns",         1,
        "Lasers",       1,
        "Machine Guns", 1,
        "Ray Guns",     2,
        "Spears",       1,
        "Swords",       2,
        "Tridents",     1,
        "Weapons",      2,
    ] ),

    nameTimeSingular : WeightedTuple( [
        "Second",       1,
        "Minute",       2,
        "Hour",         3,
        "Day",          4,
        "Week",         2,
        "Month",        2,
        "Year",         2,
        "Decade",       1,
        "Century",      1,
    ] ),

    nameTimePlural : WeightedTuple( [
        "Seconds",      1,
        "Minutes",      2,
        "Hours",        3,
        "Days",         4,
        "Weeks",        2,
        "Months",       2,
        "Years",        2,
        "Decades",      1,
        "Centuries",    1,
    ] ),

    nameObjectProper : WeightedTuple( [
        nameObjectProperSimple,                     5,
        [
            'The',
            WeightedTuple( [
                [
                    adjectiveObject,
                    nameObjectSingularCommon,
                ],                              3,
                [
                    adjectiveObject,
                    nameWeaponSingular,
                ],                              2,
                nameObjectSingularCommon,       5,
                nameWeaponSingular,             3,
            ] ),
            'of',
            WeightedTuple( [
                namePlaceProper,                3,
                [ 'The', nameDirection ],       1,
                nameHeroSingularProper,         3,
                nameHeroPluralProper,           3,
                nameVillainSingularProper,      2,
                nameVillainPluralProper,        2,
            ] )
        ],                                          6,
        [
            'The',
            adjectiveObject,
            nameObjectSingularCommon
        ],                                          6,
        [
            'The',
            adverbAdjective,
            adjectiveObjectBase,
            nameObjectSingularCommon
        ],                                          2,
        [
            nameHeroSingularProperSimplePossessive,
            ( nameObjectSingularCommon, nameWeaponSingular ),
        ],                                                  2,
        [
            nameHeroSingularProperSimplePossessive,
            ( nameConceptPositive, nameConceptNeutral ),
        ],                                                  1,
        [
            nameHeroSingularProperSimplePossessive,
            adjectiveObject,
            nameObjectSingularCommon,
        ],                                                  2,
        [
            nameHeroSingularProperSimplePossessive,
            nameObjectSingularCommon,
            'of',
            ( nameConceptPositive, nameConceptNeutral ),
        ],                                                  2,
        [
            nameVillainSingularProperSimplePossessive,
            nameObjectSingularCommon,
            'of',
            ( nameConceptPositive, nameConceptNeutral ),
        ],                                                  1,
        [
            nameHeroSingularProperSimplePossessive,
            adjectiveObject,
            nameObjectSingularCommon,
            'of',
            ( nameConceptPositive, nameConceptNeutral ),
        ],                                                  1,
        [
            nameVillainSingularProperSimplePossessive,
            adjectiveObject,
            nameObjectSingularCommon,
            'of',
            ( nameConceptNegative, nameConceptNeutral ),
        ],                                                  1,
    ] ),

    nameObjectProperSimple : WeightedTuple( (
        "Excalibur",
        "The Atomic Bomb",
        "The Holy Grail",
        "DaVinci's Code",
        "Edison's Folly",
        "The Bible Code",
        "The Secret Code",
        "The Enigma Machine",
        "The Voynich Manuscript",
        "The Maltese Falcon",
    ) ),


#//**********************************************************************
#//
#//  possessions - probably needs to be folded into other categories
#//
#//**********************************************************************

    namePossessionHeroSingular : WeightedTuple( [
        "Betrayal",             2,
        "Bravery",              3,
        "Choice",               1,
        "Conquest",             3,
        "Daughter",             1,
        "Decision",             1,
        "Fury",                 2,
        "Gun",                  1,
        "Guns",                 1,
        "Heroism",              3,
        "Legacy",               1,
        "Reign",                1,
        "Revenge",              1,
        "Righteousness",        1,
        "Son",                  1,
        "Sacrifice",            1,
        "Sword",                2,
        "Triumph",              2,
        "Victory",              2,
        "Wife",                 1,
        "Wrath",                1,
    ] ),

    namePossessionHeroPlural : WeightedTuple( [
        "Children",             2,
        "Choices",              1,
        "Conquests",            3,
        "Daughters",            2,
        "Enemies",              3,
        "Sons",                 2,
        "Swords",               1,
        "Triumphs",             2,
    ] ),


    namePossessionVillainSingular : WeightedTuple( [
        "Choice",               1,
        "Conquest",             3,
        "Daughter",             1,
        "Defeat",               2,
        "Downfall",             2,
        "Fury",                 2,
        "Gun",                  1,
        "Guns",                 1,
        "Invasion",             1,
        "Legacy",               1,
        "Reign",                1,
        "Revenge",              2,
        "Slave",                1,
        "Son",                  1,
        "Sword",                2,
        "Victim",               1,
        "Villainy",             1,
        "Wrath",                1,
    ] ),

    namePossessionVillainPlural : WeightedTuple( [
        "Children",             2,
        "Conquests",            3,
        "Daughters",            2,
        "Enemies",              3,
        "Slaves",               2,
        "Sons",                 2,
        "Victims",              2,
        "Wives",                2,
    ] ),

    prepositionalPhraseSingularCommon : WeightedTuple( [
        "Above",                1,
        "Against",              1,
        "Beneath",              1,
        "Beyond",               2,
        "In Search of",         2,
        "In",                   2,
        "Inside",               1,
        "On",                   2,
    ] ),

    prepositionalPhraseEvent : WeightedTuple( (
        "After",
        "Before",
        "During"
    ) ),

    prepositionalPhraseSingularProper : WeightedTuple( [
        "Above",                    1,
        "Beneath",                  1,
        "Beyond",                   2,
        "In",                       3,
        "Inside",                   1,
        "Outside of",               1,
        "On The Outskirts of",      1,
        "Near",                     2,
    ] ),

    prepositionalPhrasePluralCommon : WeightedTuple( (
        "Against",
        "Amidst",
        "Among",
        "Around",
        "At",
        "Beneath",
        "Beyond",
        "In Search of",
        "Inside",
        "Near",
        "Outside",
        "Underneath",
    ) ),

    prepositionalPhrasePluralProper : WeightedTuple( (
        "Against",
        "Alone In",
        "Amidst",
        "Among",
        "Around",
        "At",
        "Beneath",
        "Beyond",
        "In Search of",
        "Inside",
        "Near",
        "Outside",
        "Underneath",
    ) ),
}

