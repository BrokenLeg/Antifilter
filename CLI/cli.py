import sys
sys.path.insert(0, '/Users/deniskyslytsyn/Codebase/Antifilter')
import argparse

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description = "OOP project")
    subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")

    # Create the parser for 'chain' command
    chain_parser = subparsers.add_parser('chain', help='Create and save a chain of filters')
    chain_parser.add_argument('ids', metavar='N', type=int, nargs='+',
                            help='IDs of the filters')
    chain_parser.add_argument('--saveid', type=int, default=-1, 
                            help='ID of the saved chained filter')

    # Create the parser for 'apply' command
    apply_parser = subparsers.add_parser('apply', help="Apply a filter or a chain of filters")
    apply_parser.add_argument('id', type=int, help='ID of the filter')           
    apply_parser.add_argument('-i', '--inputfile', nargs='?', type=argparse.FileType('r'),
                                default=sys.stdin)
    apply_parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'),
                                default=sys.stdout)

    # Create the parser for 'list' command
    list_parser = subparsers.add_parser('list', help='List all filters and chains with their ids')
  
    # Parse arguments
    args = parser.parse_args()
    print(args)

    # Validate the args and call the library
    match args.subcommand:
        case 'chain':
            print('Chain hahaha')
        case 'apply':
            print('Apply lolo')
        case 'list':
            print('List lmao')

if __name__ == '__main__':
    main()