import sys
import os
import jinja2
import shutil


def createProjectStructure(projectName: str):
    os.mkdir(projectName)
    os.mkdir("{}/.vscode".format(projectName))
    os.mkdir("{}/include".format(projectName))
    os.mkdir("{}/src".format(projectName))
    os.mkdir("{}/doc".format(projectName))
    os.mkdir("{}/test".format(projectName))


def createReadMeFile(projectName: str, projectDescription: str):
    path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '../template/README.md.j2')
    with open(path) as template_file:
        template = jinja2.Template(template_file.read())

    if template is None:
        exit - 1

    with open("{}/README.md".format(projectName), "w") as readme_file:
        result = template.render(
            project={"name": projectName, "description": projectDescription})
        print(result, file=readme_file)


def createSummaryFile(path: str):
    in_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../template/SUMMARY.md")
    out_file_path = os.path.join(os.path.dirname(
        os.path.abspath(path)), "doc/SUMMARY.md")

    shutil.copyfile(in_file_path, out_file_path)


def createGitFiles(path: str):
    in_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../template/.gitattributes")
    out_file_path = os.path.join(os.path.dirname(
        os.path.abspath(path)), ".gitattributes")

    shutil.copyfile(in_file_path, out_file_path)

    in_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../template/.gitignore")
    out_file_path = os.path.join(os.path.dirname(
        os.path.abspath(path)), ".gitignore")

    shutil.copyfile(in_file_path, out_file_path)


def createLicenceFile(path: str):
    in_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "../template/LICENCE")
    out_file_path = os.path.join(os.path.dirname(
        os.path.abspath(path)), "LICENCE")

    shutil.copyfile(in_file_path, out_file_path)
