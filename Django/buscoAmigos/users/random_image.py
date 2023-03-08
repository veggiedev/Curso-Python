import os
import random
from django import template
from django.conf import settings




# module-level variable
register = template.Library()
@register.simple_tag
def random_image(image_dir):
        rel_dir = settings.RANDOM_IMAGE_DIR
        rand_dir = os.path.join(settings.MEDIA_ROOT, rel_dir)
        files = [f for f in os.listdir(rand_dir)]
        return os.path.join(rel_dir, random.choice(files))

