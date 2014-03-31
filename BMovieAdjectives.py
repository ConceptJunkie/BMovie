#!/usr/bin/env python

from BMovieConstants import *
from WeightedTuple import WeightedTuple


adjectiveWordLists = {

#//**********************************************************************
#//
#//  adjectives
#//
#//**********************************************************************

    adjectiveTexture : WeightedTuple( [
        "Alabaster",    1,
        "Amber",        2,
        "Azure",        1,
        "Black",        3,
        "Blue",         2,
        "Cerulean",     1,
        "Crimson",      2,
        "Ebony",        2,
        "Glimmering",   1,
        "Glistening",   1,
        "Glowing",      1,
        "Golden",       2,
        "Green",        2,
        "Grey",         1,
        "Many-Colored", 1,
        "Mottled",      1,
        "Orange",       1,
        "Pale",         1,
        "Psychedelic",  1,
        "Purple",       1,
        "Red",          3,
        "Shining",      1,
        "Shiny",        1,
        "Silvery",      1,
        "Sparkling",    1,
        "Speckled",     1,
        "Spotted",      1,
        "Vermillion",   1,
        "Violet",       1,
        "White",        3,
        "Yellow",       1,
    ] ),

    adjectiveTime : WeightedTuple( [
        "Ancient",      1,
        "Atom-Age",     1,
        "Eternal",      1,
        "Never-Ending", 1,
        "Prehistoric",  1,
        "Unending",     1,
    ] ),

    adjectiveMentalHero : WeightedTuple( [
        "Angry",        1,
        "Bold",         2,
        "Brave",        3,
        "Confused",     1,
        "Cpourageous",  1,
        "Crazy",        1,
        "Daring",       3,
        "Dedicated",    1,
        "Defiant",      3,
        "Determined",   1,
        "Dreaming",     1,
        "Enraged",      1,
        "Fearless",     3,
        "Furious",      1,
        "Gallant",      2,
        "Heroic",       3,
        "Indomitable",  1,
        "Insane",       1,
        "Intrepid",     2,
        "Reckless",     1,
        "Reluctant",    1,
        "Renegade",     1,
        "Stalwart",     1,
        "Unstoppable",  1,
        "Valiant",      2,
    ] ),

    adjectiveMentalVillain : WeightedTuple( [
        "Angry",        1,
        "Bold",         2,
        "Brave",        3,
        "Confused",     1,
        "Cpourageous",  1,
        "Crazy",        1,
        "Cynical",      1,
        "Daring",       3,
        "Dedicated",    1,
        "Defiant",      3,
        "Deranged",     1,
        "Deviant",      1,
        "Dreaming",     1,
        "Enraged",      1,
        "Frenzied",     1,
        "Furious",      1,
        "Insane",       1,
        "Maniacal",     1,
        "Murderous",    1,
        "Reckless",     1,
        "Renegade",     1,
        "Twisted",      1,
        "Unkillable",   1,
        "Unrepentant",  1,
        "Unstoppable",  1,
        "Villainous",   1,
    ] ),

    adjectivePhysicalHero : WeightedTuple( [
        "Beautiful",    1,
        "Cybernetic",   1,
        "Mutant",       1,
        "Radioactive",  1,
    ] ),

    adjectivePhysicalVillain : WeightedTuple( [
        "50-Foot",      1,
        "Colossal",     1,
        "Cybernetic",   2,
        "Decomposing",  1,
        "Ectoplasmic",  1,
        "Exploding",    1,
        "Fanged",       1,
        "Giant",        1,
        "Gigantic",     2,
        "Invisible",    1,
        "Monstrous",    1,
        "Mutant",       2,
        "Poisonous",    1,
        "Radioactive",  2,
        "Skeletal",     1,
        "Shriveled",    1,
        "Shrunken",     1,
        "Slimy",        1,
        "Venemous",     1,
    ] ),

    adjectiveVocationHero : WeightedTuple( [
        "Ninja",        1,
    ] ),

    adjectiveVocationVillain : WeightedTuple( [
        "Ninja",        1,
        "Pirate",       1,
    ] ),

    adjectiveActionHero : WeightedTuple( [
        "Conquering",           1,
        "Death-Defying",        1,
        "Dimension-Hopping",    1,
        "Howling",              1,
        "Kick-boxing",          1,
        "Morphing",             1,
        "Swaggering",           1,
        "Time-Travelling",      1,
    ] ),

    adjectiveActionVillain : WeightedTuple( [
        "Blood-Sucking",        1,
        "Brain-Eating",         1,
        "Dimension-Hopping",    1,
        "Horrifying",           1,
        "Howling",              1,
        "Kick-boxing",          1,
        "Killing",              1,
        "Lurching",             1,
        "Mind-Controlling",     1,
        "Morphing",             1,
        "Murdering",            1,
        "Screaming",            1,
        "Shambling",            1,
        "Swaggering",           1,
        "Terrifying",           1,
        "Time-Travelling",      1,
    ] ),

    adjectiveAge : WeightedTuple( [
        "Baby",         1,
        "Kid",          1,
        "Teenage",      3,
        "Elderly",      3,
        "Decrepit",     1,
        "Ancient",      3,
    ] ),

    adjectiveBaseHero : WeightedTuple( [
        "Accidental",           1,
        "All-Powerful",         1,
        "Amazing",              2,
        "Crosstime",            1,
        "Dangerous",            2,
        "Deadly",               2,
        "Glorious",             1,
        "Holy",                 1,
        "Impossible",           2,
        "Lost",                 2,
        "Masked",               1,
        "Mighty",               1,
        "Mystic",               1,
        "Magical",              1,
        "Mysterious",           3,
        "Powerful",             1,
        "Rocket",               1,
        "Savage",               1,
        "Space",                1,
        "Transdimensional",     1,
        "Unstoppable",          1,
        "Wild",                 2,
    ] ),

    adjectiveBaseVillain : WeightedTuple( [
        "Accidental",           1,
        "All-Powerful",         1,
        "Blood-Curdling",       1,
        "Criminal",             2,
        "Crosstime",            1,
        "Deadly",               2,
        "Dreadful",             1,
        "Elusive",              1,
        "Evil",                 2,
        "Feral",                1,
        "Ghostly",              1,
        "Horrible",             1,
        "Imooral",              1,
        "Impossible",           2,
        "Inhuman",              1,
        "Killer",               1,
        "Lost",                 2,
        "Masked",               1,
        "Monstrous",            1,
        "Mutant",               1,
        "Mysterious",           3,
        "Phantom",              1,
        "Phantasmal",           1,
        "Powerful",             1,
        "Shapeless",            1,
        "Sinister",             1,
        "Space",                1,
        "Subhuman",             1,
        "Superhuman",           1,
        "Terrible",             1,
        "Transdimensional",     1,
        "Unkillable",           1,
        "Unknowable",           1,
        "Unstoppable",          1,
        "Voodoo",               1,
        "Wicked",               1,
        "Wild",                 2,
    ] ),

    adjectiveGeographic : WeightedTuple( (
        "African",              1,
        "Alien",                1,
        "Altairian",            1,
        "American",             1,
        "Ancient",              1,
        "Antarian",             1,
        "Astral",               1,
        "Atlantean",            1,
        "Aztec",                1,
        "Babylonian",           1,
        "Cave",                 1,
        "Celtic",               1,
        "Chinese",              1,
        "Cydonian",             1,
        "Egyptian",             1,
        "Elbonian",             1,
        "Etherial",             1,
        "Extra-Dimensional",    1,
        "Extra-Terrestrial",    1,
        "Human",                1,
        "Interstellar",         1,
        "Japanese",             1,
        "Jovian",               1,
        "Lemurian",             1,
        "Lost",                 1,
        "Lunar",                1,
        "Moon",                 1,
        "Martian",              1,
        "Mountain",             1,
        "Night",                1,
        "Orion",                1,
        "Plutonian",            1,
        "Rigelian",             1,
        "Roman",                1,
        "Russian",              1,
        "Stygian",              1,
        "Subterranean",         1,
        "Sumerian",             1,
        "Swamp",                1,
        "Terran",               1,
        "Venusian",             1,
    ) ),

    adjectiveObjectBase : WeightedTuple( (
        "Adamantine",
        "All-Powerful",
        "Animatronic",          1,
        "Crosstime",
        "Crystal",
        "Cybernetic",
        "Dangerous",
        "Deadly",
        "Digital",
        "Dimension-Hopping",
        "Electronic",
        "Enchanted",
        "Eternal",
        "Faceless",
        "Giant",
        "Hidden",
        "Holy",
        "Huge",
        "Impossible",
        "Incredible",
        "Legendary",
        "Lost",
        "Magical",
        "Mechanical",
        "Miniature",
        "Morphing",
        "Mysterious",
        "Radioactive",
        "Robotic",
        "Time-Travelling",
        "Unknown",
        "Unstoppable",
    ) ),

    adjectiveObject : WeightedTuple( [
        adjectiveObjectBase,    2,
        adjectiveTexture,       1,
        adjectiveGeographic,    1,
    ] ),

    adjectivePlaceBase : WeightedTuple( (
        "Amazing",
        "Beautiful",
        "Dangerous",
        "Deadly",
        "Dark",
        "Deep",
        "Disappearing",
        "Eerie",
        "Elusive",
        "Enchanted",
        "Eternal",
        "Farthest",
        "Forbidden",
        "Giant",
        "Highest",
        "Hidden",
        "Holy",
        "Huge",
        "Impenetrable",
        "Impossible",
        "Legendary",
        "Lost",
        "Lowest",
        "Magical",
        "Mysterious",
        "Undersea",
        "Uncharted",
        "Undiscovered",
        "Unknown",
        "Vast",
        "Wild",
    ) ),

    adjectivePlace : WeightedTuple( [
        adjectivePlaceBase,     2,
        adjectiveGeographic,    1,
        adjectiveTexture,       1,
    ] ),

    adjectiveNumber : WeightedTuple( [
        "Two",                  7,
        "Three",                7,
        "Four",                 7,
        "Five",                 6,
        "Six",                  6,
        "Seven",                5,
        "Eight",                5,
        "Nine",                 5,
        "Ten",                  4,
        "Eleven",               2,
        "Twelve",               2,
        "Dozen",                2,
        "Thirteen",             1,
        "Fourteen",             1,
        "Fifteen",              1,
        "Sixteen",              1,
        "Seventeen",            1,
        "Twenty",               1,
        "Seventeen",            1,
        "One Hundred",          1,
        "One Thousand and One", 1,
    ] ),


    adjectiveHero : WeightedTuple( [
        WeightedTuple ( [
            adjectiveBaseHero,      5,
            adjectivePhysicalHero,  3,
            adjectiveActionHero,    3,
            adjectiveVocationHero,  2,
            adjectiveAge,           1,
            adjectiveGeographic,    4,
        ] ),                                    40,
        [
            WeightedTuple ( [
                adjectivePhysicalHero,  2,
                adjectiveActionHero,    2,
                adjectiveVocationHero,  2,
                adjectiveAge,           1,
                adjectiveGeographic,    4,
            ] ),
            adjectiveBaseHero,
        ],                                      30,
        [
            adjectivePhysicalHero,
            adjectiveAge,
            adjectiveVocationHero,
        ],                                      2,
        [
            WeightedTuple ( [
                adjectivePhysicalHero,  2,
                adjectiveActionHero,    2,
            ] ),
            adjectiveAge,
            adjectiveBaseHero,
        ],                                      2,
        [
            adjectiveAge,
            WeightedTuple ( [
                adjectiveVocationHero,  2,
                adjectiveGeographic,    4,
            ] ),
            adjectiveBaseHero,
        ],                                      1,
        [
            adjectiveAge,
            adjectiveGeographic,
            WeightedTuple ( [
                adjectivePhysicalHero,  3,
                adjectiveActionHero,    2,
                adjectiveVocationHero,  1,
            ] ),
            adjectiveBaseHero,
        ],                                      1,
        [
            WeightedTuple ( [
                adjectiveAge,           1,
                adjectivePhysicalHero,  2,
                adjectiveActionHero,    2,
                adjectiveHero,          2,
                adjectiveVocationHero,  2,
            ] ),
            adjectiveGeographic,
            adjectiveBaseHero,
        ],                                      1,
    ] ),

    adjectiveHeroNongeographic : WeightedTuple( [
        WeightedTuple ( [
            adjectiveBaseHero,      5,
            adjectivePhysicalHero,  3,
            adjectiveActionHero,    3,
            adjectiveVocationHero,  2,
            adjectiveAge,           1,
        ] ),                                    40,
        [
            WeightedTuple ( [
                adjectivePhysicalHero,  2,
                adjectiveActionHero,    2,
                adjectiveVocationHero,  2,
                adjectiveAge,           1,
            ] ),
            adjectiveBaseHero,
        ],                                      30,
        [
            adjectiveAge,
            adjectivePhysicalHero,
            adjectiveVocationHero,
        ],                                      2,
        [
            adjectiveAge,
            WeightedTuple ( [
                adjectivePhysicalHero,  2,
                adjectiveActionHero,    2,
                adjectiveVocationHero,  2,
            ] ),
            adjectiveBaseHero,
        ],                                      1,
    ] ),

    adjectiveVillain : WeightedTuple( [
        WeightedTuple ( [
            adjectiveBaseVillain,       5,
            adjectivePhysicalVillain,   3,
            adjectiveActionVillain,     3,
            adjectiveVocationVillain,   2,
            adjectiveAge,               1,
            adjectiveGeographic,        4,
        ] ),                                    40,
        [
            WeightedTuple ( [
                adjectivePhysicalVillain,   2,
                adjectiveActionVillain,     2,
                adjectiveVocationVillain,   2,
                adjectiveAge,               1,
                adjectiveGeographic,        4,
            ] ),
            adjectiveBaseVillain,
        ],                                      30,
        [
            adjectiveAge,
            adjectivePhysicalVillain,
            adjectiveVocationVillain,
        ],                                      2,
        [
            adjectiveAge,
            WeightedTuple ( [
                adjectivePhysicalVillain,   2,
                adjectiveActionVillain,     2,
                adjectiveVocationVillain,   2,
                adjectiveGeographic,        4,
            ] ),
            adjectiveBaseVillain,
        ],                                      2,
        [
            adjectiveAge,
            adjectiveGeographic,
            WeightedTuple ( [
                adjectivePhysicalVillain,   3,
                adjectiveActionVillain,     2,
                adjectiveVocationVillain,   1,
            ] ),
            adjectiveBaseVillain,
        ],                                      1,
        [
            WeightedTuple ( [
                adjectiveAge,               1,
                adjectivePhysicalVillain,   2,
                adjectiveActionVillain,     2,
                adjectiveVillain,           2,
                adjectiveVocationVillain,   2,
            ] ),
            adjectiveGeographic,
            adjectiveBaseVillain,
        ],                                      1,
    ] ),

    adjectiveVillainNongeographic : WeightedTuple( [
        WeightedTuple ( [
            adjectiveBaseVillain,       5,
            adjectivePhysicalVillain,   3,
            adjectiveActionVillain,     3,
            adjectiveVocationVillain,   2,
            adjectiveAge,               1,
        ] ),                                    40,
        [
            WeightedTuple ( [
                adjectivePhysicalVillain,   2,
                adjectiveActionVillain,     2,
                adjectiveVocationVillain,   2,
                adjectiveAge,               1,
            ] ),
            adjectiveBaseVillain,
        ],                                      30,
        [
            adjectiveAge,
            adjectivePhysicalVillain,
            adjectiveVocationVillain,
        ],                                      2,
        [
            adjectiveAge,
            WeightedTuple ( [
                adjectivePhysicalVillain,   2,
                adjectiveActionVillain,     2,
                adjectiveVocationVillain,   2,
            ] ),
            adjectiveBaseVillain,
        ],                                      1,
    ] ),
}
