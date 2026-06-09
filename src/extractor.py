import os


def extract_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def process_resumes(folder_path):

    for file_name in os.listdir(folder_path):

        if file_name.endswith(".txt"):

            file_path = os.path.join(folder_path, file_name)

            print("\n" + "=" * 50)
            print("Resume:", file_name)
            print("=" * 50)

            text = extract_text(file_path)

            print(text)


if __name__ == "__main__":

    process_resumes("resumes")