import os
import argparse

path = os.getcwd()

parser = argparse.ArgumentParser(
    prog='GitPush',
    description='A fast method to push'
)

parser.add_argument('--commit', '-c', help='Commit message (default: "commit")', default='commit')
parser.add_argument('--branch', '-b', help='Branch name (if not specified, only "git push" is executed)')
parser.add_argument('--upstream', '-u', help='Set upstream flag', action='store_true')

if __name__ == '__main__':
    try:
        args = parser.parse_args()

        commit = f'git commit -m "{args.commit}"'
        push = 'git push'

        if args.branch:
            upstream_flag = '-u' if args.upstream else ''
            push = f'git push {upstream_flag} origin {args.branch}'

        command = f'cd "{path}" && git add . && {commit} && {push}'

        print(f'Executing command: {command}')
        res = os.popen(command).read()
        print(res)

        print('Pushed to remote successfully!')
    except Exception as e:
        print(f'ERROR: {e}')
