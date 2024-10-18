import re
from datetime import datetime
from pprint import pprint

from docx import Document


def clean_text(text):
    # Remove newline characters and extra spaces
    text = text.replace("\n", " ").strip()

    # Remove trailing dots
    text = re.sub(r"\.\s*$", "", text)

    # Remove leading numeric lists like '1.', '2.' at the beginning of the line
    text = re.sub(r"^\d+\.\s*", "", text)

    return text


def parse_docx(file_path):
    doc = Document(file_path)
    teacher_data = []

    for table in doc.tables:
        for row in table.rows[1:]:  # Skip header row
            if "ВИКЛАДАЧІ" in row.cells[0].text:
                continue

            teacher = {}

            # Full Name
            teacher["full_name"] = parse_full_name(clean_text(row.cells[0].text))

            # Position
            teacher["position"], teacher["is_main_job"] = parse_position(
                clean_text(row.cells[1].text)
            )

            # Department and Faculty
            teacher["department"], teacher["faculty"] = parse_structural_unit(
                clean_text(row.cells[2].text)
            )

            # Qualifications
            teacher["qualification"] = parse_qualifications(
                clean_text(row.cells[3].text)
            )

            # Experience
            teacher["experience"] = parse_experience(row.cells[4].text.split('\n'))

            # Courses
            teacher["courses"] = parse_courses(clean_text(row.cells[5].text))

            # Justification
            teacher["justification"] = parse_justification(
                clean_text(row.cells[6].text)
            )

            teacher_data.append(teacher)

    return teacher_data


def parse_full_name(text):
    parts = text.split()
    return {
        "last_name": parts[0],
        "first_name": parts[1],
        "middle_name": parts[2] if len(parts) > 2 else "",
    }


def parse_position(text):
    # Check if any of the specified strings are in the text
    is_main_job = any(
        keyword in text for keyword in ["основне місце роботи"]
    )

    # Remove both 'основне місце роботи' and 'сумісництво' from the text
    position = re.sub(r"основне місце роботи|сумісництво", "", text).strip()

    # Remove any trailing comma
    position = position.rstrip(",")

    return position, is_main_job


def parse_structural_unit(text):
    department_match = re.search(r"[Кк]афедра ([^,]+)", text)
    faculty_match = re.search(r"факультет ([^,]+)", text)

    if not faculty_match:
        faculty_match = re.search(r"([^,]+)", text)

    department = department_match.group(1) if department_match else ""
    faculty = faculty_match.group(1) if faculty_match else ""

    return department, faculty


def normalize_date(date_str):
    # Normalize date to YYYY-MM-DD format
    months = {
        'січня': 'January', 'лютого': 'February', 'березня': 'March',
        'квітня': 'April', 'травня': 'May', 'червня': 'June',
        'липня': 'July', 'серпня': 'August', 'вересня': 'September',
        'жовтня': 'October', 'листопада': 'November', 'грудня': 'December'
    }
    for ukr_month, eng_month in months.items():
        date_str = date_str.replace(ukr_month, eng_month)

    # Try parsing in written-out month format (e.g., 1 липня 2016)
    try:
        return datetime.strptime(date_str, '%d %B %Y').strftime('%Y-%m-%d')
    except ValueError:
        pass

    # Try parsing in numeric format (e.g., 01.07.2016)
    try:
        return datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        return date_str  # Return the original string if parsing fails


