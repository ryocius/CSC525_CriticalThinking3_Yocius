import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def visualizePolynomial():
    plt.scatter(X, y, color='red')
    plt.plot(X, polReg.predict(polyReg.fit_transform(X)), color='blue')
    plt.title('Polynomial Regression of Salary vs. Years of Experience')
    plt.xlabel('Yrs Experience')
    plt.ylabel('Salary')
    plt.show()
    return

def takeInput(input_type="years"):
    while True:
        try:
            if input_type == "years":
                out = float(input("Enter the number of years of experience: "))
                if out < 0:
                    raise ValueError("Years of experience cannot be negative.")
            elif input_type == "yn":
                out = input("Enter y or n: ").lower()
                if out not in ("y", "n"):
                    raise ValueError("Input must be 'y' or 'n'.")
            elif input_type == "selection":
                out = int(input("Enter 1 for prediction, 2 for visualizing the polynomial curve, and 3 to quit: "))
                if out < 1 or out > 3:
                    raise ValueError("Selection must be 1, 2, or 3.")
            else:
                raise ValueError("Invalid input type.")
            return out
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def main():
    while(True):
        selection = takeInput("selection")
        if selection == 1:
            years = takeInput("years")
            prediction = polReg.predict(polyReg.fit_transform([[years]]))
            salary = prediction[0]
            print(f"Based on polynomial regression, one would expect someone with {years} years of experience to "
                  f"have a salary of ${salary:,.2f}")
        elif selection == 2:
            visualizePolynomial()
        else:
            sys.exit()


dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values
Xtrain, Xtest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

polyReg = PolynomialFeatures(degree=4)
Xpoly = polyReg.fit_transform(X)
polReg = LinearRegression()
polReg.fit(Xpoly, y)

main()









