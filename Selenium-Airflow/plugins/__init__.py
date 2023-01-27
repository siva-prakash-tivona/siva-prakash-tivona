from airflow.plugins_manager import AirflowPlugin
from plugins.hooks.Selenium_hook import SeleniumHook
from plugins.operators.Selenium_operator import SeleniumOperator


class SeleniumPlugin(AirflowPlugin):
    name = 'selenium_plugin'
    operators = [SeleniumOperator]
    hooks = [SeleniumHook]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []