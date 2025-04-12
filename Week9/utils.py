from IPython.display import Math, display

class BinomialEstimationAnalysis:
    def __init__(self):
        pass

    def section_1_1(self):
        return [
            Math(r"\displaystyle \textbf{1.1\quad Problem\ Setup\ and\ Estimators}"),
            Math(r"\text{We model the number of heads } m \text{ in } n \text{ independent tosses of a biased coin as:}"),
            Math(r"m \sim \text{Binomial}(n, p)"),
            Math(r"\text{Here, } p \text{ is the true (unknown) probability of heads.}"),
            Math(r"\hat{p} = \frac{m}{n} \quad \text{(Maximum Likelihood Estimator)}"),
            Math(r"\tilde{p} = \frac{m + 1}{n + 2} \quad \text{(Smoothed Estimator with pseudocounts)}"),
            Math(r"\text{The smoothed estimator adds 1 artificial head and 1 tail, often used in Bayesian contexts.}")
        ]

    def section_1_2(self):
        return [
            Math(r"\displaystyle \mathbf{1.2\quad \text{Unbiasedness of }} \hat{p}"),
            Math(r"\text{We compute the expectation of } \hat{p} = \frac{m}{n}."),
            Math(r"m \sim \text{Binomial}(n, p) \Rightarrow \mathbb{E}[m] = np"),
            Math(r"\Rightarrow \mathbb{E}[\hat{p}] = \mathbb{E}\left[\frac{m}{n}\right] = \frac{\mathbb{E}[m]}{n} = \frac{np}{n} = p"),
            Math(r"\boxed{\hat{p} \text{ is an unbiased estimator of } p}")
        ]

    def section_1_3(self):
        return [
            Math(r"\displaystyle \mathbf{1.3\quad \text{MSE of }} \hat{p}"),
            Math(r"\text{MSE}[\hat{p}] = \text{Var}(\hat{p}) + (\mathbb{E}[\hat{p}] - p)^2"),
            Math(r"\text{Since } \hat{p} \text{ is unbiased, bias} = 0 \Rightarrow \text{MSE}[\hat{p}] = \text{Var}(\hat{p})"),
            Math(r"\text{Var}(\hat{p}) = \text{Var}\left(\frac{m}{n}\right) = \frac{1}{n^2} \text{Var}(m)"),
            Math(r"\text{Var}(m) = np(1 - p) \Rightarrow \text{Var}(\hat{p}) = \frac{p(1 - p)}{n}"),
            Math(r"\boxed{\text{MSE}[\hat{p}] = \frac{p(1 - p)}{n}}")
        ]

    def section_1_4(self):
        return [
            Math(r"\displaystyle \mathbf{1.4\quad \text{Expectation and MSE of }} \tilde{p} = \frac{m + 1}{n + 2}"),
            Math(r"\text{We analyze the smoothed estimator } \tilde{p} = \frac{m + 1}{n + 2}."),
            Math(r"\mathbb{E}[\tilde{p}] = \mathbb{E}\left[\frac{m + 1}{n + 2}\right] = \frac{\mathbb{E}[m] + 1}{n + 2} = \frac{np + 1}{n + 2}"),
            Math(r"\Rightarrow \boxed{\mathbb{E}[\tilde{p}] = \frac{np + 1}{n + 2}}"),
            Math(r"\text{This is a biased estimator of } p."),
            Math(r"\text{Variance: } \text{Var}(\tilde{p}) = \left(\frac{1}{n + 2}\right)^2 \text{Var}(m) = \frac{np(1 - p)}{(n + 2)^2}"),
            Math(r"\text{Bias} = \mathbb{E}[\tilde{p}] - p = \frac{np + 1}{n + 2} - p = \frac{1 - 2p}{n + 2}"),
            Math(r"\text{Bias}^2 = \left(\frac{1 - 2p}{n + 2}\right)^2 = \frac{(1 - 2p)^2}{(n + 2)^2}"),
            Math(r"\text{MSE}[\tilde{p}] = \text{Var}(\tilde{p}) + \text{Bias}^2(\tilde{p})"),
            Math(r"\boxed{\text{MSE}[\tilde{p}] = \frac{np(1 - p) + (1 - 2p)^2}{(n + 2)^2}}")
        ]

    def section_1_5(self):
        return [
            Math(r"\displaystyle \textbf{1.5\quad Deriving\ the\ Maximum\ Likelihood\ Estimator}"),
            Math(r"\text{Likelihood: } L(p) = \binom{n}{m} p^m (1 - p)^{n - m}"),
            Math(r"\text{Log-likelihood: } \log L(p) = \log \binom{n}{m} + m \log p + (n - m) \log(1 - p)"),
            Math(r"\text{Differentiate and set to zero: } \frac{d}{dp} \log L(p) = \frac{m}{p} - \frac{n - m}{1 - p} = 0"),
            Math(r"\Rightarrow m(1 - p) = (n - m)p \Rightarrow m - mp = np - mp \Rightarrow m = np"),
            Math(r"\boxed{\hat{p}_{\text{MLE}} = \frac{m}{n}}")
        ]


# Create instance
analysis = BinomialEstimationAnalysis()

# Organize sections
tutorials = {
    1.1: analysis.section_1_1(),
    1.2: analysis.section_1_2(),
    1.3: analysis.section_1_3(),
    1.4: analysis.section_1_4(),
    1.5: analysis.section_1_5()
}

# Display function
def showDisplay(section):
    for item in tutorials[section]:
        display(item)