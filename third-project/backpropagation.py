import numpy as np 
import copy
import random

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
        output_hidden_layers(X, np.array(R))
    return np.array(R)

def backward_propagate(R, T, W, eta, hidden_layers, verbose=False):
    """
    Backward propagtion

    Parameters
    ----------
    R: ndarray
        Matrix that represents the output of each hidden layer in a previous 
        forward propagate iteration

    T: ndarray
        Target vector

    W: ndarray
        Matrix of current weights for each layer

    hidden_layers: list
        Represents the number of layers (len(hidden_layers)) plus the number of 
        neurons per hidden layer (hidden_layers[i])
    """
    new_W = W[::-1]
    for idx, HL in enumerate(R[::-1]): #HL: hidden layer
        #Hidden Layers
        if idx < R.shape[0]-1:
            new_W[idx][:, 1:] = hidden_layer(HL, T, R, idx, new_W)
            continue
        new_W[idx][:, 1:] = initial_weights(HL, T, R, idx, new_W)
        print(f'new_W: \n{new_W}', end='\n\n')
    return new_W

def hidden_layer(HL, T, R, idx, W):
    d_EZ = HL - T
    d_Znet = HL*(1-HL)
    alpha = d_EZ * d_Znet
    d_netV = R[idx]
    d_EV = alpha.T @ d_netV
    return W[idx][:, 1:] - (eta * d_EV)

def output_hidden_layers(X, HL):
    num_layers = HL.shape[0]
    print(f"Input: \n\t {X}")
    for i in range(1, num_layers + 1):
        if i < num_layers:
            print(f"Hidden layer #{i}: \n\t {HL[i-1]}")
            continue
        print(f"Output: \n\t {HL[i-1]}")

def error(T, Z):
    return (0.5*(T[0]-Z[0])**2).sum()

def generate_weights(X, layers):
	w=[]
	#Se crean los pesos para X0 en cada capa
	weights0=[]
	for i in range(len(layers)+1):
		weights0.append(round(random.uniform(-0.05, 0.05),2))
	aux=[]
	for i in range(layers[0]):
		auxI=[]
		for j in range(X.shape[1]+1):
			if(j==0):
				auxI.append(weights0[0])
			else:
				auxI.append(round(random.uniform(-0.05, 0.05),2))
		auxI=np.array(auxI)
		aux.append(auxI)
	w.append(aux)
	for i in range(1,len(layers)):
		print("entro")
		aux=[]	
		for j in range(layers[i]):
			auxI=[]
			for k in range(layers[i-1]+1):
				if(k==0):
					auxI.append(weights0[i])
				else:
					auxI.append(round(random.uniform(-0.05, 0.05),2))
			auxI=np.array(auxI)
			aux.append(auxI)
		w.append(aux)
	aux=[]
	for i in range(X.shape[1]):
		auxI=[]
		for j in range(layers[-1]+1):
			if(j==0):
				auxI.append(weights0[len(layers)])
			else:
				auxI.append(round(random.uniform(-0.05, 0.05),2))
		auxI=np.array(auxI)
		aux.append(auxI)
	w.append(aux)
	return np.array(w)


def neural_network(X, Y, eta, hidden_layers, verbose=False):
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
    #W = generate_weights(X, hidden_layers)
    #Forward propagation
    R = forward_propagate(X, W, hidden_layers, verbose)
    Z = R[-1]
    E = error(T, Z)
    if verbose:
        print(E)
    backward_propagate(R, T, W, eta, hidden_layers)
    

if __name__ == '__main__':
    X = np.array([[0.05, 0.1]])
    T = np.array([[0.01, 0.99]])
    hidden_layers = [2] #a neural network with one hidden layer and 2 neurons
    eta = 0.5
    neural_network(X, T, eta, hidden_layers, verbose=False)
    
