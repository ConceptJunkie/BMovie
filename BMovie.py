#!/usr/bin/env python

import argparse
import random
import string


#//**********************************************************************
#//
#//  constants
#//
#//**********************************************************************

class adjective( ) :
    def __init__( self ):
adjectiveActionHero                         = 0
adjectiveActionVillain                      = 1
adjectiveAge                                = 2
adjectiveBaseHero                           = 3
adjectiveBaseVillain                        = 4
adjectiveGeographic                         = 5
adjectiveHero                               = 6
adjectiveHeroNongeographic                  = 7
adjectiveMentalHero                         = 8
adjectiveMentalVillain                      = 9
adjectiveNumber                             = 10
adjectiveObject                             = 11
adjectiveObjectBase                         = 12
adjectivePhysicalHero                       = 13
adjectivePhysicalVillain                    = 14
adjectivePlace                              = 15
adjectivePlaceBase                          = 16
adjectiveTexture                            = 17
adjectiveTime                               = 18
adjectiveVillain                            = 19
adjectiveVillainNongeographic               = 20
adjectiveVocationHero                       = 21
adjectiveVocationVillain                    = 22

adverbVerb                                  = 100
adverbAdjective                             = 101

# all verb phrases are transitive for now, prepositions included where appropriate, the final descriptor refers to the object
verbPhrasePresentSingularCharacter          = 200
verbPhrasePresentSingularObject             = 201
verbPhrasePresentSingularPlace              = 202
verbPhrasePresentSingularGoing              = 203
verbPhrasePresentSingularAttacking          = 204
verbPhrasePresentSingularFinding            = 205

verbPhrasePresentPluralCharacter            = 300
verbPhrasePresentPluralObject               = 301
verbPhrasePresentPluralPlace                = 302
verbPhrasePresentPluralGoing                = 303
verbPhrasePresentPluralAttacking            = 304
verbPhrasePresentPluralFinding              = 305

verbPhrasePastCharacter                     = 400
verbPhrasePastObject                        = 401
verbPhrasePastPlace                         = 402
verbPhrasePastGoing                         = 403
verbPhrasePastAttacking                     = 404
verbPhrasePastFinding                       = 405

verbPhraseFutureCharacter                   = 500
verbPhraseFutureObject                      = 501
verbPhraseFuturePlace                       = 502
verbPhraseFutureGoing                       = 503
verbPhraseFutureAttacking                   = 504
verbPhraseFutureFinding                     = 505

verbPhraseGerundCharacter                   = 600
verbPhraseGerundObject                      = 601
verbPhraseGerundPlace                       = 602

namePlaceCommon                             = 700
namePlaceProper                             = 701
namePlaceProperSimple                       = 702
namePlaceProperArticle                      = 703
namePlaceArchitectureSingular               = 704
namePlaceArchitecturePlural                 = 705
namePlaceGeographySingular                  = 706
namePlaceGeographyPlural                    = 707
namePlaceTerritorySingular                  = 708
namePlaceTerritoryPlural                    = 709

nameHeroSingularCommon                      = 800
nameHeroSingularProper                      = 801
nameHeroSingularProperSimple                = 802
nameHeroSingularProperSimplePossessive      = 803
nameHeroSingularLeader                      = 804
nameHeroPluralLeader                        = 805
nameHeroPluralCommon                        = 806
nameHeroPluralGeographicCommon              = 807
nameHeroPluralProper                        = 808
nameHeroPluralProperSimple                  = 809
nameHeroPluralProperSimplePossessive        = 810

nameVillainSingularCommon                   = 900
nameVillainSingularProper                   = 901
nameVillainSingularProperSimple             = 902
nameVillainSingularProperSimplePossessive   = 903
nameVillainSingularLeader                   = 904
nameVillainPluralLeader                     = 905
nameVillainPluralCommon                     = 906
nameVillainPluralGeographicCommon           = 907
nameVillainPluralProper                     = 908
nameVillainPluralProperSimple               = 909
nameVillainPluralProperSimplePossessive     = 910

nameGroupDescription                        = 1000
nameGroupTypePrepend                        = 1001
nameGroupTypeAppend                         = 1002
nameGroupPrepend                            = 1003
nameGroupAppend                             = 1004

nameAnimalPlural                            = 1100
nameAnimalSingular                          = 1101
nameConcept                                 = 1102
nameConceptNegative                         = 1103
nameConceptPositive                         = 1104
nameConceptNeutral                          = 1105
nameDirection                               = 1106
nameEventEpoch                              = 1107
nameEventPlural                             = 1108
nameEventSingular                           = 1109
nameEventStoryPlural                        = 1110
nameEventStorySingular                      = 1111
nameModifier                                = 1112
namePlaceModifier                           = 1113
nameTimePlural                              = 1114
nameTimeSingular                            = 1115
nameVehiclePlural                           = 1116
nameVehicleSingular                         = 1117
nameTitleHero                               = 1118
nameTitleVillain                            = 1119
nameWeaponPlural                            = 1120
nameWeaponSingular                          = 1121

nameObjectPluralCommon                      = 1200
nameObjectPluralCommon1                     = 1201
nameObjectProper                            = 1202
nameObjectProperSimple                      = 1203
nameObjectSingularCommon                    = 1204
nameObjectSingularCommon1                   = 1205

namePossessionHeroSingular                  = 1300
namePossessionVillainSingular               = 1301
namePossessionHeroPlural                    = 1302
namePossessionVillainPlural                 = 1303

prepositionalPhraseSingularCommon           = 1400
prepositionalPhraseSingularProper           = 1401
prepositionalPhrasePluralCommon             = 1402
prepositionalPhrasePluralProper             = 1403
prepositionalPhraseEvent                    = 1404


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
    "- ", "-",
]


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
                # print( values[ i ] )
                # print( values[ i + 1 ] )
                self.values.extend( [ values[ i ] ] * values[ i + 1 ] )

            if len( values ) > 4:
                self.maxHistory = int( len( values ) / 4 ) + 1
            elif len( values ) == 4:
                self.maxHistory = 1
            else:
                self.maxHistory = 0

        elif type( values ) is tuple:
            self.values = values

            if len( self.values ) > 2:
                self.maxHistory = int( len( self.values ) / 2 ) + 1
            elif len( self.values ) == 2:
                self.maxHistory = 1
            else:
                self.maxHistory = 0

        self.mru = list( )

    def choice( self ):
        # print( self.values )
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
#//  Name Generator
#//
#//  C - starting consonant
#//  V - vowel
#//  D - multi-consant
#//  c - end consonant
#//  d - ending multi-consonant
#//
#//**********************************************************************

