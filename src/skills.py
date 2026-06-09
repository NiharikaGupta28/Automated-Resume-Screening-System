skills = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "power bi",
    "excel"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    return found_skills


if __name__ == "__main__":

    sample_text = """
    Python SQL Machine Learning NLP Pandas
    """

    detected_skills = extract_skills(sample_text)

    print("Detected Skills:")
    print(detected_skills)