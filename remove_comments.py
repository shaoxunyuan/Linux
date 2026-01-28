import re
import os

def remove_html_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Processed: {os.path.basename(file_path)}')

docs_dir = r'd:\WPS同步文件夹\GithubRepo\Linux\docs'
for filename in os.listdir(docs_dir):
    if filename.endswith('.html'):
        file_path = os.path.join(docs_dir, filename)
        remove_html_comments(file_path)

print('Done!')