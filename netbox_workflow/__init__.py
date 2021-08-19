from extras.plugins import PluginConfig


class Workflow(PluginConfig):
    name = "workflow"
    verbose_name = "Workflow"
    description = "Workflow for Netbox"
    version = "0.1"
    author = "Ezra Liu"
    author_email = "zerdliu@gmail.com"
    base_url = "workflow"
    required_settings = {}
    default_settings = {}

config = Workflow
