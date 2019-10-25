import sys, os
import glob

import numpy as np
import pandas as pd



input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
reference_dir = os.path.join(input_dir, 'ref')

reference_file = os.path.join(reference_dir, 'test/test_true_info.csv')
files = glob.glob(submit_dir + "/*.csv")
prediction_file = files[0] 

if not os.path.isdir(submit_dir):
    print("{} doesn't exist".format(submit_dir))
elif not os.path.isdir(reference_dir):
    print("{} doesn't exist".format(reference_dir))
else:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reference  = pd.read_csv(reference_file)
    prediction = pd.read_csv(prediction_file)

    reference  = reference.sort_values('evtID')
    prediction = prediction.sort_values('evtID')

    if not np.array_equal(reference['evtID'], prediction['evtID']):
        print("Invalid column EvtID\n")
        sys.stderr.write("Invalid column EvtID\n")
        sys.exit()
     
    E_diff  = np.mean((reference['E'] - prediction['E']) ** 2)
    R_diff = np.mean((reference['R'] - prediction['R']) ** 2)
    score = R_diff / 100000 + E_diff * 100
   
    output_filename = os.path.join(output_dir, 'scores.txt')

    print("Total: {} \n".format(score))
    print("E: {} \n".format(E_diff))
    print("R: {} \n".format(R_diff))

    with open(output_filename, 'w') as output_file:
        output_file.write("Total: {}".format(score))
        output_file.write("\n")
        output_file.write("E: {}".format(E_diff))
        output_file.write("\n")
        output_file.write("R: {}".format(R_diff))


