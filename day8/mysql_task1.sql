/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - 测试数据库
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`测试数据库` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `测试数据库`;

/*Table structure for table `表1_学生表` */

DROP TABLE IF EXISTS `表1_学生表`;

CREATE TABLE `表1_学生表` (
  `sno` char(4) NOT NULL COMMENT '学生号',
  `Sn` char(8) NOT NULL COMMENT '学生名',
  `sex` char(2) NOT NULL COMMENT '性别',
  `age` int(2) DEFAULT NULL COMMENT '年龄',
  `dept` int(11) NOT NULL COMMENT '学生所在系',
  PRIMARY KEY (`sno`),
  UNIQUE KEY `name_num1` (`sno`),
  KEY `name_num` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='学生表';

/*Data for the table `表1_学生表` */

insert  into `表1_学生表`(`sno`,`Sn`,`sex`,`age`,`dept`) values ('S1','徐啸','女',17,2),('S2','辛国华','男',18,6),('S3','徐玮','女',20,1),('S4','邓一鸥','男',23,6),('S5','张激扬','男',19,6),('S6','张辉','女',22,3),('S7','王克华','男',18,6),('S8','王忍','男',19,3);

/*Table structure for table `表2_课程表` */

DROP TABLE IF EXISTS `表2_课程表`;

CREATE TABLE `表2_课程表` (
  `cno` char(4) NOT NULL COMMENT '课程号',
  `cn` char(19) NOT NULL COMMENT '课程名',
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `表2_课程表` */

insert  into `表2_课程表`(`cno`,`cn`) values ('C1','数学'),('C2','英语'),('C3','Fortran77'),('C4','Pascal'),('C5','政治'),('C6','物理'),('C7','逻辑');

/*Table structure for table `表3_学生选课表` */

DROP TABLE IF EXISTS `表3_学生选课表`;

CREATE TABLE `表3_学生选课表` (
  `sno` char(4) NOT NULL COMMENT '学生号',
  `cno` char(4) NOT NULL COMMENT '课程号',
  `grade` int(11) DEFAULT NULL COMMENT '分数',
  KEY `FK_表3_表1_sno` (`sno`),
  KEY `FK_表3_表2_cno` (`cno`),
  CONSTRAINT `FK_表3_表1_sno` FOREIGN KEY (`sno`) REFERENCES `表1_学生表` (`sno`),
  CONSTRAINT `FK_表3_表2_cno` FOREIGN KEY (`cno`) REFERENCES `表2_课程表` (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `表3_学生选课表` */

insert  into `表3_学生选课表`(`sno`,`cno`,`grade`) values ('S1','C1',80),('S1','C2',85),('S1','C4',56),('S1','C5',90),('S1','C6',75),('S2','C1',47),('S2','C3',80),('S2','C4',75),('S2','C5',70),('S3','C1',76),('S3','C2',70),('S3','C3',85),('S3','C4',86),('S3','C5',90),('S3','C6',99),('S4','C1',83),('S4','C2',85),('S4','C3',83),('S5','C2',99),('S6','C1',96),('S6','C2',80),('S6','C3',87);

/*Table structure for table `article` */

DROP TABLE IF EXISTS `article`;

CREATE TABLE `article` (
  `商品号` char(10) NOT NULL,
  `商品名` char(10) DEFAULT NULL,
  `单价` float DEFAULT NULL,
  `库存` int(11) DEFAULT NULL,
  PRIMARY KEY (`商品号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `article` */

insert  into `article`(`商品号`,`商品名`,`单价`,`库存`) values ('S001','计算机',5000,10),('S002','打印机',1000,12),('S003','洗衣机',800,10),('S004','电冰箱',1100,20);

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `顾客号` char(10) NOT NULL,
  `顾客名` char(10) DEFAULT NULL,
  `性别` char(2) DEFAULT NULL,
  `年龄` int(11) DEFAULT NULL,
  PRIMARY KEY (`顾客号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `customer` */

insert  into `customer`(`顾客号`,`顾客名`,`性别`,`年龄`) values ('G001','顾客','男',29),('G002','李四','女',25),('G003','王五','女',31),('G004','赵六','男',25);

/*Table structure for table `orderitem` */

DROP TABLE IF EXISTS `orderitem`;

CREATE TABLE `orderitem` (
  `顾客号` char(10) NOT NULL DEFAULT '',
  `商品号` char(10) NOT NULL DEFAULT '',
  `数量` int(11) DEFAULT NULL,
  `购买价` float DEFAULT NULL,
  `购买日期` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`顾客号`,`商品号`,`购买日期`),
  KEY `FK_article_orderitem` (`商品号`),
  CONSTRAINT `FK_article_orderitem` FOREIGN KEY (`商品号`) REFERENCES `article` (`商品号`),
  CONSTRAINT `FK_customer_orderitem` FOREIGN KEY (`顾客号`) REFERENCES `customer` (`顾客号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `orderitem` */

insert  into `orderitem`(`顾客号`,`商品号`,`数量`,`购买价`,`购买日期`) values ('G001','S001',2,4000,'2015-08-16 00:00:00'),('G001','S002',1,800,'2008-01-25 00:00:00'),('G001','S003',3,600,'2008-01-25 00:00:00'),('G001','S004',1,880,'2008-01-25 00:00:00'),('G002','S001',3,4500,'2008-01-01 00:00:00'),('G003','S001',1,5000,'2008-01-01 00:00:00'),('G003','S002',1,1000,'2008-01-01 00:00:00');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
