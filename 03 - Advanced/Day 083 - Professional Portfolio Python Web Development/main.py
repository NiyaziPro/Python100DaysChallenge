# app.py - Main Flask Application
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'


# Contact Form
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')


# Sample project data
projects = [
    {
        'id': 1,
        'title': 'E-Commerce Website',
        'description': 'Full-stack e-commerce platform built with Flask, SQLAlchemy, and Bootstrap',
        'tech': ['Flask', 'SQLAlchemy', 'Bootstrap', 'JavaScript'],
        'image': 'ecommerce.jpg',
        'github': 'https://github.com/yourusername/ecommerce-project',
        'demo': 'https://your-ecommerce-demo.com'
    },
    {
        'id': 2,
        'title': 'Blog Platform',
        'description': 'Dynamic blog platform with user authentication and admin panel',
        'tech': ['Python', 'Flask', 'SQLite', 'HTML/CSS'],
        'image': 'blog.jpg',
        'github': 'https://github.com/yourusername/blog-platform',
        'demo': 'https://your-blog-demo.com'
    },
    {
        'id': 3,
        'title': 'Weather App',
        'description': 'Real-time weather application using OpenWeather API',
        'tech': ['Flask', 'API Integration', 'JavaScript', 'Chart.js'],
        'image': 'weather.jpg',
        'github': 'https://github.com/yourusername/weather-app',
        'demo': 'https://your-weather-demo.com'
    },
    {
        'id': 4,
        'title': 'Task Management System',
        'description': 'Collaborative task management tool with real-time updates',
        'tech': ['Flask-SocketIO', 'SQLAlchemy', 'Bootstrap', 'jQuery'],
        'image': 'taskmanager.jpg',
        'github': 'https://github.com/yourusername/task-manager',
        'demo': 'https://your-taskmanager-demo.com'
    }
]

# Skills data
skills = {
    'Programming Languages': ['Python', 'JavaScript', 'HTML5', 'CSS3', 'SQL'],
    'Frameworks & Libraries': ['Flask', 'Bootstrap', 'jQuery', 'SQLAlchemy', 'WTForms'],
    'Databases': ['SQLite', 'PostgreSQL', 'MySQL'],
    'Tools & Technologies': ['Git', 'GitHub', 'VS Code', 'Postman', 'Heroku']
}


@app.route('/')
def home():
    return render_template('index.html', projects=projects[:3])


@app.route('/about')
def about():
    return render_template('about.html', skills=skills)


@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)


@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real application, you would send an email or save to database
        flash(f'Thank you {form.name.data}! Your message has been sent.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)

