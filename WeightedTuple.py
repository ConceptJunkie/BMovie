#!/usr/bin/env python

from BMovieConstants import *

import random


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
            self.weighted = True
            self.values = [ ]

            for i in range( 0, len( values ) - 1, 2 ):
                self.values.extend( [ values[ i ] ] * values[ i + 1 ] )

            try:
                uniqueItems = len( set( values ) )
            except:
                uniqueItems = len( values )

            if uniqueItems > 4:
                self.maxHistory = uniqueItems // 4 + 1
            elif uniqueItems == 4:
                self.maxHistory = 1
            else:
                self.maxHistory = 0
        elif type( values ) is tuple:
            self.weighted = False
            self.values = list( values )

            try:
                uniqueItems = len( set( values ) )
            except:
                uniqueItems = len( values )

            if uniqueItems > 4:
                self.maxHistory = uniqueItems // 4 + 1
            elif uniqueItems == 4:
                self.maxHistory = 1
            else:
                self.maxHistory = 0

        self.mru = list( )

    def choice( self ):
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

    def __repr__( self ):
        return self.repr( self )

    def repr( self, target ):
        #print( 'type: ', end='' )
        #print( type( target ) )
        if type( target ) is WeightedTuple:
            result = 'WeightedTuple('

            if target.weighted:
                result += self.weighted_repr( target.values )
            else:
                result += self.repr( target.values )

            result += ')'
        elif type( target ) is str:
            result = "'" + target + "'"
        elif type( target ) is int:
            result = wordTypeDescriptions[ target ]
        elif isinstance( target, tuple ):
            result = '('

            for i in target:
                result += self.repr( i ) + ','

            result += ')'
        elif isinstance( target, list ):
            result = '['

            for i in target:
                result += self.repr( i ) + ','

            result += ']'
        else:
            result = repr( target )

        return result

    def weighted_repr( self, target ):
        repeat = 1
        oldValue = ''
        result = '['

        #print( 'type: ', end='' )
        #print( type( target ) )

        for i in target:
            #print( 'list element type: ', end='' )
            #print( type( i ) )
            #print( i )

            if i == oldValue:
                repeat += 1
            else:
                result += self.repr( i ) + ',\n' + str( repeat ) + ','
                repeat = 1
                oldValue = i

        result += self.repr( i ) + ',' + str( repeat ) + ']'

        #print( 'result: ', end='' )
        #print( result )

        return result


