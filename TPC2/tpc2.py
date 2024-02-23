import re
import sys

def headers(md):
    res = re.sub(r'^#(?!#) (.+)', r'<h1>\1</h1>', md, flags=re.MULTILINE)
    res = re.sub(r'^## (.+)', r'<h2>\1</h2>', res, flags=re.MULTILINE)
    res = re.sub(r'^### (.+)', r'<h3>\1</h3>', res, flags=re.MULTILINE)
    return "<p>" + res + "</p>"


def bold(md): 
    res = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md)
    return "<p>" + res + "</p>"

def italico(md):
    res = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md)
    return "<p>" + res + "</p>"

def imagem(md):
    res = re.sub(r'^\s*!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', md, flags=re.MULTILINE)
    return "<p>" + res + "</p>"

def link(md):
    res = re.sub(r'(?<!!)\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', md)
    return "<p>" + res + "</p>"

def listas(md):
    ol_open = False
    res = ""

    lines = md.split('\n')

    for line in lines:
        if re.match(r'^\d+\.\s+.+', line):
            if not ol_open:
                res += '<ol>'
                ol_open = True
            res += '<li>' + line.split('. ', 1)[1] + '</li>'
        else:
            if ol_open:
                res += '</ol>'
                ol_open = False
            res += line + '\n'  

    if ol_open:
        res += '</ol>'

    return "<p>" + res + "</p>"


def main(inp):
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{inp[1].replace('.md', '')}</title>
        <meta charset="UTF-8">
    </head>
    <body>
    '''
    
    with open(inp[1], 'r', encoding='utf-8') as md_file:
        md = md_file.read()
        aux = ''
        aux += imagem(link(listas(italico(bold(headers(md))))))
        lines = aux.split('\n')
        for line in lines:
            html += '<p>' + line + '</p>'
    
    html += '''
    </body>
    </html>
    '''

    html_filename = inp[1].replace('.md', '') + '.html'
    with open(html_filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html)

if __name__ == "__main__":
    main(sys.argv)
