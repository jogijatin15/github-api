# API Testing using Newman (Postman CLI)

## Installing Newman
Install Newman from npm globally on your system allowing you to run it from anywhere
```
$ npm install -g newman
```

## Execute scripts
```
newman run collections/git.postman_collection.json --environment collections/newman-env.postman_environment.json --reporters cli,junit,html --reporter-junit-export testresults/unformatted/xmlOut.xml --reporter-html-export testresults/unformatted/htmlOut.html
```

## More Info
For more information on newman cli, visit the site [newman page](https://www.getpostman.com/docs/postman/collection_runs/command_line_integration_with_newman)
