# Nom Na Tong Font

This is the repository for the "Nom Na Tong" font. The Nom Na Tong font was originally developed under the aegis of the Vietnamese Nôm Preservation Foundation <http://www.nomfoundation.org>, established in 1999. The font was developed both as a definitive source for proposals to encode the Vietnamese Hán-Nôm script in Unicode and to promote access to the heritage of works written in that script. The font currently contains over 26,000 glyphs, and represents the collective work of scholars, software engineers, and other experts. It continues to be the reference font for the on-going work of encoding Hán-Nôm in Unicode. The foundation dissolved at the end of 2018. Now the font is being provided as an open source project in the hope that a community of those interested in the preservation of the Hán-Nôm script will continue to maintain and extend it.

## Building the fonts from source

### Requirements

To build the binary font files from source, you need to have installed the [Adobe Font Development Kit for OpenType](https://github.com/adobe-type- tools/afdko/) (AFDKO) tools.

### Building the fonts

In this repository, all necessary files are in place for building 3 versions of the "Nom Na Tong" font in OpenType/CFF and TrueType format: * NomNaTong-Regular.ttf * NomNaTong-Regular.otf * NomNaTongLight.ttf


The 2 versions of TrueType font differ only in name, in particular Postscript name, with NomNaTongLight.ttf being supplied for backwards compatibility. Going forward, we encourage the use of NomNaTong-Regular, which follows the more conventional font naming scheme.

The latest pre-built binary versions of the font, can be easily downloaded from the [Latest Release](https://github.com/nomfoundation/font/releases/latest/).

The primary build script is *build.sh* This requires the 'pfa' font, *font.pfa*, which is part of the project. Simply execute *build.sh* to build the 3 versions of "Nom Na Tong".

Since many font editors do not support output of 'pfa' fonts, there is a separate build script, *build_pfa.sh*, which will generate a 'pfa' from a UFO package. Font Lab and other editors support export of UFO Packages. Run this script first if you modify the font and want to build from the UFO package.

# Thanks Special thanks to Ken Lunde for his help in setting up the ADFKO build and other guidance. 