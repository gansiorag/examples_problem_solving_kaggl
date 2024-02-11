'''
Каждая строчка наборов данных содержит следующие поля:
    Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);
    Name — имя;
    Sex — пол;
    Age — возраст;
    SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту титаника;
    Parch — количество родителей, детей (в том числе приемных) на борту титаника;
    Ticket — номер билета;
    Fare — плата за проезд;
    Cabin — каюта;
    Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).
    В поле Age приводится количество полных лет. Для детей меньше 1 года — дробное. Если возраст не известен точно,
    то указано примерное значение в формате xx.5.

    Применим следующие модели машинного обучения
    Nearest Neighbors - метод к ближайших сседей
    Linear SVM - классификации опорных векторов для случая линейного ядра
    RBF SVM;
    Gaussian Process;
    Decision Tree;
    Random Forest;
    Neural Net;
    AdaBoost;
    Naive Bayes;
    QDA

'''



from sklearn.ensemble import RandomForestClassifier
import pandas as pd

train_data = pd.read_csv("/home/al/PycharmProjects/examples_problem_solving_kaggl/competitons/titanic/data/train.csv")
test_data = pd.read_csv("/home/al/PycharmProjects/examples_problem_solving_kaggl/competitons/titanic/data/test.csv")
print(train_data.head())
print(train_data.info())

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
print(X.info())
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")

