# import torch
# import torch.nn as nn

# # Define the LSTM Model
# class LSTMModel(nn.Module):
#     def __init__(self, input_size, hidden_size, num_layers, num_classes):
#         super(LSTMModel, self).__init__()
#         self.hidden_size = hidden_size
#         self.num_layers = num_layers
        
#         # LSTM layer
#         self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        
#         # Fully connected layer
#         self.fc = nn.Linear(hidden_size, num_classes)

#     def forward(self, x):
#         # Initialize hidden and cell states
#         h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
#         c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

#         # Forward propagate LSTM
#         out, _ = self.lstm(x, (h0, c0))  

#         # Take the output of the last time step
#         out = self.fc(out[:, -1, :])  
#         return out



# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# # Build LSTM model
# model = Sequential([
#     LSTM(128, input_shape=(20, 10), return_sequences=False),  # 20 timesteps, 10 features
#     Dense(64, activation='relu'),
#     Dense(3, activation='softmax')  # 3 classes
# ])

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.summary()


# # Hyperparameters
# input_size = 10   # e.g., 10 features per timestep
# hidden_size = 128
# num_layers = 2
# num_classes = 3   # e.g., 3-class classification
# sequence_length = 20
# batch_size = 32

# # Example input
# x = torch.randn(batch_size, sequence_length, input_size)

# model = LSTMModel(input_size, hidden_size, num_layers, num_classes)
# output = model(x)
# print(output.shape)  # torch.Size([32, 3])



# import numpy as np

# text = "hello world"
# chars = sorted(list(set(text)))
# vocab_size = len(chars)

# char_to_idx = {ch:i for i,ch in enumerate(chars)}
# idx_to_char = {i:ch for i,ch in enumerate(chars)}

# encoded = np.array([char_to_idx[ch] for ch in text])
# print("Vocab:", char_to_idx)
# print("Encoded text:", encoded)

# #------------------------------------------------------------------------------------------------------------------------------------------------
# class LSTMCell:
#     def __init__(self, input_dim, hidden_dim):
#         self.input_dim = input_dim
#         self.hidden_dim = hidden_dim

#         # Xavier init
#         def xavier(shape):
#             return np.random.randn(*shape) * np.sqrt(2.0/sum(shape))

#         self.W_f = xavier((hidden_dim, hidden_dim + input_dim))
#         self.W_i = xavier((hidden_dim, hidden_dim + input_dim))
#         self.W_c = xavier((hidden_dim, hidden_dim + input_dim))
#         self.W_o = xavier((hidden_dim, hidden_dim + input_dim))

#         self.b_f = np.zeros((hidden_dim, 1))
#         self.b_i = np.zeros((hidden_dim, 1))
#         self.b_c = np.zeros((hidden_dim, 1))
#         self.b_o = np.zeros((hidden_dim, 1))

#     def step(self, x_t, h_prev, c_prev, verbose=True):
#         concat = np.vstack((h_prev, x_t))  # shape: (hidden+input, 1)

#         f_t = self._sigmoid(self.W_f @ concat + self.b_f)
#         i_t = self._sigmoid(self.W_i @ concat + self.b_i)
#         c_hat_t = np.tanh(self.W_c @ concat + self.b_c)
#         c_t = f_t * c_prev + i_t * c_hat_t
#         o_t = self._sigmoid(self.W_o @ concat + self.b_o)
#         h_t = o_t * np.tanh(c_t)

#         if verbose:
#             print("\n===== Step =====")
#             print("Input x_t:", x_t.ravel())
#             print("Forget gate f_t:", f_t.ravel())
#             print("Input gate i_t:", i_t.ravel())
#             print("Candidate c_hat_t:", c_hat_t.ravel())
#             print("Cell state c_t:", c_t.ravel())
#             print("Output gate o_t:", o_t.ravel())
#             print("Hidden state h_t:", h_t.ravel())

#         return h_t, c_t

#     def _sigmoid(self, z):
#         return 1 / (1 + np.exp(-z))



# # hyperparams
# input_dim = vocab_size   # one-hot size
# hidden_dim = 8
# seq_len = len(encoded)-1

# # init cell
# cell = LSTMCell(input_dim, hidden_dim)

# # init states
# h = np.zeros((hidden_dim, 1))
# c = np.zeros((hidden_dim, 1))

# # run through sequence
# for t in range(seq_len):
#     # one-hot encode
#     x_t = np.zeros((vocab_size, 1))
#     x_t[encoded[t]] = 1

#     # forward step
#     h, c = cell.step(x_t, h, c, verbose=True)

#     # prediction: map hidden state -> vocab
#     y = np.exp(h.ravel() @ np.random.randn(hidden_dim, vocab_size))  # random weights for demo
#     probs = y / np.sum(y)

#     print("Prediction probs for next char:", probs)
#     print("Predicted char:", idx_to_char[np.argmax(probs)])




import numpy as np

# ---------------- Prepare Data ----------------
text = "hi welcome to my training"
chars = sorted(list(set(text)))
vocab_size = len(chars)

char_to_idx = {ch: i for i, ch in enumerate(chars)}
idx_to_char = {i: ch for i, ch in enumerate(chars)}

encoded = np.array([char_to_idx[ch] for ch in text])
print("Vocab:", char_to_idx)
print("Encoded text:", encoded)

