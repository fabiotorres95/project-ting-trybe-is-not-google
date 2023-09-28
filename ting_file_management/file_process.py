import ting_file_management.file_management as file_management


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    data = file_management.txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    instance.enqueue(result)

    print(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
