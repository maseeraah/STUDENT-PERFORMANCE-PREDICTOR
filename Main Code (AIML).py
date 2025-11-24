import random

def train_linear_regression(data, lr=0.01, iters=1000):
    # adding features like  number of hours studied and the attendace
    feat = [[1, hours, attend] for hours, attend, score in data]
    val = [score for hours, attend, score in data]
    samples, nfeat = len(feat), len(feat[0])
    wvect = [0.0] * nfeat  

    for _ in range(iters):
        gvect = [0.0] * nfeat
        for i in range(samples):
            y_hat = sum(wvect[j] * feat[i][j] for j in range(nfeat))
            err = y_hat - val[i]
            for j in range(nfeat):
                gvect[j] += err * feat[i][j]
        for j in range(nfeat):
            gvect[j] /= samples
            wvect[j] -= lr * gvect[j]
    return wvect

def mse(feat, val, wvect):
    errs = [(sum(wvect[j]*feat[i][j] for j in range(len(wvect))) - val[i])**2 
            for i in range(len(feat))]
    return sum(errs)/len(errs)

def main():
    print("\n--- Student Performance Predictor ---")
    #sample data for total hours studied, attendance and the exam score
    data = [
        (2.0, 0.6, 58.0),
        (3.0, 0.7, 65.0),
        (1.5, 0.5, 50.0),
        (4.0, 0.8, 75.0),
        (5.0, 0.9, 82.0),
        (6.0, 0.9, 88.0),
        (7.0, 0.95, 92.0)
    ]
    random.shuffle(data)
    split = int(0.7 * len(data))
    train, valset = data[:split], data[split:]

    #training the model 
    wvect = train_linear_regression(train)
    feat_train = [[1,h,a] for h,a,s in train]; val_train=[s for h,a,s in train]
    feat_val = [[1,h,a] for h,a,s in valset]; val_val=[s for h,a,s in valset]

    print("Weights learned:", [round(x,2) for x in wvect])
    print("Train MSE:", round(mse(feat_train,val_train,wvect),2))
    print("Validation MSE:", round(mse(feat_val,val_val,wvect),2))

    #asking user input for predicting the scores
    h = float(input("Enter hours studied: "))
    a = float(input("Enter attendance rate (0-1): "))
    x = [1,h,a]
    y_hat = sum(wvect[i]*x[i] for i in range(len(x)))
    print(f"Predicted exam score: {y_hat:.1f}")

if __name__ == "__main__":
    main()
