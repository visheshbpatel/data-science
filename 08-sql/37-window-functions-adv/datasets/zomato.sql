-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2023 at 09:37 AM
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
-- Database: `zomato`
--

-- --------------------------------------------------------

--
-- Table structure for table `delivery_partner`
--

CREATE TABLE `delivery_partner` (
  `index` bigint(20) DEFAULT NULL,
  `partner_id` bigint(20) DEFAULT NULL,
  `partner_name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `delivery_partner`
--

INSERT INTO `delivery_partner` (`index`, `partner_id`, `partner_name`) VALUES
(0, 1, 'Suresh'),
(1, 2, 'Amit'),
(2, 3, 'Lokesh'),
(3, 4, 'Kartik'),
(4, 5, 'Gyandeep');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `index` bigint(20) DEFAULT NULL,
  `f_id` bigint(20) DEFAULT NULL,
  `f_name` text DEFAULT NULL,
  `type` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`index`, `f_id`, `f_name`, `type`) VALUES
(0, 1, 'Non-veg Pizza', 'Non-veg'),
(1, 2, 'Veg Pizza', 'Veg'),
(2, 3, 'Choco Lava cake', 'Veg'),
(3, 4, 'Chicken Wings', 'Non-veg'),
(4, 5, 'Chicken Popcorn', 'Non-veg'),
(5, 6, 'Rice Meal', 'Veg'),
(6, 7, 'Roti meal', 'Veg'),
(7, 8, 'Masala Dosa', 'Veg'),
(8, 9, 'Rava Idli', 'Veg'),
(9, 10, 'Schezwan Noodles', 'Veg'),
(10, 11, 'Veg Manchurian', 'Veg');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `index` bigint(20) DEFAULT NULL,
  `menu_id` bigint(20) DEFAULT NULL,
  `r_id` bigint(20) DEFAULT NULL,
  `f_id` bigint(20) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`index`, `menu_id`, `r_id`, `f_id`, `price`) VALUES
(0, 1, 1, 1, 450),
(1, 2, 1, 2, 400),
(2, 3, 1, 3, 100),
(3, 4, 2, 3, 115),
(4, 5, 2, 4, 230),
(5, 6, 2, 5, 300),
(6, 7, 3, 3, 80),
(7, 8, 3, 6, 160),
(8, 9, 3, 7, 140),
(9, 10, 4, 6, 230),
(10, 11, 4, 8, 180),
(11, 12, 4, 9, 120),
(12, 13, 5, 6, 250),
(13, 14, 5, 10, 220),
(14, 15, 5, 11, 180);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `index` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `r_id` bigint(20) DEFAULT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `date` text DEFAULT NULL,
  `partner_id` bigint(20) DEFAULT NULL,
  `delivery_time` bigint(20) DEFAULT NULL,
  `delivery_rating` bigint(20) DEFAULT NULL,
  `restaurant_rating` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`index`, `order_id`, `user_id`, `r_id`, `amount`, `date`, `partner_id`, `delivery_time`, `delivery_rating`, `restaurant_rating`) VALUES
(0, 1001, 1, 1, 550, '2022-05-10', 1, 25, 5, 3),
(1, 1002, 1, 2, 415, '2022-05-26', 1, 19, 5, 2),
(2, 1003, 1, 3, 240, '2022-06-15', 5, 29, 4, NULL),
(3, 1004, 1, 3, 240, '2022-06-29', 4, 42, 3, 5),
(4, 1005, 1, 3, 220, '2022-07-10', 1, 58, 1, 4),
(5, 1006, 2, 1, 950, '2022-06-10', 2, 16, 5, NULL),
(6, 1007, 2, 2, 530, '2022-06-23', 3, 60, 1, 5),
(7, 1008, 2, 3, 240, '2022-07-07', 5, 33, 4, 5),
(8, 1009, 2, 4, 300, '2022-07-17', 4, 41, 1, NULL),
(9, 1010, 2, 5, 650, '2022-07-31', 1, 67, 1, 4),
(10, 1011, 3, 1, 450, '2022-05-10', 2, 25, 3, 1),
(11, 1012, 3, 4, 180, '2022-05-20', 5, 33, 4, 1),
(12, 1013, 3, 2, 230, '2022-05-30', 4, 45, 3, NULL),
(13, 1014, 3, 2, 230, '2022-06-11', 2, 55, 1, 2),
(14, 1015, 3, 2, 230, '2022-06-22', 3, 21, 5, NULL),
(15, 1016, 4, 4, 300, '2022-05-15', 3, 31, 5, 5),
(16, 1017, 4, 4, 300, '2022-05-30', 1, 50, 1, NULL),
(17, 1018, 4, 4, 400, '2022-06-15', 2, 40, 3, 5),
(18, 1019, 4, 5, 400, '2022-06-30', 1, 70, 2, 4),
(19, 1020, 4, 5, 400, '2022-07-15', 3, 26, 5, 3),
(20, 1021, 5, 1, 550, '2022-07-01', 5, 22, 2, NULL),
(21, 1022, 5, 1, 550, '2022-07-08', 1, 34, 5, 1),
(22, 1023, 5, 2, 645, '2022-07-15', 4, 38, 5, 1),
(23, 1024, 5, 2, 645, '2022-07-21', 2, 58, 2, 1),
(24, 1025, 5, 2, 645, '2022-07-28', 2, 44, 4, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `index` bigint(20) DEFAULT NULL,
  `id` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL,
  `f_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`index`, `id`, `order_id`, `f_id`) VALUES
