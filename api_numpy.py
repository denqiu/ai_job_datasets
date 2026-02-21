import numpy
import pandas

# To easily test, enter python console. Use importlib.reload after making changes.

def apply_transformations(ai_job_dataset, ai_job_dataset1):
    dataframe_dataset = pandas.read_csv(ai_job_dataset)
    dataframe_dataset1 = pandas.read_csv(ai_job_dataset1)

    # Union of both datasets
    dataframe = pandas.concat([dataframe_dataset, dataframe_dataset1], ignore_index=True)

    # Adjusted job IDs
    total_rows = len(dataframe)
    pad_len = len(str(total_rows))
    dataframe["job_id"] = numpy.array(["AI" + str(i).zfill(pad_len) for i in range(1, total_rows + 1)])

    # Clarified salary_local column
    # Because there were nulls (or NaN) every number became a float. "Int64" ensures number remains integer while treating nulls as pandas.NA instead of numpy.NaN which causes numpy to assign the series float type and making whole numbers end in ".0".
    # Then set type to object to include string type.
    dataframe["salary_local"] = dataframe["salary_local"].astype("Int64").astype("object")
    dataframe["salary_local"] = numpy.where(
        (dataframe["salary_local"] == dataframe["salary_usd"]) | dataframe["salary_local"].isna(),
        "EQUAL",
        dataframe["salary_local"]
    )

    # Clarified employee_residence column
    dataframe["employee_residence"] = numpy.where(
        dataframe["employee_residence"] == dataframe["company_location"],
        "EQUAL",
        dataframe["employee_residence"]
    )

    experience_map = {"EN": "Entry", "MI": "Mid", "SE": "Senior", "EX": "Executive"}
    dataframe["experience_level"] = dataframe["experience_level"].map(experience_map).fillna(dataframe["experience_level"])

    employment_map = {"FT": "Full-time", "PT": "Part-time", "CT": "Contract", "FL": "Freelance"}
    dataframe["employment_type"] = dataframe["employment_type"].map(employment_map).fillna(dataframe["employment_type"])

    workplace_map = {0: "On-Site", 50: "Hybrid", 100: "Remote"}
    dataframe["remote_ratio"] = dataframe["remote_ratio"].map(workplace_map).fillna(dataframe["remote_ratio"])

    # Determining range of numbers for S, M, and L feels subjective.
    # split into number and condition columns
    company_size_map = {"S": (50, "Less Than"), "M": ("50|250", "Between"), "L": (250, "Greater Than")}
    dataframe[["company_size", "company_size_condition"]] = dataframe["company_size"].map(company_size_map).fillna(dataframe["company_size"]).apply(pandas.Series)

    # Reordered columns
    dataframe = dataframe[[
        # Job identifier
        "job_id", "job_title",
        # Salary details
        "benefits_score", "salary_currency", "salary_usd", "salary_local",
        # Company details
        "company_name", "company_size", "company_size_condition", "company_location", "employee_residence",
        # Job details
        "remote_ratio", "experience_level", "employment_type", "education_required", "years_experience",
        "posting_date", "application_deadline", "industry", "required_skills", "job_description_length"
    ]]

    # Renamed columns
    dataframe = dataframe.rename(columns={
        "benefits_score": "benefits_ranking",
        "employee_residence": "employee_location",
        "remote_ratio": "workplace_type",
        "application_deadline": "posting_deadline"
    })

    # I don't think the length of the job description provides any meaningful way to gauge
    # the job posting. This can create a bias of preferring shorter job descriptions over
    # what the job is about.
    dataframe = dataframe.drop(columns=["job_description_length"])

    return dataframe
