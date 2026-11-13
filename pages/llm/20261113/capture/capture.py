"""Day20 강의 슬라이드의 코드를 그대로 실행해 페이지 숫자를 기록한다 → capture.json

슬라이드: p.29 Tokenizer · p.34 Padding/Mask · p.43 Cosine · p.45 Sentence Embedding
          p.54 TransformerEncoderLayer · p.62 Attention · p.74 Softmax·Temperature
실행: uv run --project ~/envs/dl python capture.py
(p.29·34는 bert-base-multilingual-cased Tokenizer, p.45는 all-MiniLM-L6-v2 가중치가 필요하다)
"""
import json
import math
from pathlib import Path

import torch
import torch.nn.functional as F
from torch import nn

torch.set_num_threads(1)
OUT = {}

# p.29 실제 Tokenizer로 Token·ID·개수
from transformers import AutoTokenizer, __version__ as tf_ver

tok = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
text = "실습 파일은 개인 폴더에 보관합니다."
ids = tok(text)["input_ids"]
OUT["p29"] = {"text": text, "chars": len(text), "tokens": tok.convert_ids_to_tokens(ids),
              "ids": ids, "n_tokens": len(ids), "vocab_size": tok.vocab_size}

# p.34 잘림·패딩·마스크
texts = ["AI", "FastAPI와 PostgreSQL"]
batch = tok(texts, padding=True, truncation=True, max_length=12, return_tensors="pt")
OUT["p34"] = {"texts": texts, "shape": list(batch["input_ids"].shape),
              "input_ids": batch["input_ids"].tolist(),
              "tokens": [tok.convert_ids_to_tokens(r) for r in batch["input_ids"].tolist()],
              "attention_mask": batch["attention_mask"].tolist()}

# p.43 작은 2차원 벡터의 Cosine
a, b, c = torch.tensor([1.0, 0.0]), torch.tensor([0.8, 0.2]), torch.tensor([-1.0, 0.0])
OUT["p43"] = {"a": a.tolist(), "b": b.tolist(), "c": c.tolist(),
              "ab": float(F.cosine_similarity(a, b, dim=0)), "ac": float(F.cosine_similarity(a, c, dim=0))}

# p.45 문장 임베딩 (선택 시연)
from sentence_transformers import SentenceTransformer, __version__ as st_ver

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
sents = ["The file is in your project folder.", "Look for it in the project directory.", "The weather is sunny today."]
vecs = model.encode(sents)
OUT["p45"] = {"texts": sents, "shape": list(vecs.shape),
              "similarity": [[round(float(x), 4) for x in row] for row in model.similarity(vecs, vecs)]}

# p.54 작은 TransformerEncoderLayer의 shape
torch.manual_seed(42)
layer = nn.TransformerEncoderLayer(d_model=8, nhead=2, dim_feedforward=16, batch_first=True, dropout=0.0)
x = torch.randn(2, 5, 8)
y = layer(x)
OUT["p54"] = {"x": list(x.shape), "y": list(y.shape)}

# p.62 작은 Q/K/V로 Attention Weight (마스크 없는 경우도 함께 기록)
q = torch.tensor([[1., 0.], [0., 1.], [1., 1.]])
k, v = q.clone(), q.clone()
scores = q @ k.T / math.sqrt(2)
mask = torch.triu(torch.ones(3, 3, dtype=torch.bool), diagonal=1)
weights = torch.softmax(scores.masked_fill(mask, float("-inf")), dim=-1)
OUT["p62"] = {"q": q.tolist(), "scores": scores.tolist(), "mask": mask.tolist(),
              "weights": weights.tolist(), "weights_nomask": torch.softmax(scores, dim=-1).tolist(),
              "row_sums": weights.sum(-1).tolist(), "out": (weights @ v).tolist()}

# p.74 Softmax·Temperature
logits = torch.tensor([2.0, 1.0, 0.0])
OUT["p74"] = {"logits": logits.tolist(),
              "probs": {str(t): torch.softmax(logits / t, dim=0).tolist() for t in [0.5, 1.0, 2.0]}}

OUT["env"] = {"torch": torch.__version__, "transformers": tf_ver, "sentence_transformers": st_ver}
Path(__file__).with_name("capture.json").write_text(json.dumps(OUT, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(OUT, ensure_ascii=False)[:3000])
