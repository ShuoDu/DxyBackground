from django.contrib import admin

# Register your models here.
from models import main_message
from models import messageType
from models import service_type
from models import service_detail_type
from models import service_message
from models import message_img

import xadmin
xadmin.site.register(messageType)
xadmin.site.register(main_message)
xadmin.site.register(service_type)
xadmin.site.register(service_detail_type)
xadmin.site.register(service_message)
xadmin.site.register(message_img)
