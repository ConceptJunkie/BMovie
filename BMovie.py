#!/usr/bin/env python

import argparse
import random
import string


#//**********************************************************************
#//
#//  WeightedTuple
#//
#//  This class has a choice( ) function that allows for tracking
#//  most-recently selected items and making sure it doesn't choose the
#//  same item within a certain threshold of choices.
#//
#//  The threshold is calculated to be half the length of the list
#//  of unique choices rounded up.
#//
#//  There really isn't anything tuple-ish about this class, but it
#//  is used like a plan tuple in the data structures.
#//
#//**********************************************************************

class WeightedTuple( object ):
    def __init__( self, values ):
        if type( values ) is list:
            self.values = [ ]

            for i in range( 0, len( values ) - 1, 2 ):
                self.values.extend( [ values[ i ] ] * values[ i + 1 ] )

            if len( values ) > 4:
                self.maxHistory = ( len( values ) / 4 ) + 1
            elif len( values ) == 4:
                self.maxHistory = 1
            else:
                self.maxHistory = 0
        elif type( values ) is tuple:
            self.values = values

            uniqueItems = len( set( self.values ) )

            #print( self.values )
            #print( "unique: " + format( uniqueItems ) )

            if uniqueItems > 2:
                self.maxHistory = int( uniqueItems / 2 ) + 1
            elif uniqueItems == 2:
                self.maxHistory = 1
            else:
                self.maxHistory = 0

        self.mru = list( )

    def choice( self ):
        #print( self.values )
        while True:
            result = random.choice( self.values )

            if result not in self.mru:
                break

        self.mru.append( result )

        if len( self.mru ) > self.maxHistory:
            self.mru = self.mru[ 1 : ]

        return result

    def __len__( self ):
        return len( self.values )

    def __getitem__( self, key ):
        return self.values[ key ]


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
#//  replaceList
#//
#//**********************************************************************

replaceList = [
    "A A", "An A",
    "A E", "An E",
    "A I", "An I",
    "A O", "An O",
    "A U", "An U",
    "An Uni", "A Uni",
    "A Hour", "An Hour",
    "In The Edge", "On The Edge",
    " ,", ",",
    " :", ":",
]



