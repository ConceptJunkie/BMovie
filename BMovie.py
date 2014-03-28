#!/usr/bin/env python

import argparse
import random
import string


#//**********************************************************************
#//
#//  BMovieTuple
#//
#//  This class extends choice( ) by allowing for tracking most-recently
#//  selected items and making sure it doesn't choose the same item
#//  within a certain threshold of choices.
#//
#//  The threshold is calculated to be half
#//
#//**********************************************************************

class BMovieTuple( object ):
    def __init__( self, values ):
        global wordListCounts

        if type( values ) is list:
            self.values = [ [ item ] * repeat for item, repeat in zip( values[ : : 2 ], values[ 1 : : 2 ] ) ]
            #print( "1 --> ", end='' )
            #print( self.values )
            self.values = [ item for sublist in self.values for item in sublist ]
            #print( "2 --> ", end='' )
            #print( self.values )
        else:
            self.values = values

        self.mru = list( )

        if len( self.values ) > 2:
            self.maxHistory = len( self.values ) + 1
        elif len( self.values ) == 2:
            self.maxHistory = 1
        else:
            self.maxHistory = 0

    def choice( self ):
        while True:
            result = self.values.choice( )

            if result not in self.mru:
                break

        self.mru.append( result )

        if len( self.mru ) > len( self.values ) / 2:
            self.mru = self.mru[ 1 : ]

        return self.values[ index ]

    def __len__( self ):
        return len( self.values )

    def __getitem__( self, key ):
        return self.values[ key ]


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

nameHeroSingularCommon                      = 110
nameHeroSingularProper                      = 111
nameHeroSingularProperSimple                = 112
nameHeroSingularProperSimplePossessive      = 113
nameHeroSingularLeader                      = 114
nameHeroPluralLeader                        = 115
nameHeroPluralCommon                        = 116
nameHeroPluralProper                        = 117
nameHeroPluralProperSimple                  = 118
nameHeroPluralProperSimplePossessive        = 119

nameVillainSingularCommon                   = 130
nameVillainSingularProper                   = 131
nameVillainSingularProperSimple             = 132
nameVillainSingularProperSimplePossessive   = 133
nameVillainSingularLeader                   = 134
nameVillainPluralLeader                     = 135
nameVillainPluralCommon                     = 136
nameVillainPluralProper                     = 137
nameVillainPluralProperSimple               = 138
nameVillainPluralProperSimplePossessive     = 139

nameCharacterSingularProper                 = 150
nameCharacterPluralProper                   = 151
nameCharacterSingularProperSimplePossessive = 152
nameCharacterPluralProperSimplePossessive   = 153

nameGroupDescription                        = 160
nameGroupTypePrepend                        = 161
nameGroupTypeAppend                         = 162
nameGroupPrepend                            = 163
nameGroupAppend                             = 164

nameConcept                                 = 170
nameDirection                               = 171
nameEventSingular                           = 172
nameEventPlural                             = 173
namePlaceModifier                           = 174
nameEventEpoch                              = 175
nameEventStorySingular                      = 176
nameEventStoryPlural                        = 177
nameVehicleSingular                         = 178
nameVehiclePlural                           = 179
nameWeaponSingular                          = 180
nameWeaponPlural                            = 181
nameTimeSingular                            = 182
nameTimePlural                              = 183

nameObjectSingularCommon                    = 190
nameObjectPluralCommon                      = 191
nameObjectProper                            = 192
nameObjectProperSimple                      = 193

namePossessionSingular                      = 200
namePossessionPlural                        = 201

prepositionalPhraseSingularCommon           = 210
prepositionalPhraseSingularProper           = 211
prepositionalPhrasePluralCommon             = 212
prepositionalPhrasePluralProper             = 213
prepositionalPhraseEvent                    = 214


#//**********************************************************************
#//
#//  makePossessive
#//
#//**********************************************************************

def makePossessive( wordType ):
    result = getWord( wordType )

    if result[ -1 ] == 's':
        return result + "'"
    else:
        return result + "'s"


def makeNameHeroSingularProperSimplePossessive( ):
    return makePossessive( nameHeroSingularProperSimple )

def makeNameHeroPluralProperSimplePossessive( ):
    return makePossessive( nameHeroPluralProperSimple )