(0, 1, 1001, 1),
(1, 2, 1001, 3),
(2, 3, 1002, 4),
(3, 4, 1002, 3),
(4, 5, 1003, 6),
(5, 6, 1003, 3),
(6, 7, 1004, 6),
(7, 8, 1004, 3),
(8, 9, 1005, 7),
(9, 10, 1005, 3),
(10, 11, 1006, 1),
(11, 12, 1006, 2),
(12, 13, 1006, 3),
(13, 14, 1007, 4),
(14, 15, 1007, 3),
(15, 16, 1008, 6),
(16, 17, 1008, 3),
(17, 18, 1009, 8),
(18, 19, 1009, 9),
(19, 20, 1010, 10),
(20, 21, 1010, 11),
(21, 22, 1010, 6),
(22, 23, 1011, 1),
(23, 24, 1012, 8),
(24, 25, 1013, 4),
(25, 26, 1014, 4),
(26, 27, 1015, 4),
(27, 28, 1016, 8),
(28, 29, 1016, 9),
(29, 30, 1017, 8),
(30, 31, 1017, 9),
(31, 32, 1018, 10),
(32, 33, 1018, 11),
(33, 34, 1019, 10),
(34, 35, 1019, 11),
(35, 36, 1020, 10),
(36, 37, 1020, 11),
(37, 38, 1021, 1),
(38, 39, 1021, 3),
(39, 40, 1022, 1),
(40, 41, 1022, 3),
(41, 42, 1023, 3),
(42, 43, 1023, 4),
(43, 44, 1023, 5),
(44, 45, 1024, 3),
(45, 46, 1024, 4),
(46, 47, 1024, 5),
(47, 48, 1025, 3),
(48, 49, 1025, 4),
(49, 50, 1025, 5);

-- --------------------------------------------------------

--
-- Table structure for table `restaurants`
--

CREATE TABLE `restaurants` (
  `index` bigint(20) DEFAULT NULL,
  `r_id` bigint(20) DEFAULT NULL,
  `r_name` text DEFAULT NULL,
  `cuisine` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `restaurants`
--

INSERT INTO `restaurants` (`index`, `r_id`, `r_name`, `cuisine`) VALUES
(0, 1, 'dominos', 'Italian'),
(1, 2, 'kfc', 'American'),
(2, 3, 'box8', 'North Indian'),
(3, 4, 'Dosa Plaza', 'South Indian'),
(4, 5, 'China Town', 'Chinese');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `index` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `password` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`index`, `user_id`, `name`, `email`, `password`) VALUES
(0, 1, 'Nitish', 'nitish@gmail.com', 'p252h'),
(1, 2, 'Khushboo', 'khushboo@gmail.com', 'hxn9b'),
(2, 3, 'Vartika', 'vartika@gmail.com', '9hu7j'),
(3, 4, 'Ankit', 'ankit@gmail.com', 'lkko3'),
(4, 5, 'Neha', 'neha@gmail.com', '3i7qm'),
(5, 6, 'Anupama', 'anupama@gmail.com', '46rdw2'),
(6, 7, 'Rishabh', 'rishabh@gmail.com', '4sw123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `delivery_partner`
--
ALTER TABLE `delivery_partner`
  ADD KEY `ix_delivery_partner_index` (`index`);

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD KEY `ix_food_index` (`index`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD KEY `ix_menu_index` (`index`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD KEY `ix_orders_index` (`index`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD KEY `ix_order_details_index` (`index`);

--
-- Indexes for table `restaurants`
--
ALTER TABLE `restaurants`
  ADD KEY `ix_restaurants_index` (`index`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD KEY `ix_users_index` (`index`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
