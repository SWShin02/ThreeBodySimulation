# ThreeBodySimulation

토성의 공동궤도 위성 야누스(Janus)·에피메테우스(Epimetheus)와, 태양-목성 라그랑주점(L4)
트로이 천체를 대상으로 한 제한된 3체 문제(restricted three-body problem) 수치 시뮬레이션.
O'Neill, Hay, & deMattos (2024), *Celestial Mechanics and Dynamical Astronomy* 136(27)에
기반함 (자세한 내용은 `README.md` 참고).

## 코드 분류

이 저장소의 스크립트는 역할에 따라 네 그룹으로 나뉜다. 새 스크립트를 추가하거나 기존
스크립트를 수정할 때는 아래 구분을 유지할 것 — 시뮬레이션(적분)과 시각화(플로팅) 로직을
한 파일에 섞지 않는다.

### 1. 시뮬레이션 코드 (수치 적분 → `./data/*.h5` 생성)
- `modules/NbodySimulation.py` — 핵심 엔진. `compute_gravitational_field`(중력장 계산)와
  `RK4`(4차 Runge-Kutta 적분기)를 제공. 다른 모든 시뮬레이션 스크립트가 이 모듈을 사용.
- `JanusEpimetheus.py` — 토성-야누스-에피메테우스 3체를 적분하여 `./data/JanusEpimetheus.h5`에 저장.
- `SunJupiter.py` — 태양-목성-트로이 입자(L4 근방) 3체를 적분하여 `./data/SunJupiter.h5`에 저장.

이 스크립트들은 실행 시간이 길고(최대 20년치, 초 단위 스텝) 결과를 `./data/`에 저장한다.
`./data/` 디렉터리는 git에 포함되어 있지 않으므로 실행 전에 직접 만들어야 한다
(`mkdir -p data`).

**저장 포맷 (HDF5)**: 파일명은 천체계별로 고정(`JanusEpimetheus.h5`, `SunJupiter.h5`)이고, 실행할
때마다 파일 안에 실행 시작 시각(`yyyymmddhhmm`)을 이름으로 한 새 group이 추가된다 — 같은
파일을 여러 번 실행해도 이전 run이 덮어써지지 않고 누적된다. 각 group 안에는:
  - `innertial` — shape `(t, n_body=3, dim=2)`, 관성계 위치
  - `theta` — shape `(t,)`, 관성계-회전계 사이 회전각(평균운동 기준)

시각화/분석 스크립트가 처음 회전계 변환을 수행하면 같은 group에 `rotating` 데이터셋이
캐시로 추가된다 (`modules/CoordinateTransformation.load_data_3body_rot` 참고).
`modules/DataIO.py`가 이 저장/로드를 담당한다 (`save_run`, `load_run`, `latest_group`).

### 2. 시각화 코드 (h5 로드 → 그림/애니메이션만 생성, 적분 없음)
- `JanusEpimetheusOrbitPlot.py`, `JanusEpimetheusRadiiPlot.py`, `JanusEpimetheusAnimation.py`
- `SunJupiterPlot.py`, `SunJupiterAnimation.py`

이 스크립트들은 물리 계산을 하지 않는다. `modules/CoordinateTransformation.py`의
`load_data_3body_rot`/`innertial_to_rotating_frame_3body`로 관성계→회전계 변환만 수행한
뒤 matplotlib으로 정적 플롯(`figures/*.png`) 또는 GIF 애니메이션(`figures/*.gif`)을 만든다.
출력 파일명에는 어떤 run(group)에서 나온 그림인지 추적할 수 있도록 group 이름을 붙인다.

### 3. 분석 코드 (h5 로드 → 수치만 계산·출력, 그림 없음)
- `JanusEpimetheusLibrationAmplitude.py` — 회전계에서의 각진폭(libration amplitude) 계산.
- `JanusEpimetheusRadiusAmplitude.py` — 궤도반경 진폭(radius amplitude) 계산.

두 스크립트 모두 그래프를 먼저 보고 안정된 구간(min/max 평균낼 시간 범위)을 눈으로 확인한
뒤 코드 안의 구간 파라미터를 수동으로 맞춰야 하는 반쯤 대화형(interactive) 스크립트다.

### 4. 공용 유틸리티
- `modules/DataIO.py` — HDF5 저장/로드. `save_run`(새 group에 `innertial`/`theta` 저장, group
  이름 기본값은 실행 시각), `load_run`(group 지정 없으면 파일 내 가장 최근 group을 로드),
  `latest_group`.
- `modules/CoordinateTransformation.py` — `rotate`(2D 회전행렬 적용, 스칼라), `CM`(질량중심 계산),
  `innertial_to_rotating_frame_3body`(벡터화된 배열 변환: `(t, n_body, 2)` + `(t,)` theta →
  회전계 배열), `load_data_3body_rot`(h5 파일에서 회전계 배열을 로드하고 `rotating`
  데이터셋으로 캐싱). 시뮬레이션 스크립트(초기조건 계산에 `rotate`/`CM`)와 시각화/분석
  스크립트(좌표계 변환에 나머지 함수) 양쪽에서 공유된다.

## 실행 방법

```bash
mkdir -p data figures
python3 JanusEpimetheus.py          # 또는 SunJupiter.py — 시뮬레이션 실행, data/*.h5 에 새 run(group) 추가
python3 JanusEpimetheusOrbitPlot.py # 시각화 — 기본적으로 h5 파일의 가장 최근 run을 읽음
```

- 의존성: `numpy`, `scipy`, `matplotlib`, `h5py` (pillow가 `animation.save(..., writer='pillow')`에
  필요). 저장소에 `requirements.txt`가 없으므로 새로 추가할 경우 이 목록을 반영할 것.
- 시뮬레이션·시각화 스크립트 상단의 `group_name`/`years` 등 변수는 하드코딩되어 있다.
  `group_name = None`이면 h5 파일의 가장 최근 run을 자동으로 사용하고, 특정 과거 run을
  다시 보고 싶으면 `group_name`에 해당 `yyyymmddhhmm` 문자열을 직접 넣으면 된다.
  다른 물리 파라미터(질량비, 반경차 `Delta_r` 등)로 실행하려면 시뮬레이션 스크립트 상단의
  상수를 직접 고쳐야 한다 — 파일명은 고정이고 run마다 group으로 구분되므로, 시뮬레이션
  스크립트와 시각화 스크립트 사이에 파일명 문자열을 맞춰줄 필요는 없다.

## 코드 스타일 / 관례

- 물리 상수는 `scipy.constants`(`const.G`, `const.au`, `const.year` 등)를 사용하고, 파일
  상단에서 문제에 맞는 단위계로 변환한다 (예: `JanusEpimetheus.py`는 km·s, `SunJupiter.py`는
  AU·day·태양질량 단위).
- 좌표는 항상 `r_vec`(shape `(N_body, 2)`)와 `v_vec` 형태의 2D 벡터로 다룬다 (2D 문제로 단순화됨).
- 새 천체계 시뮬레이션을 추가할 때는 기존 패턴을 따른다: 상수 정의 → 초기 위치/속도 설정
  (`CM`으로 무게중심 보정) → `RK4` 루프 → `(t, n_body, 2)` numpy 배열에 주기적으로 기록 →
  `modules.DataIO.save_run`으로 h5 저장.
