import pickle
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X, y = preprocess_data("data/insurance.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(X.columns, open("models/columns.pkl","wb"))