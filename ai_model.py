from sklearn.linear_model import LogisticRegression

# sample training data
X = [
    [5, 0],
    [10, 0],
    [70, 1],
    [80, 1]
]

y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

def classify(cpu, keyword_flag):
    result = model.predict([[cpu, keyword_flag]])
    return "Suspicious" if result[0] == 1 else "Safe"