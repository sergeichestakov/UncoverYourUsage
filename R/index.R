packages <- function(packages) {
    for (package in packages) {
        if (!require(package, character.only = TRUE)) {
            # install package if not detected
            install.packages(pkgs = package, repos = "http://cran.r-project.org")
            require(package, character.only = TRUE)
        }
    }
}

packages(c("formatR", "car"))  # require packages

library(formatR)  # load formatting library

tidy_dir(path = ".", recursive = TRUE)  # format files

data <- read.csv("../data/recs2009_public.csv", header = TRUE)
correlationRanking <- data.frame(name = character(), rsquared = double(), lambda = double(), 
    isFactor = logical(), stringsAsFactors = FALSE)

# iterate over all variables
for (variable in names(data)) {
    print(paste("Analysis of Explanatory Variable:", variable))
    regressData <- list()
    regressData$variable = variable
    regressData$x <- data[[regressData$variable]]
    regressData$isFactor <- FALSE
    regressData$uniqueValues <- length(unique(regressData$x))
    if (regressData$uniqueValues < 2) {
        # not even unique factors to continue, skip
        next
    } else if (regressData$uniqueValues < 10) {
        # most likely a categorical variable
        regressData$isFactor <- TRUE
        regressData$x <- as.factor(regressData$x)
    }
    regressData$y <- data$KWH  # response variable
    
    regressData$formula <- regressData$y ~ regressData$x
    regressData$lm <- lm(regressData$formula)
    regressData$boxcox <- boxCox(object = regressData$lm, plotit = FALSE)
    regressData$lambda <- regressData$boxcox$x[which.max(regressData$boxcox$y)]  # account for deviances in the normality of the errors
    
    regressData$y <- yjPower(regressData$y, lambda = regressData$lambda)  ## transform data based on calculated lambda value
    regressData$formula <- regressData$y ~ regressData$x
    regressData$lm <- lm(regressData$formula)
    regressData$rsquared <- summary(regressData$lm)$r.squared
    regressData$confint <- confint(object = regressData$lm, level = 0.9)
    regressData$aov <- aov(regressData$formula)
    regressData$resid <- resid(regressData$lm)
    regressData$fitted <- fitted(regressData$lm)
    regressData$mse <- sum(regressData$resid^2)/(length(regressData$x) - 2)
    
    print(paste("Categorical:", regressData$isFactor))
    
    print("Linear Model:")
    print(summary(regressData$lm))
    
    print("Confidence Interval:")
    print(regressData$confint)
    
    print("Analysis of Variance:")
    print(summary(regressData$aov))
    
    print("Residuals:")
    print(summary(regressData$resid))
    
    print(paste("MSE:", regressData$mse))
    
    # regression line plot plot(x = regressData$x, y = regressData$y, xlab =
    # regressData$variable, ylab = 'KWH') if (!regressData$isFactor) {
    # abline(regressData$lm, col = 'blue') }
    
    # residual and normal probability plots plot(x = regressData$fitted, y =
    # regressData$resid, xlab = 'Fitted Values', ylab = 'Residuals')
    # qqnorm(regressData$resid) qqline(regressData$resid)
    
    if (!is.null(regressData$rsquared)) {
        # add to ranking of r-squared values
        correlationRanking <- rbind(correlationRanking, data.frame(name = variable, 
            rsquared = regressData$rsquared, lambda = regressData$lambda, isFactor = regressData$isFactor))
        correlationRanking <- correlationRanking[order(correlationRanking$rsquared, 
            decreasing = TRUE), ]
    }
}

print("Correlation Between Explanatory Variables and Response:")
print(correlationRanking)  # print ranking of most correlated variables

