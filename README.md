## Crawler LMS Pipefy

Crawler criado para comunicação entre pipefy e easy-lms.


Variáveis de ambiente utilizadas:

Variável de ambiente  | Valor
------------- | -------------
EASY_LMS_EMAIL | Email da conta do LMS
EASY_LMS_PASSWORD | Password da conta do LMS
TABLE_PIPEFY_ID | Identificador da database a ser puxada
SERVER_PIPEFY_API_URL | URL da api a ser chamada
SCRIPT_PATH | Onde está o script
CULTURE_FIT_EXAM_ID | ID da avaliação de cultura
DISC_EXAM_URL | URL da avaliacao DISK


## Run

Para rodar, você precisará do docker. Com docker instalado, builde a imagem
e exponha a porta 80. Dentro do repositório, digite:

`docker build .`

e depois

`docker run -p 80:80`