def parse_qualifications(text):
    qualifications = []

    # Define regex pattern for splitting qualifications
    qualification_pattern = r'(Диплом|Атестат)(.*?)(?=(Диплом|Атестат|$))'  # Split by 'Диплом' or 'Атестат'

    # Define patterns for code and both date formats (written and numeric)
    code_pattern = r'([А-ЯҐЄІЇ]{2,}\s?№?\s?\d{6})'  # Code pattern (e.g., ДД № 009858, АС № 007635)
    date_pattern = r'(\d{1,2}\s[а-я]+\s\d{4})|(\d{2}\.\d{2}\.\d{4})'  # Date pattern for both 14 травня 2020 and 01.07.2016

    # Find all qualification segments
    matches = re.findall(qualification_pattern, text, re.DOTALL)

    # Iterate over each found match and extract details
    for match in matches:
        full_match = "".join(match)  # Join all parts for the current qualification segment
        name = match[0]  # First part is the qualification name (e.g., "Диплом", "Атестат")
        code_match = re.search(code_pattern, full_match)
        date_match = re.search(date_pattern, full_match)

        # Use the full_match for the specific part of the text
        cleaned_text = full_match.strip()

        # Construct qualification data
        qualification = {
            "name": name,
            "text": match[0].strip() + " " + match[1].strip(),
            "code": code_match.group(0) if code_match else None,
            "date": normalize_date(date_match.group(0)) if date_match else None
        }
        qualifications.append(qualification)

    return qualifications


def parse_experience(nums):
    result = [re.sub(r"[^\d]", "", num) for num in nums]
    return [int(res) for res in result if res.isdigit()]

def parse_courses(text):
    return [course.strip() for course in text.split(",")]


def parse_academic_degree(text):
    # List to store all parsed degrees
    degrees_list = []

    # Split text by numbers indicating new degrees (handles multiple degrees per line)
    degree_blocks = (
        re.split(r"(?:^|\.\s|\n)\d+\.\s*", text.strip())
        if re.search(r"(?:^|\.\s|\n)\d+\.\s*", text)
        else [text]
    )

    for block in degree_blocks:

        # Primary regex to handle most common cases
        degree_sections = re.findall(
            r"((Кандидат|Доктор) [^,]+ наук),?\s*(\d{2}\.\d{2}\.\d{2})?,?\s*(«[^»]+»(?:,?\s*«[^»]+»)?),?\s*(?:[Тт]ема дисертації[:]?|тема)\s*[-–]?\s*«?([^»]+)?»?(?:\s*|\.|$)",
            block,
            re.IGNORECASE,
        )

        # If the primary regex fails, check for edge cases
        if not degree_sections:
            # Case 1: "Кандидат військових наук, 20.01.01, тема – спеціальна"
            degree_sections = re.findall(
                r"((Кандидат|Доктор) [^,]+ наук),?\s*(\d{2}\.\d{2}\.\d{2})?,?\s*(тема\s*[-–]\s*спеціальна)",
                block,
                re.IGNORECASE,
            )

            # Case 2: Handle multiple specialties with dissertation topic
            if not degree_sections:
                degree_sections = re.findall(
                    r"((Кандидат|Доктор) [^,]+ наук),?\s*(\d{2}\.\d{2}\.\d{2})?,?\s*«([^»]+)»(?:,\s*«([^»]+)»)?(?:\s*Тема дисертації:\s*«([^»]+)»)?",
                    block,
                    re.IGNORECASE,
                )

        if degree_sections:
            for match in degree_sections:
                degree = match[0] if match[0] else None
                date = convert_date(match[2]) if match[2] else None
                specialties = (
                    match[3].replace("«", "").replace("»", "")
                    if len(match) > 3 and match[3]
                    else ""
                )

                # Handle both "Тема дисертації" and edge cases
                dissertation_topic = (
                    match[4]
                    if len(match) > 4 and match[4]
                    else match[3] if "спеціальна" in match[3] else ""
                )

                # Clean "Тема дисертації" if needed
                dissertation_topic = dissertation_topic.replace(
                    "Тема дисертації:", ""
                ).strip()

                # If the dissertation topic is "тема – спеціальна", the specialty should remain empty
                if "спеціальна" in dissertation_topic:
                    specialties = ""
                    dissertation_topic = "тема – спеціальна"

                # Ignore any diploma numbers or irrelevant parts like "диплом ТН №..."
                if "диплом" in dissertation_topic:
                    dissertation_topic = dissertation_topic.split("диплом")[0].strip()
                # Append each degree's details as a dictionary
                degrees_list.append(
                    {
                        "degree": degree,
                        "date": date,
                        "specialty": specialties,
                        "dissertation_topic": dissertation_topic,
                    }
                )

    # If no degrees are found, append an empty dictionary to maintain consistent structure
    if not degrees_list:
        degrees_list.append(
            {"degree": "", "date": None, "specialty": "", "dissertation_topic": ""}
        )

    return degrees_list


