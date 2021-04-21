#! /usr/bin/env python

# Written by Dr Ken Lunde (lunde@unicode.org)
# Version 2020-07-10
#
# This tool reports to STDOUT a list of the glyphs in the specified font.
# Unlike glyph-list.py, which uses FontTools in lieu of "tx" (AFDKO), the
# specified font can be a CIDFont resource (instantiated as a file), CFF
# resource or table (instantiated as a file), or an OpenType/CFF font. By
# default, glyphs are listed as CIDs or glyph names, depending on whether
# the font is CID- or name-keyed. CIDs are prefixed with a "/" followed by
# zero-padded five-digit decimal values. The number of glyphs is reported
# to STDERR, along with the detected ROS (Registry, Ordering, and
# Supplement) for CID-keyed fonts.
#
# The "-g" command-line option will list GIDs in lieu of CIDs or glyph
# names.
#
# The "-r" command-line option will turn the list of CIDs or GIDs into
# ranges.
#
# The "-s" command-line option will additionally output lists or ranges as
# a single line with comma separators so that it can be repurposed in
# command lines.
#
# Tool Dependencies: tx (AFDKO)

__help__ = """Usage: tx-glyph-list.py [-g] [-r] [-s] <font>"""

import os, re, sys

def parseArgs(args):
    argn = len(args)
    if argn == 0:
        print("Please specify a font!", file=sys.stderr)
        exit()
    g, i, r= [0] * 3
    s = "\n"
    prefix = "/"
    font = ""
    while i < argn:
        arg = args[i]
        i += 1
        if arg[0] != "-":
            font = f"\"{arg}\""
        elif arg == "-h":
            print(__help__, file=sys.stderr)
            exit()
        elif arg == "-g":
            g = 1
            prefix = ""
        elif arg == "-r":
            r = 1
        elif arg == "-s":
            s = ","
        else:
            print("Unknown option!", file=sys.stderr)
            exit()
    return font, g, prefix, r, s

def main():
    count, second = [0] * 2
    isCIDFont = 1
    r, o, s, data = [""] * 4

    # Parse command-line arguments
    myFont, useGID, prefix, myRange, mySep = parseArgs(sys.argv[1:])

    # Compile the regular expressions that will be used
    rRegex = re.compile(r"^cid\.Registry\s+\"(.+)\"")
    oRegex = re.compile(r"^cid\.Ordering\s+\"(.+)\"")
    sRegex = re.compile(r"^cid\.Supplement\s+(\d+)")
    fontRegex = re.compile(r"^sup\.srcFontType\s+(?:TrueType|CFF \(name-keyed\)|Type 1 \(name-keyed\))$")
    gidRegex = re.compile(r"glyph\[(\d+)\]")
    cidRegex = re.compile(r"{(.+?),")

    # Parse STDIN
    for line in map(str.rstrip, os.popen("tx -1 " + myFont)):
        # Detect whether the font is TrueType or name-keyed
        if rRegex.search(line):
            r = rRegex.search(line).group(1)
        elif oRegex.search(line):
            o = oRegex.search(line).group(1)
        elif sRegex.search(line):
            s = int(sRegex.search(line).group(1))
        elif fontRegex.search(line):
            isCIDFont = 0
            prefix = ""
            if not useGID:
                myRange = 0
            continue
        if gidRegex.search(line):
            count += 1
            if useGID:
                glyph = int(gidRegex.search(line).group(1))
            elif isCIDFont:
                glyph = int(cidRegex.search(line).group(1))
            else:
                glyph = cidRegex.search(line).group(1)
            if myRange:
                if not second:
                    orig, previous = [glyph, glyph]
                    second = 1
                    continue
                if glyph != previous + 1:
                    if orig == previous:
                        data += f"{prefix}{orig}{mySep}"
                    else:
                        data += f"{prefix}{orig}-{prefix}{previous}{mySep}"
                    orig, previous = [glyph, glyph]
                else:
                    previous = glyph
            else:
                if not mySep:
                    data += f"{prefix}{glyph}\n"
                else:
                    if not data:
                        data += f"{prefix}{glyph}"
                    else:
                        data += f"{mySep}{prefix}{glyph}"
        else:
            continue

    if myRange:
        if orig == previous:
            data += f"{prefix}{orig}\n"
        else:
            data += f"{prefix}{orig}-{prefix}{previous}\n"
    else:
        data += "\n"

    print(data, end="")

    # Reporting to STDERR
    if isCIDFont:
        print("Glyphs: %d | ROS: %s-%s-%d" %(count, r ,o, s), file=sys.stderr)
    else:
        print("Glyphs: %d" % count, file=sys.stderr)

if __name__ == "__main__":
    main()
