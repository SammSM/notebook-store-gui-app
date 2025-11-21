/*
SQLyog Community v13.3.1 (64 bit)
MySQL - 8.0.42 : Database - notebook_store
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`notebook_store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `notebook_store`;

/*Table structure for table `admins` */

DROP TABLE IF EXISTS `admins`;

CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `admins` */

/*Table structure for table `brands` */

DROP TABLE IF EXISTS `brands`;

CREATE TABLE `brands` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `brands_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `brands` */

insert  into `brands`(`id`,`name`,`country_id`) values 
(1,'Apple',1),
(2,'Dell',1),
(3,'Asus',2),
(4,'Acer',2),
(5,'MSI',2),
(6,'Lenovo',3),
(7,'Samsung',4),
(8,'HP',1);

/*Table structure for table `countries` */

DROP TABLE IF EXISTS `countries`;

CREATE TABLE `countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `countries` */

insert  into `countries`(`id`,`name`) values 
(1,'USA'),
(2,'Taiwan'),
(3,'China'),
(4,'South Korea');

/*Table structure for table `models` */

DROP TABLE IF EXISTS `models`;

CREATE TABLE `models` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `brand_id` int DEFAULT NULL,
  `type_id` int DEFAULT NULL,
  `os_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_brands` (`brand_id`),
  KEY `fk` (`type_id`),
  KEY `fk_os` (`os_id`),
  CONSTRAINT `fk` FOREIGN KEY (`type_id`) REFERENCES `type` (`id`),
  CONSTRAINT `fk_brands` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`),
  CONSTRAINT `fk_os` FOREIGN KEY (`os_id`) REFERENCES `os` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `models` */

insert  into `models`(`id`,`name`,`brand_id`,`type_id`,`os_id`) values 
(4,'MacBook Air M1',1,1,2),
(5,'MacBook Air M2',1,1,2),
(6,'MacBook Air M3',1,1,2),
(7,'MacBook Pro 14',1,1,2),
(8,'MacBook Pro 16',1,1,2),
(9,'XPS 13',2,1,1),
(10,'XPS 15',2,1,1),
(11,'Alienware m15',2,2,1),
(12,'ZenBook 14',3,1,1),
(13,'ROG Strix',3,2,1),
(14,'Aspire 5',4,1,1),
(15,'Helios',4,2,1),
(16,'Pavilion 15',8,1,1),
(17,'Pavilion Gaming',8,2,1),
(18,'GF63',5,2,1),
(19,'Katana 15',5,2,1),
(20,'Yoga Slim 7',6,3,1),
(21,'Legion 7',6,2,1),
(22,'Book 4',7,3,1);

/*Table structure for table `notebook` */

DROP TABLE IF EXISTS `notebook`;

CREATE TABLE `notebook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model_id` int DEFAULT NULL,
  `ram_id` int DEFAULT NULL,
  `ssd_id` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `model_id` (`model_id`),
  KEY `ram_id` (`ram_id`),
  KEY `ssd_id` (`ssd_id`),
  CONSTRAINT `notebook_ibfk_1` FOREIGN KEY (`model_id`) REFERENCES `models` (`id`),
  CONSTRAINT `notebook_ibfk_2` FOREIGN KEY (`ram_id`) REFERENCES `ram` (`id`),
  CONSTRAINT `notebook_ibfk_3` FOREIGN KEY (`ssd_id`) REFERENCES `ssd` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `notebook` */

insert  into `notebook`(`id`,`model_id`,`ram_id`,`ssd_id`,`price`,`quantity`) values 
(7,4,1,2,1000,100),
(8,13,3,4,1200,50),
(9,9,2,2,800,10),
(11,16,2,2,999.99,10),
(12,19,4,4,2000,100),
(14,5,2,2,1500,50),
(15,12,1,1,400,20),
(16,10,1,2,550,50),
(17,11,4,3,2000,200),
(19,20,2,2,800,20),
(20,6,1,3,2000,20),
(21,19,2,3,500,30),
(22,22,2,2,850,12);

/*Table structure for table `os` */

DROP TABLE IF EXISTS `os`;

CREATE TABLE `os` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `os` */

insert  into `os`(`id`,`name`) values 
(1,'Windows'),
(2,'MacOS');

/*Table structure for table `ram` */

DROP TABLE IF EXISTS `ram`;

CREATE TABLE `ram` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ram` */

insert  into `ram`(`id`,`name`) values 
(1,'8GB'),
(2,'16GB'),
(3,'32GB'),
(4,'64GB');

/*Table structure for table `ssd` */

DROP TABLE IF EXISTS `ssd`;

CREATE TABLE `ssd` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ssd` */

insert  into `ssd`(`id`,`name`) values 
(1,'256GB'),
(2,'512GB'),
(3,'1TB'),
(4,'2TB');

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `type` */

insert  into `type`(`id`,`name`) values 
(1,'Office'),
(2,'Gaming'),
(3,'2 in 1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
