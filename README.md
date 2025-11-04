# 114-1 NTU_Maker_Workshop PART 2

---

## 簡介

本專案為 NTU Maker Workshop API Server，利用 Render 部屬專案提供 **TTS/STT API 服務**，再利用上週的 ESP32S + INMP441 達到語音辨識功能。

---

## 重要連結

* 簡報連結 [https://docs.google.com/presentation/d/1sXBzooZRVFtlOk1QXWgG5a-12z-ez6THPJ5Be3oa82g/edit?usp=sharing](https://docs.google.com/presentation/d/1sXBzooZRVFtlOk1QXWgG5a-12z-ez6THPJ5Be3oa82g/edit?usp=sharing)
* 上週程式碼連結: [https://github.com/dengdee/114-1NTU_maker_workshop](https://github.com/dengdee/114-1NTU_maker_workshop)
* AI Studio API 金鑰申請 (Google AI Studio): [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)
* Github: [https://github.com/](https://github.com/)
* Render: [https://render.com/](https://render.com/)
* Postman: [https://www.postman.com/](https://www.postman.com/)

---

## Postman 測試 Gemini API

API Endpoint:

```
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=<your_api_key>
```

### Header

| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### Body (raw JSON)

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "什麼是LLM"
        }
      ]
    }
  ]
}
```

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        { "text": "什麼是LLM" }
      ]
    }
  ],
  "system_instruction": {
    "role": "system",
    "parts": [
      { "text": "你是一位清楚解釋科技概念的老師。" }
    ]
  },
  "generationConfig": {
    "temperature": 0.7,
    "topK": 40,
    "topP": 0.9,
    "maxOutputTokens": 5120
  }
}
```
