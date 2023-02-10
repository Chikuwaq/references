# NOTE: This script has to be run twice so that bibtexparser does not complain encoding

import bibtexformatter
import sys

old_file = sys.argv[1]
new_file = sys.argv[2]

db = bibtexformatter.parse(old_file)
bibtexformatter.cleanup(db, new_file)
