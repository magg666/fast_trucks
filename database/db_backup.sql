-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: db-mysql-fra1-58798-do-user-10303697-0.b.db.ondigitalocean.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a922eaa4-4c55-11ec-a60c-6e60e1f07b0a:1-42';

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `shortcut` varchar(3) NOT NULL,
  `country` varchar(50) NOT NULL,
  PRIMARY KEY (`shortcut`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES ('BLZ','Belize'),('CAN','Canada'),('CRI','Costa Rica'),('GTM','Guatemala'),('HND','Honduras'),('MEX','Mexico'),('NIC','Nicaragua'),('PAN','Panama'),('SLV','El Salvador'),('USA','The United States');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distances`
--

DROP TABLE IF EXISTS `distances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distances` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start` varchar(3) NOT NULL,
  `end` varchar(3) NOT NULL,
  `distance` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `start` (`start`),
  KEY `end` (`end`),
  CONSTRAINT `distances_ibfk_1` FOREIGN KEY (`start`) REFERENCES `countries` (`shortcut`),
  CONSTRAINT `distances_ibfk_2` FOREIGN KEY (`end`) REFERENCES `countries` (`shortcut`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distances`
--

LOCK TABLES `distances` WRITE;
/*!40000 ALTER TABLE `distances` DISABLE KEYS */;
INSERT INTO `distances` VALUES (1,'USA','CAN',1),(2,'USA','MEX',1),(3,'MEX','BLZ',1),(4,'MEX','GTM',1),(5,'GTM','BLZ',1),(6,'GTM','SLV',1),(7,'GTM','HND',1),(8,'HND','SLV',1),(9,'HND','NIC',1),(10,'NIC','CRI',1),(11,'CRI','PAN',1);
/*!40000 ALTER TABLE `distances` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-24 22:15:55
