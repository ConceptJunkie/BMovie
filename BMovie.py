#!/usr/bin/env python

import argparse
import random
import string


#//**********************************************************************
#//
#//  constants
#//
#//**********************************************************************

adjectiveCharacter                          = 0
adjectiveCharacterBase                      = 1
adjectiveGeographic                         = 2
adjectiveMental                             = 3
adjectiveObject                             = 4
adjectiveObjectBase                         = 5
adjectivePlace                              = 6
adjectivePlaceBase                          = 7
adjectiveTexture                            = 8
adjectiveTime                               = 9
adjectiveNumber                             = 10

adverbVerb                                  = 20
adverbAdjective                             = 21

# all verb phrases are transitive for now, prepositions included where appropriate, the final descriptor refers to the object
verbPhrasePresentSingularCharacter          = 30
verbPhrasePresentSingularObject             = 31
verbPhrasePresentSingularPlace              = 32
verbPhrasePresentSingularGoing              = 33
verbPhrasePresentSingularAttacking          = 34
verbPhrasePresentSingularFinding            = 35

verbPhrasePresentPluralCharacter            = 40
verbPhrasePresentPluralObject               = 41
verbPhrasePresentPluralPlace                = 42
verbPhrasePresentPluralGoing                = 43
verbPhrasePresentPluralAttacking            = 44
verbPhrasePresentPluralFinding              = 45

verbPhrasePastCharacter                     = 50
verbPhrasePastObject                        = 51
verbPhrasePastPlace                         = 52
verbPhrasePastGoing                         = 53
verbPhrasePastAttacking                     = 54
verbPhrasePastFinding                       = 55

verbPhraseFutureCharacter                   = 60
verbPhraseFutureObject                      = 61
verbPhraseFuturePlace                       = 62
verbPhraseFutureGoing                       = 63
verbPhraseFutureAttacking                   = 64
verbPhraseFutureFinding                     = 65

verbPhraseGerundCharacter                   = 70
verbPhraseGerundObject                      = 71
verbPhraseGerundPlace                       = 72

namePlaceCommon                             = 90
namePlaceProper                             = 91
namePlaceProperSimple                       = 92
namePlaceProperArticle                      = 93
namePlaceArchitectureSingular               = 94
namePlaceArchitecturePlural                 = 95
namePlaceGeographySingular                  = 96
namePlaceGeographyPlural                    = 97
namePlaceTerritorySingular                  = 98
namePlaceTerritoryPlural                    = 99

nameCharacterSingularCommon                 = 110
nameCharacterSingularProper                 = 111
nameCharacterSingularProperSimple           = 112
nameCharacterSingularProperSimplePossessive = 113
nameCharacterSingularLeader                 = 114
nameCharacterPluralLeader                   = 115
nameCharacterPluralCommon                   = 116
nameCharacterPluralProper                   = 117
nameCharacterPluralProperSimple             = 118

nameGroupDescription                        = 130
nameGroupTypePrepend                        = 131
nameGroupTypeAppend                         = 132
nameGroupPrepend                            = 133
nameGroupAppend                             = 134

nameConcept                                 = 140
nameDirection                               = 141
nameEventSingular                           = 142
nameEventPlural                             = 143
namePlaceModifier                           = 144
nameEventEpoch                              = 145
nameEventStorySingular                      = 146
nameEventStoryPlural                        = 147
nameVehicleSingular                         = 148
nameVehiclePlural                           = 149
nameWeaponSingular                          = 150
nameWeaponPlural                            = 151
nameTimeSingular                            = 152
nameTimePlural                              = 153

nameObjectSingularCommon                    = 160
nameObjectPluralCommon                      = 161
nameObjectProper                            = 162
nameObjectProperSimple                      = 163

namePossessionSingular                      = 170
namePossessionPlural                        = 171

prepositionalPhraseSingularCommon           = 180
prepositionalPhraseSingularProper           = 181
prepositionalPhrasePluralCommon             = 182
prepositionalPhrasePluralProper             = 183
prepositionalPhraseEvent                    = 184


def makeNameCharacterSingularProperSimplePossessive( ) :
    result = getWord( nameCharacterSingularProperSimple )

    if result[ -1 ] == 's':
        return result + "'"
    else:
        return result + "'s"


