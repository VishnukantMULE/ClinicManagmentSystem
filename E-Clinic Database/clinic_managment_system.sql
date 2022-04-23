-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 23, 2022 at 08:38 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic_managment_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `current_user_data`
--

DROP TABLE IF EXISTS `current_user_data`;
CREATE TABLE IF NOT EXISTS `current_user_data` (
  `id` int NOT NULL,
  `username` varchar(200) NOT NULL,
  `usersurname` varchar(200) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `useremail` varchar(200) NOT NULL,
  `userdbo` varchar(200) NOT NULL,
  `usermob` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dr_anjali_mule`
--

DROP TABLE IF EXISTS `dr_anjali_mule`;
CREATE TABLE IF NOT EXISTS `dr_anjali_mule` (
  `TokenNo` int NOT NULL,
  `First_Name` varchar(25) NOT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Mob_No` varchar(20) NOT NULL,
  `Day` int NOT NULL,
  `Month` varchar(20) NOT NULL,
  `Year` int NOT NULL,
  `Slot` varchar(20) NOT NULL,
  `Status` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dr_ganesh_karad`
--

DROP TABLE IF EXISTS `dr_ganesh_karad`;
CREATE TABLE IF NOT EXISTS `dr_ganesh_karad` (
  `TokenNo` int NOT NULL,
  `First_Name` varchar(25) NOT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Mob_No` varchar(20) NOT NULL,
  `Day` int NOT NULL,
  `Month` varchar(25) NOT NULL,
  `Year` int NOT NULL,
  `Slot` varchar(20) NOT NULL,
  `Status` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dr_mahesh_patil`
--

DROP TABLE IF EXISTS `dr_mahesh_patil`;
CREATE TABLE IF NOT EXISTS `dr_mahesh_patil` (
  `TokenNo` varchar(20) NOT NULL,
  `First_Name` varchar(25) NOT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Gender` varchar(25) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Mob_No` varchar(20) NOT NULL,
  `Day` int NOT NULL,
  `Month` varchar(10) NOT NULL,
  `Year` int NOT NULL,
  `Slot` varchar(20) NOT NULL,
  `Status` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dr_shubhamak_sawant`
--

DROP TABLE IF EXISTS `dr_shubhamak_sawant`;
CREATE TABLE IF NOT EXISTS `dr_shubhamak_sawant` (
  `TokenNo` int NOT NULL,
  `First_Name` varchar(25) NOT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Gender` varchar(25) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Mob_No` varchar(20) NOT NULL,
  `Day` int NOT NULL,
  `Month` varchar(10) NOT NULL,
  `Year` int NOT NULL,
  `Slot` varchar(20) NOT NULL,
  `Status` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pateint_details`
--

DROP TABLE IF EXISTS `pateint_details`;
CREATE TABLE IF NOT EXISTS `pateint_details` (
  `First_Name` varchar(15) NOT NULL,
  `Last_Name` varchar(15) NOT NULL,
  `Gender` varchar(5) NOT NULL,
  `Mobile` varchar(20) NOT NULL,
  `Email` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `D_O_B` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Address` varchar(35) NOT NULL,
  `Pincode` int NOT NULL,
  `State` varchar(8) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
