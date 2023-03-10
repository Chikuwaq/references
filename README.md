## Benefits
- Make the bib file portable. You can clone this repository when writing a conference abstract.
- different styles in accordance with journal specifications

## Passive usage
If you just want to use the bib file,
1. Clone this repository next to your .tex file
2. Specify in the .tex file:
```latex
\bibliographystyle{unsrt}           % sort the references as they appear in the text
\bibliography{./references/Refs}
```

## Python formatter
You can format the bib file with the `format.py` script as you add references. 
It depends on `bibtexparser` module. We recommend to use it in a virtual Python environment:
```sh
python -m venv .venv
```
and activate the virtual environment by sourcing the script `<venv>/bin/activate`.
Then run the format script:
```sh
python format.py Refs.bib <new filename>
```
This tool features:
1. consistently sorts the keys 'title', 'author', 'journal', ... for all entries
2. sort the entries in alphabetical order
3. align indentation
4. recognize accented letters and convert to the LaTeX-conform syntax