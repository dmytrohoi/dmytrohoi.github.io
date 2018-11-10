import os

def github(publish_drafts=False): # 2

    os.system('pelican content -o output -s pelicanconf.py')
    try:  # 3
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass
    
    os.system('ghp-import output')  # 4
    os.system('git push --force git@github.com:dmytrohoi/dmytrohoi.github.io.git gh-pages:master') # 5
    os.system('rm -rf output')  # 6

def localHost():
    os.system('rm -rf output')
    os.system('fuser -k 8000/tcp')
    os.system('make html && make serve')

