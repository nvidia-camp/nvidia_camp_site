# Day16 강의 구조·핵심 설명

2026-11-09 · Vision·멀티모달 AI 응용 4/4 · OCR → 문서 구조화 → VLM 질의응답 → TensorRT·Jetson·DeepStream

교시 설명과 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준이며 인쇄 쪽수와 같습니다(전체 101쪽). 도입·마무리·참고자료는 별도 묶음으로 유지했습니다. 각 실습은 기본필수부터 진행하고 동일 입력·평가 조건을 유지한 채 선택 단계로 확장하는 구성입니다.

## 강의 목차

```text
도입 · 문서 AI의 전체 흐름과 수업 범위
├─ OCR·구조화·VLM·배포의 전체 지도
│  ├─ Vision·멀티모달 AI 응용 (PDF p.1)
│  ├─ 현업의 문서 처리와 OCR·VLM (PDF p.2)
│  ├─ 오늘 만드는 문서 AI의 전체 구조 (PDF p.3)
│  ├─ OCR 내부의 영역·문자·읽기 순서 (PDF p.4)
│  ├─ OCR 결과 안의 단어 한 건 (PDF p.5)
│  ├─ 문자열을 업무 필드로 바꾸는 구조화 (PDF p.6)
│  ├─ VLM의 입력 처리와 모델 내부 (PDF p.7)
│  ├─ VLM 답변 한 건의 값·근거·상태 (PDF p.8)
│  ├─ OCR·VLM 결과를 평가하는 서로 다른 단위 (PDF p.9)
│  ├─ TensorRT·Jetson·DeepStream의 역할 (PDF p.10)
│  └─ 문서 AI 프로젝트로 다시 합치기 (PDF p.11)
└─ 복습·운영·환경·자료 관리
   ├─ 지난 수업에서 연결한 Vision 흐름 (PDF p.12)
   ├─ 3분 확인 퀴즈 · Vision 복습 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   ├─ 실습 환경과 실행 범위를 먼저 구분한다 (PDF p.16)
   ├─ 문서 이해 서비스의 전체 흐름 (PDF p.17)
   └─ 문서 AI에서 처음부터 지켜야 할 원칙 (PDF p.18)

1교시 · OCR 전체 흐름·문서 전처리
├─ OCR 단계와 문서 입력의 어려움
│  ├─ OCR은 이미지에서 문자를 읽는 전체 과정이다 (PDF p.19)
│  ├─ 문서 이미지에서 글자까지 (PDF p.20)
│  └─ 문서 이미지가 어려운 이유 (PDF p.21)
├─ 이미지 읽기·Gray·이진화
│  ├─ 이미지 읽기와 Gray 변환 (PDF p.22)
│  ├─ cv2.imread()와 cv2.cvtColor() (PDF p.23)
│  ├─ 이진화는 글자와 배경을 분리한다 (PDF p.24)
│  ├─ 전역 Threshold와 적응형 Threshold (PDF p.25)
│  └─ cv2.adaptiveThreshold() (PDF p.26)
├─ 원근 보정과 좌표 변환
│  ├─ 원근 보정은 문서를 정면에서 본 모양으로 바꾼다 (PDF p.27)
│  └─ 문서 네 모서리로 Perspective 보정 (PDF p.28)
└─ 실습과 개념 확인
   ├─ 실습 01 · 문서 이미지 전처리 (PDF p.29)
   └─ 3분 퀴즈 · OCR 전처리 (PDF p.30)

2교시 · OCR 실행·Box·품질평가
├─ OCR 출력 형식과 페이지 구조 가정
│  ├─ OCR 엔진은 문자뿐 아니라 위치와 신뢰도를 출력할 수 있다 (PDF p.31)
│  └─ Page Segmentation Mode는 “페이지 구조 가정”이다 (PDF p.32)
├─ 단어 DataFrame과 Box·읽기 순서
│  ├─ 단어별 OCR 결과를 DataFrame으로 받기 (PDF p.33)
│  ├─ pytesseract.image_to_data() (PDF p.34)
│  └─ OCR Box·Line·Reading order (PDF p.35)
├─ Confidence 해석과 품질 지표
│  ├─ OCR Confidence를 해석할 때 (PDF p.36)
│  ├─ OCR 품질은 글자·단어·필드 단위로 나누어 평가한다 (PDF p.37)
│  └─ 간단한 CER 계산 함수 (PDF p.38)
└─ 실습과 개념 확인
   ├─ 실습 02 · OCR 실행·Box·품질평가 (PDF p.39)
   └─ 3분 퀴즈 · OCR 결과와 평가 (PDF p.40)

3교시 · 문서 정보 추출·JSON 구조화
├─ 문자열 정규화와 필드 후보 추출
│  ├─ OCR 문자열을 업무 데이터로 바꾸는 후처리 (PDF p.41)
│  ├─ 정규표현식으로 날짜와 금액 찾기 (PDF p.42)
│  └─ re.search()와 re.sub() (PDF p.43)
├─ 라벨·값·근거와 JSON 기록
│  ├─ Key-value 추출은 “라벨·값·근거”를 묶는다 (PDF p.44)
│  └─ 필드와 근거를 JSON으로 저장 (PDF p.45)
├─ 표 구조와 업무 규칙 검증
│  ├─ 표 추출은 “셀 구조”가 핵심이다 (PDF p.46)
│  ├─ 구조화 결과에 업무 규칙을 적용한다 (PDF p.47)
│  └─ 필수 필드와 금액의 최소 검증 (PDF p.48)
└─ 실습과 개념 확인
   ├─ 실습 03 · 문서 정보 추출·구조화 (PDF p.49)
   └─ 3분 퀴즈 · 구조화 (PDF p.50)

4교시 · VLM 개요·이미지 질의응답
├─ OCR·VLM 역할과 멀티모달 입력
│  ├─ OCR과 VLM은 어떤 문제에 강한가? (PDF p.51)
│  ├─ 생성형 VLM의 대표 구성 (PDF p.52)
│  └─ 멀티모달 메시지는 이미지와 텍스트를 함께 가진다 (PDF p.53)
├─ Pipeline과 Processor·Model 호출
│  ├─ 준비된 VLM으로 이미지 질문하기 (PDF p.54)
│  ├─ transformers.pipeline() (PDF p.55)
│  ├─ Processor와 Model을 직접 사용하는 흐름 (PDF p.56)
│  ├─ processor.apply_chat_template() (PDF p.57)
│  └─ model.generate() (PDF p.58)
├─ Grounding·출력 계약·Hybrid
│  ├─ VLM이 잘하는 설명과 위험한 추론을 구분한다 (PDF p.59)
│  ├─ 문서 VLM 프롬프트 구조 (PDF p.60)
│  └─ OCR과 VLM을 결합하는 세 가지 방식 (PDF p.61)
└─ 실습과 개념 확인
   ├─ 실습 04 · VLM 이미지 질의응답 (PDF p.62)
   └─ 3분 퀴즈 · VLM (PDF p.63)

5교시 · OCR·VLM 결합·평가·보안
├─ 질의응답 유형과 JSON 최소 검사
│  ├─ VLM 질의응답의 대표 유형 (PDF p.64)
│  ├─ Invoice 질문응답: 답변보다 근거를 함께 본다 (PDF p.65)
│  └─ VLM 응답 JSON의 최소 검사 (PDF p.66)
├─ 동일 데이터 비교와 접근 선택
│  ├─ OCR·VLM·Hybrid를 같은 데이터에서 비교한다 (PDF p.67)
│  └─ 문제 유형별 권장 접근 (PDF p.68)
├─ 보안·입력 크기·비디오 Frame
│  ├─ 문서 VLM 보안·개인정보 점검표 (PDF p.69)
│  ├─ VLM 입력 크기와 메모리의 관계 (PDF p.70)
│  └─ 비디오 VLM은 Frame 선택이 먼저다 (PDF p.71)
└─ 실습과 개념 확인
   ├─ 실습 05 · OCR·VLM·Hybrid 비교 (PDF p.72)
   └─ 3분 퀴즈 · OCR·VLM 평가 (PDF p.73)

6교시 · TensorRT·Jetson·DeepStream 배포 설계
├─ ONNX·TensorRT와 Build·Runtime
│  ├─ 지원되는 Vision 모델의 엣지 배포 흐름 (PDF p.74)
│  ├─ ONNX와 TensorRT의 역할 (PDF p.75)
│  ├─ TensorRT는 Build Phase와 Runtime Phase로 나뉜다 (PDF p.76)
│  ├─ trtexec 빌드·추론 명령 예시 (PDF p.77)
│  └─ TensorRT 핵심 객체 (PDF p.78)
├─ Engine 호환성과 Jetson·DeepStream
│  ├─ TensorRT Engine의 호환성을 가볍게 보지 않는다 (PDF p.79)
│  ├─ Jetson에서 고려할 것 (PDF p.80)
│  ├─ DeepStream 영상 추론 파이프라인 (PDF p.81)
│  └─ 엣지 추론에서 함께 기록할 지표 (PDF p.82)
└─ 실습과 개념 확인
   ├─ 실습 06 · TensorRT·Jetson·DeepStream 배포 설계 (PDF p.83)
   └─ 3분 퀴즈 · TensorRT와 DeepStream (PDF p.84)

7교시 · OCR·VLM 미니 애플리케이션 통합
├─ 모듈 구조와 처리 이력
│  ├─ OCR·VLM 미니 애플리케이션 구조 (PDF p.85)
│  ├─ 프로젝트 폴더와 역할 (PDF p.86)
│  └─ 한 문서의 처리 기록을 끝까지 연결한다 (PDF p.87)
├─ OCR·VLM 인터페이스와 결과 결합
│  ├─ OCR Module 인터페이스 설계 예시 (PDF p.88)
│  ├─ VLM Module 인터페이스 설계 예시 (PDF p.89)
│  └─ OCR·VLM 결과를 합치는 규칙 예시 (PDF p.90)
├─ 산출물과 실패 상황
│  ├─ 최종 산출물 (PDF p.91)
│  └─ 정상·경계·실패 상황 (PDF p.92)
└─ 통합 실습
   └─ 실습 07 · OCR·VLM 미니 애플리케이션 통합 (PDF p.93)

8교시 · 최종 검증·평가·만족도·회고
├─ 제출물과 재실행 검증
│  ├─ 과목 최종 제출물 (PDF p.94)
│  └─ 실습 08 · 최종 검증·보고서·시연 (PDF p.95)
└─ 형성평가와 만족도
   ├─ 형성평가 기준 · 100점 (PDF p.96)
   └─ 과목 만족도 조사 · 학습평가와 분리 (PDF p.97)

마무리 · 핵심 정리와 다음 수업
└─ 문서 AI 복습과 서비스 연결
   ├─ 오늘의 핵심 정리 (PDF p.98)
   └─ 다음 수업 · Vision 결과를 FastAPI 서비스로 (PDF p.99)

참고자료 · 공식 문서
└─ OCR·VLM과 엣지 배포 문서
   ├─ 공식 참고자료 · OCR·OpenCV·VLM (PDF p.100)
   └─ 공식 참고자료 · TensorRT·Jetson·DeepStream (PDF p.101)
```

