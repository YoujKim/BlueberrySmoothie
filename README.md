# 블루베리스무디

#### Django 프레임워크를 이용해 사투리 학습 웹 서비스를 구현하는 ICT 프로젝트 입니다.

<hr/>
(실행 guide)

### 1. git 연동

먼저 프로젝트를 로컬 디렉토리로 복사하기 위해서 git Bash를 실행하시고   
원하는 위치에서 다음 코드를 입력하시면 됩니다.   
<pre><code> git clone https://lab.hanium.or.kr/22_HG099/22_hg099.git  </code></pre>

저희는 일단 여러개의 브랜치를 사용하기보다는 하나의 main 브랜치를 사용해서 작업하는 것을 생각했는데,
동시에 개발할 일이 많아지면 각자 브랜치를 나눠서 작업하도록 하겠습니다.   

따라서 항상 작업 전에는 프로젝트 폴더로 이동 후 
<pre><code> git pull </code></pre>
명령어를 통해 프로젝트를 업데이트 해주신 후 코드를 수정해주시면 됩니다.

또한 코드 수정 후 다시 업로드 하실 때는 프로젝트 폴더로 이동 후  아래 코드를 순서대로 입력하시면 됩니다.
<pre><code> git add .
 git commit -m "{수정된 사항에 대한 내용 (ex ~~ 버그 수정 등)}"
 git push -u origin main </code></pre>

### 2. 프로그램 실행

프로젝트 실행을 위해서는 python 설치가 필수적입니다.    
따라서 명령 프롬프트 창에서 다음과 같이 명령어 'python'을 입력하여
<pre>C:\users\user> python</pre>
python이 실행되고 있는지, 버전은 3.x 이상인지 확인해 주시고   
python이 설치되지 않았거나 버전이 낮다면 python을 최신 버전으로 설치해주시면 됩니다.

코드를 작성하실 때는 편한 에디터 아무거나 사용하셔도 됩니다. (대표적으로 Visual Studio Code 등)

또 파이참(Pycharm)은 파이썬 개발을 위한 IDE로 설치하셔서 사용하시면 위 프로젝트를 조금 더 편하게 수행하실 수 있습니다.    
(꼭 설치할 필요는 없는 권장사항 입니다)

##### * 가상환경 실행 (중요)
위 프로젝트는 다른 프로젝트와의 충돌 등을 미연에 방지하기 위해 가상 환경에서 실행이 됩니다.    
따라서 프로젝트를 실행하실 때마다 항상 가상환경이 실행되었는지 확인하셔야 합니다.

<가상환경 설치방법>   
최초 1회만 실행해주시면 됩니다.   
1. 명령 프롬프트에 접속해서 프로젝트 폴더로 이동합니다.   
2. python -m venv venv를 입력합니다.
3. <pre> C:\Users\user\...\22_hg099> python -m venv venv </pre>

<가상환경 실행방법>
1. 명령 프롬프트에 접속해서 프로젝트 폴더로 이동합니다.
2. venv\Scripts\activate.bat을 입력합니다.   
(맥의 경우 source venv/bin.activate를 입력하시면 됩니다)
<pre> C:\Users\user\...\22_hg099> venv\Scripts\activate.bat </pre>
3. 프롬프트 앞에 (venv)라는 텍스트가 생기면 가상환경이 실행된 것입니다. 
프로젝트 실행 시 항상 이 (venv)가 앞에 표시되었는지 확인하시면 됩니다.
4. 가상환경 종료는 deactivate를 입력하면 됩니다. 

##### 프로그램 실행
가상환경 실행 후 프로젝트를 실행하기 위해서는 가상 환경 위에 Django를 비롯한 python 라이브러리들이 설치되어야 합니다.   

설치한 패키지들은 requirements.txt에 저장해두었기 때문에 가상환경하에서 해당 패키지들을 설치하면 됩니다.
requirements.txt 파일의 패키지들을 한번에 설치하는 방법은 다음과 같은 명령어를 입력하면 됩니다.
<pre> (venv) C:\Users\user\...\22_hg099> pip install -r requirements.txt </pre>
(주의) 항상 가상환경이 실행된 상태 (맨 앞에 (venv) 표시된 상황)에서 실행해주셔야 합니다.

