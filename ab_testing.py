#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# ### Load Dataset

# In[58]:


df = pd.read_csv("Data/marketing_AB.csv")


# In[59]:


df.head()


# ## Define Objective
# * The Objective is to determine if the marketing ads lead to more conversions compared to showing a PSA.

# ## Formulate Hypothesis
# * Null Hypothesis (H0): The ad does not improve conversion rates compared to the PSA.
# * Alternative Hypothesis (H1): The ad improves conversion rates

# ## Exploratory Data Analysis

# In[60]:


df.shape


# In[61]:


df.info()


# In[62]:


df.duplicated("user id").sum()


# * No duplicated values

# In[63]:


df.isna().sum().sum()


# * No Null Values

# In[64]:


# Drop unwanted columns
df = df.drop(columns = ['Unnamed: 0','user id'],axis=1)


# In[65]:


df.columns


# In[66]:


df.dtypes


# In[67]:


# Convert most ads hour to object
df['most ads hour'] = df['most ads hour'].astype(object)


# In[68]:


# define categorical columns
cat_cols = df[['test group','converted','most ads day','most ads hour']]
for i in cat_cols.columns:
  print(f"{i.upper()} : {cat_cols[i].unique()}")


# In[69]:


variable = 'test group'
plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
sns.countplot(x = df[variable],data=df, palette ='bright')
plt.title(f"count plot '{variable}'")

plt.subplot(1,2,2)
counts = df[variable].value_counts()
plt.pie( counts , labels= counts.index ,colors=['blue','orange'], autopct = "%0.2f%%")
plt.title(f"Pie plot '{variable}'")

plt.tight_layout()
plt.show()


# In[70]:


variable = 'converted'
plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
sns.countplot(x = df[variable],data=df, palette = 'bright')
plt.title(f"count plot '{variable}'")

plt.subplot(1,2,2)
counts = df[variable].value_counts()
plt.pie( counts , labels= counts.index ,colors=['b','orange'], autopct = "%0.2f%%")
plt.title(f"Pie plot '{variable}'")

plt.tight_layout()
plt.show()


# In[71]:


variable = 'most ads day'
plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
sns.countplot(x = df[variable],data=df, palette = 'bright',order=df[variable].value_counts().index)
plt.title(f"count plot- {variable}")
plt.xticks(rotation=90)

plt.subplot(1,2,2)
counts = df[variable].value_counts()
plt.pie( counts , labels= counts.index , autopct = "%0.2f%%")
plt.title(f'Pie plot- {variable}')

plt.tight_layout()
plt.show()


# In[72]:


variable = 'most ads hour'
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.countplot(x = df[variable],data=df, palette = 'bright',order=df[variable].value_counts().index)
plt.title(f"count plot- {variable}")
plt.xticks(rotation=90)

plt.subplot(1,2,2)
counts = df[variable].value_counts()
plt.pie( counts , labels= counts.index , autopct = "%0.2f%%")
plt.title(f'Pie plot- {variable}')

plt.tight_layout()
plt.show()


# In[73]:


df['total ads'].describe()


# In[74]:


pd.crosstab(df['test group'] , df['converted'],normalize = 'index')


# In[75]:


pd.crosstab(df['test group'] , df['converted'],normalize = 'index').plot(kind='bar')


# In[76]:


pd.crosstab(df['most ads day'] , df['converted'],normalize = 'index').plot(kind='bar')


# In[77]:


pd.crosstab(df['most ads hour'] , df['converted'],normalize = 'index').sort_values(by=True ,ascending=True).plot(kind='bar')


# * What is the overall conversion rate in the ad group compared to the PSA group?
# * Are there any patterns that might influence the results (e.g., the day/time people saw the ads)?

# In[78]:


ad_group = df[df['test group'] == 'ad']
psa_group = df[df['test group'] == 'psa']

ad_conversion_rate = ad_group['converted'].mean()
psa_conversion_rate = psa_group['converted'].mean()

print(f"Ad Conversion Rate : {ad_conversion_rate}")
print(f"PSA Conversion Rate : {psa_conversion_rate}")


# In[79]:


sns.barplot(x = ['Ad_group','PSA_group'] , y = [ad_conversion_rate , psa_conversion_rate], palette ='bright')
plt.title("Conversion Rate: Ad vs Psa")
plt.show()


# ## Statistical Test
# Why Conduct Statistical Tests? : Just because the ad group’s conversion rate might look higher doesn’t mean it’s significantly higher. to ensure the observed difference isn’t due to random chance. This is where statistical testing comes in. In this case,i use a Chi-Squared test to check if the difference in conversion rates between the ad and PSA groups is statistically significant.

# In[80]:


from scipy.stats import chi2_contingency
# Function to perform Chi-square test on each categorical variable
def chi_square_test(df, alpha=0.05):  # alpha is the significance level
    results = []
    cat_cols = df.select_dtypes(include=['object'])  # Select categorical columns

    for variable in cat_cols.columns:
        if variable != 'converted':  # Skip the target column
            contigency_table = pd.crosstab(df[variable], df['converted'])
            chi2, p, _, _ = chi2_contingency(contigency_table)

        if p < alpha:
          result = f'The difference in conversion rates across "{variable}" is statistically significant'
        else:
          result = f'There is no significant difference in conversion rates acorss "{variable}"'

        results.append(result)

    return results        
   


# In[81]:


import pickle
def save_ab_test_results(df, file_path='ab_test_results.pkl'):
    # Perform chi-square test
    test_results = chi_square_test(df)
    
    # Save results to .pkl
    with open(file_path, 'wb') as f:
        pickle.dump(test_results, f)
    print(f"Results saved to {file_path}")


# In[82]:


chi_square_test(df)


# In[83]:


save_ab_test_results(df)


# In[ ]:




