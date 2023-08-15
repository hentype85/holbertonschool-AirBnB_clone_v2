# AirBnB clone - Web framework

## pip3 install Flask

MySQL Default charset issues
If you get Flask errors after executing the curl ... commands, it might be because of the DEFAULT CHARSET. If it’s DEFAULT CHARSET=latam1, you might want to change it to DEFAULT CHARSET=utf8mb4, either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement.