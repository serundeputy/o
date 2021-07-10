import argparse
import os
import git

parser = argparse.ArgumentParser()
base_url = 'git@github.com'

parser.add_argument(
    '-o',
    '--org',
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
    help='where to clone the code into'
)
args = parser.parse_args()

def open_nvim(path):
    repo_exists = os.path.isdir(path)
    print('made it to args.org and args.repo')
    print(repo_exists)
    if repo_exists:
        print('exists')
        os.system(
            f'cd {path}; nvim .'
        )
    else:
        git.Git(f'{args.codedir}/{args.org}').clone(
            f'{base_url}:{args.org}/{args.repo}.git'
        )
        os.system(
            f'cd {path}; nvim .'
        )

if args.org and args.repo:
    path = f'{args.codedir}/{args.org}/{args.repo}'
    open_nvim(path)