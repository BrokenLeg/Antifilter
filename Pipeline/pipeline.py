import sys
sys.path.append('../AntiFilter')

import Filters.BasicFilters as BF

class Pipeline:
    '''
    Class that contain all of the basic and user-defined filters and manages all the commands
    '''
    def __init__(self):
        """
        Init basic filters
        TODO: deserealize chained filters and store them in dict
        """
        self.basicFilters = {1 : BF.blackWhiteFilter, 
                             2 : BF.redFilter, 
                             3 : BF.greenFilter, 
                             4 : BF.blueFilter}
        self.chainedFilters = dict()

    def apply(self, filter_id: int, inputfile, outputfile):
        """
        Applies a filter to an image and saves the output
        """
        if filter_id in self.basicFilters:
            filter = self.basicFilters[filter_id]
        elif filter_id in self.chainedFilters:
            filter = self.chainedFilters[filter_id]
        else:
            print('There are no such id of filter', file=sys.stderr)
            exit(0)

        # Load input image and create output one
        input = BF.Image.open(inputfile)
        output = BF.Image.new('RGB', input.size)

        filter.apply(input, output)

        output.save(outputfile)

        return

    def chain(self, filter_ids: list[int], saveid: int):
        """
        TODO
        """
        print('chain')
        return

    def list(self):
        """
        TODO
        """
        print('list')
        return
