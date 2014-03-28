#!/usr/bin/env python

import argparse
import string

from BMovieConstants import *
from WeightedTuple import WeightedTuple
from BMovieTitles import getTitle

#//**********************************************************************
#//
#//  constants
#//
#//**********************************************************************

PROGRAM_NAME = "BMovie"
VERSION = "0.4.4"
PROGRAM_DESCRIPTION = "B-Movie title generator"
COPYRIGHT_MESSAGE = "copyright (c) 2013, Rick Gutleber"

DESCRIPTION = PROGRAM_NAME + " " + VERSION + ", " + PROGRAM_DESCRIPTION + ", " + COPYRIGHT_MESSAGE


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    parser = argparse.ArgumentParser( prog=PROGRAM_NAME, description=DESCRIPTION )

    parser.add_argument( '-n', '--count', type=int, action='store', default=1 )
    parser.add_argument( '-s', '--stats', action='store_true' )

    args = parser.parse_args( )

    count = args.count

    for i in range( 0, count ):
        print( getTitle( ) )
        # print( getWord( nameVillainSingularProper ) )

    if args.stats:
        print( titleTypes )


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
    pageTitle = DESCRIPTION

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