nameTypes = WeightedTuple( [
    "Cv",       1,
    "CVc",      1,
    "CVcCVc",   1,
    "CVcCVd",   1,
    "CVcDVc",   1,
    "CVcDVd",   1,
    "CVCv",     1,
    "CVCVc",    1,
    "CVCVCv",   1,
    "CVCVd",    1,
    "CVd",      1,
    "DVcCVc",   1,
    "DVcCVd",   1,
    "DVcDVc",   1,
    "DVcDVd",   1,
    "DVd",      1,
    "Vc",       1,
    "VCCv",     1,
    "VCv",      1,
    "VCVc",     1,
    "VCVCv",    1,
    "VCVDv",    1,
    "Vd",       1,
    "VDVc",     1,
    "VDVCv",    1,
    "VDVDv",    1,
] )

startingConsonant = WeightedTuple( [
    "B",        1,
    "CH",       2,
    "D",        2,
    "F",        1,
    "G",        2,
    "J",        1,
    "K",        1,
    "L",        3,
    "M",        3,
    "N",        3,
    "P",        2,
    "R",        4,
    "S",        4,
    "SH",       2,
    "T",        4,
    "TH",       3,
    "V",        2,
    "W",        1,
    "Y",        1,
    "Z",        1,
] )

startingMultiConsonant = WeightedTuple( [
    "BL",       1,
    "BR",       1,
    "DR",       1,
    "FL",       1,
    "FR",       1,
    "GL",       1,
    "GR",       1,
    "KL",       1,
    "KR",       1,
    "PL",       1,
    "PR",       1,
    "SK",       1,
    "SKL",      1,
    "SKR",      1,
    "ST",       1,
    "STR",      1,
    "THR",      1,
    "TR",       1,
] )

vowel = WeightedTuple( [
    "A",        2,
    "E",        2,
    "I",        1,
    "O",        3,
    "U",        1,
    "a",        3,
    "e",        4,
    "i",        3,
    "o",        2,
    "u",        2,
    "au",       1,
] )

endingConsonant = WeightedTuple( [
    "B",        1,
    "CH",       1,
    "D",        2,
    "F",        1,
    "G",        2,
    "J",        1,
    "K",        2,
    "L",        3,
    "M",        3,
    "N",        3,
    "P",        1,
    "R",        4,
    "S",        4,
    "SH",       2,
    "T",        4,
    "TH",       4,
    "V",        2,
    "Z",        1,
] )

