from IPython.display import Math, Markdown, display

class Part1:
    def __init__(self):
        pass
    def introductionGaussian(self):
        return [
            Markdown("### **Definition**"),
            Markdown("A random variable \( X \) is said to follow a Gaussian distribution if its probability density function (PDF) is given by:"),
            Math(r"f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}"),
            Markdown("where:"),
            Math(r"- \mu \text{ is the mean (location parameter),}"),
            Math(r"- \sigma^2 \text{ is the variance (scale parameter).}"),

            Markdown("### **Properties**"),
            Markdown("Gaussian distributions have several key properties:"),
            Markdown("- **Symmetry:** The distribution is symmetric around the mean."),
            Markdown("- **68-95-99.7 Rule:** Approximately 68% of the data falls within one standard deviation from the mean, 95% within two standard deviations, and 99.7% within three standard deviations."),
            Markdown("- **Additivity:** The sum of independent Gaussian random variables is also Gaussian."),

            Markdown("### **Applications**"),
            Markdown("Gaussian distributions are used in various fields, including:"),
            Markdown("- **Statistics:** For hypothesis testing and confidence intervals."),
            Markdown("- **Natural and Social Sciences:** To model phenomena such as measurement errors, heights, and test scores."),
            Markdown("- **Machine Learning:** In algorithms like Gaussian Naive Bayes and Gaussian Processes."),
        ]

    def additionPropertyGaussian(self):
        return [
            Markdown("The sum of two independent Gaussian random variables is also Gaussian."),
            Math(r"X_1 \sim N(\mu_1, \sigma_1^2) \quad \text{and} \quad X_2 \sim N(\mu_2, \sigma_2^2)"),
            Math(r"Y = X_1 + X_2 \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)"),
            Markdown("This property highlights the stability of the Gaussian distribution under addition.")
        ]

    def scalingPropertyGaussian(self):
        return [
            Markdown("If a Gaussian random variable is multiplied by a constant, the result is still Gaussian."),
            Math(r"X \sim N(\mu, \sigma^2) \implies cX \sim N(c\mu, c^2\sigma^2) \quad \text{for any constant } c"),
            Markdown("This demonstrates how Gaussian distributions retain their shape under scaling transformations.")
        ]

    def meanVariancePropertyGaussian(self):
        return [
            Math(r"$\displaystyle For \ a \ Gaussian \ random \ variable \ X \sim N(\mu, \sigma^2):$"),
            Math(r"E[X] = \mu"),
            Math(r"\text{Var}(X) = \sigma^2"),
            Markdown("This property allows for estimation and understanding of the distribution based on its mean and variance.")
        ]

