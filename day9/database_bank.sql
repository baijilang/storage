/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bank`;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `account` varchar(8) NOT NULL COMMENT '账号',
  `sort` varchar(2) DEFAULT NULL,
  `status` char(10) DEFAULT NULL COMMENT '账户状态',
  `name` varchar(10) NOT NULL,
  `password` varchar(6) NOT NULL,
  `money` decimal(20,2) DEFAULT NULL,
  `bank_name` varchar(20) NOT NULL DEFAULT '中国工商银行',
  `country` varchar(10) DEFAULT NULL,
  `province` varchar(10) DEFAULT NULL,
  `stree` varchar(30) DEFAULT NULL,
  `tablet` varchar(20) DEFAULT NULL,
  `registerDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `users` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
