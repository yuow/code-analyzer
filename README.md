1. скачать и настроить postgreSQL
2. создать базу данных с любым названием, например `code_analyzer`
3. скачать репозиторий и открыть его содержимое в терминале, например:
    ```
    git clone git@github.com:yuow/code-analyzer.git
    cd code-analyzer
    ```

4. восстановить базу данных из дампа, например:
    ```
    pg_restore -d code_analyzer keyloggerdb
    ```
      ,где `code_analyzer` - название созданной базы данных

5. инициализировать виртуальное окружение, например:
    ```
    python -m venv venv
    ```
6. установить зависимости:
    ```
    ./venv/bin/pip install -r requirements.txt
    ```
7. прописать в файле `.env` данные для подключения к базе данных
8. запустить программу: `./venv/bin/python main.py`