## 핵심 설명

### 도입 · 문서 AI의 전체 흐름과 수업 범위

#### OCR·구조화·VLM·배포의 전체 지도

##### Vision·멀티모달 AI 응용 (PDF p.1)

- 정규교과 4/4 표지
- 문서의 문자 인식부터 구조화·질의응답·엣지 배포까지 연결하는 Day16 학습 흐름

##### 현업의 문서 처리와 OCR·VLM (PDF p.2)

- 가상 청구서에서 글자와 위치를 읽고 필요한 값을 업무 데이터로 변환하는 예시
- OCR은 글자·위치 추출, VLM은 답변 후보 생성, 검증은 원문·규칙 대조 역할
- 업무 전달 기록은 필드 값·원문 위치·검토 이유·재확인 가능한 실행 이력

##### 오늘 만드는 문서 AI의 전체 구조 (PDF p.3)

- OCR 경로는 문서 이미지 → OCR용 전처리 → 글자·위치·점수
- VLM 경로는 원본 또는 적절한 Crop과 질문 → 답변·근거 후보
- 두 경로를 선택하거나 결합한 뒤 원문·형식·업무 규칙으로 검증
- 저장 대상은 필드 JSON·검토 목록·질문과 답변 기록·평가표
- 기본 실습은 제공 OCR 결과와 VLM 응답 예시 활용 가능

##### OCR 내부의 영역·문자·읽기 순서 (PDF p.4)

- 이미지 준비 → 영역·줄 분할 → 문자 인식 → 읽기 순서·구조 정리
- 전체 문서는 페이지 구조, 한 줄 Crop은 줄 인식, 표 영역은 행·열 관계 확인에 사용
- 전처리 후보는 OCR 오류와 원문 보존을 함께 확인해 선택

##### OCR 결과 안의 단어 한 건 (PDF p.5)

- `OCRResult.words[k]`는 단어 문자열·confidence·bbox를 묶은 결과
- 가상 단어 `1,234,500원`의 confidence는 88.6, xyxy bbox는 `[530,820,790,865]`
- 좌표 기준은 설명용 1000×1200 전처리 이미지의 픽셀
- 원본에 Box를 표시할 때 전처리 좌표에서 원본 좌표로 변환

##### 문자열을 업무 필드로 바꾸는 구조화 (PDF p.6)

- `raw="1,234,500원"`을 보존하면서 `value=1234500`, `currency="KRW"`로 구조화
- 라벨·페이지·bbox를 값과 연결해 출처 유지
- 필수 항목·자료형·원문 일치·금액 관계를 확인하고 상태와 검토 이유 기록

##### VLM의 입력 처리와 모델 내부 (PDF p.7)

- `messages`의 user content에 이미지 항목과 질문 항목을 함께 구성
- Processor는 이미지 전처리·대화 형식·토큰화를 담당
- 대표 생성형 VLM은 Vision Encoder → 연결 모듈 → 언어모델 순서로 시각 특징과 질문을 연결
- 모델마다 입력 키와 세부 연결 방식이 다르므로 해당 모델의 입력 형식 확인

##### VLM 답변 한 건의 값·근거·상태 (PDF p.8)

- `answer`·`evidence`·`page`·`bbox`를 분리해 응답 후보 저장
- 값과 원문 문자열, 페이지·좌표의 실제 영역, 스키마·업무 규칙을 각각 대조
- 근거가 없으면 `null`과 검토 이유를 남기고 확인 완료·검토 필요·실패로 구분

##### OCR·VLM 결과를 평가하는 서로 다른 단위 (PDF p.9)

- 글자 오류·필드 정답·JSON 문법·원문 근거는 서로 다른 평가 단위
- 가상 금액 `1234500`을 `12345O0`으로 읽으면 정답 7글자 중 1글자 치환으로 CER 약 14.3%
- 같은 예시의 필드 정확도 2/3과 JSON 문법 유효성 1/1은 금액의 근거 일치를 보장하지 않음
- 비교 조건은 같은 문서·정답·정규화 규칙·측정 구간으로 고정

##### TensorRT·Jetson·DeepStream의 역할 (PDF p.10)

- TensorRT는 지원 모델의 엔진 빌드·추론 소프트웨어, Jetson은 현장 실행 장치
- DeepStream은 영상 입력부터 추론 결과까지 연결하는 파이프라인
- 지원 모델·ONNX 확인 → 대상 환경 엔진 Build → Runtime 품질·지연 검증 순서
- 기본 범위는 배포 설계, PC·서버 TensorRT 11.3 예시와 Jetson의 JetPack 지원 조합 구분
- 모든 OCR·VLM 애플리케이션을 하나의 엔진으로 변환하는 구조는 아님

