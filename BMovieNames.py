#!/usr/bin/env python

import random

from BMovieConstants import *

from BMovieAdjectives import adjectiveWordLists
from BMovieAdverbs import adverbWordLists
from BMovieConcepts import conceptWordLists
from BMovieEvents import eventWordLists
from BMovieObjects import objectWordLists
from BMoviePlaces import placeWordLists
from BMoviePossessions import possessionWordLists
from BMovieVerbPhrases import verbPhraseWordLists
from WeightedTuple import WeightedTuple


def makeNameHeroSingularProperSimplePossessive( ):
    return makePossessive( getWord( nameHeroSingularProperSimple ) )

def makeNameHeroPluralProperSimplePossessive( ):
    return makePossessive( getWord( nameHeroPluralProperSimple ) )

def makeNameVillainSingularProperSimplePossessive( ):
    return makePossessive( getWord( nameVillainSingularProperSimple ) )

def makeNameVillainPluralProperSimplePossessive( ):
    return makePossessive( getWord( nameVillainPluralProperSimple ) )


nameWordLists = {

#//**********************************************************************
#//
#//  name modifiers
#//
#//**********************************************************************

    nameModifier : WeightedTuple( [
        "Anti-",        1,
        "Astro-",       2,
        "Crypto-",      1,
        "Cyber-",       1,
        "Electro-",     2,
        "Galacto-",     1,
        "Hypno-",       1,
        "Magneto-",     1,
        "Mecha-",       1,
        "Mechano-",     1,
        "Mega-",        2,
        "Micro-",       1,
        "Monstro-",     1,
        "Nano-",        1,
        "Nega-",        1,
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
        "Ant",
        "Ape",
        "Arachnid",
        "Cat",
        "Cheetah",
        "Cobra",
        "Cockroach",
        "Coyote",
        "Dinosaur",
        "Dog",
        "Dragon",
        "Elephant",
        "Gorilla",
        "Gastropod",
        "Hornet",
        "Horse",
        "Insect",
        "Leopard",
        "Leech",
        "Lion",
        "Lizard",
        "Octopus",
        "Puma",
        "Python",
        "Raptor",
        "Rhino",
        "Serpent",
        "Shark",
        "Snake",
        "Spider",
        "Squid",
        "Tarantula",
        "Tiger",
        "Unicorn",
        "Viper",
        "Wasp",
        "Wolf",
    ) ),

    nameAnimalPlural : WeightedTuple( (
        "Ants",
        "Apes",
        "Arachnids",
        "Cats",
        "Cheetahs",
        "Cobras",
        "Cockroaches",
        "Coyotes",
        "Dinosaurs",
        "Dogs",
        "Dragons",
        "Elephants",
        "Gorillas",
        "Gastropods",
        "Hornets",
        "Horses",
        "Insects",
        "Leopards",
        "Leeches",
        "Lions",
        "Lizards",
        "Octopi",
        "Pumas",
        "Pythons",
        "Raptors",
        "Rhinos",
        "Serpents",
        "Sharks",
        "Snakes",
        "Spiders",
        "Squids",
        "Tarantulas",
        "Tigers",
        "Unicorns",
        "Vipers",
        "Wasps",
        "Wolfs",
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
        "El Santo",
        "Elvis",
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
        "Children",
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

    nameVillainSingularGeneric : WeightedTuple( (
        "Alien",
        "Assassin",
        "Beast",
        "Blob",
        "Brute",
        "Cannibal",
        "Commando",
        "Communist",
        "Cultist",
        "Cyborg",
        "Demon",
        "Devil",
        "Djinn",
        "Dwarf",
        "Elf",
        "Force",
        "Gangster",
        "Ghost",
        "Ghoul",
        "Goblin",
        "Invader",
        "Killer",
        "King",
        "Knight",
        "Kraken",
        "Mechanoid",
        "Mummy",
        "Nazi",
        "Ninja",
        "Orc",
        "Parasite",
        "Pirate",
        "Poltergeist",
        "Prince",
        "Princess",
        "Queen",
        "Rebel",
        "Revenant",
        "Robot",
        "Servant",
        "Slave",
        "Spook",
        "Spy",
        "Stranger",
        "Swamp Creature",
        "Thief",
        "Thrall",
        "Traitor",
        "Troll",
        "Vampire",
        "Viking",
        "Villain",
        "Warrior",
        "Werewolf",
        "Wizard",
        "Zombie",
    ) ),

    nameVillainSingularCommon : WeightedTuple( [
        nameVillainSingularGeneric,         8,
        nameAnimalSingular,                 4,
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
        "Emperor",          2,
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

    # some of these overlap with nameConceptNegative, but that's because they're really appropriate

    nameVillainGeneric : WeightedTuple( [
        "Colossus",             1,
        "Cyclops",              1,
        "Darkness",             1,
        "Sauron",               1,
        "Morgoth",              1,
        "Death",                1,
        "Doom",                 1,
        "Evil",                 1,
        "Ming",                 1,
        "Nero",                 1,
        "Pain",                 1,
        "Q",                    1,
        "X",                    1,
        "Z",                    1,
        "Zero",                 1,
        nameConceptNegative,    5,
    ] ),

    nameVillainSingularProperSimple : WeightedTuple( [
        "Colossus",                     1,
        "Dr. X",                        1,
        "Dr. Z",                        1,
        "Dracula",                      1,
        "Frankenstein",                 1,
        "Fu Manchu",                    1,
        "Harcourt Fenton Mudd",         1,
        "Hitler",                       1,
        "Jared Syn",                    1,
        "Lizzie Borden",                1,
        "Nosferatu",                    1,
        "The Cyclops",                  1,
        "The Minotaur",                 1,
        "The Sheriff of Nottingham",    1,
    ] ),

    nameVillainPluralCommon : WeightedTuple( [
        "Aliens",                               1,
        "Assassins",                            1,
        "Beasts",                               1,
        "Blobs",                                1,
        "Brutes",                               1,
        "Cannibals",                            1,
        "Commandos",                            1,
        "Commies",                              1,
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
        "Reds",                                 1,
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
        [ nameTechnologySingular, nameHeroPluralGeographicCommon ], 1,
        [ nameTechnologySingular, nameHeroPluralCommon ],           1,
    ] ),

    nameVillainPluralGeographicCommon : WeightedTuple( (
        "Barbarians",
        "Huns",
        "Jovians",
        "Lunarians",
        "Martians",
        "Mecurians",
        "Mongols",
        "Nazis",
        "Neptunians",
        "Plutonians",
        "Saturnians",
        "Titanians",
        "Uranians",
        "Venusians",
        "Zulus",
    ) ),

    nameVillainPluralProperSimple : WeightedTuple( (
        "The Red Menace",
        "Plural Villain 1",
        "Plural Villain 2",
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
        nameVillainSingularProperSimple,        10,
        [
            'The',
            nameGroupTypeAppend,
            'of',
            nameConceptNegative,
        ],                                      1,
        [
            nameConceptNegative,
            nameGroupTypePrepend
        ],                                      1,
        [
            nameTitleVillain,
            nameVillainGeneric,
        ],                                      6,
        [
            nameTitleVillain,
            nameVillainSingularGeneric,
        ],                                      3,
        [
            nameVillainSingularLeader,
            nameVillainGeneric,
        ],                                      3,
        [
            'The',
            nameVillainSingularLeader,
            'of',
            nameVillainPluralCommon,
        ],                                      2,
        [
            'The',
            nameVillainSingularLeader,
            'of',
            nameVillainPluralCommon,
        ],                                      2,
        [
            'The',
            nameVillainSingularLeader,
            'of',
            nameVillainPluralGeographicCommon,
        ],                                      2,
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

    nameGroupTypePrepend : WeightedTuple( (
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
     ) ),

    nameGroupTypeAppend : WeightedTuple( (
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
     ) ),

    nameGroupDescription : WeightedTuple( (
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
    ) ),

    nameGroupPrepend : WeightedTuple( [
        "11th",     1,
        "13th",     1,
        "17th",     1,
        "19th",     1,
        "23rd",     1,
        "29th",     1,
        "31st",     1,
        "37th",     1,
        "41st",     1,
        "43rd",     1,
        "47th",     1,
        "49th",     1,
        "50th",     1,
        "53rd",     1,
        "59th",     1,
        "61st",     1,
        "67th",     1,
        "6th",      1,
        "71st",     1,
        "73rd",     1,
        "79th",     1,
        "7th",      1,
        "83rd",     1,
        "8th",      1,
        "99th",     1,
        "9th",      1,
        "A",        1,
        "B",        1,
        "C",        1,
        "Danger",   2,
        "Eagle",    2,
        "F",        1,
        "Fifth",    1,
        "First",    3,
        "Fourth",   1,
        "Giga",     1,
        "J",        1,
        "K",        1,
        "Mega",     1,
        "Q",        1,
        "Second",   2,
        "Space",    3,
        "Super",    1,
        "Third",    2,
        "Tiger",    2,
        "Ultra",    1,
        "V",        1,
        "W",        1,
        "X",        1,
        "Z",        1,
    ] ),

    nameGroupAppend : WeightedTuple( [
        "One",      2,
        "Two",      2,
        "Three",    2,
        "Four",     2,
        "Five",     2,
        "Six",      2,
        "Seven",    2,
        "Eight",    2,
        "Nine",     2,
        "Ten",      2,
        "13",       1,
        "17",       1,
        "19",       1,
        "23",       1,
        "29",       1,
        "31",       1,
        "37",       1,
        "41",       1,
        "43",       1,
        "47",       1,
        "49",       1,
        "50",       1,
        "53",       1,
        "59",       1,
        "61",       1,
        "67",       1,
        "71",       1,
        "73",       1,
        "79",       1,
        "83",       1,
        "99",       1,
        "100",      1,
    ] ),

    nameConcept : WeightedTuple( (
        nameConceptPositive,
        nameConceptNeutral,
        nameConceptNegative,
    ) ),
}



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



