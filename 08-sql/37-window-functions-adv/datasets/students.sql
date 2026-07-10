-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2023 at 09:40 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `students`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_marks`
--

CREATE TABLE `student_marks` (
  `student_id` int(2) DEFAULT NULL,
  `name` varchar(8) DEFAULT NULL,
  `branch` varchar(4) DEFAULT NULL,
  `marks` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `student_marks`
--

INSERT INTO `student_marks` (`student_id`, `name`, `branch`, `marks`) VALUES
(1, 'Nitish', 'EEE', 82),
(2, 'Rishabh', 'EEE', 91),
(3, 'Anukant', 'EEE', 69),
(4, 'Rupesh', 'EEE', 55),
(5, 'Shubham', 'CSE', 78),
(6, 'Ved', 'CSE', 43),
(7, 'Deepak', 'CSE', 98),
(8, 'Arpan', 'CSE', 95),
(9, 'Vinay', 'ECE', 95),
(10, 'Ankit', 'ECE', 88),
(11, 'Anand', 'ECE', 81),
(12, 'Rohit', 'ECE', 95),
(13, 'Prashant', 'MECH', 75),
(14, 'Amit', 'MECH', 69),
(15, 'Sunny', 'MECH', 39),
(16, 'Gautam', 'MECH', 51),
(17, 'Abhi', 'EEE', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
