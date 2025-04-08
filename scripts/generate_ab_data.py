import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 1000

# Base conversion rates
p_A = 0.12
p_B = 0.14

def simulate_group(name, p_conv):
    converted = np.random.binomial(1, p_conv, size=n_users)
    session_duration = np.random.normal(loc=120 if name == 'A' else 135, scale=30, size=n_users).clip(10)
    pages_viewed = np.random.poisson(3 if name == 'A' else 4, size=n_users).clip(1)
    device_type = np.random.choice(['mobile', 'desktop', 'tablet'], size=n_users, p=[0.6, 0.3, 0.1])
    revenue = converted * np.round(np.random.normal(loc=35, scale=10, size=n_users).clip(5, 100), 2)

    return pd.DataFrame({
        "user_id": np.arange(1, n_users + 1) + (0 if name == 'A' else n_users),
        "group": name,
        "converted": converted,
        "session_duration": session_duration.astype(int),
        "pages_viewed": pages_viewed,
        "device_type": device_type,
        "revenue": revenue
    })

# Create both groups
group_A = simulate_group("A", p_A)
group_B = simulate_group("B", p_B)

ab_data = pd.concat([group_A, group_B])
ab_data.to_csv("data/ab_test_data.csv", index=False)

print("✅ Advanced synthetic A/B test data saved to data/ab_test_data.csv")