class Part2:
    def __init__(self):
        pass

    def create_scatter_plot(self):
        return [
            Markdown("In this section, we generate and visualize a scatter plot of 2-dimensional Gaussian data."),
            Markdown("#### **Generating 2D Gaussian Data**"),
            Markdown("We use NumPy to generate random samples from a 2D Gaussian distribution with a specified mean and covariance matrix."),
            Math(r"X \sim N(\mu, \Sigma) \text{ where } \mu = [5, 5], \Sigma = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}"),
            Markdown("#### **Scatter Plot**"),
            Markdown("The scatter plot displays the generated data points, providing a visual representation of the Gaussian distribution.")
        ]

    def fit_gaussian_check_covariance(self):
        return [
            Markdown("In this section, we fit a Gaussian Mixture Model to the generated data and extract the fitted mean and covariance matrix."),
            Markdown("#### **Fitting a Gaussian Mixture Model**"),
            Markdown("We use the `GaussianMixture` class from scikit-learn to fit a Gaussian to our data."),
            Math(r"gmm = GaussianMixture(n\_components=1)"),
            Markdown("#### **Extracting Fitted Parameters**"),
            Markdown("We retrieve the fitted mean and covariance matrix from the model to analyze how well the Gaussian fits the data.")
        ]

    def visualize_3d_plot(self):
        return [
            Markdown("In this section, we visualize the frequency distribution of the data in a 3D plot and overlay a 2D Gaussian fit surface."),
            Markdown("#### **Creating a 3D Frequency Distribution Plot**"),
            Markdown("We construct a 3D histogram to show the density of data points in 2D space."),
            Markdown("#### **Plotting the 2D Gaussian Fit Surface**"),
            Markdown("Using the fitted parameters, we compute the Gaussian function values over a grid and plot the fit surface.")
        ]

    def compute_sample_mean_covariance(self):
        return [
            Markdown("In this section, we calculate the sample mean and covariance matrix from the generated data."),
            Markdown("#### **Sample Mean Calculation**"),
            Markdown("The sample mean provides an estimate of the center of the data distribution."),
            Math(r"E[X] = \frac{1}{N} \sum_{i=1}^{N} x_i"),
            Markdown("#### **Sample Covariance Calculation**"),
            Markdown("The sample covariance matrix describes the spread of the data points around the mean."),
            Math(r"\text{Cov}(X) = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - E[X])(x_i - E[X])^T")
        ]

    def check_mahalanobis_distance(self):
        return [
            Markdown("In this section, we compute the Mahalanobis distance for specified test points."),
            Markdown("#### **Generating Test Points**"),
            Markdown("We create several test points to evaluate their distance from the fitted Gaussian mean."),
            Markdown("#### **Mahalanobis Distance Calculation**"),
            Markdown("The Mahalanobis distance measures how many standard deviations away a point is from the mean of the distribution."),
            Math(r"D_M(x) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}")
        ]

class Part3:
    def __init__(self):
        pass

    def distribution_generation(self):
        return [
            Markdown("In this section, we will generate three different distributions (Gaussian, Laplace, and Uniform) that have the same mean and variance."),
            Math(r"Mean (\mu) = 0, Variance (\sigma^2) = 1"),
            Markdown("We will generate 10,000 samples for each distribution.")
        ]

    def compute_entropy(self):
        return [
            Markdown("Entropy is a measure of the uncertainty in a probability distribution. We will compute the entropy for the Gaussian, Laplace, and Uniform distributions generated earlier."),
            Markdown("The entropy \( H \) can be computed from the histogram of the distributions."),
            Math(r"H(X) = -\sum_{i=1}^{n} p(x_i) \log p(x_i)"),
        ]

    def entropy_visualization(self):
        return [
            Markdown("We will visualize the Gaussian, Laplace, and Uniform distributions along with their probability density functions (PDFs) to compare them."),
            Markdown("This will help us understand how different distributions can have the same mean and variance but behave differently."),
        ]

