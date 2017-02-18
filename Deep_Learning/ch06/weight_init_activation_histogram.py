# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def main():
    input_data = np.random.randn(1000, 100) # 1000個のデータ
    node_num = 100 # 各隠れ層のノード(ニューロン)の数
    hidden_layer_size = 5 # 隠れ層が5層
    activations = {}

    x = input_data

    for i in range(hidden_layer_size):
        if i != 0:
            x = activations[i-1]

        w = np.random.randn(node_num, node_num) * 1
        #w = np.random.randn(node_num, node_num) * 0.01
        #w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
        #w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)

        a = np.dot(x, w)

        z = sigmoid(a)
        #z = ReLU(a)
        #z = tanh(a)
        
        activations[i] = z

    # ヒストグラムを描画
    for i, a in activations.items():
        plt.subplot(1, len(activations), i+1)
        plt.title(str(i+1) + "-layer")
        #if i != 0: plt.yticks([], [])
        plt.hist(a.flatten(), 30, range=(0,1))
    plt.show()

if __name__ == '__main__':
    main()