wordLists = {
    adjectiveTexture : (
        "Alabaster",
        "Amber",
        "Amber",
        "Azure",
        "Black",
        "Black",
        "Black",
        "Black",
        "Blue",
        "Blue",
        "Cerulean",
        "Crimson",
        "Crimson",
        "Ebony",
        "Ebony",
        "Glistening",
        "Glowing",
        "Golden",
        "Golden",
        "Green",
        "Green",
        "Grey",
        "Many-Colored",
        "Orange",
        "Pale",
        "Purple",
        "Violet",
        "Red",
        "Red",
        "Red",
        "Shining",
        "Shiny",
        "Silvery",
        "Sparkling",
        "Vermillion",
        "White",
        "White",
        "White",
        "White",
        "Yellow",
    ),

    adjectiveTime : (
        "Ancient",
        "Ancient",
        "Epic",
        "Epochal",
        "Eternal",
        "Eternal",
        "Never-Ending",
        "Unending",
    ),

    adjectiveMental : (
        "Angry",
        "Bold",
        "Bold",
        "Brave",
        "Brave",
        "Brave",
        "Confused",
        "Cpourageous",
        "Crazy",
        "Daring",
        "Daring",
        "Daring",
        "Dedicated",
        "Defiant",
        "Defiant",
        "Defiant",
        "Determined",
        "Deviant",
        "Enraged",
        "Fearless",
        "Fearless",
        "Fearless",
        "Furious",
        "Gallant",
        "Heroic",
        "Heroic",
        "Heroic",
        "Indignant",
        "Indomitable",
        "Insane",
        "Intrepid",
        "Intrepid",
        "Reckless",
        "Reluctant",
        "Renegade",
        "Renegade",
        "Stalwart",
        "Terrified",
        "Unrepentant",
        "Valiant",
        "Valiant",
    ),

    adjectiveCharacterBase : (
        "Accidental",
        "All-Powerful",
        "Amazing",
        "Amazing",
        "Beautiful",
        "Crosstime",
        "Cybernetic",
        "Dangerous",
        "Dangerous",
        "Deadly",
        "Deadly",
        "Dimension-Hopping",
        "Dreadful",
        "Evil",
        "Evil",
        "Elusive",
        "Giant",
        "Gigantic",
        "Gigantic",
        "Glorious",
        "Holy",
        "Howling",
        "Huge",
        "Impossible",
        "Incredible",
        "Kick-boxing",
        "Killer",
        "Lost",
        "Lost",
        "Monstrous",
        "Morphing",
        "Mysterious",
        "Mysterious",
        "Mysterious",
        "Powerful",
        "Screaming",
        "Teenage",
        "Time-Travelling",
        "Transdimensional",
        "Unkillable",
        "Unknowable",
        "Unstoppable",
        "Wild",
        "Wild",
    ),

    adjectiveGeographic: (
        "African",
        "Alien",
        "Altairian",
        "American",
        "Ancient",
        "Antarian",
        "Astral",
        "Atlantean",
        "Aztec",
        "Babylonian",
        "Celtic",
        "Chinese",
        "Cydonian",
        "Egyptian",
        "Etherial",
        "Extra-Dimensional",
        "Extra-Terrestrial",
        "Human",
        "Japanese",
        "Jovian",
        "Lemurian",
        "Lost",
        "Lunar",
        "Martian",
        "Orion",
        "Plutonian",
        "Rigelian",
        "Roman",
        "Russian",
        "Stygian",
        "Sumerian",
        "Terran",
        "Venusian",
    ),

    adjectiveCharacter : (  adjectiveCharacterBase, adjectiveCharacterBase, adjectiveCharacterBase, adjectiveTexture, adjectiveGeographic ),

    adjectiveObjectBase : (
        "Adamantine",
        "All-Powerful",
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
    ),

    adjectiveObject : ( adjectiveObjectBase, adjectiveObjectBase, adjectiveTexture, adjectiveGeographic ),

    adjectivePlaceBase : (
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
    ),

    adjectivePlace : ( adjectivePlaceBase, adjectivePlaceBase, adjectiveGeographic, adjectiveTexture ),

    adjectiveNumber : (
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Two",
        "Three",
        "Three",
        "Three",
        "Three",
        "Three",
        "Three",
        "Three",
        "Four",
        "Four",
        "Four",
        "Four",
        "Four",
        "Four",
        "Five",
        "Five",
        "Five",
        "Five",
        "Five",
        "Six",
        "Six",
        "Six",
        "Six",
        "Seven",
        "Seven",
        "Seven",
        "Eight",
        "Eight",
        "Nine",
        "Ten",
        "A Dozen",
        "One Thousand and One",
    ),

    adverbVerb : (
        "Accidentally",
        "Bravely",
        "Desperately",
        "Foolishly",
        "Furiously",
        "Mysteriously",
        "Savagely",
    ),

    adverbAdjective : (
        "Amazingly",
        "Impossibly",
        "Mysteriously",
        "Surprisingly",
        "Unbelievably",
    ),

    verbPhrasePresentSingularGoing : (
        "Escapes From",
        "Flies To",
        "Goes To",
        "Journeys To",
        "Sails To",
    ),

    verbPhrasePresentSingularAttacking : (
        "Battles",
        "Captures",
        "Declares War On",
        "Destroys",
    ),

    verbPhrasePresentSingularFinding : (
        "Discovers",
        "Discovers",
        "Finds",
        "Finds",
        "Seeks",
        "Uncovers",
        "Loses",
        "Loses",
    ),

    verbPhrasePresentSingularPlace : (
        verbPhrasePresentSingularGoing,
        verbPhrasePresentSingularGoing,
        verbPhrasePresentSingularAttacking,
        verbPhrasePresentSingularFinding,
    ),

    verbPhrasePresentSingularCharacter : (
        verbPhrasePresentSingularAttacking,
        verbPhrasePresentSingularFinding,
    ),

    verbPhrasePresentSingularObject : (
        verbPhrasePresentSingularFinding,
    ),

    verbPhrasePresentPluralGoing : (
        "Escape From",
        "Fly To",
        "Go To",
        "Journey To",
        "Sail To",
    ),

    verbPhrasePresentPluralAttacking : (
        "Battle",
        "Capture",
        "Declare War On",
        "Destroy",
    ),

    verbPhrasePresentPluralFinding : (
        "Discover",
        "Discover",
        "Find",
        "Find",
        "Seek",
        "Uncover",
        "Lose",
        "Lose",
    ),

    verbPhrasePresentPluralPlace : (
        verbPhrasePresentPluralGoing,
        verbPhrasePresentPluralGoing,
        verbPhrasePresentPluralAttacking,
        verbPhrasePresentPluralFinding,
    ),

    verbPhrasePresentPluralCharacter : (
        verbPhrasePresentPluralAttacking,
        verbPhrasePresentPluralFinding,
    ),

    verbPhrasePresentPluralObject : (
        verbPhrasePresentPluralFinding,
    ),

    verbPhrasePastCharacter : (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ),

    verbPhrasePastObject : (
        verbPhrasePastFinding,
    ),

    verbPhrasePastGoing : (
        "Escaped From",
        "Flew To",
        "Went To",
        "Journeyed To",
        "Sailed To",
    ),

    verbPhrasePastAttacking : (
        "Battled",
        "Captured",
        "Declared War On",
        "Destroyed",
    ),

    verbPhrasePastFinding : (
        "Discovered",
        "Found",
        "Uncovered",
        "Lost",
    ),

    verbPhrasePastPlace : (
        verbPhrasePastGoing,
        verbPhrasePastGoing,
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ),

    verbPhrasePastCharacter : (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ),

    verbPhrasePastObject : (
        verbPhrasePastFinding,
    ),

    verbPhraseFutureCharacter : (
        [ "Will", verbPhrasePresentSingularCharacter ]
    ),

    verbPhraseFutureObject : (
        [ "Will", verbPhrasePresentSingularObject ]
    ),

    verbPhraseFuturePlace : (
        [ "Will", verbPhrasePresentSingularPlace ]
    ),

    verbPhraseGerundCharacter : (
        "Approaching",
        "Considering",
        "Defying",
        "Escaping From",
        "Finding",
        "Looking For",
        "Regarding",
        "Retreating From",
        "Running From",
        "Searching For",
        "Seeking",
    ),

    verbPhraseGerundObject : (
        "Discovering",
        "Finding",
        "Looking For",
        "Running From",
        "Seeking",
        "Uncovering",
    ),

    verbPhraseGerundPlace : (
        "Approaching",
        "Considering",
        "Defying",
        "Discovering",
        "Escaping",
        "Exploring",
        "Finding",
        "Looking For",
        "Regarding",
        "Retreating From",
        "Running From",
        "Searching For",
        "Seeking",
    ),

    namePlaceModifier : (
        "Central",
        "Darkest",
        "Deepest",
        "Inner",
        "Lower",
        "Outer",
        "The Bottom of",
        "The Depths of",
        "The Edge of",
        "The Furthest Reaches of",
        "The Inside of",
        "The Outside of",
        "The Top of",
        "Upper",
    ),

    namePlaceArchitectureSingular : (
        "Castle",
        "Castle",
        "Cathedral",
        "Dungeon",
        "Fortress",
        "Fortress",
        "Inner Sanctum",
        "Palace",
        "Palace",
        "Stronghold",
        "Stronghold",
        "Temple",
        "Temple",
        "Tower",
        "Tower",
    ),

    namePlaceArchitecturePlural : (
        "Castles",
        "Castles",
        "Cathedrals",
        "Dungeons",
        "Palaces",
        "Palaces",
        "Temples",
        "Temples",
        "Towers",
        "Towers",
    ),

    namePlaceTerritorySingular : (
        "City",
        "Empire",
        "Kingdom",
        "Republic",
        "Territory",
        "City-State",
    ),

    namePlaceTerritoryPlural : (
        "Cities",
        "Empires",
        "Kingdoms",
        "Republics",
        "Territories",
        "City-States",
    ),

    namePlaceGeographySingular : (
        "Cave",
        "Cavern",
        "Continent",
        "Desert",
        "Dimension",
        "Forest",
        "Galaxy",
        "Jungle",
        "Land",
        "March",
        "Marsh",
        "Mountain",
        "Ocean",
        "Plains",
        "Planet",
        "Sea",
        "Swamp",
        "Universe",
        "Volcano",
        "Wasteland",
    ),

    namePlaceGeographyPlural : (
        "Caverns",
        "Caves",
        "Deserts",
        "Dimensions",
        "Forests",
        "Galaxies",
        "Jungles",
        "Lands",
        "Marches",
        "Marshes",
        "Mountains",
        "Planets",
        "Seas",
        "Swamps",
        "Wastelands",
    ),

    namePlaceCommon : (
        namePlaceArchitecturePlural,
        namePlaceArchitectureSingular,
        namePlaceGeographyPlural,
        namePlaceGeographyPlural,
        namePlaceGeographySingular,
        namePlaceGeographySingular,
        namePlaceTerritoryPlural,
        namePlaceTerritorySingular,
        namePlaceTerritorySingular,
    ),

    namePlaceProper : (
        namePlaceProperSimple,
        namePlaceProperSimple,
        namePlaceProperSimple,
        namePlaceProperSimple,
        namePlaceProperSimple,
        namePlaceProperSimple,
        [ namePlaceModifier, namePlaceProperSimple ],
        [ namePlaceModifier, namePlaceProperSimple ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', namePlaceProperArticle ],
        [ 'The', adjectivePlace, namePlaceCommon ],
        [ 'The', adjectivePlace, namePlaceCommon ],
        [ 'The', adjectivePlace, namePlaceCommon ],
        [ 'The', adjectivePlace, namePlaceCommon ],
        [ 'The', adjectivePlace, namePlaceProperArticle ],
        [ 'The', adjectivePlace, namePlaceProperArticle ],
        [ 'The', adjectivePlace, namePlaceProperArticle ],
        [ 'The', adjectivePlace, namePlaceProperArticle ],
        [ 'The', namePlaceCommon, 'of', nameConcept ],
        [ 'The', adjectiveObject, namePlaceCommon ],
        [ 'The', adjectiveObject, namePlaceCommon ],
        [ 'The', namePlaceCommon, 'of', namePlaceProperSimple ],
        [ 'The', namePlaceCommon, 'of The', namePlaceProperArticle ],
    ),

    namePlaceProperSimple : (
        "Africa",
        "Aldebaran",
        "Altair",
        "America",
        "Andromeda",
        "Antarctica",
        "Antares",
        "Arcturus",
        "Asia",
        "Athens",
        "Atlantis",
        "Babylon",
        "Baghdad",
        "Beijing",
        "Betelgeuse",
        "China",
        "Deep Space",
        "Djibouti",
        "Earth",
        "Egypt",
        "Europe",
        "India",
        "Inner Space",
        "Japan",
        "Jupiter",
        "London",
        "Los Angeles",
        "Marathon",
        "Mars",
        "Mercury",
        "Mount Everest",
        "Navarone",
        "Neptune",
        "New York",
        "Orion",
        "Outer Space",
        "Paris",
        "Planet X",
        "Pluto",
        "Poughkeepsie",
        "Prehistoric Times",
        "Rigel",
        "Russia",
        "Saturn",
        "Sirius",
        "Space",
        "Texas",
        "Timbuktu",
        "Tokyo",
        "Uranus",
        "Vega",
        "Venus",
        "Washington",
        "Wongo Wongo",
    ),

    namePlaceProperArticle : (
        "Amazon",
        "Amazon",
        "Andes",
        "Andromeda Galaxy",
        "Beginning of Time",
        "Beginning of Time",
        "Burmuda Triangle",
        "Congo",
        "Distant Future",
        "Distant Past",
        "Eighth Dimension",
        "Eighth Planet",
        "Eleventh Planet",
        "End of Time",
        "End of Time",
        "Fifth Dimension",
        "Fourth Dimension",
        "Future",
        "Future",
        "Himalayas",
        "Jungle",
        "Land Before Time",
        "Land of Oz",
        "Lost World",
        "Lost World",
        "Marianas Trench",
        "Milky Way",
        "Moon",
        "New World",
        "Ninth Dimension",
        "Ninth Planet",
        "North Pole",
        "Occident",
        "OK Corral",
        "Old World",
        "Orient",
        "Outback",
        "Past",
        "Past",
        "Pleiades",
        "River Kwai",
        "Sargasso Sea",
        "Seven Seas",
        "Seven Seas",
        "Seven Seas",
        "Seventh Dimension",
        "Sixth Dimension",
        "South Pole",
        "South Pole",
        "South Pole",
        "Tenth Planet",
        "Thirteenth Planet",
        "Twelfth Planet",
        "Wild West",
        "Wild West",
        "Wild West",
        [ "City of", nameConcept ],
        [ "Forest of", nameConcept ],
        [ "Island of", nameConcept ],
        [ "Lost City of", nameConcept ],
        [ "Mountains of", nameConcept ],
        [ "River of", nameConcept ],
    ),

    nameCharacterSingularLeader : (
        "Abbot",
        "Baron",
        "Bishop",
        "Caliph",
        "Chieftain",
        "Chieftain",
        "Commander",
        "Commander",
        "Commander",
        "Congress",
        "Count",
        "Count",
        "Countess",
        "Duchess",
        "Duke",
        "Duke",
        "Earl",
        "Emperor",
        "Emperor",
        "Emperor",
        "Emperor",
        "Emperoress",
        "Emperoress",
        "Hero",
        "Hero",
        "Hero",
        "Hero",
        "Heroine",
        "Heroine",
        "Heroine",
        "Heroine",
        "King",
        "King",
        "King",
        "King",
        "Knight",
        "Knight",
        "Knight",
        "Lord",
        "Lord",
        "Lord",
        "Master",
        "Master",
        "Parliament",
        "Patrician",
        "Pope",
        "President",
        "Priest",
        "Priest",
        "Priest",
        "Prime Minister",
        "Prince",
        "Prince",
        "Prince",
        "Princess",
        "Princess",
        "Princess",
        "Prophet",
        "Prophet",
        "Prophet",
        "Queen",
        "Queen",
        "Queen",
        "Queen",
        "Raj",
        "Ruler",
        "Ruler",
        "Sheik",
        "Tyrant",
        "Tyrant",
        "Tyrant",
        "Viscount",
        "Wizard",
        "Wizard",
    ),

    nameCharacterPluralLeader : (
        "Barons",
        "Bishops",
        "Chieftains",
        "Chieftains",
        "Chieftains",
        "Commanders",
        "Commanders",
        "Commanders",
        "Counts",
        "Dukes",
        "Heroes",
        "Heroes",
        "Heroes",
        "Heroes",
        "Kings",
        "Kings",
        "Kings",
        "Knights",
        "Knights",
        "Knights",
        "Knights",
        "Lords",
        "Lords",
        "Lords",
        "Masters",
        "Masters",
        "Masters",
        "Priests",
        "Priests",
        "Priests",
        "Princes",
        "Princes",
        "Princes",
        "Prophets",
        "Prophets",
        "Prophets",
        "Queens",
        "Queens",
        "Rulers",
        "Rulers",
        "Sheiks",
        "Tyrants",
        "Tyrants",
        "Tyrants",
        "Wizards",
        "Wizards",
        "Wizards",
    ),

    nameCharacterSingularCommon : (
        "Alien",
        "Ape",
        "Cat",
        "Commando",
        "Dog",
        "Dwarf",
        "Elf",
        "Gangster",
        "Gorilla",
        "Hero",
        "Kid",
        "King",
        "Knight",
        "Mummy",
        "Pauper",
        "Prince",
        "Queen",
        "Princess",
        "President",
        "Rebel",
        "Robot",
        "Mechanoid",
        "Sheriff",
        "Soldier",
        "Spy",
        "Stranger",
        "Thief",
        "Traitor",
        "Vampire",
        "Villain",
        "Wizard",
    ),

    nameCharacterSingularProperSimple : (
        "Abraham Lincoln",
        "Albert Einstein",
        "Bruce Lee",
        "Colossus",
        "Commando Cody",
        "Crow T. Robot",
        "Delta Force",
        "Don Juan",
        "Dr. Z",
        "Dracula",
        "El Santo",
        "Frankenstein",
        "Fu Manchu",
        "Gamera",
        "Gilgamesh",
        "Godzilla",
        "Harcourt Fenton Mudd",
        "Hercules",
        "Indiana Jones",
        "Jackie Chan",
        "Jared Syn",
        "Jet Jaguar",
        "King Arthur",
        "Lord Byron",
        "Lord Nelson",
        "Mark Twain",
        "Merlin",
        "Mitchell",
        "Mothra",
        "Nosferatu",
        "Perseus",
        "Philo T. Farnsworth",
        "Robin Hood",
        "Rocky Jones",
        "Samson",
        "Santa Claus",
        "Sherlock Holmes",
        "Sir Galahad",
        "Sir Lancelot",
        "Teddy Roosevelt",
        "The Cowardly Lion",
        "The Ice Cream Bunny",
        "The Scarecrow",
        "The Sheriff of Nottingham",
        "The Tin Man",
        "The Treehouse Club",
        "Thomas Edison",
        "Tom Servo",
    ),

    nameCharacterSingularProperSimplePossessive : makeNameCharacterSingularProperSimplePossessive,

    nameCharacterPluralCommon : (
        "Aliens",
        "Apes",
        "Barbarians",
        "Clones",
        "Commandos",
        "Dinosaurs",
        "Dolphins",
        "Dwarves",
        "Earthlings",
        "Gangsters",
        "Ghosts",
        "Gorillas",
        "Hordes",
        "Jovians",
        "Kings",
        "Lunarians",
        "Martians",
        "Mecurians",
        "Mummies",
        "Neptunians",
        "Plutonians",
        "Prisoners",
        "Robots",
        "Saturnians",
        "Savages",
        "Spirits",
        "Terrans",
        "Throngs",
        "Titanians",
        "Uranians",
        "Vampires",
        "Venusians",
        "Vikings",
        "Warriors",
    ),

    nameCharacterPluralProperSimple : (
        "Abbott and Costello",
        "Penn and Teller",
        "The Beatles",
        "The Green Berets",
        "The Hawklords",
        "The Martians",
        "The Space Marines",
        "The Space Rangers",
        "The Three Stooges",
    ),

    nameCharacterSingularProper : (
        [ nameCharacterSingularProperSimple ],
        [ nameCharacterSingularProperSimple ],
        [ nameCharacterSingularProperSimple ],
        [ nameCharacterSingularProperSimple ],
        [ nameCharacterSingularProperSimple ],
        [ nameGroupDescription, nameGroupTypePrepend ],
        [ nameGroupDescription, nameGroupTypePrepend ],
        [ nameGroupDescription, nameGroupTypePrepend ],
        [ nameGroupPrepend, nameGroupTypePrepend ],
        [ nameGroupPrepend, nameGroupTypePrepend ],
        [ nameGroupPrepend, nameGroupTypePrepend ],
        [ nameGroupTypeAppend, nameGroupAppend ],
        [ nameGroupTypeAppend, nameGroupDescription ],
        [ nameGroupTypeAppend, nameGroupDescription ],
        [ nameGroupTypeAppend, nameGroupDescription ],
        [ 'The', nameGroupTypeAppend, 'of', nameConcept ],
        [ nameConcept, nameGroupTypePrepend ],
    ),

    nameCharacterPluralProper : (
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ nameCharacterPluralProperSimple ],
        [ 'The', adjectiveCharacter, nameCharacterPluralCommon ],
        [ 'The', adjectiveCharacter, nameCharacterPluralCommon ],
        [ 'The', adjectiveCharacter, nameCharacterPluralCommon, 'of', nameConcept ],
        [ 'The', adjectiveCharacterBase, nameCharacterPluralCommon ],
        [ 'The', adjectiveCharacterBase, nameCharacterPluralCommon ],
        [ 'The', adjectiveObject, nameCharacterPluralCommon ],
        [ 'The', adjectiveObject, nameCharacterPluralCommon ],
        [ 'The', adjectiveObject, nameCharacterPluralCommon, 'of The', nameDirection ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon ],
        [ 'The', nameCharacterPluralCommon, 'of The', nameDirection ],
    ),

    nameGroupTypePrepend : (
        "Batallion",
        "Company",
        "Corps",
        "Department",
        "Force",
        "Patrol",
        "Platoon",
        "Regiment",
        "Squad",
        "Squadron",
        "Troop",
        "Unit",
     ),

    nameGroupTypeAppend : (
        "Batallion",
        "Company",
        "Department",
        "Force",
        "Platoon",
        "Regiment",
        "Squad",
        "Squadron",
        "Team",
        "Unit",
     ),

    nameGroupDescription : (
        "Alpha",
        "Beta",
        "Delta",
        "Epsilon",
        "Gamma",
        "Iota",
        "Kappa",
        "Lambda",
        "Omega",
        "Omicron",
        "Sigma",
        "Theta",
        "Team",
        "Upsilon",
        "Zero",
        "Zeta",
    ),

    nameGroupPrepend : (
        "11th",
        "13th",
        "17th",
        "19th",
        "23rd",
        "29th",
        "31st",
        "37th",
        "41st",
        "43rd",
        "47th",
        "49th",
        "50th",
        "53rd",
        "59th",
        "61st",
        "67th",
        "6th",
        "71st",
        "73rd",
        "79th",
        "7th",
        "83rd",
        "8th",
        "99th",
        "9th",
        "A",
        "B",
        "C",
        "Danger",
        "Danger",
        "Eagle",
        "Eagle",
        "F",
        "Fifth",
        "First",
        "First",
        "First",
        "Fourth",
        "Giga",
        "J",
        "K",
        "Mega",
        "Q",
        "Second",
        "Second",
        "Space",
        "Space",
        "Space",
        "Super",
        "Third",
        "Third",
        "Tiger",
        "Tiger",
        "Ultra",
        "V",
        "W",
        "X",
        "Z",
    ),

    nameGroupAppend : (
        "One",
        "One",
        "One",
        "One",
        "Two",
        "Two",
        "Two",
        "Two",
        "Three",
        "Three",
        "Three",
        "Three",
        "Seven",
        "Seven",
        "Seven",
        "Seven",
        "Nine",
        "Nine",
        "Nine",
        "Nine",
        "Ten",
        "Ten",
        "Ten",
        "Ten",
        "13",
        "17",
        "19",
        "23",
        "29",
        "31",
        "37",
        "41",
        "43",
        "47",
        "49",
        "50",
        "53",
        "59",
        "61",
        "67",
        "71",
        "73",
        "79",
        "83",
        "99",
        "100",
    ),

    nameConcept : (
        "Adversity",
        "Beauty",
        "Confusion",
        "Danger",
        "Danger",
        "Darkness",
        "Death",
        "Deceit",
        "Defeat",
        "Desire",
        "Destiny",
        "Doom",
        "Doom",
        "Enlightenment",
        "Eternity",
        "Everything",
        "Evil",
        "Evolution",
        "Fear",
        "Forever",
        "Glory",
        "Gold",
        "Good",
        "Gravity",
        "Hate",
        "History",
        "Hope",
        "Horror",
        "Infamy",
        "Infinity",
        "Infinity",
        "Life",
        "Light",
        "Lore",
        "Love",
        "Madness",
        "Magic",
        "Magic",
        "Mystery",
        "Mystery",
        "Oblivion",
        "Oblivion",
        "Oppression",
        "Poverty",
        "Prejudice",
        "Pride",
        "Prosperity",
        "Redemption",
        "Resurrection",
        "Revelation",
        "Righteousness",
        "Sanity",
        "Science",
        "Science",
        "Space",
        "Space",
        "Space",
        "Spirituality",
        "Technology",
        "The Occult",
        "The Occult",
        "The Universe",
        "Terror",
        "Time",
        "Triumph",
        "Truth",
        "Victory",
    ),

    nameDirection : (
        "Deep South",
        "East",
        "East",
        "Far East",
        "Far North",
        "Far West",
        "Inside",
        "North",
        "North",
        "Outside",
        "South",
        "South",
        "West",
        "West",
    ),

    nameEventSingular : (
        "Abduction",
        "Assassination",
        "Attack",
        "Battle",
        "Destiny",
        "Destruction",
        "Disappearance",
        "Downfall",
        "Game",
        "Journey",
        "Liberation",
        "Murder",
        "Peril",
        "Redemption",
        "Return",
        "Revenge",
        "Tragedy",
        "Trial",
        "Triumph",
        "Victory",
        "War",
    ),

    nameEventEpoch : (
        "Century",
        "Day",
        "Day",
        "Day",
        "Day",
        "Day",
        "Day",
        "Decade",
        "Eon",
        "Epoch",
        "Epoch",
        "Era",
        "Era",
        "Millennium",
        "Night",
        "Night",
        "Night",
        "Night",
        "Night",
        "Night",
        "Month",
        "Month",
        "Time",
        "Time",
        "Time",
        "Time",
        "Time",
        "Week",
        "Week",
        "Week",
        "Year",
        "Year",
        "Year",
    ),

    nameEventStorySingular : (
        "Adventure",
        "Epic",
        "Fable",
        "History",
        "History",
        "Legend",
        "Legend",
        "Legend",
        "Mystery",
        "Mystery",
        "Myth",
        "Odyssey",
        "Saga",
        "Saga",
        "Song",
        "Scenario",
        "Story",
        "Story",
        "Tale",
        "Tale",
        "Trilogy",
    ),

    nameEventStoryPlural : (
        "Adventures",
        "Adventures",
        "Fables",
        "Legends",
        "Legends",
        "Mysteries",
        "Myths",
        "Songs",
        "Stories",
        "Stories",
        "Tales",
        "Tales",
    ),

    nameEventPlural : (
        "Adventures",
        "Battles",
        "Destruction",
        "Games",
        "Journeys",
        "Legends",
        "Mysteries",
        "Perils",
        "Stories",
        "Trials",
        "Tribulations",
        "Triumphs",
        "Victories",
        "Wars",
    ),

    nameVehicleSingular : (
        "Battleship",
        "Fighter Jet",
        "Hovercraft",
        "Rocket",
        "Ship",
        "Spaceship",
        "Spaceship",
        "Starship",
        "Submarine",
    ),

    nameWeaponSingular : (
        "Bomb",
        "Cannon",
        "Laser",
        "Machine Gun",
        "Ray Gun",
        "Ray Gun",
        "Spear",
        "Sword",
        "Sword",
        "Trident",
        "Weapon",
        "Weapon",
        "Whip",
    ),

    nameObjectSingularCommon : (
        (
            "Android",
            "Android",
            "Book",
            "Clue",
            "Code",
            "Codex",
            "Coffin",
            "Computer",
            "Computer",
            "Mechanoid",
            "Moon",
            "Planet",
            "Robot",
            "Robot",
            "Scroll",
            "Secret",
            "Secret",
            "Skull",
            "Spell",
            "Star",
            "Tomb",
            "Treasure",
            "Treasure",
        ),
        nameVehicleSingular,
        nameWeaponSingular,
    ),

    nameVehiclePlural : (
        "Battleships",
        "Fighter Jets",
        "Rockets",
        "Ships",
        "Spaceships",
        "Spaceships",
        "Starships",
        "Submarines",
        "Tanks",
    ),

    nameWeaponPlural : (
        "Bombs",
        "Cannons",
        "Guns",
        "Lasers",
        "Machine Guns",
        "Ray Guns",
        "Ray Guns",
        "Spears",
        "Swords",
        "Swords",
        "Tridents",
        "Weapons",
        "Weapons",
    ),

    nameTimeSingular : (
        "Second",
        "Minute",
        "Minute",
        "Minute",
        "Hour",
        "Hour",
        "Hour",
        "Day",
        "Day",
        "Day",
        "Day",
        "Week",
        "Week",
        "Month",
        "Month",
        "Year",
        "Year",
        "Decade",
        "Century",
    ),

    nameTimePlural : (
        "Seconds",
        "Minutes",
        "Minutes",
        "Minutes",
        "Hours",
        "Hours",
        "Hours",
        "Days",
        "Days",
        "Days",
        "Days",
        "Weeks",
        "Weeks",
        "Months",
        "Months",
        "Years",
        "Years",
        "Decades",
        "Centuries",
    ),

    nameObjectPluralCommon : (
        (
            "Androids",
            "Computers",
            "Guns",
            "Guns",
            "Gems",
            "Jewels",
            "Mysteries",
            "Mysteries",
            "Robots",
            "Secrets",
            "Treasures",
        ),
        nameVehiclePlural,
        nameWeaponPlural,
    ),

    nameObjectProper : (
        nameObjectProperSimple,
        nameObjectProperSimple,
        nameObjectProperSimple,
        nameObjectProperSimple,
        nameObjectProperSimple,
        [ 'The', nameObjectSingularCommon, 'of', ( namePlaceProper, namePlaceProper, namePlaceProper, [ 'The', nameDirection ], nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper ) ],
        [ 'The', nameObjectSingularCommon, 'of', ( namePlaceProper, namePlaceProper, namePlaceProper, [ 'The', nameDirection ], nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper ) ],
        [ 'The', nameWeaponSingular, 'of', ( namePlaceProper, nameConcept, [ 'The', nameDirection ], nameCharacterSingularProper, nameCharacterPluralProper ) ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon ],
        [ 'The', adverbAdjective, adjectiveObjectBase, nameObjectSingularCommon ],
        [ 'The', adverbAdjective, adjectiveObjectBase, nameObjectSingularCommon ],
        [ 'The', adjectiveObject, nameObjectSingularCommon, 'of', ( namePlaceProper, namePlaceProper, namePlaceProper, [ 'The', nameDirection ], nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper ) ],
        [ 'The', adjectiveObject, nameWeaponSingular, 'of', ( namePlaceProper, nameConcept, [ 'The', nameDirection ], nameCharacterSingularProper, nameCharacterPluralProper ) ],
        [ nameCharacterSingularProperSimplePossessive, nameObjectSingularCommon ],
        [ nameCharacterSingularProperSimplePossessive, nameObjectSingularCommon ],
        [ nameCharacterSingularProperSimplePossessive, nameWeaponSingular ],
        [ nameCharacterSingularProperSimplePossessive, nameConcept ],
        [ nameCharacterSingularProperSimplePossessive, adjectiveObject, nameObjectSingularCommon ],
        [ nameCharacterSingularProperSimplePossessive, adjectiveObject, nameObjectSingularCommon ],
        [ nameCharacterSingularProperSimplePossessive, nameObjectSingularCommon, 'of', nameConcept ],
        [ nameCharacterSingularProperSimplePossessive, nameObjectSingularCommon, 'of', nameConcept ],
        [ nameCharacterSingularProperSimplePossessive, adjectiveObject, nameObjectSingularCommon, 'of', nameConcept ],
    ),

    nameObjectProperSimple : (
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
    ),

    namePossessionSingular : (
        "Anger",
        "Betrayal",
        "Bravery",
        "Choice",
        "Daughter",
        "Decision",
        "Desire",
        "Desires",
        "Father",
        "Gun",
        "Guns",
        "Intuition",
        "Legacy",
        "Revenge",
        "Son",
        "Sword",
        "Wife",
        "Wrath",
        "Wrath",
    ),

    namePossessionPlural : (
        "Sons",
        "Daughters",
        "Children",
        "Wives",
        "Enemies",
    ),

    prepositionalPhraseSingularCommon : (
        "Above",
        "Against",
        "Beneath",
        "Beyond",
        "In Search of",
        "In",
        "Inside",
        "On",
    ),

    prepositionalPhraseEvent : (
        "After",
        "Before",
        "During",
    ),

    prepositionalPhraseSingularProper : (
        "Above",
        "Beneath",
        "Beyond",
        "Beyond",
        "In",
        "In",
        "In",
        "Inside",
        "Outside of",
        "On The Outskirts of",
        "Near",
        "Near",
    ),

    prepositionalPhrasePluralCommon : (
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
    ),

    prepositionalPhrasePluralProper : (
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
    ),
}

