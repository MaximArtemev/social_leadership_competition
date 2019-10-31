import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, train_users, posts, test_users):

        """
        train_data - train data
        test_data - test data

        Method returns dataframe with predictions.
 
        """

        x = test_users["uid"]
        pred = pd.DataFrame({
            "uid": x,
            "is_leader": np.ones(len(x)),
        })

        return pred
