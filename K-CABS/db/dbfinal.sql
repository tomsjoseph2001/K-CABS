/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 5.7.40 : Database - mesmcamini_hostelapp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mesmcamini_hostelapp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mesmcamini_hostelapp`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add bed',7,'add_bed'),
(26,'Can change bed',7,'change_bed'),
(27,'Can delete bed',7,'delete_bed'),
(28,'Can view bed',7,'view_bed'),
(29,'Can add charges',8,'add_charges'),
(30,'Can change charges',8,'change_charges'),
(31,'Can delete charges',8,'delete_charges'),
(32,'Can view charges',8,'view_charges'),
(33,'Can add feenotification',9,'add_feenotification'),
(34,'Can change feenotification',9,'change_feenotification'),
(35,'Can delete feenotification',9,'delete_feenotification'),
(36,'Can view feenotification',9,'view_feenotification'),
(37,'Can add login',10,'add_login'),
(38,'Can change login',10,'change_login'),
(39,'Can delete login',10,'delete_login'),
(40,'Can view login',10,'view_login'),
(41,'Can add room',11,'add_room'),
(42,'Can change room',11,'change_room'),
(43,'Can delete room',11,'delete_room'),
(44,'Can view room',11,'view_room'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add roomassign',13,'add_roomassign'),
(50,'Can change roomassign',13,'change_roomassign'),
(51,'Can delete roomassign',13,'delete_roomassign'),
(52,'Can view roomassign',13,'view_roomassign'),
(53,'Can add foodentry',14,'add_foodentry'),
(54,'Can change foodentry',14,'change_foodentry'),
(55,'Can delete foodentry',14,'delete_foodentry'),
(56,'Can view foodentry',14,'view_foodentry'),
(57,'Can add complaint',15,'add_complaint'),
(58,'Can change complaint',15,'change_complaint'),
(59,'Can delete complaint',15,'delete_complaint'),
(60,'Can view complaint',15,'view_complaint'),
(61,'Can add driver',16,'add_clerk'),
(62,'Can change driver',16,'change_clerk'),
(63,'Can delete driver',16,'delete_clerk'),
(64,'Can view driver',16,'view_clerk'),
(65,'Can add feenotificationsub',17,'add_feenotificationsub'),
(66,'Can change feenotificationsub',17,'change_feenotificationsub'),
(67,'Can delete feenotificationsub',17,'delete_feenotificationsub'),
(68,'Can view feenotificationsub',17,'view_feenotificationsub'),
(69,'Can add payment_rent',18,'add_payment_rent'),
(70,'Can change payment_rent',18,'change_payment_rent'),
(71,'Can delete payment_rent',18,'delete_payment_rent'),
(72,'Can view payment_rent',18,'view_payment_rent'),
(73,'Can add bank',19,'add_bank'),
(74,'Can change bank',19,'change_bank'),
(75,'Can delete bank',19,'delete_bank'),
(76,'Can view bank',19,'view_bank'),
(77,'Can add payment_food',20,'add_payment_food'),
(78,'Can change payment_food',20,'change_payment_food'),
(79,'Can delete payment_food',20,'delete_payment_food'),
(80,'Can view payment_food',20,'view_payment_food');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'myapp','bed'),
(8,'myapp','charges'),
(9,'myapp','feenotification'),
(10,'myapp','login'),
(11,'myapp','room'),
(12,'myapp','user'),
(13,'myapp','roomassign'),
(14,'myapp','foodentry'),
(15,'myapp','complaint'),
(16,'myapp','driver'),
(17,'myapp','feenotificationsub'),
(18,'myapp','payment_rent'),
(19,'myapp','bank'),
(20,'myapp','payment_food');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-29 10:12:57.587775'),
(2,'auth','0001_initial','2023-10-29 10:12:58.326703'),
(3,'admin','0001_initial','2023-10-29 10:12:58.542585'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-29 10:12:58.542585'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-29 10:12:58.558219'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-29 10:12:58.630344'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-29 10:12:58.667768'),
(8,'auth','0003_alter_user_email_max_length','2023-10-29 10:12:58.701315'),
(9,'auth','0004_alter_user_username_opts','2023-10-29 10:12:58.701315'),
(10,'auth','0005_alter_user_last_login_null','2023-10-29 10:12:58.756221'),
(11,'auth','0006_require_contenttypes_0002','2023-10-29 10:12:58.756221'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-29 10:12:58.756221'),
(13,'auth','0008_alter_user_username_max_length','2023-10-29 10:12:58.803035'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-29 10:12:58.840359'),
(15,'auth','0010_alter_group_name_max_length','2023-10-29 10:12:58.875138'),
(16,'auth','0011_update_proxy_permissions','2023-10-29 10:12:58.875138'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-29 10:12:58.918915'),
(18,'myapp','0001_initial','2023-10-29 10:12:59.582755'),
(19,'sessions','0001_initial','2023-10-29 10:12:59.655573'),
(20,'myapp','0002_feenotificationsub','2023-10-31 04:09:56.833309'),
(21,'myapp','0003_payment_rent','2023-10-31 04:14:03.375859'),
(22,'myapp','0004_bank','2023-10-31 04:18:41.744550'),
(23,'myapp','0005_payment_rent_amount','2023-10-31 05:11:47.524397'),
(24,'myapp','0006_feenotification_amount','2023-10-31 06:05:44.957013'),
(25,'myapp','0007_payment_food','2023-10-31 10:11:33.268196');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('5vkgtfevfkjdmnzng6do8zgmwhtce7tj','eyJsaWQiOjJ9:1qx4MD:YhW0aJAaUCizYKPECmwFLuvesWLViO_7HEiKoNt7eSI','2023-11-12 11:53:29.933795'),
('qvewkje4ratrjyksdt6hzywpegqzvz7z','eyJsaWQiOjF9:1qxmQB:dX5ooEpKJUEGPZElqTanxOw4g1u6MY2NhDDZkVDKWWo','2023-11-14 10:56:31.820046');

/*Table structure for table `myapp_bank` */

DROP TABLE IF EXISTS `myapp_bank`;

CREATE TABLE `myapp_bank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `accountno` varchar(100) NOT NULL,
  `ifsccode` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_bank` */

insert  into `myapp_bank`(`id`,`accountno`,`ifsccode`,`password`,`amount`) values 
(1,'1','1','1',10000);

/*Table structure for table `myapp_bed` */

DROP TABLE IF EXISTS `myapp_bed`;

CREATE TABLE `myapp_bed` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bedno` varchar(20) NOT NULL,
  `ROOM_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_bed_ROOM_id_b16d5d39` (`ROOM_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_bed` */

insert  into `myapp_bed`(`id`,`bedno`,`ROOM_id`) values 
(1,'',1),
(2,'',1),
(3,'',1),
(4,'',1),
(5,'',1);

/*Table structure for table `myapp_charges` */

DROP TABLE IF EXISTS `myapp_charges`;

CREATE TABLE `myapp_charges` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `roomrent_month` int(11) NOT NULL,
  `food_daily` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_charges` */

insert  into `myapp_charges`(`id`,`roomrent_month`,`food_daily`) values 
(1,1,1);

/*Table structure for table `myapp_clerk` */

DROP TABLE IF EXISTS `myapp_clerk`;

CREATE TABLE `myapp_clerk` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `housename` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_clerk_LOGIN_id_36f22ea3` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_clerk` */

insert  into `myapp_clerk`(`id`,`name`,`email`,`phone`,`gender`,`housename`,`place`,`city`,`state`,`photo`,`LOGIN_id`) values 
(1,'Clerk1','clerk1@gmail.com','9874561231','Male','Thekkedath','Kizakkummuri','Kakkodi','Kerala','/media/20231031142455.jpg',2);

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `reply` varchar(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_USER_id_21ed0b20` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`complaint`,`date`,`status`,`reply`,`USER_id`) values 
(1,'dssadas','2023-10-29','replied','dasdsa',1),
(2,'dssadas','2023-10-29','replied','sdfsdfsd',1),
(3,'dsfsd sdf sd f','2023-10-29','pending','pending',1),
(4,'sadasd','2023-10-29','pending','pending',2),
(5,'sadas','2023-10-31','pending','pending',3),
(6,'dsfsdsd','2023-10-31','pending','pending',3);

