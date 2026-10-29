import pandas as pd
import numpy as np

data = {
    'passengerid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'survived': [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    'pclass': [3, 1, 3, 1, 3, 3, 1, 3, 2, 3],
    'sex': ['male', 'FEMALE', 'Female', 'FEMALE', 'inae', None, 'F', 'MALE', 'feamle', 'male@'],
    'age': ['22 years', '38', 'twenty-six', 'None', '35 yrs.', '-28', 'N/A', '19.5 years', 'twenty seven', '30 years old'],
    'fare': ['7.25', '71.28 Rs', '7.92', 'Rs 53.10', 'EIGHT RUPEE AND 5 PAISE', '8.46', '51.86', 'None', 'THIREE RUPEE', '28.05/-']
}

df = pd.DataFrame(data)

def clean_sex(val):
    if pd.isna(val):
        return np.nan
    val_str = str(val).lower()
    if 'female' in val_str or val_str == 'f' or val_str == 'feamle':
        return 'female'
    elif 'male' in val_str or val_str == 'm' or val_str == 'male@':
        return 'male'
    return np.nan


def clean_age(val):
    if pd.isna(val) or str(val).upper() in ['NONE', 'N/A']:
        return np.nan
    val_str = str(val).lower().replace('yrs.', '').replace('years', '').replace('old', '').strip()
    word_to_num = {'twenty-six': 26, 'twenty seven': 27}
    if val_str in word_to_num:
        return float(word_to_num[val_str])
    try:
        num = float(val_str)
        return abs(num)  # Handle negative age (-28 -> 28)
    except:
        return np.nan


def clean_fare(val):
    if pd.isna(val) or str(val).upper() in ['NONE', 'N/A']:
        return np.nan
    val_str = str(val).upper().replace('RS', '').replace('/-', '').strip()
    word_to_num = {
        'EIGHT RUPEE AND 5 PAISE': 8.05,
        'THIREE RUPEE': 3.0
    }
    if val_str in word_to_num:
        return float(word_to_num[val_str])
    try:
        clean_str = ''.join(c for c in val_str if c.isdigit() or c == '.')
        return float(clean_str) if clean_str else np.nan
    except:
        return np.nan

df['sex'] = df['sex'].apply(clean_sex)
df['age'] = df['age'].apply(clean_age)
df['fare'] = df['fare'].apply(clean_fare)

# Impute remaining NaNs with median/mode
df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].median())
df['sex'] = df['sex'].fillna(df['sex'].mode()[0])
# Save the cleaned dataframe to a CSV file
df.to_csv('cleaned_titanic.csv', index=False)
print(df)