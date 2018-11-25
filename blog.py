from app import app

@app.shell_context_processor
def make_shell_context():
    return {}

if __name__ == '__main__':
    from flask_frozen import Freezer
    freezer = Freezer(app)
    freezer.run()
