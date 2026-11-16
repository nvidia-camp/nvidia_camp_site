# Day13 강의 구조·핵심 설명

2026-11-04 · Vision·멀티모달 AI 응용 · OpenCV 이미지·영상 전처리

교시 설명과 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준입니다. PDF는 93쪽이며 p.90 이후 슬라이드의 인쇄 쪽수는 PDF 쪽수보다 1 큽니다. 도입·마무리·참고자료는 별도 묶음으로 유지했습니다.

## 강의 목차

```text
도입 · 업무 흐름과 수업 범위
├─ Vision 입력과 처리의 전체 지도
│  ├─ Vision·멀티모달 AI 응용 (PDF p.1)
│  ├─ Vision 업무에서 전처리가 필요한 이유 (PDF p.2)
│  ├─ 전체 흐름에서 오늘 배울 처리의 위치 (PDF p.3)
│  ├─ 영상에서 한 Frame, 한 Pixel, 한 채널까지 (PDF p.4)
│  ├─ 색공간과 크기를 목적에 맞게 맞춥니다 (PDF p.5)
│  ├─ Filter 안에서 이웃 Pixel과 Kernel을 봅니다 (PDF p.6)
│  ├─ 밝기 기준으로 나눈 뒤 전경 모양을 다듬습니다 (PDF p.7)
│  ├─ 영상은 같은 이미지 처리를 시간 순서로 반복합니다 (PDF p.8)
│  ├─ 학습용 증강은 라벨 의미를 유지하는 변형입니다 (PDF p.9)
│  ├─ 저장 형식과 필요한 정보를 함께 확인합니다 (PDF p.10)
│  └─ 일일 프로젝트에서 입력·처리·검증을 합칩니다 (PDF p.11)
└─ 복습·운영·환경
   ├─ 어제 우리가 배운 것 (PDF p.12)
   ├─ 3분 확인 퀴즈 · 딥러닝에서 Vision 전처리로 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   ├─ OpenCV 환경과 결과 폴더를 먼저 확인한다 (PDF p.16)
   └─ 이미지·영상 전처리의 전체 흐름 (PDF p.17)

1교시 · 이미지 배열·BGR/RGB·입출력
├─ 이미지 표현과 읽기·저장
│  ├─ 이미지는 숫자 배열이고, 색상은 채널로 나뉜다 (PDF p.18)
│  ├─ Shape·dtype·값 범위를 먼저 확인한다 (PDF p.19)
│  ├─ cv.imread()로 이미지 읽기 (PDF p.20)
│  ├─ imread·imwrite 인자와 반환값 (PDF p.21)
│  └─ imshow·waitKey는 실행 환경을 확인하고 사용한다 (PDF p.22)
├─ 채널 순서와 분해·결합
│  ├─ OpenCV BGR과 Matplotlib RGB를 구분한다 (PDF p.23)
│  └─ 채널을 나누고 다시 합친다 (PDF p.24)
└─ 실습과 개념 확인
   ├─ 실습 01 · 이미지 읽기·Shape·채널 (PDF p.25)
   └─ 3분 퀴즈 · 이미지 배열 (PDF p.26)

2교시 · 색공간·Resize·보간법
├─ 목적별 색공간 선택
│  ├─ 목적에 따라 색공간과 표현을 선택한다 (PDF p.27)
│  ├─ cv.cvtColor()로 색공간 변환 (PDF p.28)
│  └─ cvtColor 변환 코드를 읽는 방법 (PDF p.29)
├─ 크기와 보간법
│  ├─ 리사이즈는 크기뿐 아니라 보간법도 선택한다 (PDF p.30)
│  ├─ cv.resize()로 크기 변경 (PDF p.31)
│  ├─ resize의 dsize·fx·fy·interpolation (PDF p.32)
│  └─ 같은 확대라도 보간법에 따라 결과가 다르다 (PDF p.33)
└─ 실습과 개념 확인
   ├─ 실습 02 · 색공간과 리사이즈 (PDF p.34)
   └─ 3분 퀴즈 · 색공간과 Resize (PDF p.35)

3교시 · Filter·Kernel·Edge
├─ 이웃 연산과 Filter 선택
│  ├─ 필터는 주변 픽셀을 이용해 새로운 값을 만든다 (PDF p.36)
│  ├─ Kernel 크기와 가중치가 출력의 성격을 정한다 (PDF p.37)
│  ├─ Gaussian·Median·Bilateral의 차이 (PDF p.38)
│  ├─ GaussianBlur·medianBlur (PDF p.39)
│  └─ Blur 함수의 파라미터를 구분한다 (PDF p.40)
├─ Border와 Canny
│  ├─ 이미지 가장자리의 값도 처리 규칙이 필요하다 (PDF p.41)
│  └─ Canny Edge로 강한 밝기 변화를 찾는다 (PDF p.42)
└─ 실습과 개념 확인
   ├─ 실습 03 · 필터와 Edge (PDF p.43)
   └─ 3분 퀴즈 · Filter와 Edge (PDF p.44)

4교시 · Threshold·형태학 처리
├─ 전경·배경을 나누는 임계값
│  ├─ Threshold는 밝기 기준으로 전경과 배경을 나눈다 (PDF p.45)
│  ├─ cv.threshold()로 이진화 (PDF p.46)
│  └─ Otsu·Adaptive Threshold를 구분한다 (PDF p.47)
├─ 전경 모양과 Kernel
│  ├─ 형태학 처리는 전경 모양을 Kernel로 다듬는다 (PDF p.48)
│  ├─ Erosion·Dilation·Opening·Closing (PDF p.49)
│  ├─ getStructuringElement로 Kernel 모양을 만든다 (PDF p.50)
│  ├─ cv.morphologyEx()로 Opening·Closing (PDF p.51)
│  └─ Gray→Blur→Threshold→Morphology를 연결한다 (PDF p.52)
└─ 실습과 개념 확인
   ├─ 실습 04 · Threshold와 형태학 (PDF p.53)
   └─ 3분 퀴즈 · Threshold와 Morphology (PDF p.54)

5교시 · 영상 입출력·Frame 처리
├─ Frame과 입력 속성
│  ├─ 영상은 시간 순서가 있는 Frame의 연속이다 (PDF p.55)
│  ├─ 영상의 핵심 속성: Frame·FPS·크기·코덱 (PDF p.56)
│  ├─ VideoCapture로 Frame 읽기 (PDF p.57)
│  └─ VideoCapture 주요 메서드와 속성 (PDF p.58)
├─ 샘플링과 영상 저장
│  ├─ 모든 Frame을 처리할지, 일부만 처리할지 정한다 (PDF p.59)
│  ├─ VideoWriter로 처리 영상 저장 (PDF p.60)
│  ├─ VideoWriter·fourcc의 역할 (PDF p.61)
│  └─ 영상 저장 오류를 빠르게 찾는 순서 (PDF p.62)
└─ 실습과 개념 확인
   ├─ 실습 05 · 영상 Frame 처리와 저장 (PDF p.63)
   └─ 3분 퀴즈 · 영상 입출력 (PDF p.64)

6교시 · 데이터 증강 Pipeline
├─ 의미를 유지하는 변형
│  ├─ 데이터 증강은 의미를 유지한 변형을 추가한다 (PDF p.65)
│  ├─ cv.flip()로 좌우·상하 반전 (PDF p.66)
│  ├─ 회전은 중심·각도·Scale로 2×3 행렬을 만든다 (PDF p.67)
│  ├─ getRotationMatrix2D·warpAffine (PDF p.68)
│  ├─ 밝기·Crop·Blur를 짧게 조합한다 (PDF p.69)
│  └─ 증강은 라벨 의미를 보존해야 한다 (PDF p.70)
└─ 실행 조건과 실습
   ├─ 입력·설정·실행 조건을 맞춰 증강을 재현한다 (PDF p.71)
   ├─ 실습 06 · 데이터 증강 Pipeline (PDF p.72)
   └─ 3분 퀴즈 · 데이터 증강 (PDF p.73)

7교시 · 이미지·영상 전처리 프로젝트
├─ 프로젝트 구조와 함수 계약
│  ├─ 이미지·영상 전처리 프로젝트의 처리 흐름 (PDF p.74)
│  ├─ 확장 참고: 전처리 프로젝트 폴더 구조 (PDF p.75)
│  └─ 함수는 입력·출력·부작용을 명확하게 한다 (PDF p.76)
├─ 일괄 처리와 결과 검증
│  ├─ 폴더의 이미지를 일괄 처리한다 (PDF p.77)
│  ├─ 영상 Frame마다 같은 처리 함수를 적용한다 (PDF p.78)
│  ├─ 원본 대비 전처리 결과를 수치와 그림으로 검증한다 (PDF p.79)
│  └─ 단계별 프로젝트 결과물과 보고 항목 (PDF p.80)
└─ 통합 실습과 개념 확인
   ├─ 실습 07 · 이미지·영상 전처리 프로젝트 통합 (PDF p.81)
   └─ 3분 퀴즈 · 프로젝트 구조 (PDF p.82)

8교시 · 최종 검증·보고서·시연
├─ 제출 범위와 테스트 조건
│  ├─ 최종 프로젝트 · 이미지·영상 전처리 Python 프로젝트 (PDF p.83)
│  ├─ 단계별 최종 제출 파일 (PDF p.84)
│  ├─ 오늘 등장한 핵심 함수 체크리스트 (PDF p.85)
│  └─ 정상·경계·실패 상황을 구분해 확인한다 (PDF p.86)
└─ 재실행·평가·코드 점검
   ├─ 실습 08 · 최종 검증·보고서·시연 (PDF p.87)
   ├─ 형성평가 기준 · 100점 (PDF p.88)
   └─ 전처리 코드리뷰 체크리스트 (PDF p.89)

마무리 · 핵심 정리와 참고자료
├─ 정리와 다음 수업
│  ├─ 오늘의 핵심 정리 (PDF p.90)
│  └─ 다음 수업 · 전이학습 Vision 모델 (PDF p.91)
└─ 공식 자료 안내
   ├─ 공식 참고자료 · 이미지 표현과 변환 (PDF p.92)
   └─ 공식 참고자료 · 형태학·영상·Affine (PDF p.93)
```

