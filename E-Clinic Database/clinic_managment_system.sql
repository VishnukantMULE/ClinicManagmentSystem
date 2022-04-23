-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 23, 2022 at 08:31 PM
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

--
-- Dumping data for table `current_user_data`
--

INSERT INTO `current_user_data` (`id`, `username`, `usersurname`, `gender`, `useremail`, `userdbo`, `usermob`) VALUES
(1, 'avinash', 'andhale', 'Male', 'vishnukantm', '', '7410852'),
(1, 'avinash', 'andhale', 'Male', 'crsingh@apsit.edu.in', '6/08/2002', '7410852236'),
(1, '', '', '', '', '', '');

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

--
-- Dumping data for table `dr_anjali_mule`
--

INSERT INTO `dr_anjali_mule` (`TokenNo`, `First_Name`, `Last_Name`, `Gender`, `DOB`, `Email`, `Mob_No`, `Day`, `Month`, `Year`, `Slot`, `Status`) VALUES
(7623, 'anjali', 'mule', 'Female', '12/02/2005', 'vishnukantmule@yahoo.com', '2147483647', 16, 'April', 2022, 'Morning-(10AM-2PM)', 'completed');

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

--
-- Dumping data for table `dr_ganesh_karad`
--

INSERT INTO `dr_ganesh_karad` (`TokenNo`, `First_Name`, `Last_Name`, `Gender`, `DOB`, `Email`, `Mob_No`, `Day`, `Month`, `Year`, `Slot`, `Status`) VALUES
(9422, 'shital', 'agrawal', 'Female', '23/03/1987', 'syagrawal@apsit.edu.in', '8888812837', 8, 'January', 2020, 'Evening-(4PM-7PM)', 'completed'),
(4764, 'akshay', 'mule', 'Male', '16/08/2002', 'vishnukantmule@yahoo.com', '9326513775', 12, 'March', 2022, 'Morning-(10AM-2PM)', 'complet'),
(6606, 'jemin', 'bhanushali', 'Male', '16/02/2001', '20104109jeminbhanushali@gmail.', '9167904149', 12, 'March', 2022, 'Evening-(4PM-7PM)', 'completed'),
(9365, 'avinash', 'andhale', 'Male', '16/08/2200', 'vishnukantmule@yahoo.com', '74102852', 12, 'February', 2022, 'Evening-(4PM-7PM)', 'completed'),
(4138, 'avinash', 'andhale', 'Male', '6/08/2002', 'crsingh@apsit.edu.in', '7410852236', 22, 'April', 2022, 'Morning-(10AM-2PM)', 'pending');

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

--
-- Dumping data for table `dr_mahesh_patil`
--

INSERT INTO `dr_mahesh_patil` (`TokenNo`, `First_Name`, `Last_Name`, `Gender`, `DOB`, `Email`, `Mob_No`, `Day`, `Month`, `Year`, `Slot`, `Status`) VALUES
('7153', 'vishnukant', 'mule', 'Male', '16/08/2002', 'vishnukantmule@yahoo.com', '2147483647', 12, 'April', 2022, 'Evening-(4PM-7PM)', ''),
('9281', 'sidhant', 'darekar', 'Male', '15/03/2002', 'siddhantdarekar1010@gmail.com', '8454807795', 12, 'April', 2022, 'Evening-(4PM-7PM)', ''),
('6731', 'jewew', 'eww', 'Female', '12/02/2200', '20104109jeminbhanushali@gmail.', '3424', 12, 'February', 2022, 'Evening-(4PM-7PM)', '');

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

--
-- Dumping data for table `pateint_details`
--

INSERT INTO `pateint_details` (`First_Name`, `Last_Name`, `Gender`, `Mobile`, `Email`, `D_O_B`, `Address`, `Pincode`, `State`) VALUES
('vishnukant', 'mule', 'Male', '9326513775', 'vishnukantmule@yahoo.com', '16/08/2002', 'india', 400601, 'thane'),
('anjali', 'mule', 'Femal', '98214006548', 'vishnukantmule@yahoo.com', '12/02/2005', 'ayodhaya thane', 400601, 'thane'),
('sidhant', 'darekar', 'Male', '8454807795', 'siddhantdarekar1010@gmail.com', '15/03/2002', 'thane (e)', 400603, 'thane'),
('shital', 'agrawal', 'Femal', '8888812837', 'syagrawal@apsit.edu.in', '23/03/1987', 'thane', 400607, 'thane'),
('akshay', 'mule', 'Male', '9326513775', 'vishnukantmule@yahoo.com', '16/08/2002', 'aa', 400601, 'thane'),
('jaya', 'mehta', 'Femal', '92356871', 'vishnukantmule@yahoo.com', '12/02/2002', '2w2', 7410, '2w2'),
('jemin', 'bhanushali', 'Male', '9167904149', '20104109jeminbhanushali@gmail.com', '16/02/2001', 'asdfghjkl', 741085, 'thane'),
('', '', '', '', 'vishnukantmule@yahoo.com', '', '', 0, ''),
('', '', '', '', 'vishnukantmule@yahoo.com', '', '', 0, ''),
('', '', '', '', 'sdfghjk', '', '', 0, ''),
('jewew', 'eww', 'Femal', '3424', '20104109jeminbhanushali@gmail.com', '12/02/2200', 'dwd', 7410, 'thane'),
('avinash', 'andhale', 'Male', '74102852', 'vishnukantmule@yahoo.com', '16/08/2200', 'thaen', 400601, 'thane'),
('avinash', 'andhale', 'Male', '7410852', 'vishnukantm', '', '', 0, ''),
('avinash', 'andhale', 'Male', '7410852236', 'crsingh@apsit.edu.in', '6/08/2002', 'b4-304 thane', 400601, 'thane'),
('', '', '', '', '', '', '', 0, '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
