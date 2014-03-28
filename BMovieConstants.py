#!/usr/bin/env python


#//**********************************************************************
#//
#//  constants
#//
#//**********************************************************************

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

nameVillainGeneric                          = 900
nameVillainSingularCommon                   = 901
nameVillainSingularGeneric                  = 902
nameVillainSingularProper                   = 903
nameVillainSingularProperSimple             = 904
nameVillainSingularProperSimplePossessive   = 905
nameVillainSingularLeader                   = 906
nameVillainPluralLeader                     = 907
nameVillainPluralCommon                     = 908
nameVillainPluralGeographicCommon           = 909
nameVillainPluralProper                     = 910
nameVillainPluralProperSimple               = 911
nameVillainPluralProperSimplePossessive     = 912

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
nameEventSingularNeutral                    = 1110
nameEventSingularPositive                   = 1111
nameEventSingularNegative                   = 1112
nameEventStoryPlural                        = 1113
nameEventStorySingular                      = 1114
nameModifier                                = 1115
namePlaceModifier                           = 1116
nameTimePlural                              = 1117
nameTimeSingular                            = 1118
nameVehiclePlural                           = 1119
nameVehicleSingular                         = 1120
nameTechnologySingular                      = 1121
nameTitleHero                               = 1122
nameTitleVillain                            = 1123
nameWeaponPlural                            = 1124
nameWeaponSingular                          = 1125

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


