# Regression Template

# Importing the dataset
dataset = read.csv('CableImpedances.csv')
dataset = dataset[1:2]

# Splitting the dataset into the Training set and Test set
# # install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio = 2/3)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting the Regression Model to the dataset
#install.packages('e1071')
library(e1071)
regressor=svm(formula=Impedance ~ .,
              data=dataset,
              type='eps-regression')

# Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5))

# Visualising the Regression Model results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$ï..Length, y = dataset$Impedance),
             colour = 'red') +
  geom_line(aes(x = dataset$ï..Length, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Support Vector Regression Model (Normal)') +
  xlab('Length') +
  ylab('Impedance')

# Visualising the Regression Model results (for higher resolution and smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$ï..Length), max(dataset$ï..Length), 0.1)
ggplot() +
  geom_point(aes(x = dataset$ï..Length, y = dataset$Impedance),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(ï..Length = x_grid))),
            colour = 'blue') +
  ggtitle('Support Vector Regression Model') +
  xlab('Length') +
  ylab('Impedance')