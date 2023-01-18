import sys
sys.path.append('../AntiFilter')

from os import path
import argparse
import Pipeline.pipeline as ppl

def output_img_path(path_to_file):
    if not (path_to_file[-4:] == '.png' or path_to_file[-4:] == '.jpg' or path_to_file[-5:] == '.jpeg'):
        raise argparse.ArgumentTypeError(f"readable_file:{path_to_file} is not a valid image")
    
    return path_to_file

def input_img_path(path_to_file):
    if not path.isfile(path_to_file):
        raise argparse.ArgumentTypeError(f"readable_dir:{path_to_file} is not a valid path")
    
    return output_img_path(path_to_file)

def chain_save_path(path_to_file):
    if not (path_to_file[-5:] == ".json" or path_to_file == ""):
        raise argparse.ArgumentTypeError(f"readable_file:{path_to_file} is not valid format")
    
    return path_to_file

def setup_and_parse(conveyer: ppl.Pipeline):
    """
    Parses stdin and calls corresponding Pipeline methods
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(description = "OOP project")
    subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")

    # Create the parser for 'chain' command
    chain_parser = subparsers.add_parser('chain', help='Create and save a chain of filters')
    chain_parser.add_argument('ids', metavar='N', type=int, nargs='+',
                            help='IDs of the filters')
    chain_parser.add_argument('--saveid', type=int, default=-1, 
                            help='ID of the saved chained filter')
    chain_parser.add_argument('--desc', type=str, default="None", 
                            help='Description of chained filter')
    chain_parser.add_argument('-c', '--chainfile', nargs='?', type=chain_save_path)

    # Create the parser for 'apply' command
    apply_parser = subparsers.add_parser('apply', help='Apply a filter or a chain of filters')
    apply_parser.add_argument('id', type=int, help='ID of the filter')           
    apply_parser.add_argument('-i', '--inputfile', nargs='?', type=input_img_path)
    apply_parser.add_argument('-o', '--outputfile', nargs='?', type=output_img_path)
    apply_parser.add_argument('-c', '--chainfile', nargs='?', default="", type=chain_save_path)

    # Create the parser for 'list' command
    list_parser = subparsers.add_parser('list', help='List all filters and chains with their ids')
    list_parser.add_argument('-c', '--chainfile', nargs='?', default="", type=chain_save_path)
  
    # Parse arguments
    args = parser.parse_args()
    print(args)

    # Validate the args and call the library
    match args.subcommand:
        case 'chain': 
            conveyer.chain(args.ids, args.saveid, args.desc, args.chainfile)
        case 'apply':
            conveyer.apply(args.id, args.inputfile, args.outputfile, args.chainfile)
        case 'list':
            conveyer.list(args.chainfile)
