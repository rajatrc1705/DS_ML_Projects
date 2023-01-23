
# install.packages('dplyr')
# library(dplyr)
library(ggplot2)


# reading dataset
og_dataset <- read.csv("EPL_20_21.csv")
dataset <- og_dataset[5:18]


head(dataset)

# calculate the distance between each data point
distance.matrix = dist(dataset, diag=TRUE, upper=TRUE, method='euclidean')

head.matrix(distance)

mds = cmdscale(distance.matrix, eig = TRUE, x.ret=TRUE)

mds.var.per = round(mds$eig/sum(mds$eig) * 100, 2)
mds.var.per[1:5]

# format the data for ggplot
mds.values = mds$points

mds.data = data.frame(check.rows = FALSE,
                      row.names = rownames(og_dataset),
                      X = mds.values[,1],
                      Y = mds.values[,2]
                      )

mds.data

ggplot(data = mds.data, aes(x=X, y=Y, label=rownames(og_dataset))) +
  
  geom_text() +
  theme_bw() +
  xlab(paste("MDS 1 = ", mds.var.per[1], "%", sep="")) +
  ylab(paste("MDS 2 = ", mds.var.per[2], "%", sep="")) +
  ggtitle("MDS plot using Euclidean Distance (Same as PCA)")
        
