# GitLogParser

Parse Git log and output formatted JSON.

## How to use
    $ git log | python PATH/TO/parser.pyc

## Output sample

    [
        {
            "commit_id":  "commit id",
            "comment":    "some comment",
            "author":     "Hiroki Toyokawa",
            "merge":      "",
            "date":       "Fri May 10 10:00:00 2013 +0900",
            "message":    "Create README.md",
            "email":      "hoge@gmail.com"
        },
        ...
    ]

### License

MIT License
