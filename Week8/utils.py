# from IPython.display import Math, display

# class Part1:
#     def __init__(self):
#         pass

#     def part1_theory(self):
#         return [
#             Math(r"\huge \textbf{1. Theoretical Foundation}"),

#             Math(r"\Large \textbf{1.1 The Binomial Distribution}"),
#             Math(r"\text{The binomial distribution models the number of successes in } n \text{ independent Bernoulli trials, where each trial has success probability } p."),
#             Math(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad k = 0,1,2,\dots,n"),

#             Math(r"\Large \textbf{Properties:}"),
#             Math(r"\mathbb{E}[X] = np, \quad \text{Var}(X) = np(1 - p)"),
#             Math(r"\text{As } n \text{ increases, the binomial distribution approximates a Gaussian:}"),
#             Math(r"\lim_{n \to \infty} \frac{X - np}{\sqrt{np(1 - p)}} = \mathcal{N}(0,1)"),

#             Math(r"\Large \textbf{1.2 The Multinomial Distribution}"),
#             Math(r"\text{The multinomial distribution generalizes the binomial to more than two outcomes.}"),
#             Math(r"P(X_1 = x_1, ..., X_k = x_k) = \frac{n!}{x_1! x_2! ... x_k!} p_1^{x_1} p_2^{x_2} ... p_k^{x_k}"),
#             Math(r"\sum_{i=1}^{k} x_i = n, \quad \text{For large } n, \text{ the multinomial distribution approximates a multivariate normal distribution.}"),

#             Math(r"\Large \textbf{1.3 Kullback-Leibler (KL) Divergence}"),
#             Math(r"\text{KL divergence quantifies the loss of information when approximating one distribution with another:}"),
#             Math(r"D_{\text{KL}}(P \| Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}"),
#             Math(r"\text{For this case, we measure the divergence between binomial and Gaussian:}"),
#             Math(r"D_{\text{KL}}(B(n, p) \| \mathcal{N}(np, np(1-p)))"),
#         ]

#     def part2_code_explanation(self):
#         return [
#             Math(r"\huge \textbf{2. Python Implementation}"),
#             Math(r"\Large \textbf{2.1 Generating and Plotting the Binomial Distribution}"),
#             Math(r"\text{We generate and compare binomial distributions for various values of } n, \text{ overlaying a Gaussian approximation.}"),

#             Math(r"\Large \textbf{2.2 KL Divergence Calculation}"),
#             Math(r"\text{To quantify convergence, we compute the KL divergence between the binomial and normal distributions.}"),

#             Math(r"\Large \textbf{2.3 Observing Convergence for Different } p \text{ Values}"),
#             Math(r"\text{By plotting } D_{\text{KL}} \text{ for various } p, \text{ we see that convergence is faster for } p \approx 0.5 \text{ and slower for extreme values.}")
#         ]

#     def part3_observation(self):
#         return [
#             Math(r"\huge \textbf{3. Observations and Analysis}"),
#             Math(r"\textbf{1. For } p \approx 0.5, \text{ binomial convergence to Gaussian is fast due to symmetry.}"),
#             Math(r"\textbf{2. For extreme values of } p \text{ (e.g., 0.1 or 0.9), the binomial remains skewed for larger } n, \text{ delaying convergence.}"),
#             Math(r"\textbf{3. KL divergence decreases as } n \text{ increases, confirming the Central Limit Theorem.}"),
#         ]

#     def part4_conclusion(self):
#         return [
#             Math(r"\huge \textbf{4. Conclusion}"),
#             Math(r"\text{This tutorial demonstrated how binomial and multinomial distributions converge to a Gaussian and how KL divergence quantifies the difference.}"),
#             Math(r"\textbf{Key Takeaways:}"),
#             Math(r"\bullet \text{ The binomial approaches a normal distribution as } n \to \infty."),
#             Math(r"\bullet \text{ Convergence depends on } p, \text{ being faster for } p \approx 0.5."),
#             Math(r"\bullet \text{ KL divergence provides a quantitative measure of convergence speed.}"),
#         ]

