pandoc 20190527-dis.md --self-contained  --css github-pandoc.css  -o 20190527-dis.html;  pandoc ilsp_nlp_services.md --self-contained  --css github-pandoc.css  -o ilsp_nlp_services.html ; rsync -av /home/prokopis/src/eclipse-workspace-2019/DISTitles/doc/ prokopis@lingua:/var/www/html/nlp//2019-dis/doc/;  rsync -av /home/prokopis/src/eclipse-workspace-2019/DISTitles/txt/   prokopis@lingua:/var/www/html/nlp//2019-dis/txt/;
