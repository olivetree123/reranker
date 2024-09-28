# reranker
重排序模型服务，使用的是`BAAI/bge-reranker-v2-m3`模型

> Huggingface主页：https://huggingface.co/BAAI/bge-reranker-v2-m3  \
> Github主页：https://github.com/FlagOpen/FlagEmbedding/blob/master/README_zh.md

### 部署
```shell
docker run -d --name=reranker -p 5608:5608 reranker:1.0
```

### 使用
```shell
curl -X POST http://localhost:5608/reranker \
     -H "Content-Type: application/json" \
     -d '{
            "query":"你好",
            "data": ["你好啊", "你不好"]
        }'
```
返回结果：
```json
{
    "code": 0,
    "data": [
        4.499629020690918,
        -2.8593292236328125
    ],
    "message": ""
}
```