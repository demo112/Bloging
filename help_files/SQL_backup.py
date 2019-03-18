#!/usr/bin/bash


backup = '/root/djangobackup'

projectname = 'mysite'

dirname = '/root/mysite'

if [$UID -ne 0]; then
echo
"backup fail,please using root again" | mail
"sorry,backup fail"
200922702 @ qq.com

sleep(2)
exit(0)

fi

cd ${dirname};

python3
manage.py
dumpdata - -format = json > ${backup} /${projectname} - `date + % Y - % m - % d
`.json

cd ${
        backup
    } & & tar
czvf ${projectname} - `date + % Y - % m - % d
`.json.tar.gz *.json

find ${backup} - type
f - name
"*.json" - exec
rm - rf
{} \;



if [$? -eq 0]; then

echo
"backup ${projectname}-`date +%Y-%m-%d` successful" | mail
"backup success"
200922702 @ qq.com

else

echo
"backup ${projectname}-`date +%Y-%m-%d` fail" | mail
"sorry,backup fail"
200922702 @ qq.com

fi

find ${backup} - type
f - mtime + 30 | xargs
rm - rf
