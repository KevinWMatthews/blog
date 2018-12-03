from app import app, blog_post
from flask import render_template, redirect, url_for

all_blog_posts = [
    blog_post.BlogPost(
        'hello-world',
        'Hello, World!',
        '''Introduction to this blog.''',
        ['C'],
    ),
    blog_post.BlogPost(
        'python-list-comprehensions-in-ruby',
        'Python List Comprehensions... In Ruby?',
        '''What is the Ruby way?''',
        ['Ruby', 'syntax'],
    ),
    blog_post.BlogPost(
        '',
        'Test-Driven Design on AVR',
        '''Work in progress... based on
        <a href="https://github.com/KevinWMatthews/c-libATtiny861" class="in-text-link">
        this GitHub repo</a>.''',
        ['C', 'TDD', 'AVR'],
    ),
    blog_post.BlogPost(
        '',
        'C Memory Semantics',
        '''Coming soon.... Dive under the hood. Based on
        <a href="https://youtu.be/-dc5vqt2tgA" class="in-text-link">
        this awesome video</a>.''',
        ['C', 'Memory'],
    ),
    blog_post.BlogPost(
        '',
        'Rust Memory Semantics',
        '''Coming soon.... Explore how Rust's default move semantics differ from C's default copy.''',
        ['Rust', 'Memory'],
    ),
    blog_post.BlogPost(
        '',
        'Python Language Practices',
        '''Coming soon... Do you follow this core contributor's advice? Based on
        <a href="https://youtu.be/anrOzOapJ2E" class="in-text-link">
        this talk</a>.''',
        ['Python'],
    ),
    blog_post.BlogPost(
        '',
        'CSS Effects',
        '''Coming soon... transitions, animations, and general awesomeness.''',
        ['CSS'],
    ),
    blog_post.BlogPost(
        '',
        'CSS Layout',
        '''Coming soon... Boxen!''',
        ['CSS'],
    ),
    blog_post.BlogPost(
        '',
        'Parsing Command Line Options in Bash',
        '''Coming soon.... At some point everyone does it. Why not do it well? Based on
        <a href="https://github.com/KevinWMatthews/bash-arg_parse" class="in-text-link">
        this GitHub repo</a>.''',
        ['Bash'],
    ),
]

def get_tag_list():
    tags = []
    for post in all_blog_posts:
        for tag in post.tags:
            if tag not in tags:
                tags.append(tag)
    return tags

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    tags = get_tag_list()
    return render_template('index.html', posts=all_blog_posts, tags=tags)

@app.route('/post/<post>', methods=['GET'])
@app.route('/post/<post>.html', methods=['GET'])
def blog_post(post):
    return render_template('{}.html'.format(post))

@app.route('/about-me', methods=['GET'])
@app.route('/about-me.html', methods=['GET'])
def about_me():
    return render_template('blog_about_me.html')

@app.route('/about-this-blog', methods=['GET'])
@app.route('/about-this-blog.html', methods=['GET'])
def about_blog():
    return render_template('blog_about.html')

@app.route('/tags/<filter>', methods=['GET'])
@app.route('/tags/<filter>.html', methods=['GET'])
def index_filtered_by_tag(filter):
    # Convert to database - do this just to get off the ground.
    # Sanitize input!!
    posts_with_tag = []
    for post in all_blog_posts:
        for tag in post.tags:
            if tag == filter:
                posts_with_tag.append(post)

    if not posts_with_tag:
        return render_template('404.html'), 404

    all_tags = get_tag_list()
    return render_template('index.html',
        posts=posts_with_tag,
        tags=all_tags,
        filter=filter)
