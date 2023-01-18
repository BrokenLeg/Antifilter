import sys
sys.path.append('../AntiFilter')

import os
import json
import Filters.BasicFilters as BF

class Pipeline:
    '''
    Class that contain all of the basic and user-defined filters and manages all the commands
    '''
    def __init__(self):
        """
        Init basic filters
        """
        self.filters = {1 : BF.blackWhiteFilter, 
                             2 : BF.redFilter, 
                             3 : BF.greenFilter, 
                             4 : BF.blueFilter}
        

    def apply(self, filter_id: int, inputfile : str, outputfile : str, chainfile : str):
        """
        Applies a filter to an image and saves the output
        """
        if(chainfile != ""):
            self.load_chained_filters(chainfile)

        if filter_id in self.filters:
            filter = self.filters[filter_id]
        else:
            print('There are no such id of filter', file=sys.stderr)
            exit(0)

        # Load input image and create output one
        input = BF.Image.open(inputfile)
        output = BF.Image.new('RGB', input.size)

        filter.apply(input, output)

        output.save(outputfile)

        return

    def chain(self, filter_ids: list[int], saveid: int, desc: str, chainfile : str):
        """
        Saves chain in specified json file. Overwrites saveid in file. 
        When defining chained filter avoid self-usage and situation when filter to be used is defined later. 
        Example: 5: [1,2,3,4]
                6: [7,3,4]
                7: [1,2,5] 
                8: [2, 8] 
        Filter 6 uses filter 7, but filter 7 is not defined yet.
        Filter 8 uses itself, that is forbidden
        """
        if(saveid < len(self.filters)):
            print(f'Id of filter should be greater than {len(self.filters)}')
            exit(0)

        loadFileContents = os.path.exists(chainfile) and os.stat(chainfile).st_size > 0
        
        chain_data = {}

        if loadFileContents:
            with open(chainfile, "r") as file:
                chain_data.update(json.load(file))

        with open(chainfile, "w") as file:            
            chain_data[saveid] = [filter_ids, desc]
            json.dump(chain_data, file)

        return

    def list(self, chainfile : str):
        """
        Display basic filters and filters 
        """
        if(chainfile != ""):
            self.load_chained_filters(chainfile)

        for filterId, filter in self.filters.items():
            print(f'[{filterId}]: {filter.getDescription()}\n')

        return

    def load_chained_filters(self, chainfile : str):
        """
        Loads chained filters from specified file
        """
        with open(chainfile, "r") as file:
            chainData = json.load(file)
            for chainId, chainFilterData in chainData.items():
                chainedFilter = BF.ChainFilter()
                filters = [self.filters[filterId] for filterId in chainFilterData[0]]
                chainedFilter.addFiltersList(filters)
                chainedFilter.setDescription(chainFilterData[1])
                self.filters[int(chainId)] = chainedFilter