## 핵심 설명

### 도입 · 업무 흐름과 수업 범위

#### Vision 입력과 처리의 전체 지도

##### Vision·멀티모달 AI 응용 (PDF p.1)

- Day 13 이미지 표현·색공간에서 필터·형태학·영상·증강을 거쳐 전처리 프로젝트로 연결하는 수업 표지

##### Vision 업무에서 전처리가 필요한 이유 (PDF p.2)

- 촬영 조건이 다른 이미지·영상을 후속 모델과 규칙이 사용할 입력으로 준비
- 제품 외관 검사와 문서 인식은 업무 연결을 위한 가상 사례
- 오늘의 범위는 입력 준비와 결과 검증이며 모델 학습은 다음 수업으로 연결

##### 전체 흐름에서 오늘 배울 처리의 위치 (PDF p.3)

- 이미지 입력과 영상 Frame에 공통 이미지 처리 흐름 적용
- 색공간·Resize, Filter·Edge, Threshold·Morphology 중 후속 작업에 필요한 처리 선택
- 처리 파일과 함께 설정·검증표를 저장하고 원본과 비교

##### 영상에서 한 Frame, 한 Pixel, 한 채널까지 (PDF p.4)

- 영상 → Frame → Pixel → 채널의 포함 관계
- 컬러 shape `(240,320,3)`의 축은 높이·너비·채널
- uint8 값 범위는 0~255이며 한 Pixel은 `img[y,x]`로 확인

