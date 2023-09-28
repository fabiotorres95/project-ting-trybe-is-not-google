from sys import stderr


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=stderr)
        return
    try:

        with open(path_file, "r") as file:
            return _make_list(file)

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=stderr)

    # except ValueError:
    #     print("Formato inválido", file=stderr)


def _make_list(data):
    result = []
    for line in data:
        line = line.strip()
        result.append(line)

    return result


print(txt_importer("test.csv"))
