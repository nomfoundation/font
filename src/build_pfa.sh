#!/usr/bin/env sh

# run this script to build the font.pfa from a UFO, since FontLab doesn't allow export of .pfa

# Get the absolute path to the bash script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

date=$(date '+%Y-%m-%d')

# Remove old versions
for file in font.pfa
do
    if [[ -f $file ]]
    then
    filename=$(basename -- "$file")
	extension="${filename##*.}"
	filename="${filename%.*}"
	newName="$filename$date.$extension"
	echo $newName
	mv $file $newName
	echo "Renamed file"
    fi
done

# build the pfa from ufo
tx -t1 ./NomNaTong/Source-UFO/font.ufo font.pfa

# need this for any updates to the number of glyphs
python3 tx-glyph-list.py font.pfa > temp ; paste temp temp > GlyphOrderAndAliasDB ; rm temp


# EOF