패키지들이 잘 설치되었는지 확인하려면 pip list 명령어를 입력해서 확인하시면 됩니다.

또한 추후 새로운 기능 구현을 위해서 여러 패키지를 설치할 수 있기 때문에 새로 패키지를 설치하셨다면   
requirements.txt 파일을 업데이트 해주시고 github에 커밋하시면 됩니다.    
requirements.txt 파일을 업데이트 하는 방법은 가상 환경 하에서 다음 명령어를 입력하시면 됩니다.
<pre> (venv) C:\Users\user\...\22_hg099> pip freeze > requirements.txt </pre>

패키지들이 잘 설치되어 있다면 가상환경 상에서 프로젝트를 실행하시면 됩니다.    
프로젝트 실행은 프로젝트 폴더에서 다음과 같이 python manage.py runserver 명령을 입력하시면 됩니다.
<pre> (venv) C:\Users\user\...\22_hg099> python manage.py runserver </pre>

그러면 출력값 중 아래에 있는 서버 IP 주소 http://127.0.0.1:8000 를 웹 브라우저 주소 창에 입력하면 
구현된 웹 페이지를 확인할 수 있습니다.

서버를 종료하고 싶으면 ctrl+c 키를 누르시면 종료됩니다.

##### database 사용 부분
일단 저희가 로컬서버로 개발하면서 웹 페이지에 필요한 DB들(회원 목록 등)은 test용으로 사용됩니다.
data table을 새로 생성하였다면 기존 DB에 반영하기 위해 다음과 같은 명령어를 입력하시면 됩니다.   
<pre> (venv) C:\Users\user\...\22_hg099> python manage.py migrate </pre>   
아마 로그인 서비스 등의 실행을 위해서는 프로젝트 실행 전 위 명령어를 입력해야 서비스가 동작할 것입니다.   

django는 원래 기본적으로 sqlite를 이용하여 데이터베이스를 다루는데, 제가 mySQL 다루기가 편하기도 하고   
대량의 음성 DB를 구축해야하는 프로젝트 특성상 sqlite보다는 mySQL을 사용하는 것이 좋을 것 같아 mySQL 연동 코드를 config/settings.py에 추가해두었습니다.   
일단 프로젝트 구현 단계에서는 test 데이터가 쌓이기 때문에 일단 각자의 sqlite db를 사용하고,   
AWS 서버를 사용하기 시작하면 mySQL도 같이 연동하면 좋을 것 같습니다.

##### 관리자 계정 생성하기
웹 사이트의 관리자 계정을 생성하는 방법은 터미널에서 다음과 같이 python manage.py createsuperuser 명령을 입력하시면 됩니다.
<pre> (venv) C:\Users\user\...\22_hg099> python manage.py createsuperuser </pre>
그리고 사용자명과 이메일 주소를 입력하고, 비밀번호도 두번 입력하면 됩니다.

관리자 홈페이지는 다시 python manage.py runserver로 서버를 실행하고
웹 브라우저에서 http://127.0.0.1:8000/admin/  으로 접속 후 터미널에서 입력한 아이디와 비밀번호로 로그인 하면
관리자 페이지에 속할 수 있습니다.

### 3. Django 가이드

저희가 웹 서비스 구현을 위해 사용하는 프레임워크는 Django 입니다.
https://www.djangoproject.com/ (Django 공식 홈페이지)

djagno의 작동 구조를 간단하게 요약하면
1. 클라이언트가 도메인에 접속하면
2. URL에 따른 함수 실행 등의 정보가 기록되어 있는 urls.py를 요청하고
3. urls.py에서 언급하는 함수 또는 클래스는 views.py에서 정의합니다.
4. 자료의 형태를 정의한 클래스인 모델은 models.py에서 정의합니다.
5. models.py에서 정의한 모델에 맞게 데이터베이스에서 필요한 자료를 가져옵니다.
6. 데이터베이스에서 가져온 자료를 템플릿을 통해 웹 브라우저로 보냅니다.

또한 프로젝트에서 특정한 기능을 수행하는 단위 모듈인 앱을 정의해야 하는데, 이것은 시나리오 구상이 거의 완료된 후 어떤 앱을 정의할 지 논의 되면 어떤 앱을 사용할 지 결정할 예정입니다.