wordTypeDescriptions = {
    adjectiveActionHero                         : 'adjectiveActionHero',
    adjectiveActionVillain                      : 'adjectiveActionVillain',
    adjectiveAge                                : 'adjectiveAge',
    adjectiveBaseHero                           : 'adjectiveBaseHero',
    adjectiveBaseVillain                        : 'adjectiveBaseVillain',
    adjectiveGeographic                         : 'adjectiveGeographic',
    adjectiveHero                               : 'adjectiveHero',
    adjectiveHeroNongeographic                  : 'adjectiveHeroNongeographic',
    adjectiveMentalHero                         : 'adjectiveMentalHero',
    adjectiveMentalVillain                      : 'adjectiveMentalVillain',
    adjectiveNumber                             : 'adjectiveNumber',
    adjectiveObject                             : 'adjectiveObject',
    adjectiveObjectBase                         : 'adjectiveObjectBase',
    adjectivePhysicalHero                       : 'adjectivePhysicalHero',
    adjectivePhysicalVillain                    : 'adjectivePhysicalVillain',
    adjectivePlace                              : 'adjectivePlace',
    adjectivePlaceBase                          : 'adjectivePlaceBase',
    adjectiveTexture                            : 'adjectiveTexture',
    adjectiveTime                               : 'adjectiveTime',
    adjectiveVillain                            : 'adjectiveVillain',
    adjectiveVillainNongeographic               : 'adjectiveVillainNongeographic',
    adjectiveVocationHero                       : 'adjectiveVocationHero',
    adjectiveVocationVillain                    : 'adjectiveVocationVillain',

    adverbVerb                                  : 'adverbVerb',
    adverbAdjective                             : 'adverbAdjective',

    verbPhrasePresentSingularCharacter          : 'verbPhrasePresentSingularCharacter',
    verbPhrasePresentSingularObject             : 'verbPhrasePresentSingularObject',
    verbPhrasePresentSingularPlace              : 'verbPhrasePresentSingularPlace',
    verbPhrasePresentSingularGoing              : 'verbPhrasePresentSingularGoing',
    verbPhrasePresentSingularAttacking          : 'verbPhrasePresentSingularAttacking',
    verbPhrasePresentSingularFinding            : 'verbPhrasePresentSingularFinding',

    verbPhrasePresentPluralCharacter            : 'verbPhrasePresentPluralCharacter',
    verbPhrasePresentPluralObject               : 'verbPhrasePresentPluralObject',
    verbPhrasePresentPluralPlace                : 'verbPhrasePresentPluralPlace',
    verbPhrasePresentPluralGoing                : 'verbPhrasePresentPluralGoing',
    verbPhrasePresentPluralAttacking            : 'verbPhrasePresentPluralAttacking',
    verbPhrasePresentPluralFinding              : 'verbPhrasePresentPluralFinding',

    verbPhrasePastCharacter                     : 'verbPhrasePastCharacter',
    verbPhrasePastObject                        : 'verbPhrasePastObject',
    verbPhrasePastPlace                         : 'verbPhrasePastPlace',
    verbPhrasePastGoing                         : 'verbPhrasePastGoing',
    verbPhrasePastAttacking                     : 'verbPhrasePastAttacking',
    verbPhrasePastFinding                       : 'verbPhrasePastFinding',

    verbPhraseFutureCharacter                   : 'verbPhraseFutureCharacter',
    verbPhraseFutureObject                      : 'verbPhraseFutureObject',
    verbPhraseFuturePlace                       : 'verbPhraseFuturePlace',

    verbPhraseGerundCharacter                   : 'verbPhraseGerundCharacter',
    verbPhraseGerundObject                      : 'verbPhraseGerundObject',
    verbPhraseGerundPlace                       : 'verbPhraseGerundPlace',

    namePlaceCommon                             : 'namePlaceCommon',
    namePlaceProper                             : 'namePlaceProper',
    namePlaceProperSimple                       : 'namePlaceProperSimple',
    namePlaceProperArticle                      : 'namePlaceProperArticle',
    namePlaceArchitectureSingular               : 'namePlaceArchitectureSingular',
    namePlaceArchitecturePlural                 : 'namePlaceArchitecturePlural',
    namePlaceGeographySingular                  : 'namePlaceGeographySingular',
    namePlaceGeographyPlural                    : 'namePlaceGeographyPlural',
    namePlaceTerritorySingular                  : 'namePlaceTerritorySingular',
    namePlaceTerritoryPlural                    : 'namePlaceTerritoryPlural',

    nameHeroSingularCommon                      : 'nameHeroSingularCommon',
    nameHeroSingularProper                      : 'nameHeroSingularProper',
    nameHeroSingularProperSimple                : 'nameHeroSingularProperSimple',
    nameHeroSingularProperSimplePossessive      : 'nameHeroSingularProperSimplePossessive',
    nameHeroSingularLeader                      : 'nameHeroSingularLeader',
    nameHeroPluralLeader                        : 'nameHeroPluralLeader',
    nameHeroPluralCommon                        : 'nameHeroPluralCommon',
    nameHeroPluralGeographicCommon              : 'nameHeroPluralGeographicCommon',
    nameHeroPluralProper                        : 'nameHeroPluralProper',
    nameHeroPluralProperSimple                  : 'nameHeroPluralProperSimple',
    nameHeroPluralProperSimplePossessive        : 'nameHeroPluralProperSimplePossessive',

    nameVillainGeneric                          : 'nameVillainGeneric',
    nameVillainSingularCommon                   : 'nameVillainSingularCommon',
    nameVillainSingularGeneric                  : 'nameVillainSingularGeneric',
    nameVillainSingularProper                   : 'nameVillainSingularProper',
    nameVillainSingularProperSimple             : 'nameVillainSingularProperSimple',
    nameVillainSingularProperSimplePossessive   : 'nameVillainSingularProperSimplePossessive',
    nameVillainSingularLeader                   : 'nameVillainSingularLeader',
    nameVillainPluralLeader                     : 'nameVillainPluralLeader',
    nameVillainPluralCommon                     : 'nameVillainPluralCommon',
    nameVillainPluralGeographicCommon           : 'nameVillainPluralGeographicCommon',
    nameVillainPluralProper                     : 'nameVillainPluralProper',
    nameVillainPluralProperSimple               : 'nameVillainPluralProperSimple',
    nameVillainPluralProperSimplePossessive     : 'nameVillainPluralProperSimplePossessive',

    nameGroupDescription                        : 'nameGroupDescription',
    nameGroupTypePrepend                        : 'nameGroupTypePrepend',
    nameGroupTypeAppend                         : 'nameGroupTypeAppend',
    nameGroupPrepend                            : 'nameGroupPrepend',
    nameGroupAppend                             : 'nameGroupAppend',

    nameAnimalPlural                            : 'nameAnimalPlural',
    nameAnimalSingular                          : 'nameAnimalSingular',
    nameConcept                                 : 'nameConcept',
    nameConceptNegative                         : 'nameConceptNegative',
    nameConceptPositive                         : 'nameConceptPositive',
    nameConceptNeutral                          : 'nameConceptNeutral',
    nameDirection                               : 'nameDirection',
    nameEventEpoch                              : 'nameEventEpoch',
    nameEventPlural                             : 'nameEventPlural',
    nameEventSingular                           : 'nameEventSingular',
    nameEventSingularNeutral                    : 'nameEventSingularNeutral',
    nameEventSingularPositive                   : 'nameEventSingularPositive',
    nameEventSingularNegative                   : 'nameEventSingularNegative',
    nameEventStoryPlural                        : 'nameEventStoryPlural',
    nameEventStorySingular                      : 'nameEventStorySingular',
    nameModifier                                : 'nameModifier',
    namePlaceModifier                           : 'namePlaceModifier',
    nameTimePlural                              : 'nameTimePlural',
    nameTimeSingular                            : 'nameTimeSingular',
    nameTechnologySingular                      : 'nameTechnologySingular',
    nameVehiclePlural                           : 'nameVehiclePlural',
    nameVehicleSingular                         : 'nameVehicleSingular',
    nameTitleHero                               : 'nameTitleHero',
    nameTitleVillain                            : 'nameTitleVillain',
    nameWeaponPlural                            : 'nameWeaponPlural',
    nameWeaponSingular                          : 'nameWeaponSingular',

    nameObjectPluralCommon                      : 'nameObjectPluralCommon',
    nameObjectPluralCommon1                     : 'nameObjectPluralCommon1',
    nameObjectProper                            : 'nameObjectProper',
    nameObjectProperSimple                      : 'nameObjectProperSimple',
    nameObjectSingularCommon                    : 'nameObjectSingularCommon',
    nameObjectSingularCommon1                   : 'nameObjectSingularCommon1',

    namePossessionHeroSingular                  : 'namePossessionHeroSingular',
    namePossessionVillainSingular               : 'namePossessionVillainSingular',
    namePossessionHeroPlural                    : 'namePossessionHeroPlural',
    namePossessionVillainPlural                 : 'namePossessionVillainPlural',

    prepositionalPhraseSingularCommon           : 'prepositionalPhraseSingularCommon',
    prepositionalPhraseSingularProper           : 'prepositionalPhraseSingularProper',
    prepositionalPhrasePluralCommon             : 'prepositionalPhrasePluralCommon',
    prepositionalPhrasePluralProper             : 'prepositionalPhrasePluralProper',
    prepositionalPhraseEvent                    : 'prepositionalPhraseEvent',
}


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