##### 색공간과 크기를 목적에 맞게 맞춥니다 (PDF p.5)

- 표시에는 RGB, 밝기·경계에는 Gray, 색 범위 선택에는 HSV 사용
- 320×240을 절반으로 줄일 때 `dsize=(160,120)`, 컬러 출력 shape는 `(120,160,3)`
- 크기 변경 시 원본 비율과 보간법을 함께 확인

##### Filter 안에서 이웃 Pixel과 Kernel을 봅니다 (PDF p.6)

- 이웃 Pixel과 Kernel의 같은 위치 값을 곱해 합산하는 평균 Filter 예
- 중앙 100과 주변 10 여덟 개의 평균은 `(100+10×8)/9=20`
- Gaussian은 가중 평균, Median은 중앙값 선택으로 계산 방식 구분

##### 밝기 기준으로 나눈 뒤 전경 모양을 다듬습니다 (PDF p.7)

- `THRESH_BINARY`에서 값이 T보다 크면 255, 그 외는 0으로 분류
- 흰색 255를 전경으로 둔 Opening은 침식 후 팽창, Closing은 팽창 후 침식
- 잡음 제거 과정에서 필요한 작은 특징의 손실도 확인

##### 영상은 같은 이미지 처리를 시간 순서로 반복합니다 (PDF p.8)

- Frame 읽기 → 처리 → 저장을 시간 순서로 반복
- 읽기 종료·실패 시 반복을 끝내고 Capture·Writer 해제
- 30장/30FPS와 15장/15FPS는 1초, 15장/30FPS는 0.5초
- 저장 FPS와 실제 연산 처리속도 구분

##### 학습용 증강은 라벨 의미를 유지하는 변형입니다 (PDF p.9)

- 원본 단위로 먼저 분할한 뒤 train에 기본 전처리와 증강 적용
- valid/test에는 비교 가능한 고정 전처리 적용
- 문자·방향 표지의 의미를 바꾸는 반전 제외
- 기본필수는 의미가 유지되는 두 변형을 원본과 나란히 저장

##### 저장 형식과 필요한 정보를 함께 확인합니다 (PDF p.10)

- Shape·dtype·채널뿐 아니라 Frame 수·FPS·재생시간·재읽기 확인
- Opening이 실제 결함에 해당하는 작은 흰 전경까지 제거하는지 원본과 대조
- 원본·단계별 결과·설정을 함께 보존하고 정보 손실 설명

##### 일일 프로젝트에서 입력·처리·검증을 합칩니다 (PDF p.11)

- 이미지 3장과 짧은 영상 1개에 Gray·Resize·Edge 적용
- 기본필수는 제공된 한 파일에서 처리 파일·요약표를 만들고 재실행 결과를 3문장으로 설명
- 응용은 함수와 비교표, 심화·특심화는 모듈·자동 검증으로 확장

#### 복습·운영·환경

##### 어제 우리가 배운 것 (PDF p.12)

- 이전 수업의 아키텍처 입출력 구조와 Padding·Mask·데이터 분할 복습
- 모델을 만들기 전 이미지·영상 자체의 읽기와 변환으로 학습 범위 전환

##### 3분 확인 퀴즈 · 딥러닝에서 Vision 전처리로 (PDF p.13)

- Conv2d 배치 입력의 축 순서 확인
- 평가 입력에 반복 무작위 증강을 적용할 때 비교 조건이 달라지는 이유 확인
- 원본과 처리 결과를 함께 보존하는 목적 점검

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 이미지 배열·색공간·필터·형태학·영상·증강·프로젝트·검증 순서의 8교시
- 50분×8교시=400분이며 설명·시연 200분과 실습·리뷰 200분으로 구성
- 실습01은 20분, 실습02~07은 각 25분, 실습08은 30분

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘은 이미지·영상 전처리와 원본 대비 검증 프로젝트까지 수행
- 다음 수업의 전이학습·Fine-tuning·평가·Grad-CAM과 현재 전처리 범위 구분

##### OpenCV 환경과 결과 폴더를 먼저 확인한다 (PDF p.16)

- Python·OpenCV import와 NumPy·Matplotlib 환경 확인
- 원본 data는 보존하고 생성 결과는 별도 출력 위치에 저장
- 서버·원격 환경에서는 GUI 대신 이미지 파일이나 Matplotlib 저장 사용

##### 이미지·영상 전처리의 전체 흐름 (PDF p.17)

- 입력 존재·크기·채널을 확인한 뒤 목적에 맞는 변환 선택
- 이진화·형태학 또는 영상 Frame 반복을 연결
- 원본·결과·설정·검증표를 함께 남기는 전체 흐름

### 1교시 · 이미지 배열·BGR/RGB·입출력

#### 이미지 표현과 읽기·저장

##### 이미지는 숫자 배열이고, 색상은 채널로 나뉜다 (PDF p.18)

- Gray는 `[H,W]`, 컬러는 `[H,W,C]` 배열
- 일반적인 uint8 이미지는 값 범위 0~255
- OpenCV 기본 컬러 채널 순서는 BGR

##### Shape·dtype·값 범위를 먼저 확인한다 (PDF p.19)

- shape는 행·열·채널 크기, dtype은 원소 자료형
- min/max로 실제 값 범위를 확인하고 ndim으로 배열 차원 확인
- 채널 축과 공간 축을 구분해 출력 크기 오류 방지

##### cv.imread()로 이미지 읽기 (PDF p.20)

