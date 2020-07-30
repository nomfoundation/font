#!/usr/bin/env sh

# Get the absolute path to the bash script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

# Build the name-keyed OpenType/CFF font (OTF)
makeotf -f font.pfa -omitMacNames -ff features -mf FontMenuNameDB -r

# Convert the OTF to TTF
otf2ttf NomNaTong-Regular.otf
sfntedit -d DSIG NomNaTong-Regular.ttf

# EOF
