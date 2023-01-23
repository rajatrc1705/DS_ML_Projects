
# setwd("d:/College and Work/Kaggle/Datasets/EPL/")

# reading dataset
og_dataset <- read.csv("EPL_20_21.csv")
dataset <- og_dataset[5:18]

# prcomp() function is used to perform PCA, by default
# centers the variables to have means equal to 0

principal_component <- prcomp(dataset, scale. = T)

names(principal_component)

# principal components for drawing graph
principal_component$x

plot(principal_component$x[,1], principal_component$x[,2])
text(principal_component$x[,1], principal_component$x[,2],
     labels=og_dataset$Name,
     pos=3
     )

# give mean and std before doing pca
principal_component$center
principal_component$scale

# gives the principal component loading, max number of principal comp
# loadings are min(n-1, p)
principal_component$rotation

# plotting the principal components
par("mar")
biplot(principal_component, scale = 0)

library(ggplot2)
library(ggfortify)

autoplot(principal_component, data=og_dataset
         # , colour='Club'
         # , label=TRUE
         , loadings = TRUE
         , loadings.label = TRUE
         , loadings.label.size = 6
         )



# compute variance of principal components through std
std_dev <- principal_component$sdev

pc_var <- std_dev^2

# variance of first 10 components
pc_var[1:10]

# to find out total variance explained by the principal component
# we calculate proportion of variance
prop_var = pc_var/sum(pc_var)

# we can see that the first 5 pc explain about 75% of the variance
# we can decide how many pc to select using a scree plot
prop_var

plot(prop_var,
     main="Scree Plot To Select #PCs",
     xlab="Principal Component",
     ylab="Proportion of Variance Explained",
     type="b"
    )

plot(cumsum(prop_var),
     main="Scree Plot To Select #PCs",
     xlab="Principal Component",
     ylab="Proportion of Variance Explained",
     type="b"
)



# here we will select first 10 principal components
# now we have implemented pca on the training set, and we will use
# the 10 pc's as predictor variables further

# note: do not perform pca simultaneously on train and test
# note: do not perform pca separately on train and test
# use pca performed on train to get vals for test

# https://www.analyticsvidhya.com/blog/2016/03/pca-practical-guide-principal-component-analysis-python/