/*Table structure for table `myapp_feenotification` */

DROP TABLE IF EXISTS `myapp_feenotification`;

CREATE TABLE `myapp_feenotification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `month` varchar(20) NOT NULL,
  `year` int(11) NOT NULL,
  `notification` varchar(500) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_feenotification` */

insert  into `myapp_feenotification`(`id`,`month`,`year`,`notification`,`amount`) values 
(4,'1',2023,'Fee lasr date feb3',1),
(5,'10',2023,'Payment last date november 3. ',1),
(6,'10',2023,'Payment last date november 3. ',1);

/*Table structure for table `myapp_feenotificationsub` */

DROP TABLE IF EXISTS `myapp_feenotificationsub`;

CREATE TABLE `myapp_feenotificationsub` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `FEENOTIFICATION_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feenotificationsub_FEENOTIFICATION_id_d7e70d2e` (`FEENOTIFICATION_id`),
  KEY `myapp_feenotificationsub_USER_id_3b70be79` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_feenotificationsub` */

insert  into `myapp_feenotificationsub`(`id`,`date`,`status`,`FEENOTIFICATION_id`,`USER_id`) values 
(1,'2023-10-31','pending',6,1),
(2,'2023-10-31','pending',6,2),
(3,'2023-10-31','Done',6,3);

/*Table structure for table `myapp_foodentry` */

DROP TABLE IF EXISTS `myapp_foodentry`;

CREATE TABLE `myapp_foodentry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_foodentry_USER_id_0049cac0` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_foodentry` */

