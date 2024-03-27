
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        else:
            end += 1
        line, text = text[:end], text[end:]
        lines.append(line)

    return lines