# ---------------- LSTM Cell ----------------
class LSTMCell:
    def __init__(self, input_dim, hidden_dim, lr=0.1):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.lr = lr

        # Xavier init
        def xavier(shape):
            return np.random.randn(*shape) * np.sqrt(2.0 / sum(shape))

        self.W_f = xavier((hidden_dim, hidden_dim + input_dim))
        self.W_i = xavier((hidden_dim, hidden_dim + input_dim))
        self.W_c = xavier((hidden_dim, hidden_dim + input_dim))
        self.W_o = xavier((hidden_dim, hidden_dim + input_dim))

        self.b_f = np.zeros((hidden_dim, 1))
        self.b_i = np.zeros((hidden_dim, 1))
        self.b_c = np.zeros((hidden_dim, 1))
        self.b_o = np.zeros((hidden_dim, 1))

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def step(self, x_t, h_prev, c_prev):
        concat = np.vstack((h_prev, x_t))  # (hidden+input, 1)

        f_t = self._sigmoid(self.W_f @ concat + self.b_f)
        i_t = self._sigmoid(self.W_i @ concat + self.b_i)
        c_hat_t = np.tanh(self.W_c @ concat + self.b_c)
        c_t = f_t * c_prev + i_t * c_hat_t
        o_t = self._sigmoid(self.W_o @ concat + self.b_o)
        h_t = o_t * np.tanh(c_t)

        cache = (x_t, h_prev, c_prev, concat, f_t, i_t, c_hat_t, c_t, o_t, h_t)
        return h_t, c_t, cache

    def backward(self, dh_next, dc_next, cache):
        (x_t, h_prev, c_prev, concat, f_t, i_t, c_hat_t, c_t, o_t, h_t) = cache

        # Gradients of output gate
        do = dh_next * np.tanh(c_t)
        do_raw = do * o_t * (1 - o_t)

        # Gradients wrt cell state
        dc = dh_next * o_t * (1 - np.tanh(c_t) ** 2) + dc_next
        dc_hat = dc * i_t
        dc_hat_raw = dc_hat * (1 - c_hat_t ** 2)

        di = dc * c_hat_t
        di_raw = di * i_t * (1 - i_t)

        df = dc * c_prev
        df_raw = df * f_t * (1 - f_t)

        dc_prev = dc * f_t
        dh_prev = (self.W_f.T @ df_raw +
                   self.W_i.T @ di_raw +
                   self.W_c.T @ dc_hat_raw +
                   self.W_o.T @ do_raw)[:self.hidden_dim, :]

        # Weight updates
        self.W_f -= self.lr * (df_raw @ concat.T)
        self.W_i -= self.lr * (di_raw @ concat.T)
        self.W_c -= self.lr * (dc_hat_raw @ concat.T)
        self.W_o -= self.lr * (do_raw @ concat.T)

        self.b_f -= self.lr * df_raw
        self.b_i -= self.lr * di_raw
        self.b_c -= self.lr * dc_hat_raw
        self.b_o -= self.lr * do_raw

        return dh_prev, dc_prev

# ---------------- Training Setup ----------------
input_dim = vocab_size
hidden_dim = 16
cell = LSTMCell(input_dim, hidden_dim, lr=0.1)

# Output layer (hidden -> vocab)
Why = np.random.randn(vocab_size, hidden_dim) * 0.01
by = np.zeros((vocab_size, 1))

def softmax(z):
    e = np.exp(z - np.max(z))
    return e / np.sum(e)

# ---------------- Training Loop ----------------
epochs = 500
for epoch in range(epochs):
    h = np.zeros((hidden_dim, 1))
    c = np.zeros((hidden_dim, 1))

    caches = []
    xs, hs, cs, ys, ps = {}, {}, {}, {}, {}
    hs[-1] = h
    cs[-1] = c

    loss = 0

    # Forward pass through sequence
    for t in range(len(encoded) - 1):
        x_t = np.zeros((vocab_size, 1))
        x_t[encoded[t]] = 1

        h, c, cache = cell.step(x_t, hs[t - 1], cs[t - 1])
        hs[t], cs[t] = h, c
        caches.append(cache)

        # output layer
        y = Why @ h + by
        p = softmax(y)

        target_idx = encoded[t + 1]
        loss += -np.log(p[target_idx, 0] + 1e-9)

        xs[t], ys[t], ps[t] = x_t, y, p

    # Backward pass
    dWhy = np.zeros_like(Why)
    dby = np.zeros_like(by)
    dh_next = np.zeros_like(h)
    dc_next = np.zeros_like(c)

    for t in reversed(range(len(encoded) - 1)):
        # grad output
        dy = np.copy(ps[t])
        dy[encoded[t + 1]] -= 1  # softmax derivative

        dWhy += dy @ hs[t].T
        dby += dy

        dh = Why.T @ dy + dh_next
        dh_next, dc_next = cell.backward(dh, dc_next, caches[t])

    # Update output layer
    Why -= cell.lr * dWhy
    by -= cell.lr * dby

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss = {loss:.3f}")

# ---------------- Text Generation ----------------
h = np.zeros((hidden_dim, 1))
c = np.zeros((hidden_dim, 1))
x = np.zeros((vocab_size, 1))
x[encoded[0]] = 1  # start with "h"

generated = "h"
for t in range(10):
    h, c, _ = cell.step(x, h, c)
    y = Why @ h + by
    p = softmax(y)

    idx = np.random.choice(range(vocab_size), p=p.ravel())
    generated += idx_to_char[idx]

    x = np.zeros((vocab_size, 1))
    x[idx] = 1

print("\nGenerated text:", generated)
