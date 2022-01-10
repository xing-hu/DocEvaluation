
df_comment <- read.csv("comment_results_without_bias.csv")
df_comment <- df_comment[,-1]

df_commit <- read.csv("commit_results_without_bias.csv")
df_commit <- df_commit[,-1]

library(dplyr)
library(reshape2)
library(ggplot2)


library(corrplot)


corrplot::corrplot.mixed(cor(df_comment, method = "pearson"), tl.pos='lt', tl.srt=30, tl.col='black', lower.col = "black", tl.cex=0.9)
corrplot::corrplot.mixed(cor(df_comment, method = "kendall"), tl.pos='lt', tl.srt=30, tl.col='black', lower.col = "black", tl.cex=0.9)

corrplot::corrplot.mixed(cor(df_commit, method = "pearson"), tl.pos='lt', tl.srt=30, tl.col='black', lower.col = "black", tl.cex=0.9)
corrplot::corrplot.mixed(cor(df_commit, method = "kendall"), tl.pos='lt', tl.srt=30, tl.col='black', lower.col = "black", tl.cex=0.9)
