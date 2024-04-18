## Setup and deployment
If you're unfamiliar with Django, the [official tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) explains how to set up a new project.

As an overview, you'll need to clone a local copy of this repository, install the [requirements](requirements.txt), and run the database migrations using `python manage.py migrate` from within the outer `photo_gallery` directory that contains `manage.py`. From there, you can run the application locally using `python manage.py runserver` from within the same directory.

When you're ready to deploy a production (i.e. public) version of the website, be sure to read Django's [deployment documentation](https://docs.djangoproject.com/en/4.0/howto/deployment/) (including the [deployment checklist](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)) to avoid security vulnerabilities and other issues.

For this project, the following deployment steps will also be necessary:

- Use [prod_urls.py](photo_gallery/photo_gallery/prod_urls.py) (which removes [development-only media file serving](https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development)) rather than [urls.py](photo_gallery/photo_gallery/urls.py)
- Configure and use [prod_settings.py](photo_gallery/photo_gallery/prod_settings.py) (which ensures that project settings are safe and appropriate for production), referring to the settings documentation where needed, rather than [settings.py](photo_gallery/photo_gallery/settings.py)
- Run a site name data migration (which is used to construct absolute URLs, e.g. in the XML sitemap and HTML tags) using the template and instructions in [site_name_migration_template.py](photo_gallery/photo_gallery/site_name_migration_template.py)
- Change the [robots.txt](photo_gallery/templates/robots.txt) sitemap link to the correct URL (for simplicity, this doesn't use the site data in the previous step)
- Configure contact message email alerts (implemented in [contact/views.py](photo_gallery/contact/views.py)) via the email settings in [prod_settings.py](photo_gallery/photo_gallery/prod_settings.py), if desired (otherwise, just check messages regularly via the Django admin site)
- Change the [favicon](photo_gallery/global_static/favicon.ico) if desired


## DevOps Requirements 
Description

An open-source version of the photo gallery application.

Tools

● Version Control: GitHub for code storage.

● Dockerize full project.

● CI/CD: GitHub Actions for automating deployment.

● Infrastructure as Code: Terraform for defining infrastructure elements.

● Database and Log Monitoring: ELK Stack (Elasticsearch Logstash, Kibana) for log monitoring in Docker Environtment.

● Alerting: Prometheus and Grafana for alerting in Docker Environment.

● Automatic Deployment: Deploy the application automatically.

● Write Readme for each every single step for Docker , Terraform, ELK ,Prometheus , Grafana and Deployment script . 
"# photo_gallery" 
asdfdasfg
