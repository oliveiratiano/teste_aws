#!/bin/bash
set -e

cd glove

# Makes programs, downloads sample data, trains a GloVe model, and then evaluates it.
# One optional argument can specify the language used for eval script: matlab, octave or [default] python


CORPUS=$1
VOCAB_FILE=$2

echo $CORPUS e $VOCAB_FILE e TESTOUOUUUU