endingMultiConsonant = WeightedTuple( [
    "LB",       1,
    "LCH",      1,
    "LD",       1,
    "LG",       1,
    "LJ",       1,
    "LK",       1,
    "LM",       1,
    "LN",       1,
    "LP",       1,
    "LS",       1,
    "LSH",      1,
    "LST",      1,
    "LT",       1,
    "LTH",      1,
    "NCH",      1,
    "ND",       1,
    "NG",       1,
    "NJ",       1,
    "NK",       1,
    "NS",       1,
    "NSH",      1,
    "NST",      1,
    "NT",       1,
    "NTH",      1,
    "RCH",      1,
    "RD",       1,
    "RG",       1,
    "RJ",       1,
    "RLB",      1,
    "RLD",      1,
    "RLG",      1,
    "RLJ",      1,
    "RLK",      1,
    "RLM",      1,
    "RLN",      1,
    "RLSH",     1,
    "RLST",     1,
    "RLTH",     1,
    "RM",       1,
    "RN",       1,
    "RP",       1,
    "RS",       1,
    "RSH",      1,
    "RST",      1,
    "RT",       1,
    "RTH",      1,
    "SHK",      1,
    "SHT",      1,
    "SK",       1,
    "ST",       1,
] )


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

    adjectiveTime : WeightedTuple( (
        "Ancient",
        "Eternal",
        "Never-Ending",
        "Prehistoric",
        "Unending",
    ) ),

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
        "Beautiful",            1,
        "Cybernetic",           1,
        "Mutant",               1,
        "Radioactive",          1,
    ] ),

    adjectivePhysicalVillain : WeightedTuple( [
        "50-Foot",              1,
        "Colossal",             1,
        "Cybernetic",           2,
        "Decomposing",          1,
        "Ectoplasmic",          1,
        "Exploding",            1,
        "Fanged",               1,
        "Giant",                1,
        "Gigantic",             2,
        "Invisible",            1,
        "Monstrous",            1,
        "Mutant",               2,
        "Poisonous",            1,
        "Radioactive",          2,
        "Shriveled",            1,
        "Shrunken",             1,
        "Slimy",                1,
        "Venemous",             1,
    ] ),

    adjectiveVocationHero : WeightedTuple( [
        "Ninja",                1,
    ] ),

    adjectiveVocationVillain : WeightedTuple( [
        "Ninja",                1,
        "Pirate",               1,
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
        "Baby",                 1,
        "Kid",                  1,
        "Teenage",              3,
        "Elderly",              3,
        "Decrepit",             1,
        "Ancient",              3,
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
        "Attacked",
        "Battled",
        "Captured",
        "Conquered",
        "Declared War On",
        "Defeated",
        "Destroyed",
    ) ),

    verbPhrasePastFinding : WeightedTuple( (
        "Discovered",
        "Found",
        "Lost",
        "Uncovered",
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

    namePlaceModifier : WeightedTuple( [
        "Central",                  1,
        "Darkest",                  1,
        "Deepest",                  1,
        "Depths of",                1,
        "Inner",                    1,
        "Lower",                    1,
        "Outer",                    1,
        "The Bottom of",            1,
        "The Depths of",            1,
        "The Edge of",              1,
        "The Furthest Reaches of",  1,
        "The Inside of",            1,
        "The Outside of",           1,
        "The Top of",               1,
        "Upper",                    1,
    ] ),

    namePlaceArchitectureSingular : WeightedTuple( [
        "Castle",           2,
        "Cathedral",        1,
        "Cemetary",         1,
        "Circus",           1,
        "Crypt",            1,
        "Dungeon",          1,
        "Fortress",         2,
        "Inner Sanctum",    1,
        "Mausoleum",        1,
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

    namePlaceTerritorySingular : WeightedTuple( [
        "City",             1,
        "Empire",           1,
        "Kingdom",          1,
        "Republic",         1,
        "Territory",        1,
        "City-State",       1,
    ] ),

    namePlaceTerritoryPlural : WeightedTuple( [
        "Cities",           1,
        "Empires",          1,
        "Kingdoms",         1,
        "Republics",        1,
        "Territories",      1,
        "City-States",      1,
    ] ),

    namePlaceGeographySingular : WeightedTuple( [
        "Cave",             1,
        "Cavern",           1,
        "Continent",        1,
        "Desert",           1,
        "Dimension",        1,
        "Forest",           1,
        "Galaxy",           1,
        "Jungle",           1,
        "Land",             1,
        "March",            1,
        "Marsh",            1,
        "Mountain",         1,
        "Netherworld",      1,
        "Ocean",            1,
        "Plain",            1,
        "Planet",           1,
        "Sea",              1,
        "Swamp",            1,
        "Underworld",       1,
        "Universe",         1,
        "Volcano",          1,
        "Wasteland",        1,
    ] ),

    namePlaceGeographyPlural : WeightedTuple( [
        "Caverns",          1,
        "Caves",            1,
        "Deserts",          1,
        "Dimensions",       1,
        "Forests",          1,
        "Galaxies",         1,
        "Jungles",          1,
        "Lands",            1,
        "Marches",          1,
        "Marshes",          1,
        "Mountains",        1,
        "Oceans",           1,
        "Plains",           1,
        "Planets",          1,
        "Seas",             1,
        "Swamps",           1,
        "Wastelands",       1,
    ] ),

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
        "Camelot",
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
#//  name modifiers
#//
#//**********************************************************************

    nameModifier : WeightedTuple( [
        "Astro-",       2,
        "Crypto-",      1,
        "Electro-",     2,
        "Hypno-",       1,
        "Mechano-",     1,
        "Mega-",        2,
        "Micro-",       1,
        "Nano-",        1,
        "Pseudo-",      1,
        "Psycho-",      1,
        "Quasi-",       1,
        "Retro-",       1,
        "Syntho-",      1,
    ] ),


#//**********************************************************************
#//
#//  animals
#//
#//**********************************************************************

    nameAnimalSingular : WeightedTuple( (
        "Ape",
        "Arachnid",
        "Cat",
        "Dinosaur",
        "Dog",
        "Dragon",
        "Gorilla",
        "Hornet",
        "Insect",
        "Leech",
        "Lion",
        "Lizard",
        "Serpent",
        "Shark",
        "Snake",
        "Spider",
        "Tarantula",
        "Tiger",
        "Wasp",
        "Wolf",
    ) ),

    nameAnimalPlural : WeightedTuple( (
        "Apes",
        "Arachnids",
        "Cats",
        "Dinosaurs",
        "Dogs",
        "Dragons",
        "Gorillas",
        "Hornets",
        "Insects",
        "Leechs",
        "Lions",
        "Lizards",
        "Serpents",
        "Sharks",
        "Snakes",
        "Spiders",
        "Tarantulas",
        "Tigers",
        "Wasps",
        "Wolves",
    ) ),

#//**********************************************************************
#//
#//  heroes
#//
#//**********************************************************************

    nameHeroSingularCommon : WeightedTuple( [
        "Alien",            1,
        "Ape",              1,
        "Cat",              1,
        "Commando",         1,
        "Dog",              1,
        "Dwarf",            1,
        "Elf",              1,
        "Gangster",         1,
        "Gorilla",          1,
        "Hero",             1,
        "Kid",              1,
        "King",             1,
        "Knight",           1,
        "Pauper",           1,
        "Prince",           1,
        "Queen",            1,
        "Princess",         1,
        "President",        1,
        "Ranger",           1,
        "Rebel",            1,
        "Robot",            1,
        "Mechanoid",        1,
        "Sheriff",          1,
        "Soldier",          1,
        "Spy",              1,
        "Wizard",           1,
    ] ),

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

    nameHeroPluralGeographicCommon : WeightedTuple( (
        "Earthlings",
        "Jovians",
        "Lunarians",
        "Martians",
        "Mecurians",
        "Neptunians",
        "Plutonians",
        "Saturnians",
        "Terrans",
        "Titanians",
        "Uranians",
        "Venusians",
    ) ),

    nameHeroPluralCommon : WeightedTuple( (
        "Aliens",
        "Apes",
        "Barbarians",
        "Commandos",
        "Dinosaurs",
        "Dolphins",
        "Dwarves",
        "Gangsters",
        "Ghosts",
        "Gorillas",
        "Hordes",
        "Kings",
        "Mummies",
        "Prisoners",
        "Rangers",
        "Robots",
        "Savages",
        "Spirits",
        "Terrans",
        "Throngs",
        "Vampires",
        "Vikings",
        "Warriors",
    ) ),

    nameHeroPluralProperSimple : WeightedTuple( [
        "Abbott and Costello",      1,
        "Penn and Teller",          1,
        "The Beatles",              1,
        "The Green Berets",         3,
        "The Hawklords",            3,
        "The Martians",             3,
        "The Space Marines",        3,
        "The Space Rangers",        3,
        "The Three Stooges",        1,
    ] ),

    nameHeroSingularLeader : WeightedTuple( [
        "Abbot",            1,
        "Baron",            1,
        "Bishop",           1,
        "Caliph",           1,
        "Chieftain",        2,
        "Commander",        3,
        "Congress",         1,
        "Count",            2,
        "Countess",         1,
        "Duchess",          1,
        "Duke",             2,
        "Earl",             1,
        "Emperor",          4,
        "Emperess",         3,
        "Hero",             4,
        "Heroine",          4,
        "King",             4,
        "Knight",           3,
        "Lord",             3,
        "Master",           2,
        "Parliament",       1,
        "Patrician",        1,
        "Pope",             1,
        "President",        1,
        "Priest",           3,
        "Prime Minister",   1,
        "Prince",           3,
        "Princess",         3,
        "Prophet",          3,
        "Queen",            4,
        "Raj",              1,
        "Ruler",            2,
        "Sheik",            1,
        "Tyrant",           3,
        "Viscount",         1,
        "Wizard",           3,
    ] ),

    nameHeroPluralLeader : WeightedTuple( [
        "Barons",           1,
        "Bishops",          1,
        "Chieftains",       3,
        "Commanders",       3,
        "Counts",           1,
        "Dukes",            1,
        "Heroes",           4,
        "Kings",            3,
        "Knights",          4,
        "Lords",            3,
        "Masters",          3,
        "Priests",          3,
        "Princes",          3,
        "Prophets",         3,
        "Queens",           3,
        "Rulers",           2,
        "Sheiks",           1,
        "Wizards",          3,
    ] ),

    nameHeroSingularProper : WeightedTuple( [
        nameHeroSingularProperSimple,                               5,
        [ 'The', nameGroupTypeAppend, 'of', nameConceptPositive ],  1,
        [ 'The', nameGroupTypeAppend, 'of', nameConceptNeutral ],   1,
        [ nameConceptPositive, nameGroupTypePrepend ],              1,
        [ nameConceptNeutral, nameGroupTypePrepend ],               1,
        [ nameGroupDescription, nameGroupTypePrepend ],             3,
        [ nameGroupPrepend, nameGroupTypePrepend ],                 3,
        [ nameGroupTypeAppend, nameGroupAppend ],                   1,
        [ nameGroupTypeAppend, nameGroupDescription ],              3,
    ] ),

    nameHeroPluralProper : WeightedTuple( [
        nameHeroPluralProperSimple,                                                     8,
        [ 'The', adjectiveHero, nameHeroPluralCommon, 'of', nameConceptNeutral ],       1,
        [ 'The', adjectiveHero, nameHeroPluralCommon ],                                 2,
        [ 'The', adjectiveHero, nameHeroPluralCommon, 'of The', nameDirection ],        1,
        [ 'The', adjectiveHero, nameHeroPluralCommon, 'of', nameConceptPositive ],      1,
        [ 'The', adjectiveObject, nameHeroPluralCommon ],                               1,
        [ 'The', nameHeroPluralCommon ],                                                6,
        [ 'The', nameHeroPluralCommon, 'of The', nameDirection ],                       1,
    ] ),

    nameHeroSingularProperSimplePossessive : makeNameHeroSingularProperSimplePossessive,
    nameHeroPluralProperSimplePossessive : makeNameHeroPluralProperSimplePossessive,


#//**********************************************************************
#//
#//  villains
#//
#//**********************************************************************

    nameVillainSingularCommon : WeightedTuple( [
        "Alien",                            1,
        "Assassin",                         1,
        "Beast",                            1,
        "Blob",                             1,
        "Brute",                            1,
        "Cannibals",                        1,
        "Commando",                         1,
        "Communists",                       1,
        "Cultist",                          1,
        "Cyborg",                           1,
        "Demon",                            1,
        "Devil",                            1,
        "Djinn",                            1,
        "Dwarf",                            1,
        "Elf",                              1,
        "Force",                            1,
        "Gangster",                         1,
        "Ghost",                            1,
        "Ghoul",                            1,
        "Goblin",                           1,
        "Invader",                          1,
        "Killer",                           1,
        "King",                             1,
        "Knight",                           1,
        "Kraken",                           1,
        "Mechanoid",                        1,
        "Mummy",                            1,
        "Nazis",                            1,
        "Ninja",                            1,
        "Orc",                              1,
        "Parasite",                         1,
        "Pirate",                           1,
        "Prince",                           1,
        "Princess",                         1,
        "Queen",                            1,
        "Rebel",                            1,
        "Revenant",                         1,
        "Robot",                            1,
        "Servant",                          1,
        "Slave",                            1,
        "Spy",                              1,
        "Stranger",                         1,
        "Swamp Creature",                   1,
        "Thief",                            1,
        "Thrall",                           1,
        "Traitor",                          1,
        "Troll",                            1,
        "Vampire",                          1,
        "Viking",                           1,
        "Villain",                          1,
        "Warrior",                          1,
        "Werewolf",                         1,
        "Wizard",                           1,
        "Zombie",                           1,
        nameAnimalSingular,                 1,
        [ nameAnimalSingular, "Child" ],    1,
        [ nameAnimalSingular, "Creature" ], 1,
        [ nameAnimalSingular, "Man" ],      1,
        [ nameAnimalSingular, "Woman" ],    1,
    ] ),

    nameTitleHero : WeightedTuple( [
        "Captain",          3,
        "Commander",        1,
        "Doctor",           3,
        "Dr.",              3,
        "Duke",             1,
        "General",          1,
        "King",             1,
        "Lieutenant",       1,
        "Major",            1,
        "Prince",           2,
        "Princess",         2,
        "Professor",        3,
        "Queen",            1,
        "Sergeant",         2,
    ] ),

    nameTitleVillain : WeightedTuple( [
        "Captain",          3,
        "Commander",        1,
        "Doctor",           3,
        "Dr.",              3,
        "Duke",             1,
        "General",          1,
        "King",             1,
        "Lieutenant",       1,
        "Major",            1,
        "Prince",           2,
        "Princess",         2,
        "Professor",        3,
        "Queen",            1,
        "Sergeant",         2,
    ] ),

    nameVillainSingularProperSimple : WeightedTuple( (
        "Colossus",
        "Dr. X",
        "Dr. Z",
        "Dracula",
        "Frankenstein",
        "Fu Manchu",
        "Harcourt Fenton Mudd",
        "Hitler",
        "Jared Syn",
        "Lizzie Borden",
        "Nosferatu",
        "The Cyclops",
        "The Minotaur",
        "The Sheriff of Nottingham",
    ) ),

    nameVillainPluralCommon : WeightedTuple( [
        "Aliens",                               1,
        "Assassins",                            1,
        "Beasts",                               1,
        "Blobs",                                1,
        "Brutes",                               1,
        "Cannibals",                            1,
        "Commandos",                            1,
        "Communists",                           1,
        "Cultists",                             1,
        "Cyborgs",                              1,
        "Demons",                               1,
        "Devils",                               1,
        "Djinns",                               1,
        "Dwarves",                              1,
        "Elves",                                1,
        "Gangsters",                            1,
        "Ghosts",                               1,
        "Ghouls",                               1,
        "Goblins",                              1,
        "Invaders",                             1,
        "Killers",                              1,
        "Knights",                              1,
        "Krakens",                              1,
        "Mechanoids",                           1,
        "Mummies",                              1,
        "Nazis",                                1,
        "Ninjas",                               1,
        "Orcs",                                 1,
        "Pirates",                              1,
        "Rebels",                               1,
        "Revenants",                            1,
        "Robots",                               1,
        "Servants",                             1,
        "Slaves",                               1,
        "Spies",                                1,
        "Strangers",                            1,
        "Swamp Creatures",                      1,
        "Thieves",                              1,
        "Thralls",                              1,
        "Traitors",                             1,
        "Trolls",                               1,
        "Vampires",                             1,
        "Vikings",                              1,
        "Villains",                             1,
        "Warriors",                             1,
        "Werewolves",                           1,
        "Wizards",                              1,
        "Zombies",                              1,
        nameAnimalPlural,                       1,
        [ "The Cult of", nameConceptNegative ], 2,
        [ nameAnimalSingular, "Children" ],     1,
        [ nameAnimalSingular, "Creatures" ],    3,
        [ nameAnimalSingular, "Men" ],          3,
        [ nameAnimalSingular, "People" ],       3,
        [ nameAnimalSingular, "Women" ],        3,
    ] ),

    nameVillainPluralProperSimple : WeightedTuple( (
        "Plural Villain 1",
        "Plural Villain 2",
        "Plural Villain 3",
    ) ),

    nameVillainSingularLeader : WeightedTuple( [
        "Baron",        1,
        "Caliph",       1,
        "Chieftain",    3,
        "Commander",    3,
        "Conqueror",    1,
        "Corpse",       1,
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
        "Outlaw",       3,
        "Overlord",     2,
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

    nameVillainPluralLeader : WeightedTuple( [
        "Barons",       1,
        "Bishops",      1,
        "Chieftains",   3,
        "Commanders",   3,
        "Conquerors",   1,
        "Counts",       1,
        "Dictators",    2,
        "Dukes",        1,
        "Emperors",     3,
        "Emperesses",   1,
        "Kings",        3,
        "Knights",      5,
        "Lords",        3,
        "Masters",      3,
        "Outlaws",      3,
        "Overlords",    2,
        "Priests",      3,
        "Princes",      3,
        "Prophets",     3,
        "Queens",       2,
        "Rulers",       2,
        "Sheiks",       1,
        "Tyrants",      6,
        "Viziers",      3,
        "Wizards",      3,
    ] ),

    nameVillainSingularProper : WeightedTuple( [
        nameVillainSingularProperSimple,        5,
        [
            nameGroupDescription,
            nameGroupTypePrepend,
        ],                                      3,
        [
            nameGroupPrepend,
            nameGroupTypePrepend,
        ],                                      3,
        [
            nameGroupTypeAppend,
            nameGroupAppend,
        ],                                      1,
        [
            nameGroupTypeAppend,
            nameGroupDescription,
        ],                                      3,
        [
            'The',
            nameGroupTypeAppend,
            'of',
            nameConceptNegative,
        ],                                      1,
        [
            'The',
            nameGroupTypeAppend,
            'of The',
            nameDirection,
        ],                                      1,
        [
            nameConceptNegative,
            nameGroupTypePrepend
        ],                                      1,
    ] ),

    nameVillainPluralProper : WeightedTuple( [
        [ nameVillainPluralProperSimple ],      6,
        [ 'The', nameVillainPluralCommon ],     6,
        [
            'The',
            adjectiveVillain,
            nameVillainPluralCommon
        ],                                      3,
        [
            'The',
            nameVillainPluralCommon,
            'of The',
            nameDirection
        ],                                      1,
        [
            'The',
            adjectiveVillain,
            nameVillainPluralCommon,
            'of',
            nameConceptNegative
        ],                                      1,
    ] ),

    nameVillainSingularProperSimplePossessive : makeNameVillainSingularProperSimplePossessive,
    nameVillainPluralProperSimplePossessive : makeNameVillainPluralProperSimplePossessive,


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
        "League",
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
        nameConceptPositive,
        nameConceptNeutral,
        nameConceptNegative,
    ),

#//**********************************************************************
#//
#//  concepts
#//
#//**********************************************************************

    nameConceptNeutral : WeightedTuple( [
        "Destiny",          1,
        "Eternity",         1,
        "Everything",       1,
        "Evolution",        1,
        "Forever",          1,
        "Gold",             1,
        "Gravity",          1,
        "History",          1,
        "Infinity",         2,
        "Lore",             1,
        "Magic",            2,
        "Mystery",          2,
        "Science",          2,
        "Space",            3,
        "Technology",       1,
        "The Universe",     1,
        "Time",             1,
    ] ),

    nameConceptPositive : WeightedTuple( [
        "Beauty",           1,
        "Enlightenment",    1,
        "Glory",            1,
        "Good",             1,
        "Hope",             1,
        "Life",             1,
        "Light",            1,
        "Love",             1,
        "Pride",            1,
        "Prosperity",       1,
        "Redemption",       1,
        "Resurrection",     1,
        "Revelation",       1,
        "Righteousness",    1,
        "Sanity",           1,
        "Spirituality",     1,
        "Triumph",          1,
        "Truth",            1,
        "Victory",          1,
    ] ),

    nameConceptNegative : WeightedTuple ( [
        "Adversity",        1,
        "Confusion",        1,
        "Danger",           2,
        "Darkness",         1,
        "Death",            1,
        "Deceit",           1,
        "Defeat",           1,
        "Delusion",         1,
        "Despair",          1,
        "Doom",             2,
        "Evil",             1,
        "Famine",           1,
        "Fear",             1,
        "Hate",             1,
        "Horror",           1,
        "Infamy",           1,
        "Madness",          1,
        "Oblivion",         2,
        "Oppression",       1,
        "Pestilence",       1,
        "Poverty",          1,
        "Prejudice",        1,
        "Rage",             1,
        "Shame",            1,
        "Sin",              1,
        "Terror",           1,
        "The Occult",       2,
    ] ),

    nameDirection : WeightedTuple( [
        "Deep South",       1,
        "East",             2,
        "Far East",         1,
        "Far North",        1,
        "Far West",         1,
        "Inside",           1,
        "North",            2,
        "Outside",          1,
        "South",            2,
        "West",             2,
    ] ),


#//**********************************************************************
#//
#//  events
#//
#//**********************************************************************

    nameEventSingular : WeightedTuple( (
        "Abduction",
        "Assassination",
        "Attack",
        "Battle",
        "Case",
        "Conquest",
        "Curse",
        "Dance",
        "Day",
        "Destiny",
        "Destruction",
        "Disappearance",
        "Downfall",
        "Feast",
        "Game",
        "Invasion",
        "Journey",
        "Liberation",
        "Murder",
        "Night",
        "Peril",
        "Redemption",
        "Return",
        "Revenge",
        "Storm",
        "Tempest",
        "Tragedy",
        "Trial",
        "Triumph",
        "Victory",
        "War",
    ) ),

    nameEventEpoch : WeightedTuple ( [
        "Century",          1,
        "Day",              6,
        "Decade",           1,
        "Eon",              1,
        "Epoch",            2,
        "Era",              3,
        "Millennium",       1,
        "Night",            6,
        "Month",            2,
        "Time",             6,
        "Week",             3,
        "Year",             3,
    ] ),

    nameEventStorySingular : WeightedTuple( [
        "Adventure",        1,
        "Dream",            1,
        "Epic",             1,
        "Fable",            1,
        "History",          2,
        "Legend",           3,
        "Mystery",          2,
        "Myth",             1,
        "Nightmare",        1,
        "Odyssey",          1,
        "Saga",             2,
        "Song",             1,
        "Scenario",         1,
        "Story",            2,
        "Tale",             2,
        "Trilogy",          1,
    ] ),

    nameEventStoryPlural : WeightedTuple( [
        "Adventures",       2,
        "Dreams",           1,
        "Fables",           1,
        "Legends",          2,
        "Mysteries",        1,
        "Myths",            1,
        "Nightmare",        2,
        "Songs",            1,
        "Stories",          2,
        "Tales",            2,
    ] ),

    nameEventPlural : WeightedTuple ( [
        "Adventures",       2,
        "Battles",          1,
        "Conquests",        1,
        "Curses",           1,
        "Days",             1,
        "Destruction",      1,
        "Games",            1,
        "Invasions",        1,
        "Journeys",         1,
        "Legends",          2,
        "Mysteries",        2,
        "Night",            1,
        "Perils",           1,
        "Stories",          1,
        "Storms",           1,
        "Tempests",         1,
        "Trials",           1,
        "Tribulations",     1,
        "Triumphs",         1,
        "Victories",        1,
        "Wars",             1,
    ] ),


#//**********************************************************************
#//
#//  objects
#//
#//**********************************************************************

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
        ],                                          2,
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
            'The',
            adjectiveObject,
            ( nameObjectSingularCommon, nameWeaponSingular ),
            'of',
            WeightedTuple( [
                namePlaceProper,                3,
                [ 'The', nameDirection ],       1,
                nameHeroSingularProper,         3,
                nameHeroPluralProper,           3 ,
                nameVillainSingularProper,      2,
                nameVillainPluralProper,        2 ,
            ] ),
        ],                                                  2,
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


#//**********************************************************************
#//
#//  titles
#//
#//**********************************************************************

titleTypes = WeightedTuple( [
    [
        "Assignment: ",
        WeightedTuple( [
            namePlaceProper,        6,
            nameConceptPositive,    1,
            nameConceptNeutral,     1,
        ] ),
    ], 1,
    [
        Destination,
        WeightedTuple( [
            namePlaceProper,        6,
            nameConceptPositive,    1,
            nameConceptNeutral,     1,
        ] ),
    ], 1,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        prepositionalPhrasePluralCommon,
        WeightedTuple( [
            namePlaceProper,        6,
            nameConceptPositive,    1,
            nameConceptNeutral,     1,
        ] ),
    ], 1,
    [
        'The',
        adjectiveHero,
        ( nameHeroSingularCommon, nameVillainSingularCommon ),
    ], 2,
    [
        'The',
        adjectiveHero,
        ( nameHeroSingularCommon, nameVillainSingularCommon ),
        'From',
        WeightedTuple( [
            namePlaceProper,        6,
            nameConceptPositive,    1,
            nameConceptNeutral,     1,
        ] ),
    ], 1,
    [
        'To',
        verbPhrasePresentPluralCharacter,
        ( nameHeroSingularProper, nameHeroPluralProper, nameVillainSingularProper, nameVillainPluralProper, ),
    ], 1,
    [
        'To',
        verbPhrasePresentPluralObject,
        WeightedTuple( [ nameObjectProper, 3, [ 'The', nameObjectSingularCommon ], 3, [ 'The', adjectiveObject, nameObjectSingularCommon ], 1 ] ),
    ], 2,
    [
        WeightedTuple( [
            [ 'The', namePossessionHeroPlural ],    2,
            [
                'The',
                WeightedTuple( [
                    adjectiveObject,    2,
                    adjectiveHero,      1,
                    adjectiveNumber,    1,
                ] ),
                namePossessionHeroPlural
            ],                                      1,
        ] ),
        'of',
        WeightedTuple( [ nameHeroSingularProper, 2, nameHeroPluralProper, 2, namePlaceProper, 1 ] ),
    ], 2,
    [
        WeightedTuple( [
            [ 'The', namePossessionVillainPlural ], 2,
            [
                'The',
                WeightedTuple( [
                    adjectiveObject,    2,
                    adjectiveHero,      1,
                    adjectiveNumber,    1,
                ] ),
                namePossessionVillainPlural ],      1,
        ] ),
        'of',
        WeightedTuple( [ nameVillainSingularProper, 2, nameVillainPluralProper, 2, namePlaceProper, 1 ] ),
    ], 2,
    [
        WeightedTuple( (
            [ 'The', nameEventSingular ],
            [ 'The', nameEventPlural ],
            [ 'The', WeightedTuple( [ adjectiveObject, 2, adjectiveObject, 1, adjectiveNumber, 1 ] ), nameEventPlural ],
            [ 'The', adjectiveObject, nameEventSingular ],
            [ 'The', WeightedTuple( [ adjectiveObject, 2, adjectiveHero, 1, adjectiveNumber, 1 ] ), namePossessionHeroPlural ]
        ) ),
        'of',
        WeightedTuple( (
            nameHeroSingularProper,
            nameHeroPluralProper,
            [ 'The', nameHeroSingularCommon ],
            [ 'The', nameHeroPluralCommon ],
        ) ),
    ], 5,
    [
        WeightedTuple ( (
            [ 'The', nameEventSingular ],
            [ 'The', nameEventPlural ],
            [ 'The', WeightedTuple( [ adjectiveObject, 2, adjectiveObject, 1, adjectiveNumber, 1 ] ), nameEventPlural ],
            [ 'The', adjectiveObject, nameEventSingular ],
            [ 'The', WeightedTuple( [ adjectiveObject, 2, adjectiveVillain, 1, adjectiveNumber, 1 ] ), namePossessionVillainPlural ],
        ) ),
        'of',
        WeightedTuple( (
            nameVillainSingularProper,
            nameVillainPluralProper,
            [ 'The', nameVillainSingularCommon ],
            [ 'The', nameVillainPluralCommon ],
        ) ),
    ], 5,
    [
        WeightedTuple( [
            [ 'The', ( namePossessionHeroSingular, nameEventSingular ) ],   2,
            [ 'The', ( namePossessionHeroPlural, nameEventPlural ) ],       1,
        ] ),
        'of',
        WeightedTuple( [ nameHeroSingularProper, 3, nameHeroPluralProper, 3, namePlaceProper, 1 ] ),
    ], 1,
    [
        'The',
        ( namePossessionVillainSingular, namePossessionVillainPlural ),
        'of The',
        ( nameHeroPluralCommon, nameVillainPluralCommon ),
    ], 1,
    [
        WeightedTuple( [
            [ 'The', namePossessionHeroSingular ],      1,
            [ 'The', namePossessionHeroPlural ],        2,
            [ 'The', namePossessionVillainSingular ],   1,
            [ 'The', namePossessionVillainPlural ],     2,
        ] ),
        'of',
        nameObjectProper,
    ], 1,
    [
        'The',
        nameEventPlural,
        'of',
        ( nameHeroSingularProper, nameHeroPluralProper ),
    ], 2,
    [
        nameHeroPluralProper,
    ], 1,
    [
        WeightedTuple( (
            [ nameHeroSingularProper, verbPhrasePresentSingularObject ],
            [ nameHeroPluralProper, verbPhrasePresentPluralObject ],
        ) ),
        WeightedTuple( [
            nameConceptPositive,                                    2,
            nameConceptNeutral,                                 2,
            namePlaceProper,                                    2,
            [
                'The',
                nameEventSingular,
                'of',
                ( nameConceptPositive, nameConceptNeutral ),
            ],                                                  1,
        ] ),
    ], 2,
    [
        'The',
        WeightedTuple( [
            adjectiveObject,                        3,
            [ adverbAdjective, adjectiveObject ],   1,
        ] ),
        WeightedTuple( [
            nameObjectSingularCommon,   2,
            nameObjectPluralCommon,     1,
        ] ),
    ], 2,
    [
        'The',
        WeightedTuple( [
            adjectiveObject,                        3,
            adjectiveNumber,                        1,
            [ adjectiveNumber, adjectiveObject ],   1,
        ] ),
        nameObjectPluralCommon,
    ], 2,
    [
        nameObjectProper,
        WeightedTuple( [ 'of', 2, 'From', 1 ] ),
        namePlaceProper,
    ], 3,
    [
        'The',
        ( [ nameObjectSingularCommon, 'of' ], [ nameObjectPluralCommon, WeightedTuple( [ 'of', 2, 'From', 1 ] ) ] ),
        namePlaceProper,
    ], 2,
    [
        'The',
        WeightedTuple( [
            adjectiveObject,                        3,
            [ adverbAdjective, adjectiveObject ],   1,
        ] ),
        ( nameObjectSingularCommon, nameObjectPluralCommon ),
        'From',
        namePlaceProper,
    ], 1,
    [
        'The',
        ( adjectiveObject, adjectiveObject, adjectiveObject, adjectiveNumber, [ adjectiveNumber, adjectiveObject ] ),
        nameObjectPluralCommon,
        'From',
        namePlaceProper,
    ], 1,
    [
        'The',
        ( nameObjectSingularCommon, nameObjectPluralCommon ),
        'of',
        namePlaceProper,
    ], 1,
    [
        adjectiveNumber,
        (
            [ adjectiveObject, nameObjectPluralCommon ],
            [ adjectiveHero, ( nameHeroPluralCommon, nameVillainPluralCommon )
        ] )
    ], 1,
    [
        'The',
        adjectiveNumber,
        nameTimePlural,
        'of',
        nameConcept,
    ], 2,
    [
        'A',
        nameTimeSingular,
        'of',
        nameConcept,
    ], 1,
    [
        adjectiveNumber,
        nameTimePlural,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ], 1,
    [
        'A',
        nameTimeSingular,
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ], 1,
    [
        'The',
        adjectiveObject,
        nameObjectSingularCommon,
        'of',
        nameConcept
    ], 1,
    [
        'The',
        adjectiveObject,
        nameObjectSingularCommon,
        'From',
        namePlaceProper,
    ], 2,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        'From',
        namePlaceProper,
    ], 2,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        ( 'From The', "of The" ),
        namePlaceCommon,
    ], 1,
    [
        nameHeroSingularProper,
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentSingularPlace ),
        'The',
        WeightedTuple( [ adjectivePlace, 3, [ adverbAdjective, adjectivePlace ], 1 ] ),
        namePlaceCommon,
    ], 1,
    [
        nameHeroPluralProper,
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentPluralPlace ),
        'The',
        WeightedTuple( [ adjectivePlace, 3, [ adverbAdjective, adjectivePlace ], 1 ] ),
        namePlaceCommon,
    ], 1,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        ( 'and', verbPhraseGerundObject, verbPhrasePresentSingularObject ),
        WeightedTuple( [ nameObjectProper, 2, [ 'The', nameObjectSingularCommon ], 1, [ 'The', nameObjectPluralCommon ], 1 ] ),
    ], 1,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        ( 'and', 'Lost In', verbPhraseGerundPlace, verbPhrasePresentPluralPlace ),
        WeightedTuple( [ namePlaceProper, 2, [ 'The', nameEventSingular, 'of', nameConcept ], 1 ] ),
    ], 1,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        ( 'and', 'Lost In', verbPhraseGerundCharacter, verbPhrasePresentPluralCharacter ),
        nameConcept
    ], 1,
    [
        nameHeroSingularProper,
        ( verbPhrasePresentSingularCharacter ),
        ( nameVillainSingularProper, nameVillainPluralProper ),
    ], 3,
    [
        ( nameHeroSingularProper, nameHeroPluralProper ),
        ( 'Against', 'vs.', 'vs.' ),
        ( nameVillainSingularProper, nameVillainPluralProper ),
    ], 3,
    [
        verbPhraseGerundCharacter,
        ( nameHeroSingularProper, nameHeroPluralProper ),
        'With',
        ( nameHeroSingularProper, nameHeroPluralProper ),
    ], 1,
    [
        verbPhraseGerundCharacter,
        ( nameHeroSingularProper, nameHeroPluralProper, nameVillainSingularProper, nameVillainPluralProper ),
    ], 1,
    [
        verbPhraseGerundCharacter,
        nameConcept,
    ], 1,
    [
        'Have',
        WeightedTuple( [ nameObjectSingularCommon, 1, nameWeaponSingular, 2, nameVehicleSingular, 2 ] ),
        ', Will Travel',
    ], 1,
    [
        verbPhraseGerundPlace,
        ( nameConceptPositive, nameConceptNeutral ),
        'With',
        WeightedTuple( [ nameHeroSingularProper, 2, nameHeroPluralProper, 1 ] ),
    ], 1,
    [
        verbPhraseGerundPlace,
        ( nameConceptPositive, nameConceptNeutral ),
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ], 1,
    [
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ], 1,
    [
        WeightedTuple( [ nameHeroSingularProper, 3, nameHeroPluralProper, 1 ] ),
        prepositionalPhraseSingularProper,
        namePlaceProper,
    ], 1,
    [
        'The',
        namePlaceCommon,
        'of',
        namePlaceProperSimple,
    ], 2,
    [
        ( [ 'The', nameEventSingular ], [ 'The', nameEventPlural ], [ 'The', adjectivePlace, nameEventSingular ], [ 'The', adjectivePlace, nameEventPlural ] ),
        'of',
        namePlaceProper,
    ], 3,
    [
        nameHeroSingularProper,
        prepositionalPhraseSingularCommon,
        'The',
        WeightedTuple( [ adjectivePlace, 3, [ adverbAdjective, adjectivePlace ], 1 ] ),
        namePlaceCommon,
    ], 1,
    [
        nameHeroSingularCommon,
        ( 'With A', 'Without A' ),
        WeightedTuple( [ nameObjectSingularCommon, 3, [ adjectiveObject, nameObjectSingularCommon ], 1 ] ),
    ], 1,
    [
        nameHeroPluralCommon,
        ( 'With', 'Without' ),
        WeightedTuple( [
            nameObjectPluralCommon,                         3,
            [ adjectiveObject, nameObjectPluralCommon ],    1,
            nameConceptPositive,                                1,
            nameConceptNeutral,                             1,
        ] ),
    ], 1,
    [
        nameHeroSingularProper,
        'and The',
        adjectiveHero,
        nameHeroPluralCommon,
    ], 4,
    [
        'Between',
        namePlaceProper,
        'and',
        namePlaceProper,
    ], 1,
    [
        nameDirection,
        'of',
        namePlaceProper,
    ], 1,
    [
        nameConcept,
        ',',
        nameDirection,
        'of',
        namePlaceProperSimple,
    ], 1,
    [
        'A',
        nameGroupTypePrepend,
        'of',
        WeightedTuple( [
            nameHeroPluralCommon,                           2,
            nameVillainPluralCommon,                        2,
            [ adjectiveHero, nameHeroPluralCommon ],        1,
            [ adjectiveHero, nameVillainPluralCommon ],     1,
        ] ),
    ], 1,
    [
        'A',
        nameGroupTypePrepend,
        'of',
        WeightedTuple( [
            nameHeroPluralCommon,                           2,
            nameVillainPluralCommon,                        1,
            [ adjectiveHero, nameHeroPluralCommon ],        2,
            [ adjectiveVillain, nameVillainPluralCommon ],  1,
        ] ),
    ], 1,
    [
        'A',
        nameHeroSingularCommon,
        ( 'of', 'From' ),
        WeightedTuple( [ namePlaceProper, 3, nameConceptPositive, 1, nameConceptNeutral, 1 ] )
    ], 2,
    [
        'The',
        WeightedTuple( [
            nameEventPlural,                                2,
            namePossessionHeroSingular,                     2,
            namePossessionHeroPlural,                       1,
            [ adjectiveHero, namePossessionHeroPlural ],    2,
            nameEventPlural,                                1,
            [ adjectiveObject, nameEventPlural ],           1,
            nameHeroSingularLeader,                         2,
            nameHeroPluralLeader,                           1
        ] ),
        'of',
        nameHeroSingularProper
    ], 1,
    [
        nameHeroSingularProper,
        prepositionalPhraseSingularCommon,
        namePlaceProper,
    ], 1,
    [
        WeightedTuple( [ verbPhraseGerundPlace, 3, [ adverbVerb, verbPhraseGerundPlace ], 1 ] ),
        WeightedTuple( [ namePlaceProper, 3, nameConcept, 1 ] )
    ], 2,
    [
        ( 'The', 'A' ),
        nameObjectSingularCommon,
        'of',
        namePlaceProper,
    ], 2,
    [
        "I Was A",
        adjectiveVillain,
        nameVillainSingularCommon,
    ], 1,
    [
        "I",
        verbPhrasePastAttacking,
        nameVillainPluralProper,
    ], 1,
    [
        ( 'The', 'A' ),
        nameHeroSingularLeader,
        'of',
        ( nameHeroPluralProper, namePlaceProper ),
    ], 1,
    [
        ( nameHeroSingularProper, nameHeroPluralProper, [ 'The', nameEventSingular ], nameEventPlural ),
        prepositionalPhraseEvent,
        'The',
        ( nameEventSingular, nameEventPlural ),
    ], 1,
    [
        'From',
        ( nameConceptNegative, nameConceptNeutral ),
        'To',
        nameConceptPositive,
    ], 1,
    [
        WeightedTuple( [
            [ 'To', nameConceptPositive ],      1,
            [ 'To', nameConceptNeutral ],   1,
            nameConceptPositive,                2,
            nameConceptNeutral,             2,
        ] ),
        'Through',
        nameConcept,
    ], 1,
    [
        nameConcept,
        'and',
        nameConcept,
    ], 1,
    [
        nameConcept,
        ',',
        nameConcept,
        'and',
        nameConcept,
    ], 1,
    [
        'The',
        nameHeroSingularLeader,
        'of',
        ( nameConceptPositive, nameConceptNeutral ),
    ], 1,
    [
        'The',
        nameHeroSingularLeader,
        'of',
        nameHeroPluralCommon,
    ], 2,
    [
        'The',
        nameVillainSingularLeader,
        'of',
        ( nameConceptNegative, nameConceptNeutral ),
    ], 1,
    [
        'The',
        nameVillainSingularLeader,
        'of',
        nameVillainPluralCommon,
    ], 2,
    [
        ( verbPhraseGerundCharacter, verbPhraseGerundPlace, verbPhraseGerundObject ),
        nameConcept,
    ], 1,
    [
        verbPhraseGerundCharacter,
        nameConcept,
        prepositionalPhraseSingularCommon,
        namePlaceProper,
    ], 1,
    [
        'The',
        WeightedTuple( [
            nameConcept,            2,
            nameGroupDescription,   1,
        ] ),
        nameEventPlural,
    ], 2,
    [
        'The',
        adjectivePlace,
        WeightedTuple( [
            nameEventSingular,  2,
            nameEventPlural,    1,
        ] )
    ], 2,
    [
        ( 'A', 'The' ),
        nameEventStorySingular,
        'of',
        namePlaceProper,
    ], 1,
    [
        ( 'A', 'The' ),
        nameEventStorySingular,
        'of',
        nameHeroSingularProper,
    ], 1,
    [
        WeightedTuple( [
            nameEventStorySingular,                     4,
            nameEventStoryPlural,                       2,
            [ adjectiveNumber, nameEventStoryPlural ],  1,
        ] ),
        'of',
        nameConcept,
    ], 1,
    [
        'The',
        WeightedTuple( [ nameEventStorySingular, 2, nameEventStoryPlural, 1 ] ),
        'of The',
        adjectivePlace,
        WeightedTuple( [ nameEventSingular, 2, nameEventPlural, 1 ] ),
    ], 1,
    [
        'The',
        ( nameEventStorySingular , nameEventStoryPlural ),
        'of',
        nameConcept,
    ], 1,
    [
        'A',
        adjectiveGeographic,
        ( nameEventStorySingular, nameEventStoryPlural ),
    ], 3,
    [
        nameHeroSingularProperSimplePossessive,
        WeightedTuple( [
            nameObjectSingularCommon,                       3,
            nameObjectPluralCommon,                         2,
            [ adjectiveObject, nameObjectSingularCommon ],  1,
            [ adjectiveObject, nameObjectPluralCommon ],    1,
        ] ),
    ], 1,
] )


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
    pageTitle = "BMovie 0.4.1, random B-Movie title generator, by Rick Gutleber, 2012"

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

