import argparse
import pandas as pd
import numpy as np
import math

def calc_output(net):
    ans = 1/(1+math.exp(-net))
    return(ans)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--eta", required=True)
    parser.add_argument("--iterations", required=True)
    args = parser.parse_args()
    dataFile = args.data
    eta = float(args.eta)
    iterations = int(args.iterations)
    dataset = pd.read_csv(dataFile, header = None)
    a = dataset[0]
    b = dataset[1]
    target = dataset[2]
    w_bias_h1 = 0.20000
    w_a_h1 = -0.30000
    w_b_h1 = 0.40000
    w_bias_h2 = -0.50000
    w_a_h2 = -0.10000
    w_b_h2 = -0.40000
    w_bias_h3 = 0.30000
    w_a_h3 = 0.20000
    w_b_h3 = 0.10000
    w_bias_o = -0.10000
    w_h1_o = 0.10000
    w_h2_o = 0.30000
    w_h3_o = -0.40000
    print("a,b,h1,h2,h3,o,t,delta_h1,delta_h2,delta_h3,delta_o,w_bias_h1,w_a_h1,w_b_h1,w_bias_h2,w_a_h2,w_b_h2,w_bias_h3,w_a_h3,w_b_h3,w_bias_o,w_h1_o,w_h2_o,w_h3_o")
    print("-,-,-,-,-,-,-,-,-,-,-,   0.20000,  -0.30000,   0.40000,  -0.50000,  -0.10000,  -0.40000,   0.30000,   0.20000,   0.10000,  -0.10000,   0.10000,   0.30000,  -0.40000")
    n = len(a)
    for it in range(0, iterations):
        for i in range(0,n):
            h1_in = w_bias_h1 + (a[i] * w_a_h1) + (b[i] * w_b_h1)
            h2_in = w_bias_h2 + (a[i] * w_a_h2) + (b[i] * w_b_h2)
            h3_in = w_bias_h3 + (a[i] * w_a_h3) + (b[i] * w_b_h3)
            h1 = calc_output(h1_in)
            h2 = calc_output(h2_in)
            h3 = calc_output(h3_in)
            h_in = (h1 * w_h1_o) + (h2 * w_h2_o) + (h3 * w_h3_o) + w_bias_o
            o = calc_output(h_in)
            delta_o = o * (1-o) * (target[i]-o)
            delta_h1 = h1 * (1-h1) * ((w_h1_o*delta_o))
            delta_h2 = h2 * (1-h2) * ((w_h2_o*delta_o))
            delta_h3 = h3 * (1-h3) * ((w_h3_o*delta_o))

        #Updating weights

            w_bias_h1 = w_bias_h1 + (eta*delta_h1*1)
            w_a_h1 = w_a_h1 + (eta*delta_h1*a[i])
            w_b_h1 = w_b_h1 + (eta*delta_h1*b[i])
            w_bias_h2 = w_bias_h2 + (eta*delta_h2*1)
            w_a_h2 = w_a_h2 + (eta * delta_h2 * a[i])
            w_b_h2 = w_b_h2 + (eta * delta_h2 * b[i])
            w_bias_h3 = w_bias_h3 + (eta * delta_h3 * 1)
            w_a_h3 = w_a_h3 + (eta * delta_h3 * a[i])
            w_b_h3 = w_b_h3 + (eta * delta_h3 * b[i])

            w_bias_o = w_bias_o + (eta*delta_o*1)
            w_h1_o = w_h1_o + (eta*delta_o*h1)
            w_h2_o = w_h2_o + (eta*delta_o*h2)
            w_h3_o = w_h3_o + (eta*delta_o*h3)


            print("{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f},\t{:.5f} ".format(a[i],b[i],h1,h2,h3,o,target[i],delta_h1,delta_h2,delta_h3,delta_o,w_bias_h1,w_a_h1,w_b_h1,w_bias_h2,w_a_h2,w_b_h2,w_bias_h3,w_a_h3,w_b_h3,w_bias_o,w_h1_o,w_h2_o,w_h3_o))