##### 문서 AI 프로젝트로 다시 합치기 (PDF p.11)

- 문서·질문 준비 → OCR 결과·필드 정리 → 답변·근거 확인 → 저장·재실행·설명
- 기본 프로젝트는 전처리·제공 OCR 결과·필드 JSON 저장과 재생성
- 제공 VLM 응답 근거 검토와 평가표 해석은 공통 확인 활동
- 실제 VLM 호출·모듈화·GPU·엣지는 선택 확장
- 1~3교시 OCR·구조화, 4~5교시 VLM·평가, 6교시 배포 설계, 7~8교시 통합·검증으로 연결

#### 복습·운영·환경·자료 관리

##### 지난 수업에서 연결한 Vision 흐름 (PDF p.12)

- OpenCV의 픽셀·색공간·필터·형태학·증강 복습
- 사전학습 Backbone의 Head-only·Partial fine-tuning 연결
- YOLO의 객체 위치·클래스·IoU·mAP·추적 분석을 문서 문자 위치와 근거 검토로 확장

##### 3분 확인 퀴즈 · Vision 복습 (PDF p.13)

- 전처리 설정 선택용 개발·검증 문서와 최종 평가 문서의 분리 확인
- 객체탐지 Box와 OCR Word Box의 공통 위치 표현 및 OCR의 문자열·줄·블록 연결 확인
- 자연스러운 VLM 답변에도 이미지·OCR 원문 근거 검증이 필요하다는 점 확인

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 1교시 OCR 전체 흐름·문서 전처리, 2교시 OCR 실행·Box·품질평가
- 3교시 문서 정보 추출·JSON 구조화, 4교시 VLM 개요·이미지 질의응답
- 5교시 OCR·VLM 결합·평가·보안, 6교시 TensorRT·Jetson·DeepStream
- 7교시 OCR·VLM 미니 애플리케이션, 8교시 과목 실습평가·만족도·회고
- 1교시는 설명·시연 30분과 실습·리뷰 20분, 2~7교시는 각각 25분, 8교시는 각각 20분과 30분

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘 범위는 문서 보정·OCR 결과·Key-value·Table·JSON·VLM 근거 평가·배포 흐름
- 다음 수업은 HTTP 요청·응답·상태코드와 OCR·VLM 결과 조회 REST API
- 오늘 만든 JSON을 다음 수업의 API 입력으로 활용
- 실제 GPU·엣지 실행은 준비된 환경의 선택 확장

##### 실습 환경과 실행 범위를 먼저 구분한다 (PDF p.16)

- 기본 환경은 Python·OpenCV·NumPy·pandas와 Tesseract 또는 제공 OCR 결과
- VLM은 준비된 모델의 Pipeline·Processor 또는 제공 응답으로 진행
- PC TensorRT 환경과 JetPack 호환 Jetson 환경을 별도로 구분
- Python·패키지·모델·언어 데이터 버전과 장치 호환성을 기록
- 배포 실습자료 기준 VLM 기본 경로는 mock, TensorRT·Jetson·DeepStream은 설계·정적 검사 범위

##### 문서 이해 서비스의 전체 흐름 (PDF p.17)

- 문서 이미지 → 기울기·대비·이진화 전처리 → OCR Text·Box·점수 → 필드·표·JSON 구조화 → 다음 API
- VLM은 이미지와 질문을 받아 답변을 만드는 경로로 연결
- 문자를 읽는 결과와 업무 필드로 구조화한 결과를 구분

##### 문서 AI에서 처음부터 지켜야 할 원칙 (PDF p.18)

- 개인정보·기업기밀의 외부 OCR·VLM 업로드 허용 범위 확인
- 원본·전처리본·OCR 결과·최종 JSON을 분리해 추적 가능하게 보존
- 답변의 자연스러움보다 문서 근거·좌표·원문 문자열 우선
- 문서 유형·해상도·언어·표 구조별 오류 기록

### 1교시 · OCR 전체 흐름·문서 전처리

#### OCR 단계와 문서 입력의 어려움

##### OCR은 이미지에서 문자를 읽는 전체 과정이다 (PDF p.19)

- 스캔·사진·PDF 페이지·화면 캡처에서 입력 획득
- 회전·원근·밝기·대비·노이즈·이진화 전처리 후 문자·단어·줄·영역 인식
- 읽기 순서·띄어쓰기·단위·날짜·금액 후처리
- 필요한 항목을 JSON·표·검색 가능한 문서로 변환

##### 문서 이미지에서 글자까지 (PDF p.20)

- 사진 문서의 기울기·그림자·배경 노이즈를 보정하는 흐름
- Gray·Threshold·Deskew 결과를 OCR에 전달해 Text·Box·Confidence 획득
- 원문·좌표·JSON을 후속 처리의 근거로 보존

##### 문서 이미지가 어려운 이유 (PDF p.21)

- 회전·원근 왜곡은 글줄 방향을, 조명·그림자·반사광은 배경 밝기를 변화시킴
- 압축·흔들림·저해상도는 글자 획 손실, 무늬·도장·서명은 글자 가림의 원인
- 다단·표·머리글·각주·세로쓰기는 읽기 순서 복원의 어려움
- 유사 문자와 혼합 언어·단위·통화기호 구분 필요
- 체크박스·도장·선·바코드 등 비문자 요소와 텍스트 구분

#### 이미지 읽기·Gray·이진화

##### 이미지 읽기와 Gray 변환 (PDF p.22)

- `cv2.imread`는 기본 BGR 순서의 ndarray, 읽기 실패 시 `None` 반환
- `cv2.cvtColor(..., cv2.COLOR_BGR2GRAY)` 결과는 채널 축 없는 `[H,W]`
- 원본을 덮어쓰지 않고 Gray 이미지를 별도 저장
- `cv2.imwrite` 반환값으로 저장 실패 확인

##### cv2.imread()와 cv2.cvtColor() (PDF p.23)

- `imread`의 필수 인자는 이미지 경로 `filename`, `flags`는 읽기 방식 선택
- `cvtColor`의 필수 인자는 입력 배열 `src`와 변환 상수 `code`
- `dstCn=0`은 출력 채널 수 자동 결정
- 반환값은 읽은 배열 또는 `None`, 색 변환 후 배열로 구분

##### 이진화는 글자와 배경을 분리한다 (PDF p.24)

- Gray 밝기 0~255에 임계값을 적용해 두 픽셀 값으로 분리
- 예시는 글자 0·배경 255의 Binary 표현
- 픽셀 분리 결과와 실제 문자 인식 품질을 구분

##### 전역 Threshold와 적응형 Threshold (PDF p.25)

- `cv2.threshold`는 지정 임계값 또는 Otsu 자동 추정 임계값 적용
- `cv2.adaptiveThreshold`는 주변 블록 통계로 픽셀별 지역 임계값 계산
- 예제 `blockSize=31`, `C=11`은 비교용 설정
- `blockSize`는 3 이상 홀수, `C`는 지역 기준에서 빼는 상수

##### cv2.adaptiveThreshold() (PDF p.26)

- 입력 `src`는 8-bit 단일 채널 Gray 이미지
- `maxValue`는 조건 만족 픽셀 값, 일반적으로 255
- 지역 통계는 `MEAN_C` 또는 `GAUSSIAN_C`, 출력 방식은 `BINARY` 또는 `BINARY_INV`
- `blockSize`는 3 이상 홀수, `C`는 평균·가중평균에서 빼는 상수
- 반환값은 입력과 같은 높이·너비의 8-bit 이진 배열

#### 원근 보정과 좌표 변환

##### 원근 보정은 문서를 정면에서 본 모양으로 바꾼다 (PDF p.27)

- 촬영 문서의 네 모서리 `src`를 정면 문서의 네 모서리 `dst`에 대응
- 변환행렬 M으로 원근 왜곡을 보정

