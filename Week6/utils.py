from IPython.display import Math, Markdown, display

class Part1:
    def __init__(self):
        pass

    def task1_1(self):
        return [
            Markdown("### 1.a: Generate Descriptive Plots"),
            Markdown("In this task, we generate various descriptive plots such as histograms, bar charts, box plots, violin plots, and contour plots to compare the distributions of two or more attributes in a dataset. These visualizations help in understanding the underlying distribution of data points."),
            Markdown("#### Contour Plots:"),
            Markdown("Contour plots represent the probability density function of a distribution. Each contour line indicates points with equal density. A dense area of contour lines suggests higher probability density, while sparse areas indicate lower density. The mathematical representation of a contour plot for a bivariate Gaussian distribution is given by:"),
            Math(r"f(x, y) = \frac{1}{2\pi \sigma_x \sigma_y \sqrt{1 - \rho^2}} \exp\left(-\frac{1}{2(1 - \rho^2)}\left(\frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2} - \frac{2\rho(x - \mu_x)(y - \mu_y)}{\sigma_x\sigma_y}\right)\right)"),
            Math(r'\text{where } \mu \text{ is the mean, } \sigma \text{ is the standard deviation, and } \rho \text{ is the correlation coefficient between the variables.}')
        ]

    def task1_2(self):
        return [
            Markdown("### 1.b: Interpretation of Charts"),
            Markdown("This task emphasizes the importance of interpreting the generated plots. For example, in contour plots, the spacing of contour lines can indicate the concentration of data points. Dense lines suggest areas of high density, while sparse lines indicate low density."),
            Markdown("#### Reasoning:"),
            Markdown("Interpreting charts requires an understanding of the relationship between the visual representation and the underlying data. In contour plots, the contours represent levels of probability density. If contour lines are closely spaced, it indicates that data points cluster in that area, leading to higher probability density. Conversely, widely spaced contour lines indicate lower density.")
        ]

    def task1_3(self):
        return [
            Markdown("### 1.c: Experimenting with Violin/KDE Plots"),
            Markdown("In this task, we explore Kernel Density Estimation (KDE) and violin plots. Students can experiment with multiple kernels to see how different kernel functions affect the shape of the distribution."),
            Markdown("#### KDE Mathematical Foundation:"),
            Math(r'\text{KDE estimates the probability density function of a random variable. The KDE for a sample of data points } x_1, x_2, \ldots, x_n \text{ can be represented as:}'),            Math(r"\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)"),
            Math(r'\text{where } K \text{ is the kernel function (e.g., Gaussian), } h \text{ is the bandwidth, and } n \text{ is the number of data points.}'),
            Markdown("Violin plots combine KDE with box plots to visualize the distribution while showing summary statistics like median and interquartile ranges.")
        ]

    def task1_4(self):
        return [
            Markdown("### 1.d: Contour Plots for Gaussian Distribution"),
            Markdown("Contour plots for a Gaussian distribution cover points that share the same Mahalanobis distance from the mean. The Mahalanobis distance is defined as:"),
            Math(r"D_M(x) = \sqrt{(x - \mu)^T S^{-1} (x - \mu)}"),
            Markdown("#### Proof:"),
            Markdown("The Mahalanobis distance measures the distance between a point and the mean of a distribution, normalized by the covariance. For a Gaussian distribution, contours of equal density correspond to constant Mahalanobis distances, as shown by the level curves of the bivariate Gaussian probability density function."),
            Math(r"f(x) = \frac{1}{\sqrt{(2\pi)^k |S|}} \exp\left(-\frac{1}{2} D_M(x)^2\right)"),
            Markdown("The contours where \( f(x) \) is constant represent points with equal Mahalanobis distance from the mean, forming ellipsoidal shapes.")
        ]

    def task1_5(self):
        return [
            Markdown("### 1.e: Zero-mean Transformation and Its Importance"),
            Markdown("Zero-mean transformation involves centering the data by subtracting the mean, ensuring that variance calculations are not biased by the mean. This is crucial for accurate interpretations of directional variance and covariance."),
            Markdown("#### Mathematical Reasoning:"),
            Markdown("The zero-mean transformation can be represented as:"),
            Math(r"X' = X - \bar{x}"),
            Markdown("where \(X'\) is the centered data and \(\bar{x}\) is the mean vector. The variance of the zero-mean data can be calculated as:"),
            Math(r"\text{Var}(X') = \frac{1}{n-1} \sum_{i=1}^{n} (X'_i - \bar{X'})^2"),
            Math(r'\text{where } \bar{X} = 0. \text{ This emphasizes that zero-mean transformation simplifies variance calculations and clarifies the analysis of data spread.}')
        ]

