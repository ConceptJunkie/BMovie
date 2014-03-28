#!/usr/bin/env python

from itertools import chain

from BMovieConstants import *
from WeightedTuple import WeightedTuple


verbPhraseWordLists = {

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

    verbPhrasePresentSingularObject : WeightedTuple( [
        verbPhrasePresentSingularFinding,   1
    ] ),

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

    verbPhrasePastObject : WeightedTuple( [
        verbPhrasePastFinding,  1,
    ] ),

    verbPhraseFutureCharacter : WeightedTuple( [
        [ "Will", verbPhrasePresentSingularCharacter ], 1 ,
    ] ),

    verbPhraseFutureObject : WeightedTuple( [
        [ "Will", verbPhrasePresentSingularObject ],    1,
    ] ),

    verbPhraseFuturePlace : WeightedTuple( [
        [ "Will", verbPhrasePresentSingularPlace ],     1,
    ] ),

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
}