##### 문서 네 모서리로 Perspective 보정 (PDF p.28)

- 실제 문서의 네 모서리와 출력 모서리의 순서를 동일하게 구성
- `getPerspectiveTransform`은 3×3 행렬, `warpPerspective`는 보정 이미지 생성
- 출력 크기 `dsize`는 `(width,height)`, 예시는 `(700,1000)`
- OCR Box가 보정본 기준이면 원본 표시 시 역변환 필요
- 배포 응용 실습은 알려진 모서리를 사용하며 자동 모서리 검출과 구분

#### 실습과 개념 확인

##### 실습 01 · 문서 이미지 전처리 (PDF p.29)

- 20분 실습, 기본필수는 문서 3장의 Gray·Otsu 결과를 저장하고 shape·Threshold 기록
- 응용은 Adaptive Threshold·Perspective 보정 결과의 가독성 비교
- 심화는 회전·그림자·저해상도 후보를 검증 문서 CER로 선택
- 특심화는 좌표 순서·출력 크기·원본 보존을 검사하는 Pipeline과 단위 테스트
- 완료 기준은 기본 결과 저장·설정 기록 후 동일 입력·평가 조건에서 선택 확장

##### 3분 퀴즈 · OCR 전처리 (PDF p.30)

- Adaptive Threshold의 `blockSize` 조건과 `warpPerspective` 출력 크기 순서 확인
- 사람의 가독성과 OCR 오류율이 항상 같지 않다는 점 확인

**핵심:** 전처리는 원본과 좌표 변환을 보존하면서 비교하고, 육안 가독성과 검증 문서의 OCR 오류를 함께 근거로 선택.

### 2교시 · OCR 실행·Box·품질평가

#### OCR 출력 형식과 페이지 구조 가정

##### OCR 엔진은 문자뿐 아니라 위치와 신뢰도를 출력할 수 있다 (PDF p.31)

- Plain text는 전체 문자열, TSV·DataFrame은 단어별 문자열·점수·위치 표현
- HOCR·ALTO XML은 페이지·문단·줄·단어 구조와 위치 표현
- Searchable PDF는 이미지 위에 보이지 않는 텍스트 레이어 추가
- 별도 Detector·Recognizer 구성에서는 영역 탐지와 문자 인식 분리

##### Page Segmentation Mode는 “페이지 구조 가정”이다 (PDF p.32)

- PSM 3은 자동 페이지 분할, PSM 6은 균일한 텍스트 블록 가정
- PSM 7은 한 줄, PSM 8은 한 단어 가정
- Crop 영역의 구조에 맞는 PSM 선택
- 배포 실습의 PSM 3·6 전체 페이지와 PSM 7 한 줄 Crop은 평가 대상이 달라 CER 단순 순위화 제외

#### 단어 DataFrame과 Box·읽기 순서

##### 단어별 OCR 결과를 DataFrame으로 받기 (PDF p.33)

- Tesseract 실행 파일과 사용할 언어 데이터 설치 여부 확인
- 예제는 `image_to_data`에 `lang="kor+eng"`, `--oem 3 --psm 6`, `Output.DATAFRAME` 전달
- `pandas_config`에서 `text`를 문자열로 읽고 기본 NA 변환을 꺼 숫자·NA 표기 보존
- `level=5`이고 공백이 아닌 단어를 선택해 `text`·`conf`·위치 확인
- confidence 50 미만은 설명용 검토 목록이며 원본 OCR 결과 삭제 기준이 아님
- 배포 기본필수 실제 OCR은 영어 합성 문서와 `eng` 언어팩을 사용하는 경로

##### pytesseract.image_to_data() (PDF p.34)

- 필수 입력은 이미지·RGB 또는 Gray 배열·이미지 경로
- `lang`은 설치 언어 조합, `config`는 PSM·OEM 옵션 문자열
- `output_type`으로 TSV 문자열·dict·DataFrame 등 반환 형식 선택
- `timeout`은 초 단위 제한이며 0은 제한 없음
- `pandas_config`는 DataFrame 생성 시 `read_csv` 옵션

##### OCR Box·Line·Reading order (PDF p.35)

- 단어 Box에 Text·Confidence 연결
- Line·Block 관계를 이용해 읽기 순서 구성
- 제목 → 본문 → 표 → 합계 같은 구조는 좌표 목록과 별도의 복원 대상

#### Confidence 해석과 품질 지표

##### OCR Confidence를 해석할 때 (PDF p.36)

- 낮은 점수의 단어는 검토 대상으로, 같은 필드의 상대 점수는 후보 비교에 사용
- 문서 유형별 점수 분포와 원본 Crop을 함께 확인
- 엔진별 confidence 스케일·의미 차이 존재
- 짧은 숫자·기호는 낮은 점수여도 정답 가능, 높은 점수도 문맥상 정답 보장 불가
- 단일 Threshold로 모든 문서의 낮은 점수 단어를 자동 삭제하지 않음

##### OCR 품질은 글자·단어·필드 단위로 나누어 평가한다 (PDF p.37)

- CER은 글자 단위 치환·삭제·삽입 횟수를 정답 글자 수로 나눈 값
- WER은 단어 단위 치환·삭제·삽입 횟수를 정답 단어 수로 나눈 값
- Field accuracy는 날짜·금액·문서번호 등 필수 항목이 정확한 비율
- 읽기 순서·표 셀·Box의 구조 평가는 기준과 분모 별도 정의
- 페이지당 전처리·OCR·후처리 시간을 구간별 기록

##### 간단한 CER 계산 함수 (PDF p.38)

- Levenshtein distance는 두 문자열 사이 치환·삭제·삽입의 최소 횟수
- `cer`는 편집거리를 정답 문자열 길이로 나누어 계산
- 빈 정답 문서는 예제 함수에서 제외하고 별도 집계
- 공백·대소문자·기호 정규화 규칙을 비교 전에 고정
- 문서별 CER의 평균과 전체 정답 글자 수 기준 micro CER 구분

#### 실습과 개념 확인

##### 실습 02 · OCR 실행·Box·품질평가 (PDF p.39)

- 25분 실습, 기본필수는 문서 3장의 실제 또는 제공 OCR 문자열·단어 수·평균 confidence 확인
- 응용은 단어 Box 시각화와 입력 영역에 맞는 PSM 3·6·7 비교
- 심화는 CER·필드 정확도·Latency를 전처리별 표로 정리
- 특심화는 읽기 순서·confidence 정책을 포함한 OCR 결과 데이터 클래스와 테스트
- 완료 기준은 결과의 입력 영역·설정·실제 또는 제공 출처 확인

##### 3분 퀴즈 · OCR 결과와 평가 (PDF p.40)

- 한 줄 입력의 PSM 선택과 CER 분모 확인
- confidence와 문맥 정답 확률의 차이 확인

**핵심:** OCR은 문자열·위치·점수를 함께 읽고, 같은 입력 범위에서 글자 오류·필드 정답·처리 시간을 분리해 평가.

### 3교시 · 문서 정보 추출·JSON 구조화

#### 문자열 정규화와 필드 후보 추출

##### OCR 문자열을 업무 데이터로 바꾸는 후처리 (PDF p.41)

- 공백·줄바꿈·통화기호·날짜·숫자 형식 정규화
- 제목·본문·표·합계·서명을 역할별 Block으로 분리
- 문서번호·날짜·공급자·합계·세금·계좌번호 등 필요한 필드 추출
- 원문·정규화값·Box·confidence·검증 상태를 JSON으로 저장

##### 정규표현식으로 날짜와 금액 찾기 (PDF p.42)

- 날짜 패턴은 후보 탐색, `date` 객체는 실제 날짜 유효성 검증
- 유효한 날짜는 ISO 형식, 오류·미발견은 `None` 유지
- 금액은 합계 라벨 뒤 후보를 찾아 쉼표 제거 후 정수 변환
- 원문과 정규화값을 모두 보존하고 표기 변형·금액 범위는 별도 검증

