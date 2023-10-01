import torch
from transformers import AutoModel, AutoTokenizer
from pyvi.ViTokenizer import tokenize
from numpy.linalg import norm
import numpy as np


# sentences = [
#     "Trong những năm gần đây, năm nào cũng vậy, cứ vào khoảng cuối tháng 9, đầu tháng 10 hàng năm, du khách khắp mọi miền tổ quốc đều đổ về Mù Cang Chải để chiêm ngưỡng khung cảnh đẹp tuyệt vời của mảnh đất vùng cao này. Đến với nơi đây, du khách không chỉ được thưởng ngoạn vẻ đẹp của những thửa ruộng bậc thang, những biển mây trắng trên đỉnh đèo Cao Phạ mà còn được đắm mình vào những lễ hội văn hóa độc đáo của đồng bào Mông.",
#     "Bãi Hòn Chồng là một bờ biển hoang sơ, chưa bị tác động bởi các hoạt động du lịch, nhiều cảnh quan tự nhiên vẫn còn nguyên vẹn cho ta khám phá",
#     "Nằm ở vùng Đông Bắc thành phố Tây Ninh, cách TP.HCM gần 100km, núi Bà Đen không chỉ nổi tiếng với người dân tại Tây Ninh mà còn với những ai thích bộ môn trekking leo núi",
# ]
def sim_cal(root, sentences):
    PhobertTokenizer = AutoTokenizer.from_pretrained(
        "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base"
    )
    model = AutoModel.from_pretrained("VoVanPhuc/sup-SimCSE-VietNamese-phobert-base")
    sentences.append(root)
    sentences_tokenizer = [tokenize(sentence) for sentence in sentences]

    inputs = PhobertTokenizer(
        sentences_tokenizer, padding=True, truncation=True, return_tensors="pt"
    )

    with torch.no_grad():
        embeddings = model(
            **inputs, output_hidden_states=True, return_dict=True
        ).pooler_output

    cosines = []
    root = embeddings[-1]
    for sentence_embedding in embeddings[0 : len(embeddings) - 1]:
        cosine = np.dot(root, sentence_embedding) / (
            norm(root) * norm(sentence_embedding)
        )
        print("cosine with senctence")
        print(cosine)
        cosines.append(cosine)

    print(len(cosines))

    # Sort the sentences based on cosine similarity
    sorted_indices = np.argsort(cosines)[::-1]

    return sorted_indices


sentences = [
    "Bãi Hòn Chồng là một bờ biển hoang sơ, chưa bị tác động bởi các hoạt động du lịch, nhiều cảnh quan tự nhiên vẫn còn nguyên vẹn cho ta khám phá",
    "Nằm ở vùng Đông Bắc thành phố Tây Ninh, cách TP.HCM gần 100km, núi Bà Đen không chỉ nổi tiếng với người dân tại Tây Ninh mà còn với những ai thích bộ môn trekking leo núi",
]
root = "Trong những năm gần đây, năm nào cũng vậy, cứ vào khoảng cuối tháng 9, đầu tháng 10 hàng năm, du khách khắp mọi miền tổ quốc đều đổ về Mù Cang Chải để chiêm ngưỡng khung cảnh đẹp tuyệt vời của mảnh đất vùng cao này. Đến với nơi đây, du khách không chỉ được thưởng ngoạn vẻ đẹp của những thửa ruộng bậc thang, những biển mây trắng trên đỉnh đèo Cao Phạ mà còn được đắm mình vào những lễ hội văn hóa độc đáo của đồng bào Mông"


res = sim_cal(root, sentences)
print(res)
