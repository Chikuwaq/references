## Benefits
- Make the bib file portable. You can clone this repository when writing a conference abstract and thesis/dissertation.
- different styles in accordance with journal specifications

## Passive usage
If you just want to use the bib file (e.g. writing a conference abstract),
1. Clone this repository next to your .tex file, or simply copy the content of 'Refs.bib' to a file
2. Specify in the .tex file:
```latex
\bibliographystyle{unsrt}           % sort the references as they appear in the text
\bibliography{./references/Refs}
```

## Active usage: Python formatter
You can format your own bib file with the `format.py` script. 
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

If the conversion fails with a UnicodeDecodeError, make sure that the Python default encoding is set to UTF-8. The setting can be displayed by the following script:
```python
import os
import sys
import locale
print(os.environ.get("PYTHONIOENCODING"))
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print(sys.stdout.encoding)
print(locale.getpreferredencoding())
```

## Examples where manual adjustment is needed
1. If an auther's first name is abbreviated as `M.L.`, this will not be recognized as a name with two first name initials. Use the regex
```
(?<=\.)\w(?=\.)
```
in VS Code to find such cases and amend it to `M. L.`.

2. 