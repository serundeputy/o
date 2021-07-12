import argparse
from dotenv import load_dotenv
import os
import git

load_dotenv()
parser = argparse.ArgumentParser()
base_url = 'git@github.com'


parser.add_argument(
    '-e',
    '--editor',
    default=os.getenv('editor'),
    help='the github org'
)
parser.add_argument(
    '-o',
    '--org',
    default=os.getenv('org'),
    help='the github org'
)
parser.add_argument(
    '-r',
    '--repo',
    help='the github repo'
)
parser.add_argument(
    '-c',
    '--codedir',
    default=os.getenv('codedir'),
    help='where to clone the code'
)
args = parser.parse_args()

def repo_exists(path):
    return os.path.isdir(path)

def clone():
   git.Git(f'{args.codedir}').clone(
       f'{base_url}:{args.org}/{args.repo}.git'
   )

def open_nvim(path):
    if repo_exists(path):
        os.system(
            f'cd {path}; nvim .'
        )
    else:
        clone()
        os.system(
            f'cd {path}; nvim .'
        )

def open_vscode(path):
    if repo_exists(path):
        os.system(f'code {path}')
    else:
        clone()
        os.system(f'code {path}')


def open(path):
    """
    " Choose wich editor.
    """
    if args.editor == 'nvim':
        open_nvim(path)
    elif args.editor == 'vscode' or args.editor == 'code':
        open_vscode(path)


if args.org and args.repo:
    path = f'{args.codedir}/{args.repo}'
    open(path)
