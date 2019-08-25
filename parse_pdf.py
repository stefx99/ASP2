import pdftotext


def get_pdf_content(file_path):
    with open(file_path, "rb") as f:
        pdf = pdftotext.PDF(f)

        result = {'pages':[]}

        # Iterate over all the pages
        for i, content in enumerate(pdf):
            try:
                page_number = int(content[:content.index('\n')].split()[-1])
            except:
                page_number = None

            result['pages'].append({'index': i, 'page_number': page_number, 'content': content})

    return result


if __name__ == '__main__':
    path = 'Data Structures and Algorithms in Python.pdf'
    content = get_pdf_content(path)
    i = 50
    print("Page index: %d\nPage number: %s\nPage content: \n\n%s" \
          % (content['pages'][i]["index"], content['pages'][i]["page_number"], content['pages'][i]["content"]))
