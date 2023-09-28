def exists_word(word, instance):
    word_lower = word.lower()
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        path = file['nome_do_arquivo']
        lines = file['linhas_do_arquivo']
        for j in range(len(lines)):
            line = lines[j].lower()
            if word_lower in line:
                if len(result) == 0 or result[i]['arquivo'] != path:
                    result.append({
                        'palavra': word,
                        'arquivo': path,
                        'ocorrencias': [
                            {
                                'linha': j + 1
                            }
                        ]
                    })
                else:
                    result[i]['ocorrencias'].append({
                        'linha': j + 1
                    })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
