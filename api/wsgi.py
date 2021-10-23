# coding: utf-8

from src import create_app, db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db}


if __name__ == '__main__':
    app.run(debug=True, port='8000')