def makeNameVillainSingularProperSimplePossessive( ):
    return makePossessive( nameVillainSingularProperSimple )

def makeNameVillainPluralProperSimplePossessive( ):
    return makePossessive( nameVillainPluralProperSimple )



wordLists = {

#//**********************************************************************
#//
#//  adjectives
#//
#//**********************************************************************

    adjectiveTexture : BMovieTuple( [
        "Alabaster",    1,
        "Amber",        2,
        "Azure",        1,
        "Black",        3,
        "Blue",         2,
        "Cerulean",     1,
        "Crimson",      2,
        "Ebony",        2,
        "Glistening",   1,
        "Glowing",      1,
        "Golden",       2,
        "Green",        2,
        "Grey",         1,
        "Many-Colored", 1,
        "Orange",       1,
        "Pale",         1,
        "Purple",       1,
        "Violet",       1,
        "Red",          3,
        "Shining",      1,
        "Shiny",        1,
        "Silvery",      1,
        "Sparkling",    1,
        "Vermillion",   1,
        "White",        3,
        "Yellow",       1,
    ] ),

    adjectiveTime : BMovieTuple( (
        "Ancient",
        "Eternal",
        "Never-Ending",
        "Unending",
    ) ),

    adjectiveMental : BMovieTuple( [
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
        "Deviant",      1,
        "Enraged",      1,
        "Fearless",     3,
        "Furious",      1,
        "Gallant",      1,
        "Heroic",       3,
        "Indignant",    1,
        "Indomitable",  1,
        "Insane",       1,
        "Intrepid",     2,
        "Reckless",     1,
        "Reluctant",    1,
        "Renegade",     1,
        "Stalwart",     1,
        "Terrified",    1,
        "Unrepentant",  1,
        "Valiant",      2,
    ] ),

    adjectiveCharacterBase : BMovieTuple( [
        "Accidental",           1,
        "All-Powerful",         1,
        "Amazing",              2,
        "Beautiful",            1,
        "Crosstime",            1,
        "Cybernetic",           1,
        "Dangerous",            2,
        "Deadly",               2,
        "Dimension-Hopping",    1,
        "Dreadful",             1,
        "Evil",                 2,
        "Elusive",              1,
        "Giant",                1,
        "Gigantic",             2,
        "Glorious",             1,
        "Holy",                 1,
        "Howling",              1,
        "Huge",                 1,
        "Impossible",           2,
        "Kick-boxing",          1,
        "Killer",               1,
        "Lost",                 2,
        "Monstrous",            1,
        "Morphing",             1,
        "Mysterious",           3,
        "Powerful",             1,
        "Screaming",            1,
        "Teenage",              1,
        "Time-Travelling",      1,
        "Transdimensional",     1,
        "Unkillable",           1,
        "Unknowable",           1,
        "Unstoppable",          1,
        "Wild",                 2,
    ] ),

    adjectiveGeographic : BMovieTuple( (
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
    ) ),

    adjectiveCharacter : BMovieTuple( [
        adjectiveCharacterBase, 3,
        adjectiveTexture,       1,
        adjectiveGeographic,    1,
    ] ),

    adjectiveObjectBase : BMovieTuple( (
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
    ) ),

    adjectiveObject : BMovieTuple( [
        adjectiveObjectBase,    2,
        adjectiveTexture,       1,
        adjectiveGeographic,    1,
    ] ),

    adjectivePlaceBase : BMovieTuple( (
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
    ) ),

    adjectivePlace : BMovieTuple( [
        adjectivePlaceBase,     2,
        adjectiveGeographic,    1,
        adjectiveTexture
    ] ),

    adjectiveNumber : BMovieTuple( [
        "Two",                  7,
        "Three",                7,
        "Four",                 7,
        "Five",                 6,
        "Six",                  6,
        "Seven",                5,
        "Eight",                5,
        "Nine",                 5,
        "Ten",                  4,
        "A Dozen",              2,
        "A Hundred",            1,
        "One Thousand and One", 1,
    ] ),


#//**********************************************************************
#//
#//  adverbs
#//
#//**********************************************************************

    adverbVerb : BMovieTuple( (
        "Accidentally",
        "Bravely",
        "Desperately",
        "Foolishly",
        "Furiously",
        "Mysteriously",
        "Savagely",
    ) ),

    adverbAdjective : BMovieTuple( (
        "Amazingly",
        "Impossibly",
        "Mysteriously",
        "Surprisingly",
        "Unbelievably",
    ) ),


#//**********************************************************************
#//
#//  verb phrases
#//
#//**********************************************************************

    verbPhrasePresentSingularGoing : BMovieTuple( (
        "Escapes From",
        "Flies To",
        "Goes To",
        "Journeys To",
        "Sails To",
    ) ),

    verbPhrasePresentSingularAttacking : BMovieTuple( (
        "Battles",
        "Captures",
        "Declares War On",
        "Destroys",
    ) ),

    verbPhrasePresentSingularFinding : BMovieTuple( [
        "Discovers",    2,
        "Finds",        2,
        "Seeks",        1,
        "Uncovers",     1,
        "Loses",        1,
    ] ),

    verbPhrasePresentSingularPlace : BMovieTuple( [
        verbPhrasePresentSingularGoing,     2,
        verbPhrasePresentSingularAttacking, 1,
        verbPhrasePresentSingularFinding,   1,
    ] ),

    verbPhrasePresentSingularCharacter : BMovieTuple( (
        verbPhrasePresentSingularAttacking,
        verbPhrasePresentSingularFinding,
    ) ),

    verbPhrasePresentSingularObject : BMovieTuple( (
        verbPhrasePresentSingularFinding,
    ) ),

    verbPhrasePresentPluralGoing : BMovieTuple( (
        "Escape From",
        "Fly To",
        "Go To",
        "Journey To",
        "Sail To",
    ) ),

    verbPhrasePresentPluralAttacking : BMovieTuple( (
        "Battle",
        "Capture",
        "Declare War On",
        "Destroy",
    ) ),

    verbPhrasePresentPluralFinding : BMovieTuple( [
        "Discover", 2,
        "Find",     2,
        "Seek",     1,
        "Uncover",  1,
        "Lose",     2,
    ] ),

    verbPhrasePresentPluralPlace : BMovieTuple ( [
        verbPhrasePresentPluralGoing,       2,
        verbPhrasePresentPluralAttacking,   1,
        verbPhrasePresentPluralFinding,     1,
    ] ),

    verbPhrasePresentPluralCharacter : BMovieTuple( (
        verbPhrasePresentPluralAttacking,
        verbPhrasePresentPluralFinding,
    ) ),

    verbPhrasePresentPluralObject : BMovieTuple( (
        verbPhrasePresentPluralFinding,
    ) ),

    verbPhrasePastCharacter : BMovieTuple( (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastObject : BMovieTuple( (
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastGoing : BMovieTuple( (
        "Escaped From",
        "Flew To",
        "Went To",
        "Journeyed To",
        "Sailed To",
    ) ),

    verbPhrasePastAttacking : BMovieTuple( (
        "Battled",
        "Captured",
        "Declared War On",
        "Destroyed",
    ) ),

    verbPhrasePastFinding : BMovieTuple( (
        "Discovered",
        "Found",
        "Uncovered",
        "Lost",
    ) ),

    verbPhrasePastPlace : BMovieTuple( [
        verbPhrasePastGoing,        2,
        verbPhrasePastAttacking,    1,
        verbPhrasePastFinding,      1,
    ] ),

    verbPhrasePastCharacter : BMovieTuple( (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastObject : BMovieTuple( (
        verbPhrasePastFinding,
    ) ),

    verbPhraseFutureCharacter : BMovieTuple( (
        [ "Will", verbPhrasePresentSingularCharacter ]
    ) ),

    verbPhraseFutureObject : BMovieTuple( (
        [ "Will", verbPhrasePresentSingularObject ]
    ) ),

    verbPhraseFuturePlace : BMovieTuple( (
        [ "Will", verbPhrasePresentSingularPlace ]
    ) ),

    verbPhraseGerundCharacter : BMovieTuple( (
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
    ) ),

    verbPhraseGerundObject : BMovieTuple( (
        "Discovering",
        "Finding",
        "Looking For",
        "Running From",
        "Seeking",
        "Uncovering",
    ) ),

    verbPhraseGerundPlace : BMovieTuple( (
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
    ) ),


#//**********************************************************************
#//
#//  places
#//
#//**********************************************************************

    namePlaceModifier : BMovieTuple( (
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
    ) ),

    namePlaceArchitectureSingular : BMovieTuple( [
        "Castle",           2,
        "Cathedral",        1,
        "Dungeon",          1,
        "Fortress",         2,
        "Inner Sanctum",    1,
        "Palace",           2,
        "Stronghold",       2,
        "Temple",           2,
        "Tower",            2,
    ] ),

    namePlaceArchitecturePlural : BMovieTuple( [
        "Castles",          2,
        "Cathedrals",       1,
        "Dungeons",         1,
        "Palaces",          2,
        "Temples",          2,
        "Towers",           2,
    ] ),

    namePlaceTerritorySingular : BMovieTuple( (
        "City",
        "Empire",
        "Kingdom",
        "Republic",
        "Territory",
        "City-State",
    ) ),

    namePlaceTerritoryPlural : BMovieTuple( (
        "Cities",
        "Empires",
        "Kingdoms",
        "Republics",
        "Territories",
        "City-States",
    ) ),

    namePlaceGeographySingular : BMovieTuple( (
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
    ) ),

    namePlaceGeographyPlural : BMovieTuple( (
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
    ) ),

    namePlaceCommon : BMovieTuple( [
        namePlaceArchitecturePlural,    1,
        namePlaceArchitectureSingular,  1,
        namePlaceGeographyPlural,       2,
        namePlaceGeographySingular,     2,
        namePlaceTerritoryPlural,       1,
        namePlaceTerritorySingular,     2,
    ),

    namePlaceProper : BMovieTuple( [
        namePlaceProperSimple,                                          6,
        [ namePlaceModifier, namePlaceProperSimple ],                   2,
        [ 'The', namePlaceProperArticle ],                              6,
        [ 'The', adjectivePlace, namePlaceCommon ],                     4,
        [ 'The', adjectivePlace, namePlaceProperArticle ],              4,
        [ 'The', namePlaceCommon, 'of', nameConcept ],                  2,
        [ 'The', namePlaceCommon, 'of', namePlaceProperSimple ],        1,
        [ 'The', namePlaceCommon, 'of The', namePlaceProperArticle ],   1,
    ] ),

    namePlaceProperSimple : BMovieTuple( (
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

    namePlaceProperArticle : BMovieTuple( [
        "Amazon",                           2,
        "Andes",                            1,
        "Andromeda Galaxy",                 1,
        "Beginning of Time",                2,
        "Burmuda Triangle",                 1,
        "Congo",                            1,
        "Distant Future",                   1,
        "Distant Past",                     1,
        "Eighth Dimension",                 1,
        "Eighth Planet",                    1,
        "Eleventh Planet",                  1,
        "End of Time",                      2,
        "Fifth Dimension",                  1,
        "Fourth Dimension",                 1,
        "Future",                           2,
        "Himalayas",                        1,
        "Jungle",                           1,
        "Land Before Time",                 1,
        "Land of Oz",                       1,
        "Lost World",                       2,
        "Marianas Trench",                  1,
        "Milky Way",                        1,
        "Moon",                             1,
        "New World",                        1,
        "Ninth Dimension",                  1,
        "Ninth Planet",                     1,
        "North Pole",                       1,
        "Occident",                         1,
        "OK Corral",                        1,
        "Old World",                        1,
        "Orient",                           1,
        "Outback",                          1,
        "Past",                             2,
        "Pleiades",                         1,
        "River Kwai",                       1,
        "Sargasso Sea",                     1,
        "Seven Seas",                       3,
        "Seventh Dimension",                1,
        "Sixth Dimension",                  1,
        "South Pole",                       3,
        "Tenth Planet",                     1,
        "Thirteenth Planet",                1,
        "Twelfth Planet",                   1,
        "Wild West",                        3,
        [ "City of", nameConcept ],         1,
        [ "Forest of", nameConcept ],       1,
        [ "Island of", nameConcept ],       1,
        [ "Lost City of", nameConcept ],    1,
        [ "Mountains of", nameConcept ],    1,
        [ "River of", nameConcept ],        1,
    ),

#//**********************************************************************
#//
#//  heroes
#//
#//**********************************************************************

    nameHeroSingularLeader : (
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

    nameHeroPluralLeader : (
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

    nameHeroSingularCommon : (
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

    nameHeroSingularProperSimple : (
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


    nameHeroPluralCommon : (
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

    nameHeroPluralProperSimple : (
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

    nameHeroSingularProper : (
        [ nameHeroSingularProperSimple ],
        [ nameHeroSingularProperSimple ],
        [ nameHeroSingularProperSimple ],
        [ nameHeroSingularProperSimple ],
        [ nameHeroSingularProperSimple ],
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

    nameHeroPluralProper : (
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ nameHeroPluralProperSimple ],
        [ 'The', adjectiveCharacter, nameHeroPluralCommon ],
        [ 'The', adjectiveCharacter, nameHeroPluralCommon ],
        [ 'The', adjectiveCharacter, nameHeroPluralCommon, 'of', nameConcept ],
        [ 'The', adjectiveCharacterBase, nameHeroPluralCommon ],
        [ 'The', adjectiveCharacterBase, nameHeroPluralCommon ],
        [ 'The', adjectiveObject, nameHeroPluralCommon ],
        [ 'The', adjectiveObject, nameHeroPluralCommon ],
        [ 'The', adjectiveObject, nameHeroPluralCommon, 'of The', nameDirection ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon ],
        [ 'The', nameHeroPluralCommon, 'of The', nameDirection ],
    ),

    nameHeroSingularProperSimplePossessive : makeNameHeroSingularProperSimplePossessive,
    nameHeroPluralProperSimplePossessive : makeNameHeroPluralProperSimplePossessive,


#//**********************************************************************
#//
#//  villains
#//
#//**********************************************************************

    nameVillainSingularLeader : (
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

    nameVillainPluralLeader : (
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

    nameVillainSingularCommon : (
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

    nameVillainSingularProperSimple : (
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

    nameVillainPluralCommon : (
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

    nameVillainPluralProperSimple : (
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

    nameVillainSingularProper : (
        [ nameVillainSingularProperSimple ],
        [ nameVillainSingularProperSimple ],
        [ nameVillainSingularProperSimple ],
        [ nameVillainSingularProperSimple ],
        [ nameVillainSingularProperSimple ],
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

    nameVillainPluralProper : (
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ nameVillainPluralProperSimple ],
        [ 'The', adjectiveCharacter, nameVillainPluralCommon ],
        [ 'The', adjectiveCharacter, nameVillainPluralCommon ],
        [ 'The', adjectiveCharacter, nameVillainPluralCommon, 'of', nameConcept ],
        [ 'The', adjectiveCharacterBase, nameVillainPluralCommon ],
        [ 'The', adjectiveCharacterBase, nameVillainPluralCommon ],
        [ 'The', adjectiveObject, nameVillainPluralCommon ],
        [ 'The', adjectiveObject, nameVillainPluralCommon ],
        [ 'The', adjectiveObject, nameVillainPluralCommon, 'of The', nameDirection ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon ],
        [ 'The', nameVillainPluralCommon, 'of The', nameDirection ],
    ),

    nameVillainSingularProperSimplePossessive : makeNameVillainSingularProperSimplePossessive,
    nameVillainPluralProperSimplePossessive : makeNameVillainPluralProperSimplePossessive,

    nameCharacterSingularProper : ( nameHeroSingularProper, nameVillainSingularProper ),
    nameCharacterPluralProper : ( nameHeroPluralProper, nameVillainPluralProper ),

    nameCharacterSingularProperSimplePossessive : ( nameHeroSingularProperSimplePossessive, nameHeroPluralProperSimplePossessive ),
    nameCharacterSingularProperSimplePossessive : ( nameVillainSingularProperSimplePossessive, nameVillainPluralProperSimplePossessive ),


#//**********************************************************************
#//
#//  groups
#//
#//**********************************************************************

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

    prepositionalPhrasePluralProper : [
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
    ],
}


#//**********************************************************************
#//
#//  titles
#//
#//**********************************************************************

titleTypes = (
    [
        ( nameCharacterSingularProper, nameCharacterPluralProper ),
        prepositionalPhrasePluralCommon,
        namePlaceProper
    ],
    [
        'The',
        adjectiveCharacter,
        ( nameHeroSingularCommon, nameVillainSingularCommon ),
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
        ( nameCharacterSingularProper, nameCharacterSingularProper, nameCharacterPluralProper, nameCharacterPluralProper, nameCharacterPluralProper, [ 'The', nameHeroSingularCommon ], [ 'The', nameHeroSingularCommon ], [ 'The', nameVillainSingularCommon ], [ 'The', nameVillainSingularCommon ], ),
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
        ( nameHeroPluralCommon, nameVillainPluralCommon ),
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
        ( [ adjectiveObject, nameObjectPluralCommon ], [ adjectiveCharacter, ( nameHeroPluralCommon, nameVillainPluralCommon ) ] )
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
        nameHeroSingularCommon,
        ( 'With A', 'Without A' ),
        ( nameObjectSingularCommon, nameObjectSingularCommon, nameObjectSingularCommon, [ adjectiveObject, nameObjectSingularCommon ] ),
    ],
    [
        nameHeroPluralCommon,
        ( 'With', 'Without' ),
        ( nameObjectPluralCommon, nameObjectPluralCommon, nameObjectPluralCommon, [ adjectiveObject, nameObjectPluralCommon ], nameConcept ),
    ],
    [
        nameHeroSingularProper,
        'and The',
        adjectiveCharacter,
        nameHeroPluralCommon,
    ],
    [
        nameHeroSingularProper,
        'and The',
        adjectiveCharacter,
        nameHeroPluralCommon,
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
        ( nameHeroPluralCommon, nameHeroPluralCommon, nameVillainPluralCommon, nameVillainPluralCommon, [ adjectiveCharacter, nameHeroPluralCommon ], [ adjectiveCharacter, nameHeroPluralCommon ] ),
    ],
    [
        'A',
        nameGroupTypePrepend,
        'of',
        ( nameHeroPluralCommon, nameHeroPluralCommon, nameVillainPluralCommon, nameVillainPluralCommon, [ adjectiveCharacter, nameHeroPluralCommon ], [ adjectiveCharacter, nameHeroPluralCommon ] ),
    ],
    [
        'A',
        nameHeroSingularCommon,
        ( 'of', 'From' ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept ),
    ],
    [
        'A',
        nameHeroSingularCommon,
        ( 'of', 'From' ),
        ( namePlaceProper, namePlaceProper, namePlaceProper, nameConcept ),
    ],
    [
        'The',
        ( nameEventPlural, nameEventPlural, namePossessionSingular, namePossessionSingular, namePossessionPlural, [ adjectiveCharacter, namePossessionPlural ], [ adjectiveCharacter, namePossessionPlural ], nameEventPlural, [ adjectiveObject, nameEventPlural ], nameHeroSingularLeader, nameHeroSingularLeader, nameHeroPluralLeader ),
        'of',
        nameHeroSingularProper
    ],
    [
        'The',
        ( nameEventPlural, nameEventPlural, namePossessionSingular, namePossessionSingular, namePossessionPlural, [ adjectiveCharacter, namePossessionPlural ], [ adjectiveCharacter, namePossessionPlural ], nameEventPlural, [ adjectiveObject, nameEventPlural ], nameHeroSingularLeader, nameHeroSingularLeader, nameHeroPluralLeader ),
        'of',
        nameHeroSingularProper
    ],
    [
        nameHeroSingularProper,
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
        nameVillainSingularCommon,
    ],
    [
        ( 'The', 'A' ),
        nameHeroSingularLeader,
        'of',
        ( nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        ( 'The', 'A' ),
        nameHeroSingularLeader,
        'of',
        ( nameCharacterPluralProper, namePlaceProper ),
    ],
    [
        ( nameHeroSingularProper, nameHeroPluralProper, [ 'The', nameEventSingular ], nameEventPlural ),
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
        nameHeroSingularLeader,
        'of',
        nameConcept,
    ],
    [
        'The',
        nameHeroSingularLeader,
        'of',
        nameHeroPluralCommon,
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
    elif type( wordType ) in ( tuple, BMovieTuple ):
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
        # print( getTitle( ) )
        print( getWord( prepositionalPhrasePluralProper ) )


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

