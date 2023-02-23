#!.venv/Scripts/python

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding


def parse(bibfile):
   """
   Parse a BibTeX file and create bibtexparser database object.
   """
   # convert accents to LaTeX syntax to avoid encode error in bibtexparser
   import subprocess
   import sys
   subprocess.Popen(['pwsh', 'preprocess.ps1', bibfile], stdout=sys.stdout)

   # parse
   with open(bibfile, 'r') as file:
      database = bibtexparser.load(file)  # simple parse
      # homogenize_latex_encoding is terrible, breaks the original content
      # parser = BibTexParser()
      # parser.customization = homogenize_latex_encoding
      # database = bibtexparser.load(file, parser=parser)
   return database


def cleanup(database, outfile):
   """
   Clean up the bibtexparser database and export file.
   """
   for i, entry in enumerate(database.entries):
      entry = clean_authors(entry)
      entry = clean_journal_abbreviations(entry)
      # entry = clean_title(entry)
      # entry = clean_publisher(entry)
      # entry = clean_type(entry)
      # entry = clean_school(entry)
      entry = delete_month(entry)
      database.entries[i] = entry

   with open(outfile, 'w') as file:
      bibtexparser.dump(database, file)




##### clean up methods #########################################
def clean_authors(entry):
   """ Check if authors are present in the entry """
   if 'author' not in entry.keys():
      print(entry)
      raise KeyError(f"The entry {entry['ID']} does not contain 'author'!")
   return entry

def clean_journal_abbreviations(entry):
   if entry['ENTRYTYPE'] in ['phdthesis', 'book', 'inbook']: 
      return entry
   if ('journal' not in entry.keys()) and ('Journal' not in entry.keys()):
      print(entry)
      raise KeyError(f"The entry {entry['ID']} does not contain 'journal'!")

   clean_entry = entry
   clean_entry['journal'] = entry['journal'].replace("physics", "Phys.")
   clean_entry['journal'] = entry['journal'].replace("Physics", "Phys.")
   clean_entry['journal'] = entry['journal'].replace("physical", "Phys.")
   clean_entry['journal'] = entry['journal'].replace("Physical", "Phys.")
   clean_entry['journal'] = entry['journal'].replace("journal of", "J.")
   clean_entry['journal'] = entry['journal'].replace("Journal of", "J.")
   clean_entry['journal'] = entry['journal'].replace("computation ", "Comput. ")
   clean_entry['journal'] = entry['journal'].replace("computer ", "Comput. ")
   clean_entry['journal'] = entry['journal'].replace("Computation ", "Comput. ")
   clean_entry['journal'] = entry['journal'].replace("Computer ", "Comput. ")
   clean_entry['journal'] = entry['journal'].replace("technology", "Tech.")
   clean_entry['journal'] = entry['journal'].replace("Technology", "Tech.")
   clean_entry['journal'] = entry['journal'].replace("nature", "Nat.")
   clean_entry['journal'] = entry['journal'].replace("Nature", "Nat.")
   clean_entry['journal'] = entry['journal'].replace("communication", "Comm.")
   clean_entry['journal'] = entry['journal'].replace("Communication", "Comm.")
   clean_entry['journal'] = entry['journal'].replace("review", "Rev.")
   clean_entry['journal'] = entry['journal'].replace("Review", "Rev.")
   clean_entry['journal'] = entry['journal'].replace("reviews", "Rev.")
   clean_entry['journal'] = entry['journal'].replace("Reviews", "Rev.")
   clean_entry['journal'] = entry['journal'].replace("applied", "Appl.")
   clean_entry['journal'] = entry['journal'].replace("Applied", "Appl.")
   clean_entry['journal'] = entry['journal'].replace("Letters", "Lett.")
   return clean_entry

# def clean_title(entry):
#    if 'title' not in entry.keys():
#       raise KeyError(f"The entry {entry['ID']} does not contain 'title'!")
#    clean_entry = entry

#    # things that is wrongly modified by `homogenize_latex_encoding`
#    clean_entry['title'] = entry['title'].replace("{I}II", "{III}")
#    clean_entry['title'] = entry['title'].replace("{I}I", "{II}")
#    clean_entry['title'] = entry['title'].replace("{S}b-", "{Sb}-")
#    clean_entry['title'] = entry['title'].replace("{I}nAs", "{InAs}")
#    clean_entry['title'] = entry['title'].replace("{G}aSb", "{GaSb}")
#    clean_entry['title'] = entry['title'].replace("{A}lSb", "{AlSb}")
#    clean_entry['title'] = entry['title'].replace("{S}iGe", "{SiGe}")
#    clean_entry['title'] = entry['title'].replace("{G}aN", "{GaN}")
#    clean_entry['title'] = entry['title'].replace("{A}lN", "{AlN}")
#    clean_entry['title'] = entry['title'].replace(r"k\textbackslash ensuremath\cdot p", r"k\ensuremath{\cdot}p")
#    clean_entry['title'] = entry['title'].replace(r"\textdollar ", r"$")
#    clean_entry['title'] = entry['title'].replace(r"\textbackslash mathcal{F}_-3/2", r"\mathcal{F}_{-3/2}")
#    clean_entry['title'] = entry['title'].replace(r"\textdollar ", r"$")
#    clean_entry['title'] = entry['title'].replace(r"\_", "_")
#    clean_entry['title'] = entry['title'].replace("{\{A}A}", "{\AA}")
#    return clean_entry

# def clean_publisher(entry):
#    if 'publisher' not in entry.keys():
#       return entry
#    clean_entry = entry
#    # curly bracket is ripped off by `homogenize_latex_encoding`
#    clean_entry['publisher'] = entry['publisher'].replace("IOP ", "{IOP} ")
#    return clean_entry
   
# def clean_type(entry):
#    if 'type' not in entry.keys():
#       return entry
#    clean_entry = entry
#    # curly bracket is ripped off by `homogenize_latex_encoding`
#    clean_entry['type'] = entry['type'].replace("Ph.D. ", "{Ph.D.} ")
#    return clean_entry

# def clean_school(entry):
#    if 'school' not in entry.keys():
#       return entry
#    clean_entry = entry
#    # messed up by `homogenize_latex_encoding`
#    clean_entry['school'] = entry['school'].replace(r"M\textbackslash n\"chen", r"M{\"u}nchen")
#    return clean_entry

def delete_month(entry):
   """ month is an useful info for personal reference, but contaminates the bibtex output (Christian did not like it) """
   if 'month' in entry.keys(): entry.pop('month')
   return entry
   