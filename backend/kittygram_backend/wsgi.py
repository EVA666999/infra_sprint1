<<<<<<< HEAD


=======
>>>>>>> 19ba369 (починил сертификат)
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kittygram_backend.settings')

application = get_wsgi_application()