class Part2:
    def __init__(self):
        pass

    def task2_1(self):
        return [
            Markdown("### 2.a: Compute Directional Variance"),
            Markdown("In this task, we compute the directional variance of a dataset along a specified direction vector. The directional variance is calculated using the formula:"),
            Math(r"V(v) = v^T \left( \sum_{i} x_i x_i^T \right) v"),
            Markdown("#### Derivation:"),
            Markdown("The directional variance quantifies how much variance exists in the direction of \(v\). It can also be expressed using the covariance matrix \(S\):"),
            Math(r"V(v) = v^T S v"),
            Math(r'\text{where } S = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(x_i - \bar{x})^T. \text{ This representation emphasizes that directional variance is a quadratic form of the covariance matrix.}')
        ]

    def task2_2(self):
        return [
            Markdown("### 2.b: Generating a 2D Gaussian Scatter Plot"),
            Markdown("Here, we generate a 2D Gaussian scatter plot to visualize the data distribution. The scatter plot highlights the spread of data points, which can be influenced by the covariance structure of the underlying Gaussian distribution."),
            Markdown("#### Mathematical Representation:"),
            Markdown("A 2D Gaussian distribution is defined as:"),
            Math(r"f(x, y) = \frac{1}{2\pi \sigma_x \sigma_y} \exp\left(-\frac{1}{2}\left(\frac{(x - \mu_x)^2}{\sigma_x^2} + \frac{(y - \mu_y)^2}{\sigma_y^2}\right)\right)"),
            Math(r'\text{This shows that the spread of points in the scatter plot is influenced by the standard deviations } \sigma_x \text{ and } \sigma_y \text{ in the } x \text{ and } y \text{ directions.}')        ]

    def task2_3(self):
        return [
            Markdown("### 2.c: Directional Variance Along Multiple Directions"),
            Markdown("In this task, we calculate the directional variance along multiple directions. By comparing the calculated variances to the plot of the dataset, students can observe if the directions of maximum and minimum variance match the observed spread of the data."),
            Markdown("#### Reasoning:"),
            Markdown("The directions with the highest and lowest variance correspond to the eigenvectors of the covariance matrix, and their associated eigenvalues represent the amount of variance captured. This relationship can be expressed as:"),
            Math(r"S v = \lambda v"),
            Math(r'\text{where } S \text{ is the covariance matrix, } v \text{ is the eigenvector, and } \lambda \text{ is the eigenvalue.}')
        ]

    def task2_4(self):
        return [
            Markdown("### 2.d: Interpretation of Results in Terms of Covariance Matrix"),
            Markdown("The covariance matrix summarizes the relationships between different dimensions of the dataset and is defined as:"),
            Math(r"S = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(x_i - \bar{x})^T"),
            Markdown("where \(\bar{x}\) is the mean of the data points. The eigenvalues of the covariance matrix correspond to the variance captured along the principal components, providing insights into data spread and correlation."),
            Markdown("#### Principal Component Analysis (PCA):"),
            Markdown("PCA utilizes the covariance matrix to identify principal components. The principal components are the eigenvectors of the covariance matrix associated with the largest eigenvalues. This method reduces the dimensionality of the data while preserving variance.")
        ]

part1 = Part1()
part2 = Part2()

tutorials = {
    1.1: part1.task1_1(),
    1.2: part1.task1_2(),
    1.3: part1.task1_3(),
    1.4: part1.task1_4(),
    1.5: part1.task1_5(),
    2.1: part2.task2_1(),
    2.2: part2.task2_2(),
    2.3: part2.task2_3(),
    2.4: part2.task2_4(),
}

def showDisplay(section):
    for item in tutorials[section]:
        display(item)
