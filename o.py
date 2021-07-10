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

# @TODO add readin the .env file and allow overrides via --OPTIONS

# @TODO abstract open_vim and open_code into their own modules?
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

# @TODO add open_code()
# i.e open in vscode

if args.org and args.repo:
    path = f'{args.codedir}/{args.org}/{args.repo}'
    open_nvim(path)
