from app import app

@app.shell_context_processor
def make_shell_context():
    return {}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Create static website content')
    parser.add_argument('-b', '--build', help="Build static pages", action='store_true')
    parser.add_argument('-t', '--test', help="Serve static pages from test server", action='store_true')
    parser.add_argument('-d', '--deploy', help="Create Netlify deploy", action='store_true')
    args = parser.parse_args()

    if args.build:
        print('Building static files')
    elif args.test:
        print('Serving static files')
    elif args.deploy:
        print('Creating Netlify deploy')
    else:
        parser.print_help()
        parser.exit()

    from flask_frozen import Freezer
    freezer = Freezer(app)

    @freezer.register_generator
    def error_handlers():
        yield "/404.html"

    if args.build:
        freezer.freeze()
    elif args.test:
        freezer.run()
    elif args.deploy:
        freezer.freeze()
    
        from pathlib import Path
        import shutil
        file = Path('_redirects')
        source = Path('netlify') / file
        target = Path('app/build') / file
        shutil.copy(str(source), str(target))
