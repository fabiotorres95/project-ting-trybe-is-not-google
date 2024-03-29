import ting_file_management.file_management as file_management
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    data = file_management.txt_importer(path_file)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }
    instance.enqueue(result)

    print(result)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")

    result = instance.dequeue()

    print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))

    except IndexError:
        print("Posição inválida", file=sys.stderr)
