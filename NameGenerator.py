#!/usr/bin/env python

# Step 1.   Generate phonetic name
# Step 2.   Figure out how to spell it.


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
    "LCH",      2,
    "LD",       3,
    "LG",       1,
    "LJ",       1,
    "LK",       2,
    "LM",       2,
    "LN",       2,
    "LP",       2,
    "LS",       2,
    "LSH",      2,
    "LST",      2,
    "LT",       3,
    "LTH",      2,
    "NCH",      2,
    "ND",       3,
    "NG",       3,
    "NJ",       2,
    "NK",       2,
    "NS",       2,
    "NSH",      1,
    "NST",      2,
    "NT",       5,
    "NTH",      2,
    "RCH",      2,
    "RD",       1,
    "RG",       2,
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
    "RN",       2,
    "RP",       2,
    "RS",       2,
    "RSH",      1,
    "RST",      2,
    "RT",       2,
    "RTH",      2,
    "SHK",      1,
    "SHT",      1,
    "SK",       2,
    "ST",       5,
] )


