#!/bin/env python3

import sys
import io
import re

with io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8') as f:
  s = re.compile("""
    ( \s
    | South.Carolina.Social.Studies.College..and.Career.Ready.Standards\s+Page\s+\d+
    | Key\s+Concepts?\s+Standards
    | The.student.will:
    | References\s+Anderson.*
    )
    \s*
    """, re.X | re.S | re.M)
  content = s.sub(' ', f.read())
  content = re.compile(r'\s+').sub(' ', content);
  # print (content)
  # return
  s = re.compile("""
    (
      ((?P<T1>[0-9A-Z]{1,3}(\.[0-9A-Z]{1,2}){2,4}))
    | ((?P<T2>Standard\s\d):)
    | ((Enduring\s(?P<T3>Understanding)):)
    )
    \s
    (?P<TS>(([(A-Z]([^.:]|[a-z]\.[a-z]\.|U\.\s?S\.?|\.\.){8,}\.[)]?)\s)+)
    """, re.X)
  n = 0
  for m in s.finditer(content):
      n = n + 1
      tags = [ m.group(i) for i in ['T1','T2','T3'] ]
      tag = next(( i for i in tags if i is not None ),"?")
      print(u'{},"{}","{}"'.format( n, tag, m.group('TS')))