- `imread`는 경로와 읽기 옵션을 받아 성공 시 ndarray, 실패 시 None 반환
- 읽기 성공을 확인한 뒤 shape·dtype·값 범위 조회
- 출력 폴더를 준비하고 `imwrite`의 저장 성공 bool 확인

##### imread·imwrite 인자와 반환값 (PDF p.21)

- `imread`의 filename은 필수이며 flags로 읽기 표현 선택
- `imwrite`는 파일명·이미지를 받아 저장 성공 여부 반환
- GRAYSCALE은 2차원 밝기 배열, UNCHANGED는 Alpha 유지 가능
- 읽기 디코더와 저장 확장자의 인코더 지원 확인

##### imshow·waitKey는 실행 환경을 확인하고 사용한다 (PDF p.22)

- `imshow`는 운영체제 GUI 창으로 이미지 표시
- `waitKey(0)`은 키 입력까지 무기한 대기
- 원격·Notebook 등 GUI 미지원 환경에서는 저장 또는 RGB 변환 후 Matplotlib 표시

#### 채널 순서와 분해·결합

##### OpenCV BGR과 Matplotlib RGB를 구분한다 (PDF p.23)

- OpenCV BGR `[20,80,200]`과 RGB `[200,80,20]`은 같은 색의 다른 채널 순서
- BGR 배열을 RGB로 해석하면 빨강·파랑의 표시가 달라짐
- Matplotlib 표시 전 `COLOR_BGR2RGB` 적용

##### 채널을 나누고 다시 합친다 (PDF p.24)

- `split`은 채널별 `[H,W]` 배열 반환
- `merge`는 같은 H·W의 채널 배열을 지정 순서로 결합
- 순서·shape·dtype을 확인하고 재결합 결과와 원본 비교
- RGB 표시용 배열을 OpenCV로 저장할 때는 BGR로 복귀

#### 실습과 개념 확인

##### 실습 01 · 이미지 읽기·Shape·채널 (PDF p.25)

- 기본필수는 정상 이미지를 읽어 shape·dtype·min/max를 출력하고 BGR 복사본 저장
- 응용은 RGB 표시 비교와 채널 평균 기록
- 심화는 읽기 옵션·PNG/JPEG 파일 크기와 품질 비교
- 특심화는 stride·copy/view·메모리 연속성과 기준색 패치 검사

##### 3분 퀴즈 · 이미지 배열 (PDF p.26)

- 컬러 shape의 높이·너비·채널 의미 확인
- 읽기 실패 반환값과 채널 순서에 따른 표시 차이 점검

**핵심:** 읽기 성공·배열 축·채널 순서를 확인한 뒤 표시와 저장에 맞는 표현 선택.

### 2교시 · 색공간·Resize·보간법

#### 목적별 색공간 선택

##### 목적에 따라 색공간과 표현을 선택한다 (PDF p.27)

- BGR/RGB는 컬러, Gray는 밝기 중심 표현
- 일반 uint8 HSV는 H 0~179, S·V 0~255
- Binary는 색공간이 아닌 전경·배경 Mask

##### cv.cvtColor()로 색공간 변환 (PDF p.28)

- `cvtColor`의 src와 code로 목적에 맞는 색공간 변환
- Gray 출력은 `[H,W]`, RGB·HSV 출력은 `[H,W,3]`
- 반환 배열의 shape로 변환 결과 확인

##### cvtColor 변환 코드를 읽는 방법 (PDF p.29)

- BGR2RGB는 표시, BGR2GRAY는 Threshold·Edge, BGR2HSV는 색 범위 분리 목적
- GRAY2BGR은 1채널을 3채널 표현으로 바꾸는 변환
- 색공간은 후속 처리 목적에 따라 선택

#### 크기와 보간법

##### 리사이즈는 크기뿐 아니라 보간법도 선택한다 (PDF p.30)

- 축소는 여러 Pixel 정보를 요약하고 확대는 주변 값에서 새 값을 추정
- INTER_AREA는 축소에 자주 사용
- INTER_LINEAR는 기본 보간법이며 확대에도 사용

##### cv.resize()로 크기 변경 (PDF p.31)

- 고정 크기는 dsize, 비율 변경은 fx·fy로 지정
- `dsize=(W,H)`와 배열 shape의 `(H,W)` 구분
- 224×224 축소 예에서 INTER_AREA를 명시

##### resize의 dsize·fx·fy·interpolation (PDF p.32)

- src는 입력 배열, dsize는 출력 크기를 지정하는 필수 자리
- dsize를 None 또는 (0,0)으로 두고 fx·fy로 출력 크기 결정 가능
- 고정 크기와 배율 중 한 방식을 골라 의도 명시
- interpolation으로 Pixel 추정 방법 선택

##### 같은 확대라도 보간법에 따라 결과가 다르다 (PDF p.33)

- 같은 입력·확대 크기에서 최근접과 선형 보간 결과 비교
- 최근접은 Pixel 경계가 뚜렷하지만 계단 현상 발생 가능
- 선형은 주변 네 값을 이용해 부드럽게 보간

#### 실습과 개념 확인

##### 실습 02 · 색공간과 리사이즈 (PDF p.34)

- 기본필수는 Gray·RGB 변환과 224×224 축소 후 저장·shape 확인
- 응용은 NEAREST·LINEAR·AREA 비교
- 심화는 HSV Mask와 비율을 유지하는 Letterbox 구현
- 특심화는 좌표 역변환을 포함한 Resize 객체 검증

##### 3분 퀴즈 · 색공간과 Resize (PDF p.35)

- shape와 dsize의 축 순서 차이 점검
- Gray 배열 차원과 축소 보간법의 선택 이유 확인

