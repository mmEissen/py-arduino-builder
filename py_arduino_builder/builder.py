import os
import shutil
import typing as t


TEMPLATE_SUFFIX = ".template"

def build_template(template_path: str, context: t.Any, output_path: str,) -> None:
    with open(template_path) as template_file:
        content = template_file.read()
    content = content.format(context=context)
    with open(output_path, "w") as output_file:
        output_file.write(content)


def build_templates(template_dir: str, context: t.Any, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    for dirpath, dirnames, filenames in os.walk(template_dir):
        for dirname in dirnames:
            full_name = os.path.join(dirpath, dirname)
            relative_name = os.path.relpath(full_name, start=template_dir)
            os.mkdir(os.path.join(output_dir, relative_name))
        for filename in filenames:
            full_name = os.path.join(dirpath, filename)
            relative_name = os.path.relpath(full_name, start=template_dir)
            if full_name.endswith(TEMPLATE_SUFFIX):
                output_name = os.path.join(output_dir, relative_name[:-len(TEMPLATE_SUFFIX)])
                build_template(full_name, context, output_name)
            else:
                shutil.copy(full_name, os.path.join(output_dir, relative_name))



