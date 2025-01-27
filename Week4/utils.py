from IPython.display import Math, Markdown, display

def showDisplay(section):
    tutorials = {
        1: linearity_of_expectations(),
        2: linearity_of_variance(),
        3: markovs_inequality(),
        4: chebyshevs_inequality(),
        5: weak_law_of_large_numbers(),
    }
    for item in tutorials[section]:
        display(item)

def linearity_of_expectations():
    return [
        # Markdown("# **1. Linearity of Expectations**"),
        Markdown("## **1.1 Introduction**"),
        Markdown("Linearity of expectations states that the expectation of the sum of random variables is equal to the sum of their individual expectations:"),
        Math(r"E[X + Y] = E[X] + E[Y]"),
        Markdown("This property holds regardless of whether \( X \) and \( Y \) are independent."),
        Markdown("For multiple random variables, it generalizes as:"),
        Math(r"E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]"),

        Markdown("## **1.2 Basic Derivation and Reasoning**"),
        Markdown("Using the definition of expectation:"),
        Math(r"E[X + Y] = \int_{-\infty}^\infty (x + y) \cdot f_{X+Y}(x, y) \, dx \, dy"),
        Markdown("This can be split into two integrals:"),
        Math(r"E[X + Y] = \int_{-\infty}^\infty x \cdot f_X(x) \, dx + \int_{-\infty}^\infty y \cdot f_Y(y) \, dy"),
        Math(r"E[X + Y] = E[X] + E[Y]"),
        Markdown("This holds because addition is distributive over integration."),

        Markdown("## **1.3 Real-Life Use Cases**"),
        Markdown("1. **Finance:** Expected returns of a portfolio are the sum of expected returns from individual assets."),
        Markdown("2. **Supply Chain Management:** The expected demand for a product across multiple regions is additive."),
        Markdown("3. **Gaming:** Expected scores in a game with multiple rounds are additive across rounds.")
    ]

def linearity_of_variance():
    return [
        # Markdown("# **2. Linearity of Variance (Under Independence)**"),
        Markdown("## **2.1 Introduction**"),
        Markdown("Variance measures the spread of a random variable. For independent random variables, the variance of their sum is the sum of their variances:"),
        Math(r"\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)"),
        Markdown("For multiple independent random variables:"),
        Math(r"\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)"),

        Markdown("## **2.2 Basic Derivation and Reasoning**"),
        Markdown("From the definition of variance:"),
        Math(r"\text{Var}[X + Y] = E[(X + Y)^2] - (E[X + Y])^2"),
        Markdown("Expanding \( (X + Y)^2 \):"),
        Math(r"E[(X + Y)^2] = E[X^2] + E[Y^2] + 2E[XY]"),
        Markdown("For independent \( X \) and \( Y \), \( E[XY] = E[X]E[Y] \), so:"),
        Math(r"\text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y]"),

        Markdown("## **2.3 Real-Life Use Cases**"),
        Markdown("1. **Insurance:** Risk assessment by summing individual claim variances."),
        Markdown("2. **Investment:** Combining variances of independent stock returns to calculate portfolio risk."),
        Markdown("3. **Manufacturing:** Variance in dimensions of products assembled from independent components.")
    ]

def markovs_inequality():
    return [
        # Markdown("# **3. Markov's Inequality**"),
        Markdown("## **3.1 Introduction**"),
        Markdown("Markov's inequality provides an upper bound on the probability that a non-negative random variable exceeds a certain value:"),
        Math(r"P(X \geq a) \leq \frac{E[X]}{a}, \quad a > 0"),

        Markdown("## **3.2 Basic Derivation and Reasoning**"),
        Markdown("From the definition of expectation:"),
        Math(r"E[X] = \int_0^\infty x \cdot f_X(x) \, dx"),
        Math(r"\text{Split the integral into two parts, } [0, a] \text{ and } [a, \infty]:"),
        Math(r"E[X] \geq a \cdot P(X \geq a)"),
        Markdown("Rearranging gives:"),
        Math(r"P(X \geq a) \leq \frac{E[X]}{a}"),

        Markdown("## **3.3 Real-Life Use Cases**"),
        Markdown("1. **Queuing Theory:** Bounding waiting times in service systems."),
        Markdown("2. **Network Traffic:** Estimating probability of high data loads."),
        Markdown("3. **Project Management:** Bounding budget or schedule overruns.")
    ]

def chebyshevs_inequality():
    return [
        # Markdown("# **4. Chebyshev's Inequality**"),
        Markdown("## **4.1 Introduction**"),
        Markdown("Chebyshev's inequality provides a bound on the probability that a random variable deviates from its mean by more than \( k \) standard deviations:"),
        Math(r"P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad k > 0"),
        Markdown("This inequality applies to any random variable with finite variance, regardless of its distribution."),

        Markdown("## **4.2 Basic Derivation and Reasoning**"),
        Markdown("From Markov's inequality:"),
        Math(r"P(|X - \mu| \geq k\sigma) = P((X - \mu)^2 \geq k^2\sigma^2)"),
        Math(r"\leq \frac{E[(X - \mu)^2]}{k^2\sigma^2}"),
        Math(r"\text{Since } E[(X - \mu)^2] = \sigma^2, \text{ this simplifies to:}"),
        Math(r"P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}"),

        Markdown("## **4.3 Real-Life Use Cases**"),
        Markdown("1. **Quality Control:** Ensuring products meet tolerance limits by bounding probabilities of extreme deviations."),
        Markdown("2. **Weather Prediction:** Estimating probabilities of extreme temperature deviations."),
        Markdown("3. **Risk Management:** Bounding the probability of significant financial losses in markets.")
    ]

def weak_law_of_large_numbers():
    return [
        # Markdown("# **5. Weak Law of Large Numbers (WLLN)**"),
        Markdown("## **5.1 Introduction**"),
        Markdown("The Weak Law of Large Numbers (WLLN) states that the sample average of independent, identically distributed (i.i.d.) random variables converges in probability to the population mean as the sample size grows:"),
        Math(r"P(|\bar{X}_n - \mu| \geq \epsilon) \to 0 \quad \text{as } n \to \infty, \quad \epsilon > 0"),
        Markdown("This is a foundational result in probability and statistics, ensuring the reliability of sample means."),

        Markdown("## **5.2 Basic Derivation and Reasoning**"),
        Markdown("From Chebyshev's inequality:"),
        Math(r"P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\text{Var}(\bar{X}_n)}{\epsilon^2}"),
        Math(r"\text{The variance of the sample mean } \bar{X}_n \text{ is given by:}"),
        Math(r"\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}"),
        Markdown("Substituting this into Chebyshev's inequality:"),
        Math(r"P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\sigma^2}{n\epsilon^2}"),
        Math(r"\text{As } n \to \infty, \, P(|\bar{X}_n - \mu| \geq \epsilon) \to 0."),

        Markdown("## **5.3 Real-Life Use Cases**"),
        Markdown("1. **Polls and Surveys:** Ensures sample means approximate population means in large surveys."),
        Markdown("2. **Manufacturing:** Averages of large production runs stabilize, reducing variability."),
        Markdown("3. **Gambling:** Explains how casinos profit due to the law of averages.")
    ]