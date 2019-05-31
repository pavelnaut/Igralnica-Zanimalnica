from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ChildApplicationPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class ChildApplicationPluginPublisher(CMSPluginBase):
    model = ChildApplicationPluginModel  # model where plugin data are saved
    module = _("Applications")
    name = _("Applications Plugin")  # name of the plugin in the interface
    render_template = "application.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context