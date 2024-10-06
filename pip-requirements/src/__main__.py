from argparse import ArgumentParser

from re import sub as re_sub
from json import dumps as json_dumps
from subprocess import run as p_run
from requirements import parse as req_parse


if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument('command', metavar='command', type=str,
                        nargs='?', help='conftest command')
    parser.add_argument('requirements', metavar='file', type=str,
                        nargs='?', help='requirements.txt file')
    args, unknown = parser.parse_known_args()

    if args.command and args.requirements:
        with open(args.requirements, 'r') as fd:
            rf_prsd = req_parse(fd)
            rf_json = json_dumps({
                'requirements': {
                    re_sub(r'([0-9a-zA-Z])[-_\.]+', r'\1-', r.name).lower():
                        r.__dict__ for r in rf_prsd
                }
            })
            p_run(['conftest', args.command, '-'] + unknown, input=rf_json, encoding='utf-8')
