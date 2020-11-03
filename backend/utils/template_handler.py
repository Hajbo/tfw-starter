from jinja2 import Template

def render_template(path_to_template_file, data):
    with open(path_to_template_file, 'r') as template_file:
        template = Template(template_file.read())
    return template.render(data=data)