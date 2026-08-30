# ThreeBodySimulation

토성의 공동궤도 위성 야누스(Janus)·에피메테우스(Epimetheus)와, 태양-목성 라그랑주점(L4)
트로이 천체를 대상으로 한 제한된 3체 문제(restricted three-body problem) 수치 시뮬레이션.
O'Neill, Hay, & deMattos (2024), *Celestial Mechanics and Dynamical Astronomy* 136(27)에
기반함 (자세한 내용은 `README.md` 참고).

## 코드 분류

이 저장소의 스크립트는 역할에 따라 네 그룹으로 나뉜다. 새 스크립트를 추가하거나 기존
스크립트를 수정할 때는 아래 구분을 유지할 것 — 시뮬레이션(적분)과 시각화(플로팅) 로직을
한 파일에 섞지 않는다.

### 1. 시뮬레이션 코드 (수치 적분 → `./data/*.csv` 생성)
- `modules/NbodySimulation.py` — 핵심 엔진. `compute_gravitational_field`(중력장 계산)와
  `RK4`(4차 Runge-Kutta 적분기)를 제공. 다른 모든 시뮬레이션 스크립트가 이 모듈을 사용.
- `JanusEpimetheus.py` — 토성-야누스-에피메테우스 3체를 적분하여 관성계 좌표 csv를 생성.
- `SunJupiter.py` — 태양-목성-트로이 입자(L4 근방) 3체를 적분하여 관성계 좌표 csv를 생성.

이 스크립트들은 실행 시간이 길고(최대 20년치, 초 단위 스텝) 결과를 `./data/`에 저장한다.
`./data/` 디렉터리는 git에 포함되어 있지 않으므로 실행 전에 직접 만들어야 한다
(`mkdir -p data`).

### 2. 시각화 코드 (csv 로드 → 그림/애니메이션만 생성, 적분 없음)
- `JanusEpimetheusOrbitPlot.py`, `JanusEpimetheusRadiiPlot.py`, `JanusEpimetheusAnimation.py`
- `SunJupiterPlot.py`, `SunJupiterAnimation.py`

이 스크립트들은 물리 계산을 하지 않는다. `modules/CoordinateTransformation.py`의
`load_data_3body_rot`/`innertial_to_rotating_frame_3body`로 관성계→회전계 변환만 수행한
뒤 matplotlib으로 정적 플롯(`figures/*.png`) 또는 GIF 애니메이션(`figures/*.gif`)을 만든다.

### 3. 분석 코드 (csv 로드 → 수치만 계산·출력, 그림 없음)
- `JanusEpimetheusLibrationAmplitude.py` — 회전계에서의 각진폭(libration amplitude) 계산.
- `JanusEpimetheusRadiusAmplitude.py` — 궤도반경 진폭(radius amplitude) 계산.

두 스크립트 모두 그래프를 먼저 보고 안정된 구간(min/max 평균낼 시간 범위)을 눈으로 확인한
뒤 코드 안의 구간 파라미터를 수동으로 맞춰야 하는 반쯤 대화형(interactive) 스크립트다.

### 4. 공용 유틸리티
- `modules/CoordinateTransformation.py` — `rotate`(2D 회전행렬 적용), `CM`(질량중심 계산),
  `innertial_to_rotating_frame_3body`, `load_data_3body_rot`(캐싱 로더: `*_rot.csv`가 있으면
  재사용, 없으면 변환 후 저장). 시뮬레이션 스크립트(초기조건 계산)와 시각화/분석 스크립트
  (좌표계 변환) 양쪽에서 공유된다.

## 실행 방법

```bash
mkdir -p data figures
python3 JanusEpimetheus.py          # 또는 SunJupiter.py — 시뮬레이션 실행, data/*.csv 생성
python3 JanusEpimetheusOrbitPlot.py # 시각화 — 위에서 만든 csv 필요
```

- 의존성: `numpy`, `pandas`, `scipy`, `matplotlib` (pillow가 `animation.save(..., writer='pillow')`에
  필요). 저장소에 `requirements.txt`가 없으므로 새로 추가할 경우 이 목록을 반영할 것.
- 시뮬레이션·시각화 스크립트 상단의 `filename`/`info`/`years` 등 변수는 하드코딩되어 있다.
  다른 파라미터(질량비, 반경차 `Delta_r` 등)로 실행하려면 이 값들을 직접 고쳐야 한다.
  스크립트 간에는 파일명 문자열(예: `f'JanusEpimetheus-{M_Janus/M_Epimetheus:.1f}-{Delta_r}.csv'`)로
  느슨하게 연결되어 있으므로, 시뮬레이션 스크립트의 출력 파일명과 시각화 스크립트가 읽는
  `filename`을 맞춰줘야 한다.

## 코드 스타일 / 관례

- 물리 상수는 `scipy.constants`(`const.G`, `const.au`, `const.year` 등)를 사용하고, 파일
  상단에서 문제에 맞는 단위계로 변환한다 (예: `JanusEpimetheus.py`는 km·s, `SunJupiter.py`는
  AU·day·태양질량 단위).
- 좌표는 항상 `r_vec`(shape `(N_body, 2)`)와 `v_vec` 형태의 2D 벡터로 다룬다 (2D 문제로 단순화됨).
- 새 천체계 시뮬레이션을 추가할 때는 기존 패턴을 따른다: 상수 정의 → 초기 위치/속도 설정
  (`CM`으로 무게중심 보정) → `RK4` 루프 → `pandas.DataFrame`에 주기적으로 기록 → csv 저장.
