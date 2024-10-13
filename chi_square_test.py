import pandas as pd
from scipy.stats import chi2_contingency
import pickle

# Function to perform Chi-square test on each categorical variable
def chi_square_test(df, alpha=0.05):  # alpha is the significance level
    results = []
    cat_cols = df.select_dtypes(include=['object'])  # Select categorical columns

    for variable in cat_cols.columns:
        if variable != 'converted':  # Skip the target column
            contigency_table = pd.crosstab(df[variable], df['converted'])
            chi2, p, _, _ = chi2_contingency(contigency_table)

            if p < alpha:
                result = f'The difference in conversion rates across "{variable}" is statistically significant (p = {p:.4f})'
            else:
                result = f'There is no significant difference in conversion rates across "{variable}" (p = {p:.4f})'

            results.append(result)

    return results

# Perform the test, and save results as pickle
def save_ab_test_results(df, file_path='ab_test_results.pkl'):
    # Perform chi-square test
    test_results = chi_square_test(df)
    
    # Save results to .pkl
    with open(file_path, 'wb') as f:
        pickle.dump(test_results, f)
    print(f"Results saved to {file_path}")

# Example usage
if __name__ == '__main__':
    # Load the dataset (hardcoded path)
    df = pd.read_csv("Data\marketing_AB.csv")
    save_ab_test_results(df)
