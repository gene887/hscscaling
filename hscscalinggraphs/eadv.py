import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from sklearn.metrics import mean_absolute_error, r2_score

def predict_hsc_mark(raw_mark):
    df = pd.read_csv("eadv.csv")

    x = np.array(df["Raw Mark"].tolist())
    y = np.array(df["HSC Mark"].tolist())

    model = Polynomial.fit(x, y, deg=2)

    y_pred = model(x)

    # mae and r^2
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print("MAE: ", mae)
    print("R2: ", r2)

    prediction = model(raw_mark)
    print(f"A raw mark of {raw_mark} would scale to: {prediction:.2f}")

    # linspace provides evenly spaced numbers over a specified interval
    curvy_line = np.linspace((df["Raw Mark"].min() // 10) * 10, 100, 1000)

    #plotting
    plt.title("Raw Mark to HSC Mark Prediction for English Advanced")
    plt.xlabel("Raw Mark")
    plt.ylabel("HSC Mark")
    plt.scatter(x, y, c='blue')
    plt.plot(curvy_line, model(curvy_line), c='black', linewidth = 3, label="Prediction based off HSC Raw Marks Database")
    plt.plot(curvy_line, curvy_line/2 + 50, c='green', linewidth = 2, linestyle = "dashed", label = "Divide by 2, Add 50")
    plt.legend()
    plt.show()

# ENTER YOUR RAW MARK HERE
predict_hsc_mark(82)
