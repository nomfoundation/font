#!/usr/bin/env sh

# Get the absolute path to the bash script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

# Remove old versions
for file in NomNaTong-Regular.otf NomNaTong-Regular.ttf NomNaTongLight.ttf
do
    if [[ -f $file ]]
    then
	rm $file
	echo "Removed $file"
    fi
done

# Hint the source Type 1 font
psautohint -a font.pfa

# Build the name-keyed OpenType/CFF font (OTF)
makeotf -r -f font.pfa -omitMacNames -ff features.txt -mf FontMenuNameDB -ga -ci UnicodeVariationSequences.txt

# Convert the OTF to TTF
otf2ttf NomNaTong-Regular.otf
sfntedit -d DSIG NomNaTong-Regular.ttf

# build NomNaTongLight.ttf for backwards compatibillity with some Microsoft apps
cp NomNaTong-Regular.ttf NomNaTongLight.ttf
ttx  -f -m  NomNaTongLight.ttf NomNaTongLight_name.ttx

# EOF
