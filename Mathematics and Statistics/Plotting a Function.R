
# function as an expression
f = function(y) exp(-y)

# drawing the function
curve(f, from=0, to=20)

# using ggplot
library("ggplot2")

ggplot(data.frame(x=c(1, 20)), aes(x=x)) + 
  stat_function(fun=f)
