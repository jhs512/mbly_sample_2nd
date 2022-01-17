# 팁과 작업내역

---

# 팁 1

- .gitignore 파일이 없다면 https://www.toptal.com/developers/gitignore/api/pycharm,django 파일로부터 만들어보세요.
    - 이 앱(https://www.toptal.com/developers/gitignore)은 각종 IDE와 프레임워크 조합에 맞는 .gitignore 파일을 만들어준다.

# 팁 2

- git에서 관리를 시작한 파일의 이름이나 위치를 변경할 때는 git mv 명령어를 쓰면 좋습니다.
    - git mv 원래경로/원래파일명 새경로/새파일명
        - EX : git mv db.sql database_util.sql
    - 이렇게 하지 않고 그냥 파일명을 변경하면 git에서는 해당 파일이 삭제되고 새로운 파일이 생겼다고 판단합니다.

# 팁 3

- git에서 관리를 시작한 파일이나 폴더를 제거하려면 git rm 명령어를 사용하면 좋습니다.
    - git mv 원래파일경로 새래파일경로
        - EX : git mv db.sql database_util.sql
    - 이렇게 하지 않고 그냥 파일명을 변경하면 git에서는 해당 파일이 삭제되고 새로운 파일이 생겼다고 판단합니다.

# 팁 3

- 혹시나 git에서 관리를 시작한 파일의 이름이나 위치를 변경할 때는 git mv 명령어를 쓰면 좋습니다.
    - git rm -r 폴더경로
        - 폴더삭제
        - 실제로 폴더가 삭제되진 않는다. git 에서만 제거됨
    - git rm --cached -r 폴더경로
        - git add 만 진행되었고, 아직 커밋되지 않은 건은 --cached 를 붙여주세요.
    - git rm 파일경로
        - 파일삭제
    - git rm --cached -r 파일경로
        - git add 만 진행되었고, 아직 커밋되지 않은 건은 --cached 를 붙여주세요.

---

# 커밋 1

- 기존 리포지터리 https://github.com/jhs512/django_sample1 의 마스터 브랜치 내용 복사해서 새로 시작
- 기존 코드에 문제가 많으니 하나하나, 고쳐가 봅시다.

# 커밋 2

- .gitignore 파일이 없어서 생성
- db.sql파일을 database_util.sql으로 이름 변경
    - 해당 파일은 유용한 SQL을 모아두는 용도이기 때문에, 해당 이름이 더 적절하다고 판단.

# 커밋 3

- .idea 폴더를 git 관리대상에서 제외
  - git rm -r .idea 