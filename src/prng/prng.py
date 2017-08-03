#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# prng.py
# -------
# A simple lfsr based prng used to generate random looking
# strings of text. This code is for modelling.
#
#
# Author: Joachim Strömbergson
# Copyright (c) 2017
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

import sys
import os


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_prng1_state(state):
    state[0] += 1 & 0xff
    state[1] = state[1] ^ state[0] ^ state[3]
    state[2] = (state[2] + state[1]) & 0xff
    state[3] = (state[3] + (state[2] >> 1) ^ state[1]) & 0xff
    return state


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_prng1_state():
    state = [1, 1, 1, 1]
    for i in range(1000000):
        state = update_prng1_state(state)
#        print(state[3], state[3] & 0x1f)
        print("%s" % chr(state[3]), end="")
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_prng2_state(state):
    state << 1
    if (state > 255):
        state = (state ^ 0x88) & 0xff
    return state 


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_prng2_state():
    state = 1
    for i in range(100):
        state = update_prng2_state(state)
        print(state)
#        print("%s" % chr(state[3]), end="")
    print("")



#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
#    test_prng1_state()
    test_prng2_state()

#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF string2hash.py
#=======================================================================
