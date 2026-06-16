import re

def check_quality(df):

    report = {}

    report["Total Rows"] = len(df)

    report["Missing Values"] = df.isnull().sum().to_dict()

    report["Duplicate Rows"] = int(df.duplicated().sum())

    # OUTLIERS
    outliers = 0

    if "salary" in df.columns:
        mean = df["salary"].mean()
        std = df["salary"].std()

        upper = mean + 2 * std
        lower = mean - 2 * std

        outliers = len(df[(df["salary"] > upper) | (df["salary"] < lower)])

    report["Outliers"] = outliers

    # EMAIL VALIDATION
    invalid_emails = 0

    if "email" in df.columns:

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        invalid_emails = len(
            df[
                df["email"].fillna("").apply(
                    lambda x: not bool(re.match(pattern, str(x)))
                )
            ]
        )

    report["Invalid Emails"] = invalid_emails

    return report