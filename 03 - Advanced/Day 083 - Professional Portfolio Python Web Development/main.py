from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# Example project data (normally this would live in data/projects.json)
PROJECTS = [
    {
        "title": "Personal Blog (Flask)",
        "slug": "flask-blog",
        "summary": "A markdown-based blog built with Flask and SQLite.",
        "description": "Full CRUD, tagging, markdown support, and deployment pipeline.",
        "featured": True,
        "tech": ["Flask", "SQLAlchemy", "Markdown"],
        "link": "https://example.com"
    },
    {
        "title": "Weather App (API)",
        "slug": "weather-api-app",
        "summary": "A small app that fetches weather from a public API.",
        "description": "Shows usage of external APIs, caching, and error handling.",
        "featured": True,
        "tech": ["Flask", "Requests", "Redis"],
        "link": "https://example.com"
    }
]

# Minimal inline templates
layout = """
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>{{ title or 'My Portfolio' }}</title></head>
<body>
<nav>
  <a href="/">Home</a> |
  <a href="/projects">Projects</a> |
  <a href="/about">About</a> |
  <a href="/contact">Contact</a>
</nav>
<hr>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>{% for m in messages %}<li>{{ m }}</li>{% endfor %}</ul>
  {% endif %}
{% endwith %}

{% block content %}{% endblock %}
</body>
</html>
"""

@app.route('/')
def index():
    featured = [p for p in PROJECTS if p.get('featured')][:3]
    template = """{% extends layout %}{% block content %}
    <h1>Welcome to my Portfolio</h1>
    <h2>Featured Projects</h2>
    <ul>{% for p in projects %}<li><a href='/projects/{{p.slug}}'>{{p.title}}</a></li>{% endfor %}</ul>
    {% endblock %}"""
    return render_template_string(template, layout=layout, projects=featured)

@app.route('/about')
def about():
    template = """{% extends layout %}{% block content %}<h1>About</h1><p>This is my portfolio site built with Flask.</p>{% endblock %}"""
    return render_template_string(template, layout=layout)

@app.route('/projects')
def projects():
    template = """{% extends layout %}{% block content %}<h1>All Projects</h1>
    <ul>{% for p in projects %}<li><a href='/projects/{{p.slug}}'>{{p.title}}</a></li>{% endfor %}</ul>
    {% endblock %}"""
    return render_template_string(template, layout=layout, projects=PROJECTS)

@app.route('/projects/<slug>')
def project_detail(slug):
    project = next((p for p in PROJECTS if p['slug'] == slug), None)
    if not project:
        return "<h1>404 - Project Not Found</h1>", 404
    template = """{% extends layout %}{% block content %}
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <p><strong>Tech:</strong> {{ project.tech|join(', ') }}</p>
    <p><a href='{{ project.link }}'>Live demo / repo</a></p>
    {% endblock %}"""
    return render_template_string(template, layout=layout, project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thanks for your message — I will reply soon!')
        return redirect(url_for('contact'))
    template = """{% extends layout %}{% block content %}
    <h1>Contact</h1>
    <form method='post'>
      <input name='name' placeholder='Your Name'><br>
      <input name='email' type='email' placeholder='Your Email'><br>
      <textarea name='message' placeholder='Message'></textarea><br>
      <button type='submit'>Send</button>
    </form>
    {% endblock %}"""
    return render_template_string(template, layout=layout)

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)