titleTypes = (
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        prepositionalPhrasePluralCommon,
        namePlaceProper
    ],
    [
        'The',
        adjectiveCharacter,
        nameCharacterSingularCommon,
    ],
    [
        'To',
        verbPhrasePresentPluralCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        'To',
        verbPhrasePresentPluralObject,
        ( nameObjectProper, nameObjectProper, nameObjectProper, [ 'The', nameObjectSingularCommon ], [ 'The', nameObjectSingularCommon ], [ 'The', nameObjectSingularCommon ], [ 'The', adjectiveObject, nameObjectSingularCommon ] ),
    ],
    [
        ( [ 'The', namePossessionPlural ], [ 'The', namePossessionPlural ], [ 'The', ( adjectiveObject, adjectiveObject, adjectiveCharacter, adjectiveNumber ), namePossessionPlural ] ),
        'of',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        ( [ 'The', nameEventSingular ], [ 'The', nameEventPlural ], [ 'The', ( adjectiveObject, adjectiveObject, adjectiveObject, adjectiveNumber ), nameEventPlural ], [ 'The', adjectiveObject, nameEventSingular ], [ 'The', ( adjectiveObject, adjectiveObject, adjectiveCharacter, adjectiveNumber ), namePossessionPlural ] ),
        'of',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper, [ 'The', nameCharacterSingularCommon ], [ 'The', nameCharacterSingularCommon ] ),
    ],
    [
        ( [ 'The', ( namePossessionSingular, nameEventSingular ) ], [ 'The', ( namePossessionSingular, nameEventSingular ) ], [ 'The', ( namePossessionPlural, nameEventPlural ) ] ),
        'of',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        'The',
        ( namePossessionSingular, namePossessionPlural ),
        'of The',
        nameCharacterPluralCommon,
    ],
    [
        ( [ 'The', namePossessionSingular ], [ 'The', namePossessionSingular ], [ 'The', namePossessionPlural ] ),
        'of',
        nameObjectProper,
    ],
    [
        'The',
        nameEventPlural,
        'of',
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        nameCharacterPluralProper,
    ],
    [
        ( [ nameCharacterSingularProper, verbPhrasePresentSingularObject ], [ nameCharacterPluralProper, verbPhrasePresentPluralObject ] ),
        ( nameConcept, nameConcept, namePlaceProper, namePlaceProper, [ 'The', nameEventSingular, 'of', nameConcept ] ),
    ],
    [
        ( [ nameCharacterSingularProper, verbPhrasePresentSingularObject ], [ nameCharacterPluralProper, verbPhrasePresentPluralObject ] ),
        ( nameConcept, nameConcept, namePlaceProper, namePlaceProper, [ 'The', nameEventSingular, 'of', nameConcept ] ),
    ],
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, [ adverbAdjective, adjectiveObject ] ),
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectPluralCommon ),
    ],
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, [ adverbAdjective, adjectiveObject ] ),
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectPluralCommon ),
    ],
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, adjectiveNumber, [ adjectiveNumber, adjectiveObject ] ),
        nameObjectPluralCommon,
    ],
    [
        nameObjectProper,
        ( 'of', 'of', 'From' ),
        namePlaceProper,
    ],
    [
        nameObjectProper,
        ( 'of', 'of', 'From' ),
        namePlaceProper,
    ],
    [
        'The',
        ( [ nameObjectSingularCommon, 'of' ], [ nameObjectPluralCommon, ( 'of', 'of', 'From' ) ] ),
        namePlaceProper,
    ],
    [
        'The',
        ( [ nameObjectSingularCommon, 'of' ], [ nameObjectPluralCommon, ( 'of', 'of', 'From' ) ] ),
        namePlaceProper,
    ],
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, [ adverbAdjective, adjectiveObject ] ),
        ( nameObjectSingularCommon, nameObjectPluralCommon ),
        'From',
        namePlaceProper,
    ],
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, adjectiveNumber, [ adjectiveNumber, adjectiveObject ] ),
        nameObjectPluralCommon,
        'From',
        namePlaceProper,
    ],
    [
        'The',
        ( nameObjectSingularCommon, nameObjectPluralCommon ),
        'of',
        namePlaceProper,
    ],
    [
        adjectiveNumber,
        ( [ adjectiveObject, nameObjectPluralCommon ], [ adjectiveCharacter, nameCharacterPluralCommon ] )
    ],
    [
        'The',
        adjectiveNumber,
        nameTimePlural,
        'of',
        nameConcept,
    ],
    [
        adjectiveNumber,
        nameTimePlural,
        'of',
        nameConcept,
    ],
    [
        'A',
        nameTimeSingular,
        'of',
        nameConcept,
    ],
    [
        adjectiveNumber,
        nameTimePlural,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        'A',
        nameTimeSingular,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        'The',
        adjectiveObject,
        nameObjectSingularCommon,
        'of',
        nameConcept
    ],
    [
        'The',
        adjectiveObject,
        nameObjectSingularCommon,
        'From',
        namePlaceProper,
    ],
    [
        'The',
        adjectiveObject,
        nameObjectSingularCommon,
        'From',
        namePlaceProper,
    ],
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        'From',
        namePlaceProper,
    ],
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        'From',
        namePlaceProper,
    ],
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentSingularPlace ),
        'The',
        ( adjectivePlace, adjectivePlace, adjectivePlace, [ adverbAdjective, adjectivePlace ] ),
        namePlaceCommon,
    ],
    [
        nameCharacterSingularProper,
        ( 'and', verbPhraseGerundObject, verbPhrasePresentSingularObject ),
        ( nameObjectProper, nameObjectProper, [ 'The', nameObjectSingularCommon ], [ 'The', nameObjectPluralCommon ] ),
    ],
    [
        nameCharacterPluralProper,
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentPluralPlace ),
        ( namePlaceProper, namePlaceProper, [ 'The', nameEventSingular, 'of', nameConcept ] ),
    ],
    [
        nameCharacterPluralProper,
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentPluralPlace ),
        ( namePlaceProper, namePlaceProper, [ 'The', nameEventSingular, 'of', nameConcept ] ),
    ],
    [
        nameCharacterPluralProper,
        ( 'and', 'Lost In', verbPhraseGerundCharacter, verbPhrasePresentPluralCharacter ),
        nameConcept
    ],
    [
        nameCharacterSingularProper,
        ( verbPhrasePresentSingularCharacter ),
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        nameCharacterPluralProper,
        ( verbPhrasePresentPluralCharacter ),
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        ( 'Against', 'vs.', 'vs.' ),
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        'With',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        'With',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundCharacter,
        nameConcept,
    ],
    [
        'Have',
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameWeaponSingular, nameWeaponSingular, nameVehicleSingular, nameVehicleSingular, nameObjectProper ),
        'Will Travel',
    ],
    [
        verbPhraseGerundPlace,
        nameConcept,
        'With',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundPlace,
        nameConcept,
        'With',
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundPlace,
        nameConcept,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        verbPhraseGerundCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        verbPhraseGerundCharacter,
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
    ],
    [
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        nameCharacterSingularProper,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ],
    [
        'The',
        namePlaceCommon,
        'of',
        namePlaceProperSimple,
    ],
    [
        'The',
        namePlaceCommon,
        'of',
        namePlaceProperSimple,
    ],
    [
        ( [ 'The', nameEventSingular ], [ 'The', nameEventPlural ], [ 'The', adjectivePlace, nameEventSingular ], [ 'The', adjectivePlace, nameEventPlural ] ),
        'of',
        namePlaceProper,
    ],
    [
        ( [ 'The', nameEventSingular ], [ 'The', nameEventPlural ], [ 'The', adjectivePlace, nameEventSingular ], [ 'The', adjectivePlace, nameEventPlural ] ),
        'of',
        namePlaceProper,
    ],
    [
        ( [ 'The', nameEventSingular ], [ 'The', nameEventPlural ], [ 'The', adjectivePlace, nameEventSingular ], [ 'The', adjectivePlace, nameEventPlural ] ),
        'of',
        namePlaceProper,
    ],
    [
        nameCharacterSingularProper,
        prepositionalPhraseSingularCommon,
        'The',
        ( adjectivePlace, adjectivePlace, adjectivePlace, [ adverbAdjective, adjectivePlace ] ),
        namePlaceCommon,
    ],
    [
        nameCharacterSingularCommon,
        ( 'With A', 'Without A' ),
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectSingularCommon, [ adjectiveObject, nameObjectSingularCommon ] ),
    ],
    [
        nameCharacterPluralCommon,
        ( 'With', 'Without' ),
        ( nameObjectPluralCommon, nameObjectPluralCommon, nameObjectPluralCommon, [ adjectiveObject, nameObjectPluralCommon ], nameConcept ),
    ],
    [
        nameCharacterSingularProper,
        'and The',
        adjectiveCharacter,
        nameCharacterPluralCommon,
    ],
    [
        nameCharacterSingularProper,
        'and The',
        adjectiveCharacter,
        nameCharacterPluralCommon,
    ],
    [
        'Between',
        namePlaceProper,
        'and',
        namePlaceProper,
    ],
    [
        nameDirection,
        'of',
        namePlaceProper,
    ],
    [
        nameConcept,
        ',',
        nameDirection,
        'of',
        namePlaceProperSimple,
    ],
    [
        'A',
        nameGroupTypePrepend,
        'of',
        ( nameCharacterPluralCommon, nameCharacterPluralCommon, [ adjectiveCharacter, nameCharacterPluralCommon ] ),
    ],
    [
        'A',
        nameGroupTypePrepend,
        'of',
        ( nameCharacterPluralCommon, nameCharacterPluralCommon, [ adjectiveCharacter, nameCharacterPluralCommon ] ),
    ],
    [
        'A',
        nameCharacterSingularCommon,
        ( 'of', 'From' ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept ),
    ],
    [
        'A',
        nameCharacterSingularCommon,
        ( 'of', 'From' ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept ),
    ],
    [
        'The',
        ( nameEventPlural, nameEventPlural, namePossessionSingular, namePossessionSingular, namePossessionPlural, [ adjectiveCharacter, namePossessionPlural ], [ adjectiveCharacter, namePossessionPlural ], nameEventPlural, [ adjectiveObject, nameEventPlural ], nameCharacterSingularLeader, nameCharacterSingularLeader, nameCharacterPluralLeader ),
        'of',
        nameCharacterSingularProper
    ],
    [
        'The',
        ( nameEventPlural, nameEventPlural, namePossessionSingular, namePossessionSingular, namePossessionPlural, [ adjectiveCharacter, namePossessionPlural ], [ adjectiveCharacter, namePossessionPlural ], nameEventPlural, [ adjectiveObject, nameEventPlural ], nameCharacterSingularLeader, nameCharacterSingularLeader, nameCharacterPluralLeader ),
        'of',
        nameCharacterSingularProper
    ],
    [
        nameCharacterSingularProper,
        prepositionalPhraseSingularCommon,
        namePlaceProper,
    ],
    [
        ( verbPhraseGerundPlace, verbPhraseGerundPlace, verbPhraseGerundPlace, [ adverbVerb, verbPhraseGerundPlace ] ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept )
    ],
    [
        ( verbPhraseGerundPlace, verbPhraseGerundPlace, verbPhraseGerundPlace, [ adverbVerb, verbPhraseGerundPlace ] ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept )
    ],
    [
        ( 'The', 'A' ),
        nameObjectSingularCommon,
        'of',
        namePlaceProper,
    ],
    [
        ( 'The', 'A' ),
        nameObjectSingularCommon,
        'of',
        namePlaceProper,
    ],
    [
        "I Was A",
        adjectiveCharacter,
        nameCharacterSingularCommon,
    ],
    [
        ( 'The', 'A' ),
        nameCharacterSingularLeader,
        'of',
        ( nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        ( 'The', 'A' ),
        nameCharacterSingularLeader,
        'of',
        ( nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper, [ 'The', nameEventSingular ], nameEventPlural ),
        prepositionalPhraseEvent,
        'The',
        ( nameEventSingular, nameEventPlural ),
    ],
    [
        'From',
        nameConcept,
        'To',
        nameConcept,
    ],
    [
        ( [ 'To', nameConcept ], nameConcept, nameConcept ),
        'Through',
        nameConcept,
    ],
    [
        nameConcept,
        'and',
        nameConcept,
    ],
    [
        nameConcept,
        ',',
        nameConcept,
        'and',
        nameConcept,
    ],
    [
        'The',
        nameCharacterSingularLeader,
        'of',
        nameConcept,
    ],
    [
        'The',
        nameCharacterSingularLeader,
        'of',
        nameCharacterPluralCommon,
    ],
    [
        ( verbPhraseGerundCharacter, verbPhraseGerundPlace, verbPhraseGerundObject ),
        nameConcept,
    ],
    [
        verbPhraseGerundCharacter,
        nameConcept,
        prepositionalPhraseSingularCommon,
        namePlaceProper,
    ],
    [
        'The',
        ( nameConcept, nameConcept, nameGroupDescription ),
        nameEventPlural,
    ],
    [
        'The',
        ( nameConcept, nameConcept, nameGroupDescription ),
        nameEventPlural,
    ],
    [
        'The',
        adjectivePlace,
        ( nameEventSingular, nameEventSingular, nameEventPlural )
    ],
    [
        'The',
        adjectivePlace,
        ( nameEventSingular, nameEventSingular, nameEventPlural )
    ],
    [
        ( 'A', 'The' ),
        nameEventStorySingular,
        'of',
        namePlaceProper,
    ],
    [
        ( 'A', 'A', 'The' ),
        nameEventStorySingular,
        'of',
        nameCharacterSingularProper,
    ],
    [
        ( nameEventStorySingular, nameEventStorySingular, nameEventStorySingular, nameEventStorySingular, nameEventStoryPlural, nameEventStoryPlural, [ adjectiveNumber, nameEventStoryPlural ] ),
        'of',
        nameConcept,
    ],
    [
        'The',
        ( nameEventStorySingular, nameEventStorySingular, nameEventStoryPlural ),
        'of The',
        adjectivePlace,
        ( nameEventSingular, nameEventSingular, nameEventPlural ),
    ],
    [
        'The',
        ( nameEventStorySingular , nameEventStoryPlural ),
        'of',
        nameConcept,
    ],
    [
        'A',
        adjectiveGeographic,
        nameEventStorySingular,
    ],
    [
        'A',
        adjectiveGeographic,
        nameEventStorySingular,
    ],
    [
        'The',
        adjectiveGeographic,
        ( nameEventStorySingular, nameEventStoryPlural ),
    ],
    [
        'The',
        adjectiveGeographic,
        ( nameEventStorySingular, nameEventStoryPlural ),
    ],
    [
        nameCharacterSingularProperSimplePossessive,
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectSingularCommon, nameObjectPluralCommon, nameObjectPluralCommon, [ adjectiveObject, nameObjectSingularCommon ], [ adjectiveObject, nameObjectPluralCommon ] ),
    ],
    [
        nameCharacterSingularProperSimplePossessive,
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectSingularCommon, nameObjectPluralCommon, nameObjectPluralCommon, [ adjectiveObject, nameObjectSingularCommon ], [ adjectiveObject, nameObjectPluralCommon ] ),
    ],
)


