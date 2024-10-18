import re

def parse_qualifications(text):
    def parse_citation_from_text(self, activity):
        text = activity.text

        parsed_data = {
            'authors': [],
            'title': '',
            'publication_year': '',
            'publisher_name': '',
            'publication_city': '',
            'pages': '',
            'document_type': ''
        }

        # Pattern to extract authors (both in English and Ukrainian formats)
        authors_pattern = r'([А-ЯA-Z][а-яa-zA-Z]*\s+[А-ЯA-Z][а-яa-zA-Z]*\.*(?:\s+[А-ЯA-Z][а-яa-zA-Z]*\.*)?)'
        authors = re.findall(authors_pattern, text)
        parsed_data['authors'] = authors

        # Pattern to extract the title (everything between the last author and the first period)
        title_pattern = r'{}\.\s*([^\.]+)'.format(re.escape(authors[-1])) if authors else r'([^\.]+)\.'
        title_match = re.search(title_pattern, text)
        if title_match:
            parsed_data['title'] = title_match.group(1).strip()

        # Pattern to extract publication year
        year_pattern = r'\b(20\d{2}|19\d{2})\b'
        year_match = re.search(year_pattern, text)
        if year_match:
            parsed_data['publication_year'] = year_match.group(0)

        # Pattern to extract publisher name (after title and before year)
        publisher_pattern = r'([^—,]+)(?:\s*—)?\s*\b{}\b'.format(parsed_data['publication_year'])
        publisher_match = re.search(publisher_pattern, text)
        if publisher_match:
            parsed_data['publisher_name'] = publisher_match.group(1).strip()

        # Pattern to extract publication city (appears after publisher, before pages or year)
        city_pattern = r'—\s*([^,]+)\s*—'
        city_match = re.search(city_pattern, text)
        if city_match:
            parsed_data['publication_city'] = city_match.group(1).strip()

        # Pattern to extract pages (if any)
        pages_pattern = r'С\.\s*(\d+-?\d*)'
        pages_match = re.search(pages_pattern, text)
        if pages_match:
            parsed_data['pages'] = pages_match.group(1)

        # Determine document type based on keywords in the string
        if 'конференції' in text or 'тези' in text:
            parsed_data['document_type'] = 'conference'
        elif 'книга' in text or 'видання' in text:
            parsed_data['document_type'] = 'book'
        elif 'стаття' in text:
            parsed_data['document_type'] = 'article'
        else:
            parsed_data['document_type'] = 'other'

    return parsed_data

# Example usage
text = """
Диплом кандидата наук ДК №005323 від 8 грудня 1999 р.   Атестат доцента АД №007886 від 29 червня 2021 р.
Диплом доктора наук ДД № 012766 від 01.02.2022 року.  Атестат доцента ДЦ № 004694 від 10.10.1988 року.
"""

qualifications = parse_qualifications(text)
for q in qualifications:
    print(q)
