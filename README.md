<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Job Portal - README by Aniket</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      line-height: 1.6;
      color: #333;
    }
    h1, h2, h3 {
      color: #005b96;
    }
    code, pre {
      background: #f4f4f4;
      padding: 6px;
      border-radius: 5px;
      display: block;
      margin-bottom: 10px;
    }
    ul {
      margin-left: 20px;
    }
    a {
      color: #0077cc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .section {
      margin-bottom: 40px;
    }
  </style>
</head>
<body>

  <h1>🧑‍💼 Job Portal - Django Project</h1>
  <p>A full-featured Job Portal web application built with Django by <strong>Aniket Sahu</strong>. This project allows users to register, search for jobs, apply online, and manage job postings—ideal for learning Django and job board systems.</p>

  <div class="section">
    <h2>🚀 Features</h2>
    <ul>
      <li>📝 User Registration & Authentication</li>
      <li>🔍 Search and Filter Jobs</li>
      <li>📄 Job Posting & Application Management</li>
      <li>👨‍💼 Admin Dashboard for Job Management</li>
      <li>📁 Static and Template Integration</li>
      <li>🔒 Secure Login System</li>
    </ul>
  </div>

  <div class="section">
    <h2>🛠️ Technologies Used</h2>
    <ul>
      <li><strong>Backend:</strong> Python, Django</li>
      <li><strong>Frontend:</strong> HTML, CSS, Django Templates</li>
      <li><strong>Database:</strong> SQLite</li>
      <li><strong>Others:</strong> Django Admin, Migrations, Static Files</li>
    </ul>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre><code>
JOBPORTAL/
├── JOB/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
├── JOBPORTAL/
│   └── settings.py
├── manage.py
    </code></pre>
  </div>

  <div class="section">
    <h2>🧑‍💻 Getting Started</h2>
    <h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/jobportal.git
cd jobportal</code></pre>

    <h3>2. Create & Activate Virtual Environment</h3>
    <pre><code>python -m venv venv
venv\Scripts\activate  (Windows)
source venv/bin/activate  (macOS/Linux)</code></pre>

    <h3>3. Install Dependencies</h3>
    <pre><code>pip install django</code></pre>

    <h3>4. Apply Migrations</h3>
    <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

    <h3>5. Create Superuser (Optional)</h3>
    <pre><code>python manage.py createsuperuser</code></pre>

    <h3>6. Run the Server</h3>
    <pre><code>python manage.py runserver</code></pre>

    <p>Open in browser: <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a></p>
  </div>

  <div class="section">
    <h2>📌 Author</h2>
    <p><strong>Aniket Sahu</strong></p>
    <p>
      <a href="https://www.linkedin.com/" target="_blank">LinkedIn</a> • 
      <a href="https://github.com/aniket-sahu" target="_blank">GitHub</a> • 
      <a href="mailto:aniketsahu@example.com">Email</a>
    </p>
  </div>

  <div class="section">
    <h2>📃 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
  </div>

</body>
</html>