#//**********************************************************************
#//
#//  getWord
#//
#//**********************************************************************

def getWord( wordType ):
    if type( wordType ) is int:
        return getWord( wordLists[ wordType ] )
    elif type( wordType ) is tuple:
        return getWord( random.choice( wordType ) )
    elif type( wordType ) is str:
        return wordType
    elif type( wordType ) is list:
        result = ''

        for word in wordType:
            if result != '':
                result += ' '
            result += getWord( word )

        return result
    elif hasattr( wordType, '__call__' ):
        return wordType( )


#//**********************************************************************
#//
#//  getTitle
#//
#//**********************************************************************

def getTitle( ):
    result = getWord( random.choice( titleTypes ) )

    result = result.replace( "A A", "An A" )
    result = result.replace( "A E", "An E" )
    result = result.replace( "A I", "An I" )
    result = result.replace( "A O", "An O" )
    result = result.replace( "A U", "An U" )
    result = result.replace( "An Uni", "A Uni" )
    result = result.replace( "A Hour", "An Hour" )
    result = result.replace( "In The Edge", "On The Edge" )
    result = result.replace( " ,", "," )

    return result


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    parser = argparse.ArgumentParser( prog='BMovie' )

    parser.add_argument( '-n', '--count', type=int, action='store', default=1 )
    parser.add_argument( '-s', '--stats', action='store_true' )

    args = parser.parse_args( )

    count = args.count

    for i in range( 0, count ):
        print( getTitle( ) )


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    main( )


