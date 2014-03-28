#!/usr/bin/env python

from BMovieConstants import *
from WeightedTuple import WeightedTuple


#//**********************************************************************
#//
#//  possessions - probably needs to be folded into other categories
#//
#//**********************************************************************

possessionWordLists = {
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
        "Against",              1,
        "Amidst",               1,
        "Among",                1,
        "Around",               1,
        "At",                   1,
        "Beneath",              1,
        "Beyond",               1,
        "In Search of",         1,
        "Inside",               1,
        "Near",                 1,
        "Outside",              1,
        "Underneath",           1,
    ) ),

    prepositionalPhrasePluralProper : WeightedTuple( (
        "Against",              1,
        "Alone In",             1,
        "Amidst",               1,
        "Among",                1,
        "Around",               1,
        "At",                   1,
        "Beneath",              1,
        "Beyond",               1,
        "In Search of",         1,
        "Inside",               1,
        "Near",                 1,
        "Outside",              1,
        "Underneath",           1,
    ) ),
}

