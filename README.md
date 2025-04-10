# 🧪 A/B Testing Simulation

This project demonstrates the end-to-end process of designing, simulating, and analyzing A/B tests using real-world-style data and statistical methods.

## 🧠 Features

- Descriptive statistics and visual exploration of A/B test metrics
- Statistical testing using appropriate methods:
  - T-tests, Mann-Whitney U tests, Z-tests, Chi-square tests, Kruskal-Wallis
- Normality checks using Shapiro-Wilk and visualizations (histograms, Q-Q plots)
- Device-type-specific analysis (mobile, desktop, tablet)
- Clear interpretation of results and statistical significance
- Summary tables highlighting results and group performance

## 📁 Structure

- `data/`: Synthetic A/B test data
- `notebooks/`: Step-by-step analysis notebooks
- `scripts/`: Data generation scripts
- `images/`: Plots and charts for documentation

## 🚀 How to Use

1. Install dependencies:

```bash
pip install -r requirements.txt

2. Launch the notebook (in Gitpod or locally):
jupyter notebook
```


## 🔮 Next Steps

Here are some directions to extend this project:

- **Bayesian A/B Testing**  
  Implement Bayesian hypothesis testing to compare posterior distributions of conversion rates and visualize uncertainty more intuitively.

- **Sample Size & Power Simulations**  
  Add simulations to estimate the required sample size for detecting meaningful effects with desired power (e.g., 80%).

- **Uplift Modeling**  
  Go beyond average treatment effects by building models (e.g., decision trees or causal forests) to identify user segments most influenced by the treatment.

- **Real-Time Experimentation**  
  Simulate or build infrastructure to analyze A/B test results in real-time using tools like Kafka, Redis, or dashboards.

- **Segmentation Analysis**  
  Extend device-level analysis to include other user segments (e.g., country, gender, acquisition channel) to uncover interaction effects.

- **Multi-Metric Optimization**  
  Introduce a multi-objective evaluation framework to optimize for several KPIs at once (e.g., revenue + retention + conversion).

- **Multiple Testing Correction**  
  Account for inflated Type I error rates due to repeated or multi-metric testing using Bonferroni, Holm, or FDR correction.

