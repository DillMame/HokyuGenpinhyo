import fitz
from tkinter import messagebox

def PR_1_split_A4_9(file):
    if not file:
        messagebox.showerror('ファイルなし','（テスト用）ファイルがありません。終了します。')
        return

    combined_doc = fitz.open()
    doc = fitz.open(file)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        width, height = page.rect.width, page.rect.height

        section_height = height // 3
        section_width = width // 3

        # 3×3の分割ループ
        for i in range(3):  # 縦方向
            for j in range(3):  # 横方向
                rect = fitz.Rect(
                    j * section_width,
                    i * section_height,
                    (j + 1) * section_width,
                    (i + 1) * section_height
                )

                text = page.get_text(clip=rect)
                if 'Z08' not in text:
                    continue

                new_page = combined_doc.new_page(width=section_width, height=section_height)
                new_page.show_pdf_page(new_page.rect, doc, page_num, clip=rect)
    doc.close()

    return combined_doc

if __name__ == '__main__':
    file = r'C:\Users\masayo.umezawa\PycharmProjects\pythonProject\補給現品票\補給用現品票_test.pdf'
    PR_1_split_A4_9(file)