wordLists = {

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

    adjectiveTime : WeightedTuple( (
        "Ancient",
        "Eternal",
        "Never-Ending",
        "Unending",
    ) ),

    adjectiveMental : WeightedTuple( [
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

    adjectiveCharacterBase : WeightedTuple( [
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

    adjectiveGeographic : WeightedTuple( (
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

    adjectiveCharacter : WeightedTuple( [
        adjectiveCharacterBase, 3,
        adjectiveTexture,       1,
        adjectiveGeographic,    1,
    ] ),

    adjectiveObjectBase : WeightedTuple( (
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
        "A Dozen",              2,
        "A Hundred",            1,
        "One Thousand and One", 1,
    ] ),


#//**********************************************************************
#//
#//  adverbs
#//
#//**********************************************************************

    adverbVerb : WeightedTuple( (
        "Accidentally",
        "Bravely",
        "Desperately",
        "Foolishly",
        "Furiously",
        "Mysteriously",
        "Savagely",
    ) ),

    adverbAdjective : WeightedTuple( (
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

    verbPhrasePresentSingularGoing : WeightedTuple( (
        "Escapes From",
        "Flies To",
        "Goes To",
        "Journeys To",
        "Sails To",
    ) ),

    verbPhrasePresentSingularAttacking : WeightedTuple( (
        "Battles",
        "Captures",
        "Declares War On",
        "Destroys",
    ) ),

    verbPhrasePresentSingularFinding : WeightedTuple( [
        "Discovers",    2,
        "Finds",        2,
        "Seeks",        1,
        "Uncovers",     1,
        "Loses",        1,
    ] ),

    verbPhrasePresentSingularPlace : WeightedTuple( [
        verbPhrasePresentSingularGoing,     2,
        verbPhrasePresentSingularAttacking, 1,
        verbPhrasePresentSingularFinding,   1,
    ] ),

    verbPhrasePresentSingularCharacter : WeightedTuple( (
        verbPhrasePresentSingularAttacking,
        verbPhrasePresentSingularFinding,
    ) ),

    verbPhrasePresentSingularObject : WeightedTuple( (
        verbPhrasePresentSingularFinding,
    ) ),

    verbPhrasePresentPluralGoing : WeightedTuple( (
        "Escape From",
        "Fly To",
        "Go To",
        "Journey To",
        "Sail To",
    ) ),

    verbPhrasePresentPluralAttacking : WeightedTuple( (
        "Battle",
        "Capture",
        "Declare War On",
        "Destroy",
    ) ),

    verbPhrasePresentPluralFinding : WeightedTuple( [
        "Discover", 2,
        "Find",     2,
        "Seek",     1,
        "Uncover",  1,
        "Lose",     2,
    ] ),

    verbPhrasePresentPluralPlace : WeightedTuple ( [
        verbPhrasePresentPluralGoing,       2,
        verbPhrasePresentPluralAttacking,   1,
        verbPhrasePresentPluralFinding,     1,
    ] ),

    verbPhrasePresentPluralCharacter : WeightedTuple( (
        verbPhrasePresentPluralAttacking,
        verbPhrasePresentPluralFinding,
    ) ),

    verbPhrasePresentPluralObject : WeightedTuple( (
        verbPhrasePresentPluralFinding,
    ) ),

    verbPhrasePastCharacter : WeightedTuple( (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastObject : WeightedTuple( (
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastGoing : WeightedTuple( (
        "Escaped From",
        "Flew To",
        "Went To",
        "Journeyed To",
        "Sailed To",
    ) ),

    verbPhrasePastAttacking : WeightedTuple( (
        "Battled",
        "Captured",
        "Declared War On",
        "Destroyed",
    ) ),

    verbPhrasePastFinding : WeightedTuple( (
        "Discovered",
        "Found",
        "Uncovered",
        "Lost",
    ) ),

    verbPhrasePastPlace : WeightedTuple( [
        verbPhrasePastGoing,        2,
        verbPhrasePastAttacking,    1,
        verbPhrasePastFinding,      1,
    ] ),

    verbPhrasePastCharacter : WeightedTuple( (
        verbPhrasePastAttacking,
        verbPhrasePastFinding,
    ) ),

    verbPhrasePastObject : WeightedTuple( (
        verbPhrasePastFinding,
    ) ),

    verbPhraseFutureCharacter : WeightedTuple( (
        [ "Will", verbPhrasePresentSingularCharacter ]
    ) ),

    verbPhraseFutureObject : WeightedTuple( (
        [ "Will", verbPhrasePresentSingularObject ]
    ) ),

    verbPhraseFuturePlace : WeightedTuple( (
        [ "Will", verbPhrasePresentSingularPlace ]
    ) ),

    verbPhraseGerundCharacter : WeightedTuple( (
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

    verbPhraseGerundObject : WeightedTuple( (
        "Discovering",
        "Finding",
        "Looking For",
        "Running From",
        "Seeking",
        "Uncovering",
    ) ),

    verbPhraseGerundPlace : WeightedTuple( (
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

    namePlaceModifier : WeightedTuple( (
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

    namePlaceArchitectureSingular : WeightedTuple( [
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

    namePlaceArchitecturePlural : WeightedTuple( [
        "Castles",          2,
        "Cathedrals",       1,
        "Dungeons",         1,
        "Palaces",          2,
        "Temples",          2,
        "Towers",           2,
    ] ),

    namePlaceTerritorySingular : WeightedTuple( (
        "City",
        "Empire",
        "Kingdom",
        "Republic",
        "Territory",
        "City-State",
    ) ),

    namePlaceTerritoryPlural : WeightedTuple( (
        "Cities",
        "Empires",
        "Kingdoms",
        "Republics",
        "Territories",
        "City-States",
    ) ),

    namePlaceGeographySingular : WeightedTuple( (
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

    namePlaceGeographyPlural : WeightedTuple( (
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

    namePlaceCommon : WeightedTuple( [
        namePlaceArchitecturePlural,    1,
        namePlaceArchitectureSingular,  1,
        namePlaceGeographyPlural,       2,
        namePlaceGeographySingular,     2,
        namePlaceTerritoryPlural,       1,
        namePlaceTerritorySingular,     2,
    ] ),

    namePlaceProper : WeightedTuple( [
        namePlaceProperSimple,                                          6,
        [ namePlaceModifier, namePlaceProperSimple ],                   2,
        [ 'The', namePlaceProperArticle ],                              6,
        [ 'The', adjectivePlace, namePlaceCommon ],                     4,
        [ 'The', adjectivePlace, namePlaceProperArticle ],              4,
        [ 'The', namePlaceCommon, 'of', nameConcept ],                  2,
        [ 'The', namePlaceCommon, 'of', namePlaceProperSimple ],        1,
        [ 'The', namePlaceCommon, 'of The', namePlaceProperArticle ],   1,
    ] ),

    namePlaceProperSimple : WeightedTuple( (
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
     ) ),

    namePlaceProperArticle : WeightedTuple( [
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
    ] ),


#//**********************************************************************
#//
#//  heroes
#//
#//**********************************************************************

    nameHeroSingularLeader : WeightedTuple( (
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
    ) ),

    nameHeroPluralLeader : WeightedTuple( [
        "Barons",       1,
        "Bishops",      1,
        "Chieftains",   3,
        "Commanders",   3,
        "Counts",       1,
        "Dukes",        1,
        "Heroes",       4,
        "Kings",        3,
        "Knights",      4,
        "Lords",        3,
        "Masters",      3,
        "Priests",      3,
        "Princes",      3,
        "Prophets",     3,
        "Queens",       3,
        "Rulers",       2,
        "Sheiks",       1,
        "Wizards",      3,
    ] ),

    nameHeroSingularCommon : WeightedTuple( (
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
    ) ),

    nameHeroSingularProperSimple : WeightedTuple( (
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
    ) ),

    nameHeroPluralCommon : WeightedTuple( (
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
    ) ),

    nameHeroPluralProperSimple : WeightedTuple( (
        "Abbott and Costello",
        "Penn and Teller",
        "The Beatles",
        "The Green Berets",
        "The Hawklords",
        "The Martians",
        "The Space Marines",
        "The Space Rangers",
        "The Three Stooges",
    ) ),

    nameHeroSingularProper : WeightedTuple( [
        [ nameHeroSingularProperSimple ],                   5,
        [ nameGroupDescription, nameGroupTypePrepend ],     3,
        [ nameGroupPrepend, nameGroupTypePrepend ],         3,
        [ nameGroupTypeAppend, nameGroupAppend ],           1,
        [ nameGroupTypeAppend, nameGroupDescription ],      3,
        [ 'The', nameGroupTypeAppend, 'of', nameConcept ],  1,
        [ nameConcept, nameGroupTypePrepend ],              1,
    ] ),

    nameHeroPluralProper : WeightedTuple( [
        [ nameHeroPluralProperSimple ],                                             8,
        [ 'The', adjectiveCharacter, nameHeroPluralCommon ],                        2,
        [ 'The', adjectiveCharacter, nameHeroPluralCommon, 'of', nameConcept ],     1,
        [ 'The', adjectiveCharacterBase, nameHeroPluralCommon ],                    2,
        [ 'The', adjectiveObject, nameHeroPluralCommon ],                           2,
        [ 'The', adjectiveObject, nameHeroPluralCommon, 'of The', nameDirection ],  1,
        [ 'The', nameHeroPluralCommon ],                                            7,
        [ 'The', nameHeroPluralCommon, 'of The', nameDirection ],                   1,
    ] ),

    nameHeroSingularProperSimplePossessive : makeNameHeroSingularProperSimplePossessive,
    nameHeroPluralProperSimplePossessive : makeNameHeroPluralProperSimplePossessive,


#//**********************************************************************
#//
#//  villains
#//
#//**********************************************************************

    nameVillainSingularLeader : WeightedTuple( [
        "Baron",        1,
        "Caliph",       1,
        "Chieftain",    3,
        "Commander",    3,
        "Congress",     1,
        "Count",        2,
        "Countess",     1,
        "Duchess",      1,
        "Duke",         2,
        "Earl",         1,
        "Emperor",      6,
        "Emperess",     4,
        "King",         4,
        "Knight",       3,
        "Lord",         3,
        "Master",       2,
        "Parliament",   1,
        "Patrician",    3,
        "President",    1,
        "Priest",       3,
        "Prince",       3,
        "Princess",     3,
        "Prophet",      3,
        "Queen",        4,
        "Raj",          1,
        "Ruler",        2,
        "Sheik",        1,
        "Tyrant",       6,
        "Viscount",     1,
        "Wizard",       3,
    ] ),

    nameVillainPluralLeader : WeightedTuple( (
        "Barons",       1,
        "Bishops",      1,
        "Chieftains",   3,
        "Commanders",   3,
        "Counts",       1,
        "Dictators",    2,
        "Dukes",        1,
        "Emperors",     3,
        "Emperesses",   1,
        "Kings",        3,
        "Knights",      5,
        "Lords",        3,
        "Masters",      3,
        "Priests",      3,
        "Princes",      3,
        "Prophets",     3,
        "Queens",       2,
        "Rulers",       2,
        "Sheiks",       1,
        "Tyrants",      6,
        "Viziers",      3,
        "Wizards",      3,
    ) ),

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

    nameConcept : WeightedTuple ( [
        "Adversity",        1,
        "Beauty",           1,
        "Confusion",        1,
        "Danger",           2,
        "Darkness",         1,
        "Death",            1,
        "Deceit",           1,
        "Defeat",           1,
        "Desire",           1,
        "Destiny",          1,
        "Doom",             2,
        "Enlightenment",    1,
        "Eternity",         1,
        "Everything",       1,
        "Evil",             1,
        "Evolution",        1,
        "Fear",             1,
        "Forever",          1,
        "Glory",            1,
        "Gold",             1,
        "Good",             1,
        "Gravity",          1,
        "Hate",             1,
        "History",          1,
        "Hope",             1,
        "Horror",           1,
        "Infamy",           1,
        "Infinity",         2,
        "Life",             1,
        "Light",            1,
        "Lore",             1,
        "Love",             1,
        "Madness",          1,
        "Magic",            2,
        "Mystery",          2,
        "Oblivion",         2,
        "Oppression",       1,
        "Poverty",          1,
        "Prejudice",        1,
        "Pride",            1,
        "Prosperity",       1,
        "Redemption",       1,
        "Resurrection",     1,
        "Revelation",       1,
        "Righteousness",    1,
        "Sanity",           1,
        "Science",          2,
        "Space",            3,
        "Spirituality",     1,
        "Technology",       1,
        "The Occult",       2,
        "The Universe",     1,
        "Terror",           1,
        "Time",             1,
        "Triumph",          1,
        "Truth",            1,
        "Victory",          1,
    ] ),

    nameDirection : WeightedTuple( [
        "Deep South",   1,
        "East",         2,
        "Far East",     1,
        "Far North",    1,
        "Far West",     1,
        "Inside",       1,
        "North",        2,
        "Outside",      1,
        "South",        2,
        "West",         2,
    ] ),

    nameEventSingular : WeightedTuple( (
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
    ) ),

    nameEventEpoch : WeightedTuple ( [
        "Century",      1,
        "Day",          6,
        "Decade",       1,
        "Eon",          1,
        "Epoch",        2,
        "Era",          3,
        "Millennium",   1,
        "Night",        6,
        "Month",        2,
        "Time",         6,
        "Week",         3,
        "Year",         3,
    ] ),

    nameEventStorySingular : WeightedTuple( [
        "Adventure",    1,
        "Epic",         1,
        "Fable",        1,
        "History",      2,
        "Legend",       3,
        "Mystery",      2,
        "Myth",         1,
        "Odyssey",      1,
        "Saga",         2,
        "Song",         1,
        "Scenario",     1,
        "Story",        2,
        "Tale",         2,
        "Trilogy",      1,
    ] ),

    nameEventStoryPlural : WeightedTuple( [
        "Adventures",   2,
        "Fables",       1,
        "Legends",      2,
        "Mysteries",    1,
        "Myths",        1,
        "Songs",        1,
        "Stories",      2,
        "Tales",        2,
    ] ),

    nameEventPlural : WeightedTuple ( (
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
    ) ),

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

    nameObjectSingularCommon : (
        WeightedTuple( [
            "Android",      2,
            "Book",         1,
            "Clue",         1,
            "Code",         1,
            "Codex",        1,
            "Coffin",       1,
            "Computer",     2,
            "Mechanoid",    1,
            "Moon",         1,
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

    nameObjectPluralCommon : (
        WeightedTuple( [
            "Androids",     1,
            "Computers",    1,
            "Guns",         3,
            "Jewels",       1,
            "Mysteries",    2,
            "Robots",       1,
            "Secrets",      1,
            "Treasures",    1,
        ] ),
        nameVehiclePlural,
        nameWeaponPlural,
    ),

    nameObjectProper : WeightedTuple( [
        nameObjectProperSimple,                             5,
        [
            'The',
            nameObjectSingularCommon,
            'of',
            WeightedTuple( [
                namePlaceProper,                3,
                [ 'The', nameDirection ],       1,
                nameCharacterSingularProper,    3,
                nameCharacterPluralProper,      3 ,
            ] )
        ],                                                  2,
        [
            'The',
            nameWeaponSingular,
            'of',
            (
                namePlaceProper,
                nameConcept,
                [ 'The', nameDirection ],
                nameCharacterSingularProper,
                nameCharacterPluralProper
            )
        ],                                                  1,
        [
            'The',
            adjectiveObject,
            nameObjectSingularCommon
        ],                                                  6,
        [
            'The',
            adverbAdjective,
            adjectiveObjectBase,
            nameObjectSingularCommon
        ],                                                  2,
        [
            'The',
            adjectiveObject,
            nameObjectSingularCommon,
            'of',
            WeightedTuple( [
                namePlaceProper,                3,
                [ 'The', nameDirection ],       1,
                nameCharacterSingularProper,    3,
                nameCharacterPluralProper,      3,
            ] ),
        ],                                                  1,
        [
            'The',
            adjectiveObject,
            nameWeaponSingular,
            'of',
            (
                namePlaceProper,
                nameConcept,
                [ 'The', nameDirection ],
                nameCharacterSingularProper,
                nameCharacterPluralProper,
            )
        ],                                                  1,
        [
            nameCharacterSingularProperSimplePossessive,
            nameObjectSingularCommon
        ],                                                  2,
        [
            nameCharacterSingularProperSimplePossessive,
            nameWeaponSingular
        ],                                                  1,
        [
            nameCharacterSingularProperSimplePossessive,
            nameConcept
        ],                                                  1,
        [
            nameCharacterSingularProperSimplePossessive,
            adjectiveObject,
            nameObjectSingularCommon,
        ],                                                  2,
        [
            nameCharacterSingularProperSimplePossessive,
            nameObjectSingularCommon,
            'of',
            nameConcept,
        ],                                                  2,
        [
            nameCharacterSingularProperSimplePossessive,
            nameObjectSingularCommon,
            'of',
            nameConcept
        ],                                                  1,
        [
            nameCharacterSingularProperSimplePossessive,
            adjectiveObject,
            nameObjectSingularCommon,
            'of',
            nameConcept
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

    namePossessionSingular : WeightedTuple( (
        "Anger",
        "Betrayal",
        "Bravery",
        "Choice",
        "Daughter",
        "Decision",
        "Desire",
        "Desires",
        "Father",
        "Fury",
        "Gun",
        "Guns",
        "Intuition",
        "Legacy",
        "Revenge",
        "Son",
        "Sword",
        "Wife",
        "Wrath",
    ) ),

    namePossessionPlural : WeightedTuple( (
        "Sons",
        "Daughters",
        "Children",
        "Wives",
        "Enemies",
    ) ),

    prepositionalPhraseSingularCommon : WeightedTuple( (
        "Above",
        "Against",
        "Beneath",
        "Beyond",
        "In Search of",
        "In",
        "Inside",
        "On",
    ) ),

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
        WeightedTuple( [ nameObjectProper, 3, [ 'The', nameObjectSingularCommon ], 3, [ 'The', adjectiveObject, nameObjectSingularCommon ] ] ),
    ],
    [
        ( [ 'The', namePossessionPlural ], [ 'The', namePossessionPlural ], [ 'The', ( adjectiveObject, adjectiveObject, adjectiveCharacter, adjectiveNumber ), namePossessionPlural ] ),
        'of',
        WeightedTuple( [ nameCharacterSingularProper, 2, nameCharacterPluralProper, 2, namePlaceProper ] ),
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
        WeightedTuple( [ adjectivePlace, 3, [ adverbAdjective, adjectivePlace ], 1 ] ),
        namePlaceCommon,
    ],
    [
        nameHeroSingularCommon,
        ( 'With A', 'Without A' ),
        WeightedTuple( [ nameObjectSingularCommon, 3, [ adjectiveObject, nameObjectSingularCommon ], 1 ] ),
    ],
    [
        nameHeroPluralCommon,
        ( 'With', 'Without' ),
        WeightedTuple( [ nameObjectPluralCommon, 3, [ adjectiveObject, nameObjectPluralCommon ], 1, nameConcept, 1 ] ),
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
        WeightedTuple( [ nameHeroPluralCommon, 2, nameVillainPluralCommon, 2, [ adjectiveCharacter, nameHeroPluralCommon ], 1, [ adjectiveCharacter, nameVillainPluralCommon ], 1 ] ),
    ],
    [
        'A',
        nameGroupTypePrepend,
        'of',
        WeightedTuple( [ nameHeroPluralCommon, 1, nameVillainPluralCommon, 2, [ adjectiveCharacter, nameHeroPluralCommon ], 2 ] ),
    ],
    [
        'A',
        nameHeroSingularCommon,
        ( 'of', 'From' ),
        WeightedTuple( [ namePlaceProper, 3, nameConcept, 1 ] )
    ],
    [
        'A',
        nameHeroSingularCommon,
        ( 'of', 'From' ),
        WeightedTuple( [ namePlaceProper, 3, nameConcept, 1 ] )
    ],
    [
        'The',
        WeightedTuple( [
            nameEventPlural,                                2,
            namePossessionSingular,                         2,
            namePossessionPlural,                           1,
            [ adjectiveCharacter, namePossessionPlural ],   2,
            nameEventPlural,                                1,
            [ adjectiveObject, nameEventPlural ],           1,
            nameHeroSingularLeader,                         2,
            nameHeroPluralLeader,                           1
        ] ),
        'of',
        nameHeroSingularProper
    ],
    [
        'The',
        WeightedTuple( [
            nameEventPlural,                                2,
            namePossessionSingular,                         2,
            namePossessionPlural,                           1,
            [ adjectiveCharacter, namePossessionPlural ],   2,
            nameEventPlural,                                1,
            [ adjectiveObject, nameEventPlural ],           1,
            nameHeroSingularLeader,                         2,
            nameHeroPluralLeader,                           1
        ] ),
        'of',
        nameHeroSingularProper
    ],
    [
        nameHeroSingularProper,
        prepositionalPhraseSingularCommon,
        namePlaceProper,
    ],
    [
        WeightedTuple( [ verbPhraseGerundPlace, 3, [ adverbVerb, verbPhraseGerundPlace ], 1 ] ),
        WeightedTuple( [ namePlaceProper, 3, nameConcept, 1 ] )
    ],
    [
        WeightedTuple( [ verbPhraseGerundPlace, 3, [ adverbVerb, verbPhraseGerundPlace ], 1 ] ),
        WeightedTuple( [ namePlaceProper, 3, nameConcept, 1 ] )
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
        WeightedTuple( [ nameEventStorySingular, 4, nameEventStoryPlural, 2, [ adjectiveNumber, nameEventStoryPlural ] , 1 ] ),
        'of',
        nameConcept,
    ],
    [
        'The',
        WeightedTuple( [ nameEventStorySingular, 2, nameEventStoryPlural, 1 ] ),
        'of The',
        adjectivePlace,
        WeightedTuple( [ nameEventSingular, 2, nameEventPlural, 1 ] ),
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
        WeightedTuple( [
            nameObjectSingularCommon,                       3,
            nameObjectPluralCommon,                         2,
            [ adjectiveObject, nameObjectSingularCommon ],  1,
            [ adjectiveObject, nameObjectPluralCommon ],    1,
        ] ),
    ],
    [
        nameCharacterSingularProperSimplePossessive,
        WeightedTuple( [
            nameObjectSingularCommon,                       3,
            nameObjectPluralCommon,                         2,
            [ adjectiveObject, nameObjectSingularCommon ],  1,
            [ adjectiveObject, nameObjectPluralCommon ],    1,
        ] ),
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
    elif type( wordType ) is WeightedTuple:
        return getWord( wordType.choice( ) )
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

    for i in range( 0, len( replaceList ) - 1, 2 ):
        result = result.replace( replaceList[ i ], replaceList[ i + 1 ] )

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
    pageTitle = "BMovie 1.3, random B-Movie title generator, by Rick Gutleber, 2012"

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

