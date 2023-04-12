## Benefits
- Make the bib file portable. You can clone this repository when writing a conference abstract and thesis/dissertation.
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
and activate the virtual environment by sourcing the script `<venv>/Scripts/Activate.ps1`.
If you use pip, install the dependencies as:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Then run the format script:
```sh
python format.py
```
This tool features:
1. Consistently sorts the keys 'title', 'author', 'journal', ... for all entries
2. Sort the entries in alphabetical order
3. Align indentation
4. Recognize accented letters and convert to the LaTeX-conform syntax