**핵심:** 색공간과 출력 크기·보간법을 후속 작업과 원본 정보 보존 기준으로 선택.

### 3교시 · Filter·Kernel·Edge

#### 이웃 연산과 Filter 선택

##### 필터는 주변 픽셀을 이용해 새로운 값을 만든다 (PDF p.36)

- Kernel이 이웃을 순회하며 새 Pixel 값 계산
- Blur는 잡음과 세부를 부드럽게 만들고 Sharpen은 경계·고주파 강조
- Edge는 밝기 변화가 큰 위치 검출

##### Kernel 크기와 가중치가 출력의 성격을 정한다 (PDF p.37)

- 작은 Kernel은 세부 보존과 약한 효과, 큰 Kernel은 강한 Blur와 연산 증가
- 합이 1인 평균 Kernel은 밝기 평균화
- 음수 가중치를 포함한 Kernel은 경계·선명도 강조 가능

##### Gaussian·Median·Bilateral의 차이 (PDF p.38)

- Gaussian은 가우시안 가중 평균으로 잡음과 Edge를 함께 완화
- Median은 중앙값 선택으로 점 잡음에 강한 방식
- Bilateral은 공간 거리와 밝기 차이를 함께 사용해 Edge를 보존하지만 비교적 느림

##### GaussianBlur·medianBlur (PDF p.39)

- GaussianBlur는 src·ksize·sigmaX를 지정하며 예제는 (5,5), sigmaX=0
- medianBlur는 src·ksize를 지정하며 ksize는 1보다 큰 홀수
- 노이즈 종류와 Edge 보존 요구에 따라 Filter 선택

##### Blur 함수의 파라미터를 구분한다 (PDF p.40)

- GaussianBlur의 Kernel 크기는 양수 홀수 또는 자동 크기 0 사용 조건 확인
- medianBlur의 Kernel은 3·5·7 등의 홀수
- Bilateral의 d·sigmaColor·sigmaSpace 역할 구분
- 큰 파라미터의 정보 손실과 연산량 증가 함께 비교

#### Border와 Canny

##### 이미지 가장자리의 값도 처리 규칙이 필요하다 (PDF p.41)

- Kernel이 이미지 밖을 참조할 때 Border 규칙 적용
- REFLECT는 경계 반사, REPLICATE는 가장자리 Pixel 반복
- 같은 Kernel도 Border 규칙에 따라 경계 결과가 달라짐

##### Canny Edge로 강한 밝기 변화를 찾는다 (PDF p.42)

- Gray → GaussianBlur → Canny 순서로 잡음 Edge 감소
- 예제 Canny 임계값은 70·150이며 출력은 0·255의 1채널 배열
- 낮은 임계값의 잡음 증가와 높은 임계값의 약한 경계 손실 비교

#### 실습과 개념 확인

##### 실습 03 · 필터와 Edge (PDF p.43)

- 기본필수는 GaussianBlur와 Canny 결과를 저장하고 Kernel·임계값 기록
- 응용은 같은 이미지에서 Gaussian·Median의 Edge Pixel 수 비교
- 심화는 처리시간과 Edge 보존을 함께 비교
- 특심화는 Border·Kernel·임계값을 바꿔 품질·시간의 Pareto 후보 탐색

##### 3분 퀴즈 · Filter와 Edge (PDF p.44)

- Median Kernel 제약과 Canny 전 Blur의 역할 확인
- 큰 Kernel이 항상 좋은 결과를 보장하지 않는 이유 점검

**핵심:** 잡음 감소·경계 보존·연산량을 함께 비교하고 Kernel과 임계값의 선택 이유 설명.

### 4교시 · Threshold·형태학 처리

#### 전경·배경을 나누는 임계값

##### Threshold는 밝기 기준으로 전경과 배경을 나눈다 (PDF p.45)

- Gray 밝기값이 임계값보다 크면 255, 그 외는 0으로 분류하는 예
- Binary Mask를 후속 형태학 입력으로 사용
- 고정 임계값은 조명 변화가 클 때 불안정

##### cv.threshold()로 이진화 (PDF p.46)

- threshold는 src·thresh·maxval·type을 지정
- 반환값은 사용 임계값 retval과 결과 이미지 dst
- 예제는 thresh=140·maxval=255·THRESH_BINARY이며 반전 방식과 구분

##### Otsu·Adaptive Threshold를 구분한다 (PDF p.47)

- Fixed는 사용자가 전역 임계값 하나 지정
- Otsu는 히스토그램으로 임계값을 자동 결정하며 두 분포가 분리될 때 유용
- Adaptive는 지역별 임계값을 계산하며 blockSize·C 조정 필요
- 조명·분포·속도·후속 작업 기준으로 선택

#### 전경 모양과 Kernel

##### 형태학 처리는 전경 모양을 Kernel로 다듬는다 (PDF p.48)

- 실습에서 흰색 255는 전경, 검은색 0은 배경
- Erosion은 전경 축소, Dilation은 전경 확대
- Opening은 작은 흰 전경 잡음 제거, Closing은 작은 검은 구멍 보완
- 도식의 검은 전경 표시와 실습의 흰 전경 관례 구분

##### Erosion·Dilation·Opening·Closing (PDF p.49)

- Opening은 Erosion → Dilation 순서
- Closing은 Dilation → Erosion 순서
- 연산에 따른 경계 축소·확대와 끊긴 부분·구멍의 변화 비교

##### getStructuringElement로 Kernel 모양을 만든다 (PDF p.50)

- getStructuringElement에 shape·ksize를 지정해 형태학 Kernel 생성
- RECT·ELLIPSE·CROSS의 이웃 모양 구분
- Kernel 크기와 반복 횟수가 영향 범위를 함께 결정

