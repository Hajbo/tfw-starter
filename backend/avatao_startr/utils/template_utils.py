from jinja2 import Template


def render_template(template_file, destination_file, data) -> None:
    with open(destination_file, "w+") as result_file:
        with open(template_file, "r") as empty_template_file:
            template = Template(empty_template_file.read())
        result_file.write(template.render(data=data))