def convert_date(date_string):
    # Parse the date string in DD.MM.YYYY format
    try:
        parsed_date = datetime.strptime(date_string, "%d.%m.%Y").date()
        return parsed_date
    except ValueError:
        # Handle invalid date format
        return None


def parse_professional_development(text):
    professional_development = []
    # Match entries that are separated by numbered bullets like '1. ...'
    entries = re.findall(r"\d+\.\s*(.*?)(?=\d+\.\s|\Z)", text, re.DOTALL)

    for entry in entries:
        cleaned_entry = re.sub(r"^\d+\.\s*", "", entry).strip()

        # Search for certificate or equivalent
        match_certificate = re.search(
            r"(Сертифікат|Свідоцтво)\s+([^,]+)\s+(\d{2}\.\d{2}\.\d{4})", cleaned_entry
        )
        if match_certificate:
            professional_development.append(
                {
                    "type": match_certificate.group(1),
                    "details": match_certificate.group(2),
                    "date": convert_date(match_certificate.group(3)),
                    "duration": None,
                }
            )
        else:
            # Improved regex to capture duration (e.g., "180 годин", "hours 180 ECTS")
            match_duration_1 = re.search(
                r"(\b(?:[0-9]{1,3})(?:\.[0-9]{1,2})?\b\s+(?:години|годин|кредити|год|hours))",
                cleaned_entry,
            )
            match_duration_2 = re.search(
                r"(?:години|годин|кредити|год|hours)\s+(\b[0-9]{1,3}(?:\.[0-9]{1,2})?\b)",
                cleaned_entry,
            )
            match_duration = match_duration_1 or match_duration_2

            # Extract duration if found
            duration = match_duration.group(0) if match_duration else ""
            if cleaned_entry and duration:
                professional_development.append(
                    {
                        "type": None,
                        "details": cleaned_entry,
                        "date": None,
                        "duration": duration,
                    }
                )

    return professional_development


def parse_professional_activity(text):
    professional_activity = []

    # Step 1: Split the text by paragraphs that must be followed by a valid numeric identifier
    # First number should be between 1 and 20, avoid splitting on dates, DOIs, or URLs
    # Exclude common date formats (e.g., dd.mm.yyyy, dd.mm.yy) and special cases
    paragraph_split_pattern = r"(п\.\s*\d+)(\s+(?:1[0-9]|20|\d)\.\d+\.\s)"
    paragraphs = re.split(paragraph_split_pattern, text)

    combined_paragraphs = []
    for i in range(1, len(paragraphs), 3):
        paragraph_title = paragraphs[i]
        content = paragraphs[i + 1].strip() + " " + paragraphs[i + 2].strip()
        combined_paragraphs.append((paragraph_title, content))

    for paragraph_title, paragraph in combined_paragraphs:

        # Extract paragraph number (e.g., "п. 1", "п. 1.", "п. 6.1", etc.)
        paragraph_number_match = re.search(r"п\.\s*(\d+)(?:\.(\d+))?", paragraph_title)
        if paragraph_number_match:
            paragraph_number = paragraph_number_match.group(1)
            if paragraph_number_match.group(2):  # If there's a sub-number, append it
                paragraph_number += f".{paragraph_number_match.group(2)}"
        else:
            paragraph_number = None

        # Step 2: Use a refined pattern to correctly split citations and avoid misclassification
        # Restrict the first number between 1 and 20, avoid dates or known invalid patterns (e.g., dd.mm.yyyy, dd.mm.yy, and special numeric cases)
        # Use negative lookahead to avoid splitting on dates (e.g., dd.mm.yyyy)
        citation_pattern = r"((?:1[0-9]|20|\d)\.(?!0)\d{1,2}\.\s)(.*?)(?=(?:1[0-9]|20|\d)\.(?!0)\d{1,2}\.\s|\Z|(?<!\d{2})\.\d{2}\.\d{2,4}(?!\.))"

        citations = re.findall(citation_pattern, paragraph, re.DOTALL)

        for citation in citations:
            # Clean up the citation text, remove leading/trailing whitespace and ensure it's properly captured
            numeric_id, citation_text = citation
            cleaned_citation = citation_text.strip()

            citation_data = {"paragraph": paragraph_number, "text": cleaned_citation}
            professional_activity.append(citation_data)

    return professional_activity


