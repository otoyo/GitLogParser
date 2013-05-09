#!/usr/bin/python
# coding: utf-8
import sys
import commands
import re
import json
import urllib

def main():
    p_commits   = re.compile('^commit ', re.MULTILINE)
    p_merge     = re.compile('^Merge: *(.*)$')
    p_author    = re.compile('^Author: *(.*) <(\S+)>$')
    p_date      = re.compile('^Date: *(.*)$')
    p_message   = re.compile('^ {4}(.*)$')

    stdin = sys.stdin.read()
    
    if not stdin:
        print "[error] no input"
        sys.exit()

    commits = p_commits.split(stdin)

    if len(commits) < 2:
        print "[error] no log"
        sys.exit()

    commits.pop(0)

    logs = []

    for commit in commits:
        lines = commit.splitlines()

        commit_id = lines.pop(0)

        merge   = ''
        author  = ''
        email   = ''
        date    = ''
        body    = ''
        message = ''
        comment = ''

        for line in lines:
            m_merge     = p_merge.search(line)
            m_author    = p_author.search(line)
            m_date      = p_date.search(line)

            if m_merge:
                merge = m_merge.group(1)
            elif m_author:
                author = m_author.group(1)
                email  = m_author.group(2)
            elif m_date:
                date = m_date.group(1)
            else:
                body = body + line + '\n'

        comment_lines = body.splitlines()
        comment_lines.pop(0)
        
        message = p_message.sub(r'\1', comment_lines.pop(0))

        if len(comment_lines) > 0:
            comment = '\n'.join(comment_lines)
        
        try:
            logs.append({
                'commit_id': commit_id,
                'merge': merge,
                'author': author,
                'email': email,
                'date': date,
                'message': unicode(message, 'utf-8'),
                'comment': unicode(comment, 'utf-8')
            })
        except:
            print '[error] ', sys.exc_info()[0]
            sys.exit()
    
    print json.dumps(logs)

if __name__ == '__main__':
    main()
