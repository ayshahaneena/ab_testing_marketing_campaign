# A/B Testing for Marketing Campaign

## Overview

This project analyzes the effectiveness of a marketing campaign through A/B testing. The primary goal is to determine if there are significant differences in conversion rates based on various factors, such as the test group (ads vs. PSA), the day ads were shown, and the hour ads were shown. The analysis is conducted using statistical methods, primarily the Chi-square test.

## Table of Contents

- [Installation](#installation)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/ayshahaneena/ab_testing_marketing_campaign.git
cd ab_testing_marketing_campaign
```

Install the necessary packages by running:

```bash
pip install -r requirements.txt
```


This command will launch the application in your web browser, where you can input your data and see the results of the A/B testing analysis.

## Data Analysis

The analysis involves several key steps:

1. **Data Cleaning and Preprocessing**: Prepare the dataset by handling missing values and ensuring the data is in the correct format for analysis.
2. **Statistical Testing**: Perform Chi-square tests to evaluate whether there are significant differences in conversion rates across various dimensions.
3. **Visualization**: Create visual representations of the data to facilitate understanding and interpretation of the results.

## Results

The Chi-square test results provide insights into whether there are statistically significant differences in conversion rates across:

- User IDs
- Test groups (Ads vs. PSAs)
- Most ads shown by day
- Most ads shown by hour

### Example Output

- "The difference in conversion rates across 'test group' is statistically significant."
- "The difference in conversion rates across 'most ads day' is statistically significant."
- "The difference in conversion rates across 'most ads hour' is statistically significant."

## Technologies Used

- **Programming Language**: Python
- **Data Manipulation**: Pandas
- **Numerical Computation**: NumPy
- **Statistical Analysis**: Scikit-learn
- **Data Visualization**: Matplotlib/Seaborn (if used for visualizations)

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or would like to report an issue, please feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
