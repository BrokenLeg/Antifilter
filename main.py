import Pipeline.pipeline as pipeline
import Filters.BasicFilters as BF
import CLI.cli as cli

def main():
    conveyer = pipeline.Pipeline()
    cli.setup_and_parse(conveyer)
    return

if __name__ == '__main__':
    main()