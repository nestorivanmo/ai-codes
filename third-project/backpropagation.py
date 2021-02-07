import numpy as np 
import copy

def net(w0, W, X):
    return (w0 + np.dot(W, X.T))[0]

def o(net):
    return 1 / (1 + np.e ** (-net))

def forward_propagate(X, W, L, verbose=False):
    """
    Forward propagates into the neural network 

    Parameters
    ----------
    X: ndarray
        
    W: ndarray
        Matrix that contains the weights for each hidden layer

    L: list
        Contains the number of neurons per hidden layer

    verbose: Boolean
        Indicates if the ouput of each hidden layer should be displayed
    """
    layers = L.copy()
    layers.append(X.shape[1])
    layers = np.array(layers)
    if layers.shape[0] != W.shape[0]:
        raise Exception("The length of W should be equal to the number of layers")
    R = []
    Yi = X
    for idx, neurons in enumerate(layers):
        W_matrix = W[idx]
        Y_temp = []
        for neuron in range(neurons):
            Wi = W_matrix[neuron]
            net_i = net(Wi[0], Wi[1:], Yi)
            Y_temp.append(o(net_i))
        Yi = np.array([Y_temp])
        R.append(Yi)
    if verbose:
        output_hidden_layers(np.array(R))
    return np.array(R[-1])

def output_hidden_layers(HL):
    num_layers = HL.shape[0]
    for i in range(1, num_layers + 1):
        if i < num_layers:
            print(f"Hidden layer #{i}: \n\t {HL[i-1]}")
            continue
        print(f"Output: \n\t {HL[i-1]}")

def error(T, Z):
    return (0.5*(T[0]-Z[0])**2).sum()

def generate_weights(X, layers):
    num_input = X.shape[1]
    num_layers = layers.shape[0] + 1 # +1 para considerar los pesos de y a z
    for layer in layers:
        num_neuron = layer.shape[0]


"Alberto"
def generate_weights(X, layers):

    w=[]
    for i in range((len(X)+1)*(layers[0]+1)):
        w.append(0.1)
    
    for i in range(len(layers)-1):

        for j in range(1,(layers[i-1]+1)*(layers[i]+1)):
            w.append(0.1)
        
    for i in range(layers[-1]+1):
        w.append(0.1)

    return w


"""
INP UT:
X = np.array([
        [0.5, 0.1]
    ])

1 capa con 2 neuronas
layers = [2]

PROCESS:
generate_weights(X, layers)
    W = []
    for ...
        w_i = []
        procesamiento
        W.append(np.array(w_i))
    return np.array(W)

OUTPUT
W = np.array([
    np.array([
        [0.35, 0.15, 0.2],
        [0.35, 0.25, 0.3]
    ]),
    np.array([
        [0.6, 0.4, 0.45],
        [0.6, 0.5, 0.55]
    ])
])
"""

def neural_network(X, Y, hidden_layers, verbose=False):
    """
    Implements backpropagation algorithm

    Parameters
    ----------
    X: ndarray

    Y: ndarray

    hidden_layers: list
        Represents the number of layers (len(hidden_layers)) plus the number of 
        neurons per hidden layer (hidden_layers[i]). For example, a neural 
        network with 2 hidden layers and 3 and 5 neurons respectively would be 
        represented as: 
        hidden_layers = [3, 5]
            number of hidden layers = len(hidden_layers) = 2
            neurons per hidden layer :
                hidden layer #1 = hidden_layers[0] = 3
                hidden layer #2 = hidden_layers[1] = 5
    """
    #W = generate_weights(X, hidden_layers)
    W = np.array([
        np.array([
            [0.35, 0.15, 0.2],
            [0.35, 0.25, 0.3]
        ]),
        np.array([
            [0.6, 0.4, 0.45],
            [0.6, 0.5, 0.55]
        ])
    ])
    #Forward propagation
    Z = forward_propagate(X, W, hidden_layers, verbose)
    E = error(T, Z)
    print(E)

if __name__ == '__main__':
    X = np.array([[0.05, 0.1]])
    T = np.array([[0.01, 0.99]])
    hidden_layers = [2] #a neural network with one hidden layer and 2 neurons
    neural_network(X, T, hidden_layers, verbose=True)
    