##### re.search()와 re.sub() (PDF p.43)

- `search(pattern,string,flags=0)`는 첫 패턴 후보의 Match 또는 `None` 반환
- `sub(pattern,repl,string,count=0,flags=0)`는 치환한 새 문자열 반환
- `count=0`은 전체 치환, `flags`는 대소문자·여러 줄 등 동작 옵션
- 검색 결과 존재 여부 확인 후 그룹 값 사용

#### 라벨·값·근거와 JSON 기록

##### Key-value 추출은 “라벨·값·근거”를 묶는다 (PDF p.44)

- 발행일·공급자·합계 라벨을 해당 값과 연결
- 날짜·금액 후보에 원문 Box·confidence·검증 상태 부여
- 첫 숫자를 금액으로 선택하는 대신 라벨과 위치 관계로 필드 식별

##### 필드와 근거를 JSON으로 저장 (PDF p.45)

- `value`는 정규화값, `raw`는 OCR 원문
- 필드별 confidence·bbox와 문서 ID·페이지·이미지 크기·좌표계 저장
- 설명용 좌표는 1000×1200 이미지 기준이며 앞선 700×1000 보정본과 별개
- 실제 기록에는 이미지 경로·변환·schema version 추가
- UTF-8과 `ensure_ascii=False`로 원문 문자를 보존해 저장

#### 표 구조와 업무 규칙 검증

##### 표 추출은 “셀 구조”가 핵심이다 (PDF p.46)

- 선이 분명하고 열 위치가 일정한 표는 셀 Crop·한 줄 OCR·금액 관계 검증으로 처리 가능
- 선 없는 표·다단 헤더·병합 셀은 추가 모델·규칙의 대상
- 문서마다 바뀌는 열 위치와 셀 소속·읽기 순서 복원은 문자 인식과 별개 문제

##### 구조화 결과에 업무 규칙을 적용한다 (PDF p.47)

- 필수 필드는 `document_id`·`issued_at`·`supplier`·`total_amount`
- 날짜 ISO 8601·금액 정수·통화 별도 필드의 형식 검증
- 공급가액+세액=합계, 수량×단가≈금액의 관계 확인
- 날짜·금액·수량의 허용 범위 확인
- `passed`·`warning`·`failed`와 사람이 확인할 이유 기록

##### 필수 필드와 금액의 최소 검증 (PDF p.48)

- 입력과 `fields`가 dict인지 확인한 뒤 필드 접근
- 필수 값의 `None`·빈 문자열과 유효한 금액 0 구분
- 합계는 `type(value) is int`인 0 이상 값으로 제한해 bool 제외
- 오류 목록과 검토 필요 여부를 별도 기록
- 날짜·문자열·좌표의 전체 검증은 Schema로 확장하는 범위

#### 실습과 개념 확인

##### 실습 03 · 문서 정보 추출·구조화 (PDF p.49)

- 25분 실습, 기본필수는 제공 OCR의 발행일·공급자·합계를 JSON으로 저장
- 응용은 라벨 오른쪽 단어를 찾아 raw·value·confidence·bbox 저장
- 심화는 표 3행과 금액 관계·필수 필드·읽기 순서 검증
- 특심화는 문서 유형별 Extractor·Schema version·정상·누락·오인식 테스트
- 완료 기준은 원문 근거를 보존한 필드 JSON과 검증 결과 확인

##### 3분 퀴즈 · 구조화 (PDF p.50)

- 정규화값만 저장할 때 원문·위치 추적이 어려워지는 이유 확인
- 문자 인식과 표 셀·행·열 구조 인식의 차이 확인
- 검증 실패를 0·빈 문자열로 덮지 않고 상태·검토 이유로 남기는 기준 확인

**핵심:** 구조화는 라벨과 값의 관계를 원문·좌표와 함께 저장하고, 형식·범위·업무 관계를 별도로 검증하는 과정.

### 4교시 · VLM 개요·이미지 질의응답

#### OCR·VLM 역할과 멀티모달 입력

##### OCR과 VLM은 어떤 문제에 강한가? (PDF p.51)

- OCR은 문자·단어·줄 전사와 위치 연결, 숫자·문서번호·규칙 기반 후보 추출에 활용
- VLM은 이미지와 질문을 함께 보고 표·도식·화면의 문맥을 종합
- 문서 유형이 다양하면 VLM 질의응답이 유연하지만 자연스러운 오답·무근거 추론 가능

##### 생성형 VLM의 대표 구성 (PDF p.52)

- Vision Encoder가 이미지 픽셀에서 시각 특징 추출
- Projector가 시각 특징을 언어 공간으로 연결
- LLM이 시각 정보와 질문·지시문을 이용해 답변 생성

##### 멀티모달 메시지는 이미지와 텍스트를 함께 가진다 (PDF p.53)

- `role`은 system·user·assistant 등의 대화 역할
- `content`는 image·text 항목의 목록
- Processor는 이미지 전처리·특수 토큰·Chat template·토큰화를 함께 처리
- `generate`는 준비된 토큰·attention mask·pixel values로 생성 수행
- 지원 이미지 수·해상도·VRAM과 모델별 입력 형식 확인

#### Pipeline과 Processor·Model 호출

##### 준비된 VLM으로 이미지 질문하기 (PDF p.54)

- 준비된 모델 ID·로컬 경로로 `image-text-to-text` Pipeline 구성
- 이미지 경로와 합계·근거 질문을 user messages로 전달
- 예제 생성 조건은 `max_new_tokens=128`, `do_sample=False`
- `return_full_text=False`는 새 답변 부분만 반환하는 옵션
- 실제 모델 호출은 선택 경로, 기본필수는 제공 응답의 근거 검토로 진행 가능

##### transformers.pipeline() (PDF p.55)

- `task`는 수행 작업, `model`은 모델 ID·로컬 경로·로드한 모델
- 모델·Processor·전후처리를 호출 가능한 Pipeline 객체로 구성
- `device_map`은 장치 배치 전략, `dtype`은 모델 자료형
- `processor`는 멀티모달 전처리 객체, `device`는 단일 장치 직접 지정

##### Processor와 Model을 직접 사용하는 흐름 (PDF p.56)

- `AutoProcessor`와 `AutoModelForImageTextToText`를 같은 모델에서 로드
- `apply_chat_template`로 모델 입력을 생성하고 입력 키·Tensor shape 확인
- `generate` 결과는 토큰 ID이며 `decode`로 답변 문자열 변환
- Decoder-only 모델은 입력 토큰 길이만큼 앞부분 제거, Encoder-decoder는 이 제거를 적용하지 않음
- 모델 구조·전처리·생성 조건을 실행 이력으로 기록

##### processor.apply_chat_template() (PDF p.57)

- `messages`를 모델별 멀티모달 대화 형식으로 변환
- `add_generation_prompt`는 답변 시작 위치 추가 옵션
- `tokenize=False`는 문자열 포맷, `True`는 토큰화까지 수행
- `tokenize=True`·`return_dict=True`는 `input_ids`·`pixel_values` 등의 입력 dict 반환
- `return_tensors="pt"`는 PyTorch Tensor, `num_frames`는 지원 모델의 비디오 샘플링 옵션

##### model.generate() (PDF p.58)

- Processor 입력을 바탕으로 다음 토큰을 반복 생성
- `max_new_tokens`는 새 토큰 수 상한, `do_sample`은 샘플링 여부
- `temperature`는 `do_sample=True`일 때 샘플링 분포 조절
- `num_beams` 증가는 탐색 비용 증가, `use_cache`는 Key/Value cache 재사용
- 기본 반환값은 생성 토큰 ID Tensor, 옵션에 따라 GenerateOutput 반환

#### Grounding·출력 계약·Hybrid

##### VLM이 잘하는 설명과 위험한 추론을 구분한다 (PDF p.59)

