# o 

open a codebase in your favourite `editor` or clone it and open it if it is not cloned yet.

## Install

```bash
git clone git@github.com:serundeputy/o.git
```

## Alias

Open your `.zshrc` or `.bashrc` file and add an alias.

```bash
alias o="python PATH_TO_WHERE_YOU_CLONED/o.py"
```

## Usage
`o -h`
```bash
➜  o git:(mainline) ✗ o -h
usage: o.py [-h] [-o ORG] [-r REPO] [-c CODEDIR]

optional arguments:
  -h, --help            show this help message and exit
  -o ORG, --org ORG     the github org
  -r REPO, --repo REPO  the github repo
  -c CODEDIR, --codedir CODEDIR
                        where to clone the code
```

for example to clone gff's [neovim config](https://github.com/serundputy/gffNeovim):

```bash
o -o serundeputy -r gffNeovim -c ~/code
```