##### cv.morphologyEx()로 Opening·Closing (PDF p.51)

- morphologyEx에 src·op·kernel을 지정해 Opening·Closing 적용
- iterations·anchor·Border를 선택 설정으로 관리
- 연산 전에 전경이 흰색인지 확인

##### Gray→Blur→Threshold→Morphology를 연결한다 (PDF p.52)

- Gray → Blur → Threshold → Morphology의 순서에 따른 결과 관찰
- 각 단계 입력·출력 shape와 값 범위 기록
- 처리 순서 변경에 따른 결과 차이 확인

#### 실습과 개념 확인

##### 실습 04 · Threshold와 형태학 (PDF p.53)

- 기본필수는 Gray → Threshold → Opening 또는 Closing 한 가지와 단계별 PNG 저장
- 응용은 Fixed·Otsu 임계값과 전경 Pixel 수 비교
- 심화는 Kernel 모양·크기·iterations와 객체 손실 분석
- 특심화는 파라미터 탐색·연결요소 품질 지표·원본 보존 검사 자동화

##### 3분 퀴즈 · Threshold와 Morphology (PDF p.54)

- Opening 순서와 Closing의 적용 목적 확인
- threshold의 두 반환값 구분

**핵심:** 전경의 의미를 먼저 정한 뒤 이진화와 형태학 처리의 효과·손실을 원본과 대조.

### 5교시 · 영상 입출력·Frame 처리

#### Frame과 입력 속성

##### 영상은 시간 순서가 있는 Frame의 연속이다 (PDF p.55)

- 영상은 시간 순서가 있는 Frame의 연속
- 각 Frame에 동일한 전처리 적용 후 영상 저장
- FPS·크기·코덱은 유지하거나 변경 내용을 명시

##### 영상의 핵심 속성: Frame·FPS·크기·코덱 (PDF p.56)

- Frame은 시간 t의 이미지, FPS는 초당 재생 Frame 수
- Frame Size는 `(width,height)`, Codec은 압축·저장 방식
- 영상 처리를 이미지 처리·시간 순서·저장 설정으로 분해

##### VideoCapture로 Frame 읽기 (PDF p.57)

- Capture를 열고 isOpened로 입력 소스 열림 확인
- read의 `(ok,frame)`에서 ok=False면 종료 또는 읽기 실패로 반복 종료
- 반복 후 release로 파일·카메라 자원 해제

##### VideoCapture 주요 메서드와 속성 (PDF p.58)

- VideoCapture의 source로 파일 경로나 카메라 번호 지정
- get은 속성값 float를 반환하지만 코덱에 따라 부정확 가능
- set의 설정 지원 여부는 백엔드에 따라 달라짐

#### 샘플링과 영상 저장

##### 모든 Frame을 처리할지, 일부만 처리할지 정한다 (PDF p.59)

- Frame index 나머지 조건이나 Timestamp로 처리 대상 선택
- 샘플링으로 처리량은 줄지만 빠른 사건을 놓칠 수 있음
- 저장 Frame 수와 출력 FPS 변경에 따른 재생시간 확인

##### VideoWriter로 처리 영상 저장 (PDF p.60)

- 출력 폴더와 유효한 양수·유한 FPS 확인
- 파일명·fourcc·FPS·frameSize로 Writer를 만들고 열림 확인
- 각 Frame은 반복 안에서 write, 종료 후 release
- 저장 Frame 크기·채널을 Writer 설정과 일치

##### VideoWriter·fourcc의 역할 (PDF p.61)

- fourcc는 코덱 식별자이며 파일 확장자와 지원 코덱 조합 확인
- fps는 재생속도, frameSize는 모든 Frame의 `(W,H)`
- isColor와 실제 Gray·컬러 채널을 일치

##### 영상 저장 오류를 빠르게 찾는 순서 (PDF p.62)

- Writer 열림 → Frame 크기 → 채널 → 확장자·코덱 순서로 점검
- release 후 파일 크기와 재읽기로 저장 완료 확인
- 파일 생성만으로 영상 정상 저장을 판단하지 않음

#### 실습과 개념 확인

##### 실습 05 · 영상 Frame 처리와 저장 (PDF p.63)

- 기본필수는 입력 FPS·크기·Frame 수 확인과 Gray 또는 Edge 영상 저장
- 응용은 매 N번째 Frame 처리와 입출력 재생시간 비교
- 심화는 Frame 처리 함수·평균 처리시간 보고
- 특심화는 비동기 Decode·처리·Encode의 큐·드롭·지연 측정

##### 3분 퀴즈 · 영상 입출력 (PDF p.64)

- read의 반환값과 Writer frameSize의 순서 확인
- 같은 Frame 수에서 출력 FPS를 낮췄을 때 재생시간 변화 점검

**핵심:** Frame 반복의 정상 종료와 Writer 설정을 확인하고 저장 후 Frame 수·FPS·크기를 재검증.

### 6교시 · 데이터 증강 Pipeline

#### 의미를 유지하는 변형

##### 데이터 증강은 의미를 유지한 변형을 추가한다 (PDF p.65)

- Flip·Crop·Rotation·Brightness·Blur로 학습 자료의 조건 다양화
- 라벨 의미가 바뀌는 변형 제외
- valid/test에는 결정적 변환 사용

##### cv.flip()로 좌우·상하 반전 (PDF p.66)

- flipCode=1은 좌우, 0은 상하, 음수는 양쪽 반전
- 반전 후 정답 의미가 유지되는지 원본과 비교

##### 회전은 중심·각도·Scale로 2×3 행렬을 만든다 (PDF p.67)

- 회전 중심·각도·Scale로 2×3 변환 행렬 생성
- angle은 degree 단위
- 실제 Pixel 재배치는 warpAffine에서 수행

