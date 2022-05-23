from sklearn.model_selection import train_test_split

def train_test_split_series(dataset):
    # Train-Test Split
    train_temp, test = train_test_split(dataset, test_size=0.2)

    # Train-Val Split
    train, val = train_test_split(train_tmp, test_size=0.2)

    #print(len(train), 'train examples')
    #print(len(val), 'validation examples')
    #print(len(test), 'test examples')

    # Separating features and target in the Train, Val and Test Set
    X_train = train[:,:-1]
    y_train = train[:,-1]

    X_val = val[:,:-1]
    y_val = val[:,-1]

    X_test = test[:,:-1]
    y_test = test[:,-1]

    return X_train, y_train, X_val, y_val, X_test, y_test
