import fitz
import datetime as dt

def restructure_combined_pdf(original_pdf,target_dir):
    now = dt.datetime.now()
    ymdhms = now.strftime('%Y%m%d%H%M%S')
    output_pdf = fitz.open()

    a4_rect = fitz.paper_rect('a4')
    section_width = a4_rect.width / 3
    section_height = a4_rect.height / 3

    for i in range(0, original_pdf.page_count, 9):
        new_page = output_pdf.new_page(width=a4_rect.width, height=a4_rect.height)

        for j in range(9):
            if i + j < original_pdf.page_count:
                row = j // 3
                col = j % 3
                x = col * section_width
                y = row * section_height

                new_page.show_pdf_page(
                    fitz.Rect(x, y, x + section_width, y + section_height),
                    original_pdf,
                    i + j
                )

    output_path = target_dir / f'補給現品票{ymdhms}.pdf'
    output_pdf.save(output_path,garbage=4, deflate=True)
    original_pdf.close()
    output_pdf.close()

if __name__ == '__main__':
    input_path = r'C:\Users\masayo.umezawa\PycharmProjects\pythonProject\補給現品票\combined_pdf.pdf'
    restructure_combined_pdf(input_path)