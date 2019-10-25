import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, pmts_pos, spmt_hits, lpmt_hits, true_info, test_l_hits, test_s_hits):

        """
        pmts_pos - positions of small and large PMTs
        spmt_hits - train data with info for small PMTs hits
        lpmt_hits - train data with info for large PMTs hits
        true_info - train true info
        test_l_hits - test data with info for large PMTs hits
        test_s_hits - test data with info for small PMTs hits

        Method returns dataframe with predictions.
 
        """

        x = test_l_hits["event"].unique()
        pred = pd.DataFrame({
            "evtID": x,
            "R": np.random.normal(size=len(x)),
            "E": np.random.normal(size=len(x))
        	})
        

        return pred