##### getRotationMatrix2D·warpAffine (PDF p.68)

- getRotationMatrix2D로 중심·10도·Scale 1.0의 행렬 생성 예
- warpAffine에 src·M·출력 `(W,H)` 지정
- 회전 후 모서리 손실과 Border 처리 결과 확인

##### 밝기·Crop·Blur를 짧게 조합한다 (PDF p.69)

- convertScaleAbs의 밝기 변환은 Scale·이동 외 절댓값·uint8 변환도 포함
- Crop 후 원래 크기로 Resize하는 과정의 정보 손실 확인
- Blur·밝기·Crop 조합에서도 라벨 의미 유지 여부 확인

##### 증강은 라벨 의미를 보존해야 한다 (PDF p.70)

- 일반 사물·OCR·교통 표지·의료 영상에 동일한 증강 정책을 일괄 적용하지 않음
- OCR 문자와 방향 표지는 반전으로 의미가 바뀔 가능성
- 도메인과 관심 정보에 따라 변형 범위 제한

#### 실행 조건과 실습

##### 입력·설정·실행 조건을 맞춰 증강을 재현한다 (PDF p.71)

- 변환 설정을 dict·JSON에 저장
- Seed·난수 도구·호출 순서·버전을 함께 기록
- 원본 단위 분할 후 train에만 무작위 변환 적용
- 원본을 보존하고 출력 파일명에 변환 정보 기록

##### 실습 06 · 데이터 증강 Pipeline (PDF p.72)

- 기본필수는 의미를 유지하는 두 변형과 원본 비교 저장
- 응용은 같은 Seed의 동일 결과 확인
- 심화는 폴더 일괄 처리·설정·경로·검증표 CSV 저장
- 특심화는 라벨 규칙·확률적 변환·다중 Worker 재현성과 변환 분포 검증

##### 3분 퀴즈 · 데이터 증강 (PDF p.73)

- 평가 입력의 반복 무작위 변형이 성능 비교에 미치는 영향 점검
- OCR 반전의 의미 변화와 Seed 기록 목적 확인

**핵심:** 원본 분할과 라벨 의미를 유지하면서 train 변형의 실행 조건을 재현 가능하게 기록.

### 7교시 · 이미지·영상 전처리 프로젝트

#### 프로젝트 구조와 함수 계약

##### 이미지·영상 전처리 프로젝트의 처리 흐름 (PDF p.74)

- 이미지·영상의 설정과 처리 흐름 통합
- 단계별 처리·출력 위치·원본 대비 비교를 구분
- 실행 설정과 검증 결과를 보고서에 저장하는 확장 흐름

##### 확장 참고: 전처리 프로젝트 폴더 구조 (PDF p.75)

- main은 설정·작업·전체 실행, image_ops는 이미지 처리, video_ops는 Frame 반복·저장 담당
- augment는 학습 변형, reports는 입출력 shape·설정·성공 여부 기록
- 모듈 구조는 확장 참고이며 기본필수의 필수 구현 범위와 구분

##### 함수는 입력·출력·부작용을 명확하게 한다 (PDF p.76)

- 읽기 함수는 경로에서 BGR 배열, 전처리 함수는 배열·설정에서 처리 배열 반환
- 저장 함수와 영상 처리 함수의 파일 생성 부작용 구분
- 증강 함수는 배열·Seed를 받아 변형 배열 반환

#### 일괄 처리와 결과 검증

##### 폴더의 이미지를 일괄 처리한다 (PDF p.77)

- 정렬한 파일 경로로 순회 순서 고정
- 이미지 읽기 실패와 저장 실패를 경로·이유로 확인
- 정상 입력 수와 출력 shape를 확인하며 일괄 처리

##### 영상 Frame마다 같은 처리 함수를 적용한다 (PDF p.78)

- Frame 함수는 BGR 배열을 받아 Writer 설정과 같은 크기·채널 반환
- Gray Edge를 BGR로 바꾸어 3채널 Writer에 전달
- 파일 열기·닫기와 반복은 상위 함수 담당
- 처리 전후 Frame 수·FPS·크기 비교

##### 원본 대비 전처리 결과를 수치와 그림으로 검증한다 (PDF p.79)

- 파일 수·shape·dtype·값 범위·재읽기를 원본·설정과 대조
- 표의 입력 10개·240×320 결과는 예시이며 실제 실습 파일 수와 구분
- 수치 검사와 원본 대비 그림 확인을 함께 수행

##### 단계별 프로젝트 결과물과 보고 항목 (PDF p.80)

- 처리 이미지·영상 1개·설정과 성공 여부의 요약 CSV 준비
- README에 실행 명령·처리 순서·역할·한계 기록
- 기본필수의 원본 대비 설명은 3문장, 확장은 보고서
- 처리시간 기록은 확장 범위

#### 통합 실습과 개념 확인

##### 실습 07 · 이미지·영상 전처리 프로젝트 통합 (PDF p.81)

- 기본필수는 한 파일에서 이미지 3장·영상 1개의 Gray·Resize·Edge와 요약표 생성
- 응용은 함수 분리와 원본·결과 비교표
- 심화는 모듈형 설정 연결과 수치 검사 자동화
- 특심화는 병렬·로그·실패 복구·Frame drop·성능 측정 실행 체계

##### 3분 퀴즈 · 프로젝트 구조 (PDF p.82)

- Frame 함수 내부의 반복 파일 열기가 자원·성능에 미치는 영향 점검
- 원본 보존의 비교·재현·복구 목적 확인
- 입력 경로·처리 설정·출력 shape와 성공 여부의 기록 점검

**핵심:** 자기 단계의 구조 안에서 이미지와 영상에 일관된 처리를 적용하고 결과·설정을 함께 검증.