def parse_education(text):
    # First attempt with the first regex pattern
    result = re.findall(r"\d+\.\s*[^,]+,\s*\d{4}\s*р\.,\s*[^,]+,\s*[^.]+\.", text)

    # If the first pattern doesn't yield results, try the second pattern
    if not result:
        result = re.findall(r"\d+\.\s*«[^»]+»,\s*\d{4}.*?(?=\d+\.|$)", text)

    # If no result is found with either regex, return the original text as a single element list
    if not result:
        return [text]

    # Clean up: remove leading numeric identifiers and strip extra spaces
    education_list = []
    for entry in result:
        cleaned_entry = re.sub(r"^\d+\.\s*", "", entry).strip()
        if cleaned_entry:
            education_list.append(cleaned_entry)

    return education_list


def parse_justification(text):
    text = text.replace("\n", " ").strip()

    justification_data = {
        "education": "",
        "academicDegree": "",
        "academicTitle": "",
        "professionalDevelopment": [],
        "professionalActivity": [],
    }

    # Extract education
    education_match = re.search(
        r"Освіта:\s*(.*?)(?=\s*Науковий ступінь|Вчене звання|Підвищення кваліфікації|Види і результати професійної діяльності|$)",
        text,
    )
    if education_match:
        justification_data["education"] = parse_education(
            education_match.group(1).strip()
        )

    # Flexible academic degree parsing for both "кандидат наук" and "доктор наук"
    academic_degree_match = re.search(
        r"Науковий ступінь:\s*(.*?)(?=\s*Вчене звання|Підвищення кваліфікації|Види і результати професійної діяльності|$)",
        text,
    )
    if academic_degree_match:
        justification_data["academicDegree"] = parse_academic_degree(
            academic_degree_match.group(1).strip()
        )

    # Extract academic title
    academic_title_match = re.search(
        r"Вчене звання:\s*(.*?)(?=\s*Підвищення кваліфікації|Види і результати професійної діяльності|$)",
        text,
    )
    if academic_title_match:
        justification_data["academicTitle"] = academic_title_match.group(1).strip()

    # Extract professional development
    professional_development_match = re.search(
        r"Підвищення кваліфікації:\s*(.*?)(?=\s*Види і результати професійної діяльності|$)",
        text,
    )
    if professional_development_match:
        justification_data["professionalDevelopment"] = parse_professional_development(
            professional_development_match.group(1).strip()
        )

    # Extract professional activity
    professional_activity_match = re.search(
        r"Види і результати професійної діяльності:\s*(.*)", text
    )
    if professional_activity_match:
        justification_data["professionalActivity"] = parse_professional_activity(
            professional_activity_match.group(1).strip()
        )

    return justification_data


# Example usage:
# file_path = r'C:\Users\Alex\Desktop\Таблиця 2 2023_10_15 11-11.docx'
# parsed_data = parse_docx(file_path)
# pprint(parsed_data)
