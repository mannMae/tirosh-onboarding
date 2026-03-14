1. Introduction

이번 온보딩에서는 **서비스 lifecycle을 단계적으로 구현**합니다.

각 챕터에서는 다음 단계의 실습을 수행하게 됩니다.

```
Repository Setup
Git Workflow
Issue-driven Development
Service Packaging
Continuous Integration
Service Execution & Containerization
Logging
Metrics
Tracing
Continuous Deployment
```

각 단계는 다음 조건을 만족해야 다음 단계로 진행할 수 있습니다.

- Pull Request 생성 가능
- CI 검증 통과
- 패키지 빌드 성공
- 서비스 실행 가능
- Observability 데이터 확인 가능

2. Repository Setup

- Public GitHub repository 생성 후, 다음 설정을 구성합니다.
    - main branch protection rule 생성
    - main branch 직접 push 금지
    - Pull Request를 통해서만 merge 가능
    - squash merge만 허용
    - merge 전에 CI 통과 필요
- 또한 로컬 환경에서 repository를 clone하여 다음 작업을 수행합니다.
    
    ```bash
    git clone
    git switch
    git add
    git commit
    git push
    ```
    
- feature branch를 생성하고 첫 Pull Request를 생성합니다.