### 8교시 · 최종 검증·보고서·시연

#### 제출 범위와 테스트 조건

##### 최종 프로젝트 · 이미지·영상 전처리 Python 프로젝트 (PDF p.83)

- 이미지 폴더와 짧은 영상에서 필요한 전처리를 골라 일정 형식으로 변환
- 파일 수·shape·dtype·FPS·재읽기로 결과 검증
- 코드·결과·요약표·자기 단계의 README와 설명 준비

##### 단계별 최종 제출 파일 (PDF p.84)

- 기본필수는 전체 실행 한 파일로 구성 가능
- image_ops·video_ops 모듈 분리는 자기 단계 안내에 맞춰 적용
- 처리 이미지·영상, 요약표, 실행법·순서·해석의 README 제출

##### 오늘 등장한 핵심 함수 체크리스트 (PDF p.85)

- 입출력·색공간·크기·필터·이진화·형태학·영상·증강의 핵심 함수 복습
- 호출 함수별 입력·필수 인자·선택 인자의 역할 설명

##### 정상·경계·실패 상황을 구분해 확인한다 (PDF p.86)

- 정상 PNG는 읽기·처리·저장 후 shape·dtype·재읽기 확인
- 다른 크기·Gray 입력은 비율 왜곡과 채널 분기 확인
- 빈 영상·손상 파일은 실패를 기록하고 정상 결과로 취급하지 않음
- FPS 0·미확인은 대체 규칙 또는 중단 후 보고
- 출력 폴더가 없으면 생성 후 파일 수 확인

#### 재실행·평가·코드 점검

##### 실습 08 · 최종 검증·보고서·시연 (PDF p.87)

- 기본필수는 기존 프로젝트를 재실행해 파일 수·shape 재현과 결과 3문장 설명
- 응용은 짝이 README만으로 실행하고 FPS·경로·설정 대조
- 심화는 정상·경계·실패 입력과 정보 손실·처리시간 보고
- 특심화는 프로세스·코덱 차이·결정성·성능 회귀와 재현 한계 검증

##### 형성평가 기준 · 100점 (PDF p.88)

- 입력·표현 15점, 이미지 전처리 25점, 영상 처리 20점
- 증강·검증 15점, 프로젝트 완성 15점, 재현·설명 10점
- 공통 100점 안에서 자기 단계의 구현 범위와 결과 설명 평가

##### 전처리 코드리뷰 체크리스트 (PDF p.89)

- 읽기 직후 None·shape·dtype과 채널·공간 축 순서 점검
- Filter·Threshold·Morphology 설정과 원본 보존 확인
- Writer FPS·Frame Size·채널 일치 확인
- 다른 사람이 README로 결과를 재현할 수 있는지 점검

**핵심:** 동일 재실행·입출력 검증·결과 해석으로 프로젝트의 완성과 한계를 증명.

### 마무리 · 핵심 정리와 참고자료

#### 정리와 다음 수업

##### 오늘의 핵심 정리 (PDF p.90)

- NumPy 배열 표현과 OpenCV 기본 BGR 정리
- 목적과 인자를 기록한 변환, Frame·FPS·크기·코덱 관리 정리
- 라벨을 유지하는 train 증강과 원본·결과·설정·검증표·README 보존 정리

##### 다음 수업 · 전이학습 Vision 모델 (PDF p.91)

- 11/05 전이학습·데이터셋 설계로 전처리·Resize·Normalize 기준 연결
- 11/06 YOLO·IoU·mAP로 Frame·좌표·영상 처리 연결
- 11/09 OCR·VLM·추론 최적화와 11/10 이후 API·LLM·RAG로 확장하는 교재 예고

#### 공식 자료 안내

##### 공식 참고자료 · 이미지 표현과 변환 (PDF p.92)

- 이미지 입출력·색공간·기하 변환·Smoothing·Thresholding의 공식 참고자료 안내

##### 공식 참고자료 · 형태학·영상·Affine (PDF p.93)

- 형태학·영상 입출력·Affine·배열 연산의 공식 참고자료 안내
- 실제 설치된 OpenCV 4.x의 공식 문서를 최종 기준으로 확인

## 자료 간 차이

- 실습 README의 PPT 15·24·33·43·53·62·71·77장은 이전 자료 기준입니다. 현재 PDF의 실습01~08은 p.25·34·43·53·63·72·81·87입니다.
- PDF p.42 Canny 예제는 70/150이며 현재 기본필수 README의 실습03·07은 80/160입니다. 결과를 비교할 때 각 설정과 처리 순서를 구분합니다.
- PDF p.60은 mp4v/MP4 예제이며 배포 실습은 MJPG/AVI·48Frame·12FPS·320×240의 합성 영상입니다. 코덱과 출력 형식은 자기 단계 README 기준입니다.
- 기본필수는 함수·클래스·예외처리를 새로 작성하지 않고 TODO 9곳을 완성합니다. 결과는 같은 폴더의 p01_~p07_ 접두어로 생성하며, 07 결과는 PNG 9개·AVI 1개·CSV 1개입니다. 실습08은 07을 재실행하고 설명 3문장을 작성하는 과정입니다.
- 기본필수 요약 CSV는 이미지 3행이며 응용 프로젝트의 단계별 표는 9행입니다. 단계마다 표의 집계 단위가 다릅니다.
- PDF p.69의 convertScaleAbs는 절댓값을 포함합니다. 배포 실습의 밝기 처리는 float 변환 → 덧셈 → clip → uint8이며 두 연산을 모든 입력에서 동일한 식으로 간주하지 않습니다.
- README의 실행 예와 수치는 배포 자료의 기준입니다. 이번 정리는 실습 코드의 실행·채점 완료를 의미하지 않습니다.
