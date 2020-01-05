-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: newpbssdatabase
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-11-28 03:09:28.029297'),(2,'auth','0001_initial','2019-11-28 03:09:31.975019'),(3,'admin','0001_initial','2019-11-28 03:10:01.660348'),(4,'admin','0002_logentry_remove_auto_add','2019-11-28 03:10:10.069529'),(5,'admin','0003_logentry_add_action_flag_choices','2019-11-28 03:10:10.256422'),(6,'contenttypes','0002_remove_content_type_name','2019-11-28 03:10:14.344078'),(7,'auth','0002_alter_permission_name_max_length','2019-11-28 03:10:18.662607'),(8,'auth','0003_alter_user_email_max_length','2019-11-28 03:10:19.310252'),(9,'auth','0004_alter_user_username_opts','2019-11-28 03:10:19.420168'),(10,'auth','0005_alter_user_last_login_null','2019-11-28 03:10:21.424022'),(11,'auth','0006_require_contenttypes_0002','2019-11-28 03:10:21.564942'),(12,'auth','0007_alter_validators_add_error_messages','2019-11-28 03:10:21.739839'),(13,'auth','0008_alter_user_username_max_length','2019-11-28 03:10:25.869474'),(14,'auth','0009_alter_user_last_name_max_length','2019-11-28 03:10:32.381739'),(15,'auth','0010_alter_group_name_max_length','2019-11-28 03:10:33.255439'),(16,'auth','0011_update_proxy_permissions','2019-11-28 03:10:33.345388'),(17,'contact','0001_initial','2019-11-28 03:10:35.844958'),(18,'fbaform','0001_initial','2019-11-28 03:10:37.515998'),(19,'fbaform','0002_remove_triggers_location','2019-11-28 03:10:42.951882'),(20,'fbaform','0003_auto_20190923_1819','2019-11-28 03:10:45.576377'),(21,'fbaform','0004_anticident','2019-11-28 03:10:47.459298'),(22,'newsletter','0001_initial','2019-11-28 03:10:49.713005'),(23,'newsletter','0002_delete_newsletterusers','2019-11-28 03:10:50.489561'),(24,'positivebehaviour','0001_initial','2019-11-28 03:10:51.282110'),(25,'sessions','0001_initial','2019-11-28 03:10:52.105655'),(26,'users','0001_initial','2019-11-28 03:10:53.460857');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-29 11:51:22
