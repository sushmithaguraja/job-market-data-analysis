import pandas as pd

def load_data(path="data/job_market_skills_dataset.csv"):
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Rename columns for consistency
    df = df.rename(columns={
        "job title": "job_title",
        "skills": "skills",
        "location": "location",
        "salary": "salary"
    })

    # Drop rows with missing values
    df = df.dropna(subset=["job_title", "skills"])

    # Clean salary column if present
    if "salary" in df.columns:
        df["salary"] = (
            df["salary"]
            .astype(str)
            .str.replace(",", "")
            .str.extract(r"(\d+)")
        )
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    return df


def top_skills_by_role(df, role, top_n=10):
    role_df = df[df["job_title"].str.contains(role, case=False, na=False)]

    skills = (
        role_df["skills"]
        .str.split(",")
        .explode()
        .str.strip()
        .str.lower()
    )

    return skills.value_counts().head(top_n)


def demand_by_location(df, top_n=10):
    return df["location"].value_counts().head(top_n)


def salary_distribution(df):
    if "salary" not in df.columns:
        return None
    return df["salary"].dropna()

"""Once you have the content, you can copy and paste it into a new code cell, or if you prefer an automated way, you can generate a new cell programmatically (though direct generation of arbitrary code cells from string content into the notebook is not a standard Colab API feature for users, printing it is the most direct way for you to then copy/paste or execute dynamically if needed)."""
