CREATE TABLE IF NOT EXISTS `albums` (
  `aid` mediumint(8) NOT NULL AUTO_INCREMENT,
  `author_id` mediumint(8) NOT NULL,
  `title` varchar(120) NOT NULL,
  PRIMARY KEY (`aid`),
  UNIQUE KEY `author_id` (`author_id`,`title`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `photos` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` mediumint(9) NOT NULL,
  `album_id` mediumint(9) NOT NULL,
  `filename` varchar(33) NOT NULL,
  `caption` text,
  `tags` text,
  PRIMARY KEY (`pid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `users` (
  `uid` mediumint(9) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(41) NOT NULL,
  `bio` text,
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;