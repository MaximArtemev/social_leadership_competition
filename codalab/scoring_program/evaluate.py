import sys, os
import glob

import numpy as np
import pandas as pd


input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
reference_dir = os.path.join(input_dir, 'ref')

reference_file = os.path.join(reference_dir, 'test_data.csv')
files = glob.glob(submit_dir + "/*.csv")
prediction_file = files[0] 

if not os.path.isdir(submit_dir):
    print("{} doesn't exist".format(submit_dir))
elif not os.path.isdir(reference_dir):
    print("{} doesn't exist".format(reference_dir))
else:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reference = pd.read_csv(reference_file)
    prediction = pd.read_csv(prediction_file)

    reference = reference.sort_values('uid')
    prediction = prediction.sort_values('uid')

    if not np.array_equal(reference['uid'], prediction['uid']):
        print("Invalid column EvtID\n")
        sys.stderr.write("Invalid column EvtID\n")
        sys.exit()

    precision_at_k = np.mean(abs(reference['is_leader'] - prediction['is_leader']))/len(reference)
    metric_2 = 0
    metric_3 = 0
    metric_4 = 0
    
    score = precision_at_k + metric_2 + metric_3 + metric_4
   
    output_filename = os.path.join(output_dir, 'scores.txt')

    print("Total: {} \n".format(score))
    print("Precision_at_K: {} \n".format(precision_at_k))
    print("Metric_2: {} \n".format(metric_2))
    print("Metric_3: {} \n".format(metric_3))
    print("Metric_4: {} \n".format(metric_4))

    with open(output_filename, 'w') as output_file:
        output_file.write("Total: {}".format(score))
        output_file.write("\n")
        output_file.write("Precision_at_K: {}".format(precision_at_k ))
        output_file.write("\n")
        output_file.write("Metric_2: {}".format(metric_2))
        output_file.write("\n")
        output_file.write("Metric_3: {}".format(metric_3))
        output_file.write("\n")
        output_file.write("Metric_4: {}".format(metric_4))
        output_file.write("\n")