- 관찰은 실제 보이는 글자·색·표·객체 설명
- 추론은 목적·의도·원인·법적 의미의 추정
- Hallucination은 보이지 않는 값·표·근거 생성
- Grounding은 원문 문자열·페이지·Box·Crop으로 답변을 연결하는 기록
- 근거가 부족하면 확인 불가와 검토 필요 상태 반환

##### 문서 VLM 프롬프트 구조 (PDF p.60)

- 입력에 문서 유형·페이지 범위·질문과 이미지에서 허용되는 정보 범위 명시
- 모르는 값은 `null` 또는 확인 불가, 금액·날짜·문서번호는 원문도 반환
- 출력 JSON key·자료형을 고정하고 answer·evidence·page·bbox 분리
- 지원하지 않는 좌표·근거는 `null`
- 스키마·원문 검증 실패는 재시도 또는 사람 검토로 연결

##### OCR과 VLM을 결합하는 세 가지 방식 (PDF p.61)

- OCR Text·Box → 규칙·Schema 경로는 정형 문서에 적용
- VLM → 근거 검증 경로는 다양한 문서 질의응답에 적용
- OCR과 Crop → VLM 판단 경로는 두 방식의 결합

#### 실습과 개념 확인

##### 실습 04 · VLM 이미지 질의응답 (PDF p.62)

- 25분 실습, 기본필수는 이미지와 질문 3개의 messages 및 실제·제공 응답의 문자열·근거 저장
- 응용은 JSON·모르면 null·근거 필드를 자유 응답과 비교
- 심화는 OCR 대조로 근거 있는 답·근거 없는 답·부분 정답 분류
- 특심화는 Processor·생성 옵션·장치·입력 해상도를 Config로 관리하고 재현성·메모리 검사
- 배포 기본 경로의 messages JSON 저장·mock 파일 읽기는 실제 모델 생성과 구분

##### 3분 퀴즈 · VLM (PDF p.63)

- 멀티모달 Chat template를 담당하는 Processor 역할 확인
- `do_sample=False`로 결과 변동을 줄이는 이유 확인
- 금액·날짜·번호 답변의 OCR 원문·위치 대조 필요성 확인

**핵심:** VLM은 모델별 Processor로 이미지와 질문을 구성해 답변 후보를 생성하며, 후보의 값·원문·좌표를 확인한 뒤 상태 결정.

### 5교시 · OCR·VLM 결합·평가·보안

#### 질의응답 유형과 JSON 최소 검사

##### VLM 질의응답의 대표 유형 (PDF p.64)

- 읽기는 문서 제목, 탐색은 합계 영역의 위치 확인
- 비교는 두 표의 변화, 설명은 흐름도 단계·관계 요약
- 검증은 OCR 결과와 이미지의 날짜 등 원문 일치 확인

##### Invoice 질문응답: 답변보다 근거를 함께 본다 (PDF p.65)

- 합계 질문에 answer뿐 아니라 page·evidence·bbox를 함께 기록
- 예시 답변 `1,234,500원`을 실제 문서의 합계 영역과 연결
- 근거 위치가 없는 답변과 원문 위치를 확인한 답변 구분

##### VLM 응답 JSON의 최소 검사 (PDF p.66)

- JSON 구문 오류와 최상위 dict 여부 확인
- 필수 key `answer`·`evidence`·`page`·`bbox`의 누락 확인
- bbox는 수치 4개의 목록이며 `0≤x1<x2≤1000`, `0≤y1<y2≤1200` 검사
- 1000×1200은 설명용 이미지 크기, 실제 검사는 해당 기준 이미지 크기 사용
- 이 코드는 최소 검사이며 answer·page·evidence의 전체 검증과 원문·Crop 대조는 별도

#### 동일 데이터 비교와 접근 선택

##### OCR·VLM·Hybrid를 같은 데이터에서 비교한다 (PDF p.67)

- 동일 문서·질문·정답에서 필드 정확도·근거 일치·총 시간 비교
- OCR은 CER·Box IoU, VLM은 답변·JSON 유효성·근거 없는 답 평가
- Hybrid는 필드 정확도·검토율·실패 복구율·총 비용 평가
- 영수증·계약서·표·손글씨·저해상도·다국어 Slice별 오류 분리
- 운영 비교는 처리량·VRAM·로딩시간·개인정보 처리 위치 포함
- 배포 mock·기록 경로는 평가 구조 연습이며 실제 모델 추론 시간은 미측정 `null`

##### 문제 유형별 권장 접근 (PDF p.68)

- 정확한 문서번호 전사는 OCR 우선과 VLM 검증의 조합
- 표·도식 의미 설명은 VLM에 OCR 원문을 함께 제공하는 접근
- 고정 양식 Key-value는 규칙 추출 후 예외 문서를 VLM으로 전달
- 다양한 문서 질의응답은 VLM의 유연성과 OCR evidence 연결
- 엣지 실시간 처리는 모델 규모·비용을 고려한 단계별 라우팅

#### 보안·입력 크기·비디오 Frame

##### 문서 VLM 보안·개인정보 점검표 (PDF p.69)

- 외부 API 전송 이미지의 개인정보·계약정보 확인
- 원본·OCR 원문·프롬프트·응답·로그의 보존 기간 설정
- 프로젝트 폴더·Object Storage·Model cache 접근 권한 확인
- 민감 영역 마스킹 여부와 자동 추출 결과의 후속 사용 범위 확인

##### VLM 입력 크기와 메모리의 관계 (PDF p.70)

- Processor의 해상도·패치·이미지 수 증가는 계산·메모리 비용 증가 요인
- 큰 문서는 필요한 영역 Crop·페이지 분할과 질문 관련 페이지 선택 검토
- 모델 로딩 메모리와 추론 Activation·KV cache 구분
- GPU는 워밍업 후 같은 조건의 Latency·처리량·Peak VRAM 비교

##### 비디오 VLM은 Frame 선택이 먼저다 (PDF p.71)

- 고정 간격·장면 변화·이벤트 중심으로 Frame 샘플링
- `num_frames`는 모델 지원 길이·샘플링 정책·자원에 맞게 설정
- 프레임별 OCR·탐지 결과를 VLM의 요약 근거로 활용 가능
- frame index·timestamp로 시간 순서 보존
- 특정 프레임 관찰과 영상 전체 결론 구분

#### 실습과 개념 확인

##### 실습 05 · OCR·VLM·Hybrid 비교 (PDF p.72)

- 25분 실습, 기본필수는 문서 5장의 질문별 정답과 OCR 필드 정확도 비교
- 응용은 VLM answer·evidence·JSON 유효성을 분리 평가
- 심화는 같은 문서에서 OCR-only·VLM-only·Hybrid의 정확도·Latency·사람 검토 수 비교
- 특심화는 Slice·마스킹·비용·VRAM을 포함한 평가 Harness와 회귀 테스트
- 배포 실습은 5문서×3필드=15필드 분모를 유지하고 답변 커버리지·검토 수를 함께 기록
- 보류를 정답으로 집계하지 않고 정답 파일은 평가에만 사용

##### 3분 퀴즈 · OCR·VLM 평가 (PDF p.73)

- JSON 파싱 성공과 내용의 사실성·근거 일치 차이 확인
- 전체 최대 해상도와 필요한 영역 Crop의 비용 차이 확인
- Hybrid는 역할 분리와 실패 보완이며 두 모델 점수 평균과 다른 개념임을 확인

**핵심:** OCR·VLM·Hybrid는 같은 문서와 분모에서 값·형식·근거·보류·검토를 나누어 평가하고, 실측 출처와 처리 비용을 함께 기록.

### 6교시 · TensorRT·Jetson·DeepStream 배포 설계

#### ONNX·TensorRT와 Build·Runtime

##### 지원되는 Vision 모델의 엣지 배포 흐름 (PDF p.74)

- 지원 PyTorch Model → ONNX Graph → TensorRT Engine → Jetson·GPU Runtime → 애플리케이션
- 영상 연결은 Decode → Batch → Infer → Track → Display의 DeepStream 흐름
- 배포 실습은 지원 신경망 모델의 경로 설계이며 Tesseract 자체의 ONNX 변환 과제가 아님

