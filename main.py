from functions import *

# Lấy dữ liệu từ vnexpress
doc = lay_du_lieu('https://vnexpress.net/du-bao-gia-xang-dau-moi-nhat-gia-xang-co-the-giam-manh-ve-duoi-30-000-dong-4485667.html').text

# Xóa các thẻ html
re.sub(r'<[^>]*>', '', doc)

# Chuẩn hóa cách gõ dấu tiếng Việt
doc = chuan_hoa_dau_cau_tieng_viet(doc)

# Tách từ
doc = word_tokenize(doc, format="text")

# Chuyển về chữ viết thường
doc = doc.lower()

# Xóa các ký tự không cần thiết
doc = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',doc)

# Xóa khoảng trắng thừa
doc = re.sub(r'\s+', ' ', doc).strip()

# Xóa các stopword
doc = remove_stopwords(doc)

# Hiển thị kết quả
print(doc)