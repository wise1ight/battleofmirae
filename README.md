# battleofmirae
미래관을 만화화 스타일로 변환하기 위한 인간과 ChatGPT의 대결  
미래(관)이 달린 문제...

## GPT4 방식
일반적으로 공개된 GPT3.5 모델은 흔할 것 같아 GPT4 모델을 통해 [코드](./gpt4.py)를 생성

### 프롬프트
![GPT프롬프트](./asset/gpt4.png)

### 방식 설명
1. Grayscale로 변환
2. Median Blur 적용
3. Adaptive threshold로 Edge 검출
4. Bilateral Filter 적용
5. Edge와 색상 Bilateral Filter를 적용한 이미지 결합

## 결과물 비교
| 원본 | 인간 | GPT4 |
|-----|-----|------|
|![원본](./input.jpg)|![인간결과물](./asset/man_output.jpg)|![GPT4결과물](./asset/gpt_output.jpg)|

## 참고자료
[Cartoon Effect on Image using OpenCV](https://www.youtube.com/watch?v=2xqvGZS7NCw)