##### ONNX와 TensorRT의 역할 (PDF p.75)

- ONNX는 입력·출력 이름·shape·연산자를 명시하는 계산 그래프 교환 형식
- Export 후 ONNX Runtime 등으로 원본과 수치 대조
- TensorRT는 연산 결합·상수 접기·커널 선택으로 NVIDIA GPU 추론 엔진 최적화
- 강의의 TensorRT 11.x 경로는 정밀도를 모델 Tensor 자료형에 반영
- 동적 shape·지원 연산자·GPU·버전 호환성 확인

##### TensorRT는 Build Phase와 Runtime Phase로 나뉜다 (PDF p.76)

- Build는 ONNX·Network와 BuilderConfig에서 Serialized Engine 생성
- Build 중 커널 후보 측정과 연산 결합·최적화 수행
- Runtime은 Engine 역직렬화 후 ExecutionContext 생성
- 반복 추론은 Buffer·Shape 설정 → 비동기 실행 → 완료 확인 → 출력 읽기
- Engine은 실행 가능한 아티팩트이므로 신뢰 가능한 출처만 로드

##### trtexec 빌드·추론 명령 예시 (PDF p.77)

- `--onnx`는 모델 입력, `--saveEngine`은 빌드 결과 저장, `--loadEngine`은 저장 엔진 실행
- TensorRT 11.3 예시는 FP16 ONNX를 사전 준비하고 수치 검증
- PDF의 11.x 설명에서 `--fp16`은 제거된 옵션으로 구분
- 동적 입력은 실제 입력 이름에 min·opt·max shape 프로파일 지정
- Jetson은 해당 JetPack 호환 버전의 명령 사용
- 실행 성공과 원본 모델 대비 수치 일치 검증을 분리

##### TensorRT 핵심 객체 (PDF p.78)

- Builder는 Network·BuilderConfig로 엔진 빌드
- BuilderConfig는 메모리·타이밍·최적화 프로파일 관리
- Runtime은 Serialized Engine 역직렬화, Engine은 최적화된 입력·출력·연산 정보 보유
- ExecutionContext는 동적 shape·Tensor 주소·추론 상태 관리
- CUDA Stream은 비동기 실행과 동기화 시점 제어

#### Engine 호환성과 Jetson·DeepStream

##### TensorRT Engine의 호환성을 가볍게 보지 않는다 (PDF p.79)

- 기본적으로 OS·플랫폼·TensorRT 버전·GPU 조건을 맞춰 엔진 실행
- 버전·하드웨어 호환 옵션은 편의와 성능의 절충
- 같은 아키텍처여도 VRAM·공유 메모리·커널 선택에 따라 실행 가능성 차이
- 모델·ONNX·Engine·환경·입력 shape의 버전을 manifest로 기록
- 신뢰할 수 없는 엔진 역직렬화 제외

##### Jetson에서 고려할 것 (PDF p.80)

- Camera·Sensor → CPU·GPU Decode·Preprocess → JetPack 호환 TensorRT → App
- JetPack·TensorRT 지원 조합과 카메라 연결 확인
- 전력·온도·공유 메모리·FPS를 장치 조건과 함께 기록

##### DeepStream 영상 추론 파이프라인 (PDF p.81)

- Source의 RTSP·File 입력 → Decode → `nvstreammux` Batch → `nvinfer` TensorRT 추론
- 이후 `nvtracker` → OSD → Sink로 추적·표시·출력 연결
- Metadata에 Frame·Object·Box·Class·Confidence·Track ID 전달

##### 엣지 추론에서 함께 기록할 지표 (PDF p.82)

- End-to-end Latency는 입력부터 결과까지, Model Latency는 전처리·후처리 제외 추론 구간
- Throughput은 초당 처리 이미지·프레임 수
- Queue delay·Dropped frames·Batch wait time 별도 기록
- 메모리·전력·온도·Throttling과 장치별 측정 기준 확인
- 정밀도별 품질 차이와 해상도·Batch·Stream 수에 따른 정확도 기록

#### 실습과 개념 확인

##### 실습 06 · TensorRT·Jetson·DeepStream 배포 설계 (PDF p.83)

- 25분 실습, 기본필수는 PyTorch → ONNX → TensorRT → Runtime 순서도·체크리스트
- 응용은 설치 버전의 입력·출력·정밀도 옵션과 Engine manifest 초안
- 심화는 Jetson 전력·온도·공유 메모리·FPS 측정 계획과 DeepStream 설계
- 특심화는 엔진 호환·동적 shape·다중 Stream·성능 회귀 검사 명세와 테스트
- 완료 기준은 흐름·환경·미실행 범위의 명시, 정적 manifest 검사와 실제 엔진 실행 검증 구분

##### 3분 퀴즈 · TensorRT와 DeepStream (PDF p.84)

- Engine Build와 Runtime의 단계 차이 확인
- 실행 가능한 엔진 파일의 출처 신뢰 경계 확인
- `gst-nvinfer`의 TensorRT 기반 추론 역할 확인

**핵심:** 배포는 지원 모델의 변환·엔진 빌드·실행을 구분하고, 대상 장치의 호환성과 품질·지연·자원을 검증하는 과정.

### 7교시 · OCR·VLM 미니 애플리케이션 통합

#### 모듈 구조와 처리 이력

##### OCR·VLM 미니 애플리케이션 구조 (PDF p.85)

- 문서·질문 입력을 OCR Text·Box·Conf와 VLM Answer·Evidence로 연결
- Fusion·Validation이 Schema·업무 규칙을 검사해 결과 JSON 생성
- 원본·전처리본·OCR JSON·VLM JSON·Report·Log를 아티팩트로 보존

##### 프로젝트 폴더와 역할 (PDF p.86)

- `main`은 입력·실행 순서·출력 경로, `preprocess`는 Gray·Threshold·Perspective 담당
- `ocr`는 Text·Box·Confidence, `extract`는 Key-value·Table·JSON 담당
- `vlm`은 이미지 질의응답, `validate`는 Schema·근거·업무 규칙 담당
- data·outputs·reports를 분리하고 README·환경 명세로 재현 절차 기록
- 슬라이드 구조는 설계 예시이며 기본필수는 한 파일 연결, 모듈 분리는 선택 확장

##### 한 문서의 처리 기록을 끝까지 연결한다 (PDF p.87)

- document_id·원본 hash 생성 후 전처리 설정·결과 이미지 경로 기록
- OCR Text·Box·confidence에 기준 이미지·크기 연결
- 질문·VLM answer·evidence와 Schema·업무 규칙·근거 대조 결과 저장
- 최종 JSON과 사람 검토 목록으로 처리 이력 연결
- 제공 OCR 기록은 실제 기록의 기준 원본에 연결하고 새 전처리본의 신규 추론으로 표시하지 않음

#### OCR·VLM 인터페이스와 결과 결합

##### OCR Module 인터페이스 설계 예시 (PDF p.88)

- `OCRWord`는 text·confidence·xyxy bbox의 공통 구조
- `OCRResult`는 full_text·words·engine 보유
- 설정·기준 이미지·크기는 별도 실행 이력에 저장
- `run_ocr`는 인터페이스 예시이며 엔진·제공 결과 어댑터 구현은 별도

##### VLM Module 인터페이스 설계 예시 (PDF p.89)

- `VLMResult`는 answer·evidence·raw_text·model_id 보유
- 질문·모델 ID·실제 또는 제공 backend를 실행 이력으로 기록
- `ask_document`는 messages 구성까지의 예시이며 실제 호출·응답 파싱은 별도 어댑터
- evidence가 없으면 검토 대상으로 전달

##### OCR·VLM 결과를 합치는 규칙 예시 (PDF p.90)