insert  into `myapp_foodentry`(`id`,`Date`,`USER_id`) values 
(1,'2023-10-29',1),
(2,'2023-10-29',2),
(3,'2023-10-29',3),
(4,'2023-10-30',1),
(5,'2023-10-30',2),
(6,'2023-10-01',1),
(7,'2023-10-02',1),
(8,'2023-10-03',1),
(9,'2023-10-04',1);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','1','admin'),
(2,'clerk1@gmail.com','1','driver'),
(3,'user1@gmail.com','1','user'),
(4,'student2@gmail.com','1','user'),
(5,'sneha@gmail.com','1','user');

/*Table structure for table `myapp_payment_food` */

DROP TABLE IF EXISTS `myapp_payment_food`;

CREATE TABLE `myapp_payment_food` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `accountno` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_food_USER_id_e5b8d655` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_payment_food` */

insert  into `myapp_payment_food`(`id`,`accountno`,`amount`,`date`,`USER_id`) values 
(1,'1','1','2023-10-31',3);

/*Table structure for table `myapp_payment_rent` */

DROP TABLE IF EXISTS `myapp_payment_rent`;

CREATE TABLE `myapp_payment_rent` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `accountno` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `FEENOTIFICATIONSUB_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  `amount` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_rent_FEENOTIFICATIONSUB_id_a11d1614` (`FEENOTIFICATIONSUB_id`),
  KEY `myapp_payment_rent_USER_id_9b0f69bc` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_payment_rent` */

insert  into `myapp_payment_rent`(`id`,`accountno`,`date`,`FEENOTIFICATIONSUB_id`,`USER_id`,`amount`) values 
(1,'1','2023-10-31',3,3,'1');

/*Table structure for table `myapp_room` */

DROP TABLE IF EXISTS `myapp_room`;

CREATE TABLE `myapp_room` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `roomname` varchar(100) NOT NULL,
  `floornumber` varchar(100) NOT NULL,
  `totalbeds` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_room` */

insert  into `myapp_room`(`id`,`roomname`,`floornumber`,`totalbeds`) values 
(1,'Room1','1',5);

/*Table structure for table `myapp_roomassign` */

DROP TABLE IF EXISTS `myapp_roomassign`;

CREATE TABLE `myapp_roomassign` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `BED_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_roomassign_BED_id_17fdf31d` (`BED_id`),
  KEY `myapp_roomassign_USER_id_2ee89aee` (`USER_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_roomassign` */

insert  into `myapp_roomassign`(`id`,`BED_id`,`USER_id`) values 
(1,3,1),
(2,3,1),
(3,3,1),
(4,4,2);

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `photo` varchar(500) NOT NULL,
  `housename` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `parentname` varchar(100) NOT NULL,
  `parentphone` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`email`,`phone`,`gender`,`photo`,`housename`,`place`,`city`,`state`,`parentname`,`parentphone`,`status`,`LOGIN_id`) values 
(1,'User1','admin@gmail.com','09946520656','Male','/media/20231029154840.jpg','Thekkedath','Place','Kakkodi','Kerala','User1parent','admin@gmail.com','done',3),
(2,'Student2','student2@gmail.com','9874561231','Male','/media/20231029162724.jpg','Housename','Kizakkummuri','Kozhikode','Kerala','Student2father','7854215478','done',4),
(3,'Sneha Mam','sneha@gmail.com','7845125478','FeMale','/media/20231030153238.jpg','Nandana','Kuttikkaattoot','Kozhikode','Kerla','Sneha parent','7889655421','pending',5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
