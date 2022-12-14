import os, argparse

path = os.getcwd()

parser = argparse.ArgumentParser(
    prog='GitPush',
    description='A fast method to push'
)
parser.add_argument('--commit', '-c', help='Commit (default: '')', default='')
parser.add_argument('--branch', '-b', help='Branch name (default: main)', default='main')

if __name__ == '__main__':
    args = parser.parse_args()

    command = f'cd "{path}" && git add . && git commit -m "{args.commit}" && git push origin {args.branch}'

    os.system(command)