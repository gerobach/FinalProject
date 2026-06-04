import pandas as pd


def create_smoking_score(df):

    df["smoking_status"] = pd.Series(
        pd.NA,
        index=df.index,
        dtype="object"
    )

    df.loc[df["smoked_100_cigs?"] == 2, "smoking_status"] = "Never"
    df.loc[df["smoker_now?"] == 3, "smoking_status"] = "Former"
    df.loc[df["smoker_now?"] == 2, "smoking_status"] = "Current Some Days"
    df.loc[df["smoker_now?"] == 1, "smoking_status"] = "Current Every Day"

    smoking_score_map = {
        "Never": 0,
        "Former": 1,
        "Current Some Days": 2,
        "Current Every Day": 3
    }

    df["smoking_score"] = df["smoking_status"].map(smoking_score_map)

    return df


def create_hba1c_group(df):

    df["hba1c_group"] = pd.cut(
        df["hba1c_%"],
        bins=[0, 5.7, 6.5, 20],
        labels=[
            "Normal",
            "Prediabetes",
            "Diabetes"
        ]
    )

    return df

def create_alcohol_frequency_features(df):

    df["alcohol_frequency_group"] = pd.Series(
        pd.NA,
        index=df.index,
        dtype="object"
    )

    # Never drank alcohol at all
    df.loc[
        df["alc_consum?"] == 2,
        "alcohol_frequency_group"
    ] = "Never Drank"

    # Drank before, but not in last 12 months
    df.loc[
        df["alc_<12m?"] == 0,
        "alcohol_frequency_group"
    ] = "Former / None Last Year"

    # Few times per year
    df.loc[
        df["alc_<12m?"].isin([8, 9, 10]),
        "alcohol_frequency_group"
    ] = "Few Times / Year"

    # Monthly
    df.loc[
        df["alc_<12m?"] == 7,
        "alcohol_frequency_group"
    ] = "Monthly"

    # Weekly
    df.loc[
        df["alc_<12m?"].isin([3, 4, 5, 6]),
        "alcohol_frequency_group"
    ] = "Weekly"

    # Daily / near daily
    df.loc[
        df["alc_<12m?"].isin([1, 2]),
        "alcohol_frequency_group"
    ] = "Daily / Near Daily"

    alcohol_frequency_map = {
        "Never Drank": 0,
        "Former / None Last Year": 1,
        "Few Times / Year": 2,
        "Monthly": 3,
        "Weekly": 4,
        "Daily / Near Daily": 5
    }

    df["alcohol_frequency_score"] = (
        df["alcohol_frequency_group"]
        .map(alcohol_frequency_map)
    )

    return df