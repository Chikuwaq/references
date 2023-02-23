# NOTE: This script has to be run twice if bibtexparser complains about encoding.

import bibtexformatter

old_file = 'Refs_raw.bib'
new_file = 'Refs.bib'

db = bibtexformatter.parse(old_file)
bibtexformatter.cleanup(db, new_file)
