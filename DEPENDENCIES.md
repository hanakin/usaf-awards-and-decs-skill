# Dependencies

This skill is intended to be easy to share and install from GitHub.

## Python

- Python `3.10+`
- No third-party Python packages are currently required

Install note:

```bash
python3 --version
python3 -m pip install -r requirements.txt
```

`requirements.txt` is intentionally empty aside from comments because the skill scripts use only the Python standard library.

## System dependencies

The following command-line tools are required for optional helper scripts:

### `aspell`

Used by:

- `scripts/check_spelling_grammar.py`

Install on macOS with Homebrew:

```bash
brew install aspell
```

Install on Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y aspell
```

### `pdftotext` from Poppler

Used by:

- `scripts/build_tongue_and_quill_refs.py`

Install on macOS with Homebrew:

```bash
brew install poppler
```

Install on Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y poppler-utils
```

## Dependency map

- `scripts/count_text.py`: Python standard library only
- `scripts/validate_acronyms.py`: Python standard library only
- `scripts/search_tongue_and_quill.py`: Python standard library only
- `scripts/check_spelling_grammar.py`: Python standard library + `aspell`
- `scripts/build_tongue_and_quill_refs.py`: Python standard library + `pdftotext`

## Recommended setup check

```bash
python3 scripts/count_text.py --text 'test'
python3 scripts/validate_acronyms.py --text 'SrA Smith led TDY support.'
python3 scripts/check_spelling_grammar.py --text 'SrA Smith led unit readiness.'
```

If you plan to rebuild the Tongue and Quill chapter files, also verify:

```bash
pdftotext -v
```