class Part4:
    def __init__(self):
        pass

    def generate_datasets(self):
        return [
            Markdown("In this section, we will generate various datasets, including:"),
            Markdown("- **Thin-tailed distribution:**"),
            Markdown("  - **Normal Distribution:**"),
            Math("X \\sim \\mathcal{N}(\\mu, \\sigma^2) \\text{ with } \\mu = 0 \\text{ and } \\sigma = 1."),
            Markdown("- **Thick-tailed distribution:**"),
            Markdown("  - **t-Distribution:**"),
            Math("X \\sim t_{df=3} \\text{ where degrees of freedom (} df \\text{) affect tail thickness.}"),
            Markdown("- **Categorical data:**"),
            Markdown("  - Random counts across categories \( C = \\{A, B, C, D\\} \)."),
            Markdown("Understanding these distributions helps in identifying data characteristics and patterns.")
        ]

    def box_plots(self):
        return [
            Markdown("- **Purpose:** Visualize median, quartiles, and outliers."),
            Markdown("- **Five-number summary:**"),
            Math(" \\text{Minimum: } \\text{min}(X) "),
            Math(" \\text{First Quartile: } Q_1 = \\text{median}(X \\leq Q_1) "),
            Math(" \\text{Median: } \\text{median}(X) "),
            Math(" \\text{Third Quartile: } Q_3 = \\text{median}(X \\geq Q_3) "),
            Math(" \\text{Maximum: } \\text{max}(X) "),
            Markdown("- **Outliers:** Points outside:"),
            Math(" x < Q_1 - 1.5 \\times \\text{IQR} \\quad \\text{or} \\quad x > Q_3 + 1.5 \\times \\text{IQR},"),
            Markdown("where \( \\text{IQR} = Q_3 - Q_1 \)."),
            Markdown("Box plots are crucial for comparative analysis of thin-tailed and thick-tailed datasets.")
        ]

    def frequency_plots(self):
        return [
            Markdown("- **Histograms:** Show frequency of data within specified bins:"),
            Math("\\text{hist}(X_i) = \\sum_{j=1}^{N} I(X_j \\in [x_i, x_{i+1}))"),
            Markdown("- **KDE (Kernel Density Estimate):** Smooth representation of the distribution:"),
            Math("\\hat{f}(x) = \\frac{1}{N h} \\sum_{i=1}^{N} K\\left(\\frac{x - X_i}{h}\\right)"),
            Markdown("where \(K\) is the kernel function and \(h\) is the bandwidth."),
            Markdown("Key insights:"),
            Markdown("- **Thin-tailed:** Sharp peak around the mean."),
            Markdown("- **Thick-tailed:** Flatter peak, indicating more spread and potential outliers.")
        ]

    def bar_charts(self):
        return [
            Markdown("- **Purpose:** Compare different categories visually."),
            Markdown("- **Representation:** Each bar's height corresponds to the count of occurrences."),
            Markdown("- **Mean Value Calculation:**"),
            Math("\\bar{y} = \\frac{1}{n} \\sum_{i=1}^{n} y_i"),
            Markdown("where \(y_i\) is the value for category \(i\)."),
            Markdown("Useful for identifying trends and patterns across categories.")
        ]

    def outlier_identification(self):
        return [
            Markdown("- **Outliers:** Values significantly different from others, defined as:"),
            Markdown("  - For box plots: Any value \(x\) where:"),
            Math("x < Q_1 - 1.5 \\times \\text{IQR} \\quad \\text{or} \\quad x > Q_3 + 1.5 \\times \\text{IQR}"),
            Markdown("- **Impact:** Can skew results in statistical analysis."),
            Markdown("Detection methods:"),
            Markdown("- **Box plots:** Mark points outside whiskers."),
            Markdown("- **Histograms:** Show extreme values affecting distribution.")
        ]

    def unnormalized_data(self):
        return [
            Markdown("- **Purpose:** Demonstrate the effects of unnormalized data on visualizations."),
            Markdown("- **Exponential Distribution:**"),
            Math("X \\sim \\text{Exponential}(\\lambda)"),
            Markdown("where \(\\lambda\) is the rate parameter."),
            Markdown("- **Visualization Impact:** Skewness and long tails can distort the interpretation of central tendency and dispersion."),
            Markdown("Understanding these concepts is crucial for accurate data representation.")
        ]

part1 = Part1()
part2 = Part2()
part3 = Part3()
part4 = Part4()
tutorials = {
    1: part1.introductionGaussian(),
    1.1: part1.additionPropertyGaussian(),
    1.2: part1.scalingPropertyGaussian(),
    1.3: part1.meanVariancePropertyGaussian(),
    2.1: part2.create_scatter_plot(),
    2.2: part2.fit_gaussian_check_covariance(),
    2.3: part2.visualize_3d_plot(),
    2.4: part2.compute_sample_mean_covariance(),
    2.5: part2.check_mahalanobis_distance(),
    3.1: part3.distribution_generation(),
    3.2: part3.compute_entropy(),
    3.3: part3.entropy_visualization(),
    4.1: part4.generate_datasets(),
    4.2: part4.box_plots(),
    4.3: part4.frequency_plots(),
    4.4: part4.bar_charts(),
    4.5: part4.outlier_identification(),
    4.6: part4.unnormalized_data(),
}

def showDisplay(section):
    for item in tutorials[section]:
        display(item)