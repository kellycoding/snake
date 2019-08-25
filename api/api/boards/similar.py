import os
import json
from django.conf import settings


similar_file = os.path.join(settings.BASE_DIR, 'data', 'similar.json')
with open(similar_file) as f:
    similar_data = json.loads(f.read())

def similar(word):
    return similar_data.get(word, [])