# part1 = Part1()

# tutorials = {
#     1.1: part1.part1_theory(),
#     1.2: part1.part2_code_explanation(),
#     1.3: part1.part3_observation(),
#     1.4: part1.part4_conclusion(),
# }

# def showDisplay(section):
#     for item in tutorials[section]:
#         display(item)

from IPython.display import Math, display

class BinomialMultinomialAnalysis:
    def __init__(self):
        pass

    def theory_section(self):
        return [
            Math(r"\huge \textbf{1. Theoretical Foundation}"),
            Math(r"\Large \textbf{1.1 Binomial Distribution}"),
            Math(r"\text{The binomial distribution models the number of successes in } n \text{ independent trials, each with probability } p."),
            Math(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad k = 0,1,2,\dots,n"),
            Math(r"\mathbb{E}[X] = np, \quad \text{Var}(X) = np(1 - p)"),
            Math(r"\text{As } n \to \infty, \text{ the binomial distribution approximates a normal distribution:}"),
            Math(r"\lim_{n \to \infty} \frac{X - np}{\sqrt{np(1 - p)}} = \mathcal{N}(0,1)"),

            Math(r"\Large \textbf{1.2 Multinomial Distribution}"),
            Math(r"P(X_1 = x_1, ..., X_k = x_k) = \frac{n!}{x_1! x_2! ... x_k!} p_1^{x_1} p_2^{x_2} ... p_k^{x_k}"),
            Math(r"\sum_{i=1}^{k} x_i = n, \quad \text{For large } n, \text{ the multinomial distribution approximates a multivariate normal distribution.}"),

            Math(r"\Large \textbf{1.3 Kullback-Leibler (KL) Divergence}"),
            Math(r"D_{\text{KL}}(P \| Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}"),
        ]

    def implementation_section(self):
        return [
            Math(r"\huge \textbf{2. Python Implementation}"),
            Math(r"\Large \textbf{2.1 Generating and Plotting the Binomial Distribution}"),
            Math(r"\text{We compare binomial distributions for various } n, \text{ overlaying a Gaussian approximation.}"),

            Math(r"\Large \textbf{2.2 KL Divergence Calculation}"),
            Math(r"\text{We compute the KL divergence between binomial and normal distributions.}"),

            Math(r"\Large \textbf{2.3 Convergence for Different } p"),
            Math(r"\text{By plotting } D_{\text{KL}}, \text{ we see that convergence is faster for } p \approx 0.5 \text{ and slower for extreme values.}"),
        ]

    def observation_section(self):
        return [
            Math(r"\huge \textbf{3. Observations and Analysis}"),
            Math(r"\textbf{1. For } p \approx 0.5, \text{ binomial convergence to Gaussian is fast due to symmetry.}"),
            Math(r"\textbf{2. For extreme values of } p \text{ (e.g., 0.1 or 0.9), the binomial remains skewed for larger } n, \text{ delaying convergence.}"),
            Math(r"\textbf{3. KL divergence decreases as } n \text{ increases, confirming the Central Limit Theorem.}"),
        ]

    def conclusion_section(self):
        return [
            Math(r"\huge \textbf{4. Observations and Conclusion}"),
            Math(r"\bullet \text{ For } p \approx 0.5, \text{ binomial convergence to Gaussian is fast due to symmetry.}"),
            Math(r"\bullet \text{ For extreme values of } p \text{ (e.g., 0.1 or 0.9), binomial remains skewed for large } n."),
            Math(r"\bullet \text{ KL divergence decreases as } n \to \infty, \text{ confirming the Central Limit Theorem.}"),
        ]

# Create an instance to display sections
analysis = BinomialMultinomialAnalysis()

tutorials = {
    1.1: analysis.theory_section(),
    1.2: analysis.implementation_section(),
    1.3: analysis.observation_section(),
    1.4: analysis.conclusion_section()
}

def showDisplay(section):
    for item in tutorials[section]:
        display(item)