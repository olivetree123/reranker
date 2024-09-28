from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from FlagEmbedding import FlagReranker

app = FastAPI()

# Setting use_fp16 to True speeds up computation with a slight performance degradation
reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True, cache_dir="/cache_model")


class RerankParam(BaseModel):
    query: str
    data: List[str]


@app.post("/rerank")
async def handler(param: RerankParam):
    data = [[param.query, d] for d in param.data]
    scores = reranker.compute_score(data)
    return {"code": 0, "data": scores, "message": ""}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5608)