- 값이 같고 원문·구조·업무 규칙을 통과하면 근거와 `passed` 기록
- 값이 다르면 원문·Crop·업무 규칙 대조 후 `warning`·검토 필요 표시
- VLM 근거 후보는 OCR 위치와 실제 이미지까지 대조
- 두 결과가 모두 없거나 근거가 불일치하면 `failed`·사람 검토
- 최종 선택 규칙은 문서 유형·오류 비용에 따라 설정
- 배포 실습에서 정답 파일은 추출·답변 선택에 사용하지 않고 불일치 값을 자동 덮어쓰지 않음

#### 산출물과 실패 상황

##### 최종 산출물 (PDF p.91)

- `document.json`은 필드 값·원문·bbox·confidence·상태와 Schema·필수 필드 검사
- `ocr_words.csv`는 단어·위치·confidence·페이지와 원본 Crop 대조
- `vlm_answers.json`은 실제·제공 응답·질문·근거 검토와 JSON 유효성 확인
- `evaluation.csv`는 필드 정확도·제공 CER·시간과 측정 출처
- `final_report.md`는 오류·근거 검토·한계·배포 설계와 재실행 아티팩트 경로
- 이름은 강의의 산출물 예시이며 배포 기본필수의 최종 파일은 `p07_documents.json`

##### 정상·경계·실패 상황 (PDF p.92)

- 정상 문서는 필수 필드·Box·원문을 확인해 OCR·필드·근거 생성
- 기울어진 문서는 CER·필드 정확도로 보정 효과 확인 또는 warning
- 표는 행·열·합계 관계 보존 여부를 확인하거나 검토 표시
- VLM 근거 없는 답은 failed 또는 review
- 개인정보 포함 문서는 마스킹·로컬 처리 정책과 로그·전송 경로 확인
- 엔진 불일치는 실행 중단 후 버전·GPU·shape manifest 출력

#### 통합 실습

##### 실습 07 · OCR·VLM 미니 애플리케이션 통합 (PDF p.93)

- 25분 실습, 기본필수는 한 파일에서 전처리 → OCR 결과 읽기 → 필드 JSON 저장
- 응용은 mock 또는 실제 VLM의 answer·evidence를 final JSON에 결합
- 심화는 모듈·평가표·오류 문서·보안 점검·README 재현 절차 완성
- 특심화는 Config·artifact manifest·mock/real backend·성능 회귀·배포 manifest 구현
- 기본필수는 문서 3장, 응용 통합은 문서 5장으로 배포 경로 구분
- 완료 기준은 생성 파일 재읽기·필드 확인과 사용한 backend·근거·한계 설명

**핵심:** 통합 프로젝트는 각 결과를 동일 문서와 기준 이미지에 연결하고, 값이 다르거나 근거가 부족한 경우를 검토 목록으로 보존.

### 8교시 · 최종 검증·평가·만족도·회고

#### 제출물과 재실행 검증

##### 과목 최종 제출물 (PDF p.94)

- 기본 코드는 전처리·OCR 결과 읽기·필드 JSON, 실제 VLM 연결은 선택
- OCR·필드 JSON과 제공 VLM 응답 검토·평가표 제출
- Box·Crop을 기준 이미지와 대조해 시각 근거 확인
- 보고서에 제공 지표 해석·오류·개인정보·배포 설계·한계 기록
- README에 입력·설정·환경과 실제·제공 결과 구분

##### 실습 08 · 최종 검증·보고서·시연 (PDF p.95)

- 30분 실습, 기본필수는 같은 프로젝트 재실행 후 문서 수·필드·결과 파일 재생성과 설명
- 응용은 짝이 README로 실행하고 차이가 나면 모델·질문·전처리·경로·seed 확인
- 심화는 정상·기울기·표·근거 없는 답·개인정보 상황 시연과 배포 전 점검
- 특심화는 실제·mock backend·다중 문서·TensorRT manifest·회귀·복구 검증
- 실습 07의 프로젝트를 이어서 사용하며 별도 프로그램 재작성은 불필요

#### 형성평가와 만족도

##### 형성평가 기준 · 100점 (PDF p.96)

- 전처리·OCR 20점은 원본 보존·Text·Box·Confidence·설정 기록
- 구조화·검증 20점은 raw·value·bbox·필수 필드·업무 규칙
- VLM·근거 20점은 실제·제공 응답의 질문·답·근거 검토
- 평가·보안 20점은 제공 지표 해석·필드 정확도·개인정보
- 재현·설명 20점은 README·결과 재생성·환경·한계·개인 설명

##### 과목 만족도 조사 · 학습평가와 분리 (PDF p.97)

- 이해에 도움 된 활동과 어려웠던 OCR·구조화·VLM·배포 영역 기록
- 기본필수·응용·심화·특심화의 난이도 적절성 확인
- OCR 언어 데이터·GPU·모델·TensorRT·코덱의 환경 문제 기록
- FastAPI 연결 단계에서 필요한 추가 설명 수집
- 만족도는 학습평가와 별도로 진행

**핵심:** 최종 완료는 같은 입력·설정에서 결과를 재생성하고, 실제·제공 결과와 근거·오류·한계를 자신의 말로 설명할 수 있는 상태.

### 마무리 · 핵심 정리와 다음 수업

#### 문서 AI 복습과 서비스 연결

##### 오늘의 핵심 정리 (PDF p.98)

- OCR은 전처리 → Text·Box·Confidence → 후처리 → 구조화·검증
- VLM의 이미지·질문 이해 결과는 근거 없는 답 검증과 함께 사용
- Hybrid는 OCR 전사·위치와 VLM 문맥 설명을 근거로 상호 검증
- 배포는 지원 모델의 ONNX·TensorRT 검증과 목표 장치·SDK 조합 확인
- 원본·근거·결과·평가·보안을 함께 보존해 재현 가능한 문서 AI 구성

##### 다음 수업 · Vision 결과를 FastAPI 서비스로 (PDF p.99)

- 강의자료 일정의 11월 10일은 FastAPI·HTTP·URL·View·JSON 조회 API로 결과 연결
- 11월 11일은 PostgreSQL·SQL·ERD로 문서·질문·결과·검토 이력 저장
- 11월 12일은 FastAPI–PostgreSQL·ORM CRUD로 처리 작업·결과 API 연결
- 11월 13일은 생성형 AI·LLM·Tokenization·Context로 언어모델 부분 확장

### 참고자료 · 공식 문서

#### OCR·VLM과 엣지 배포 문서

##### 공식 참고자료 · OCR·OpenCV·VLM (PDF p.100)

- OpenCV의 Threshold·Adaptive Threshold·Perspective 이미지 처리 문서
- Tesseract의 출력 품질·페이지 분할 모드와 pytesseract API
- Hugging Face Transformers의 멀티모달 Chat template·Image-text-to-text 문서
- Python `re`·`json` 표준 라이브러리 문서

##### 공식 참고자료 · TensorRT·Jetson·DeepStream (PDF p.101)

- TensorRT의 개요·동작·엔진 빌드·호환성 문서
- DeepStream의 `Gst-nvinfer` 플러그인 문서
- Jetson의 JetPack·TensorRT·DeepStream 지원 조합
- 교육 계획의 TensorRT 11.3과 Jetson 장치별 지원 조합을 구분해 확인

## 자료 간 표기 차이

- 원본 배포 자료의 PPT 대응표와 실습 README의 페이지 표시는 실습 01~08을 19·29·39·52·62·73·83·85쪽으로 안내하지만, 현재 PDF에서는 29·39·49·62·72·83·93·95쪽에 해당. 이 요약의 모든 페이지는 현재 PDF 기준.
- 수강생용 README의 “PPT 67쪽의 --fp16 예시” 설명은 현재 PDF와 불일치. 현재 PDF p.77은 TensorRT 11.x에서 해당 옵션이 제거된 경로로 설명하며, 응용 실습은 10.x 명령 설계 예시를 별도로 유지. 버전별 경로 구분 필요.