#//**********************************************************************
#//
#//  index
#//
#//**********************************************************************

def index( req ):
    pageTitle = "BMovie 1.2, random B-Movie title generator, by Rick Gutleber, 2012"

    site = siteHeader( pageTitle )
    site += siteBody( pageTitle )
    site += siteFooter( )
    return site


#//**********************************************************************
#//
#//  siteHeader
#//
#//**********************************************************************

def siteHeader( title ):
    str = "<html><head><title>"
    str += title
    str += "</title></head><body>\n"
    return str


#//**********************************************************************
#//
#//  siteBody
#//
#//**********************************************************************

def siteBody( title ):
    result = "<h2>" + title + "</h2>"
    result += "Inspired by Mike Nelson in the Rifftrax presentation of 'Prisoners of the Lost Universe'"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "<h2>" + getTitle( ) + "</h2>"
    result += "Hit 'Refresh' for more names.  Props to Richard Hatch!<br>"
    result += "Thanks for many additional suggestions from Ian, Francine and Jeremy.<br>"
    result += "If you see a real movie name, it's luck... nothing is hard-coded.<br><br>"
    result += 'Your B-Movie needs a hero!  Why not give him a <a href="http://conceptjunkie.gotdns.com/BigMcLargeHuge.py">name</a>?<br>'
    result += 'Send suggestions, complaints or meandering stories about your goiter to <a href="mailto:rickg@his.com?subject=BigMcLargeHuge">rickg@his.com</a><br><br><br>'

    return result


#//**********************************************************************
#//
#//  siteFooter
#//
#//**********************************************************************

def siteFooter( ):
    str = "\n</body></html>"
    return str

