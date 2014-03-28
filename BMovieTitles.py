#!/usr/bin/env python

import random

from BMovieAdjectives import adjectiveWordLists
from BMovieAdverbs import adverbWordLists
from BMovieConcepts import conceptWordLists
from BMovieConstants import *
from BMovieEvents import eventWordLists
from BMovieNames import nameWordLists
from BMovieObjects import objectWordLists
from BMoviePlaces import placeWordLists
from BMoviePossessions import possessionWordLists
from BMovieVerbPhrases import verbPhraseWordLists
from WeightedTuple import WeightedTuple


#//**********************************************************************
#//
#//  wordLists
#//
#//**********************************************************************

wordLists = { }

wordLists.update( adjectiveWordLists )
wordLists.update( adverbWordLists )
wordLists.update( verbPhraseWordLists )
wordLists.update( placeWordLists )
wordLists.update( nameWordLists )
wordLists.update( conceptWordLists )
wordLists.update( eventWordLists )
wordLists.update( objectWordLists )
wordLists.update( possessionWordLists )


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
    return makePossessive( getWord( nameHeroSingularProperSimple ) )

def makeNameHeroPluralProperSimplePossessive( ):
    return makePossessive( getWord( nameHeroPluralProperSimple ) )

def makeNameVillainSingularProperSimplePossessive( ):
    return makePossessive( getWord( nameVillainSingularProperSimple ) )

def makeNameVillainPluralProperSimplePossessive( ):
    return makePossessive( getWord( nameVillainPluralProperSimple ) )





#//**********************************************************************
#//
#//  getTitle
#//
#//**********************************************************************

def getTitle( ):
    result = getWord( titleTypes.choice( ) )

    for i in range( 0, len( replaceList ) - 1, 2 ):
        result = result.replace( replaceList[ i ], replaceList[ i + 1 ] )

    return result


#//**********************************************************************
#//
#//  titles
#//
#//**********************************************************************

titleTypes = WeightedTuple( [
    [
        'Assignment:',
        WeightedTuple( [
            namePlaceProper,        6,
            nameConceptPositive,    1,
            nameConceptNeutral,     1,
        ] ),
    ], 1,
    [
        'Destination',
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
        (
            nameHeroSingularProper,
            nameHeroPluralProper,
            nameVillainSingularProper,
            nameVillainPluralProper,
        ),
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
        WeightedTuple( [
            nameVillainSingularProper, 4,
            nameVillainPluralProper, 1,
            namePlaceProper, 1
        ] ),
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
            [
                'The',
                WeightedTuple( [
                    adjectiveObject,    2,
                    adjectiveObject,    1,
                    adjectiveNumber,    1,
                ] ),
                nameEventPlural
            ],
            [ 'The', adjectiveObject, nameEventSingular ],
            [
                'The',
                WeightedTuple( [
                    adjectiveObject,    2,
                    adjectiveVillain,   1,
                    adjectiveNumber,    1,
                ] ),
                namePossessionVillainPlural
            ],
        ) ),
        'of',
        WeightedTuple( [
            nameVillainSingularProper,              2,
            nameVillainPluralProper,                1,
            [ 'The', nameVillainSingularCommon ],   1,
            [ 'The', nameVillainPluralCommon ],     1,
        ] ),
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
        WeightedTuple( [
            nameVillainSingularProper,  3,
            nameVillainPluralProper,    1,
        ] ),
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
        (
            nameHeroSingularProper,
            nameHeroPluralProper,
            nameVillainSingularProper,
            nameVillainPluralProper
        ),
    ], 1,
    [
        verbPhraseGerundCharacter,
        nameConcept,
    ], 1,
    [
        'Have',
        WeightedTuple( [
            nameObjectSingularCommon,   1,
            nameWeaponSingular,         2,
            nameVehicleSingular,        2,
        ] ),
        ', Will Travel',
    ], 1,
    [
        verbPhraseGerundPlace,
        ( nameConceptPositive, nameConceptNeutral ),
        'With',
        WeightedTuple( [
            nameHeroSingularProper, 2,
            nameHeroPluralProper,   1,
        ] ),
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
        WeightedTuple( [
            nameHeroSingularProper, 3,
            nameHeroPluralProper,   1,
        ] ),
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
        (
            [ 'The', nameEventSingular ],
            [ 'The', nameEventPlural ],
            [ 'The', adjectivePlace, nameEventSingular ],
            [ 'The', adjectivePlace, nameEventPlural ]
        ),
        'of',
        namePlaceProper,
    ], 3,
    [
        nameHeroSingularProper,
        prepositionalPhraseSingularCommon,
        'The',
        WeightedTuple(
            [ adjectivePlace,                       3,
            [ adverbAdjective, adjectivePlace ],    1,
        ] ),
        namePlaceCommon,
    ], 1,
    [
        nameHeroSingularCommon,
        ( 'With A', 'Without A' ),
        WeightedTuple( [
            nameObjectSingularCommon,       3,
            [
                adjectiveObject,
                nameObjectSingularCommon,
            ],                              1,
        ] ),
    ], 1,
    [
        nameHeroPluralCommon,
        ( 'With', 'Without' ),
        WeightedTuple( [
            nameObjectPluralCommon,                         3,
            [ adjectiveObject, nameObjectPluralCommon ],    1,
            nameConceptPositive,                            1,
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
    [
        nameVillainSingularProper,
    ], 8,

] )


