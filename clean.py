import pandas as pd


def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df3 = pd.merge(df1, df2, left_on='respondent_id', right_on='id').dropna()
    df3 = df3.drop('id', axis=1)
    df3 = df3[~df3['job'].str.contains('insurance|Insurance')]
    return df3


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file1 (CSV)')
    parser.add_argument('input2', help='Data file2 (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    print('The shape of the file:', cleaned.shape)
    cleaned.to_csv(args.output, index=False)
