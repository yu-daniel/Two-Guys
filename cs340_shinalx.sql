-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 09, 2021 at 12:20 AM
-- Server version: 10.4.17-MariaDB-log
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_shinal`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `customer_id` int(6) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customers`
--

INSERT INTO `Customers` (`customer_id`, `first_name`, `last_name`, `email`, `phone_number`) VALUES
(102336, 'Jeannie', 'Newberry', 'jnewberry9@ocn.ne.jp', '8816768306'),
(112344, 'Niall', 'Danielli', 'ndaniellih@geocities.com', '3679279352'),
(116486, 'Dietrich', 'Cockshutt', 'dcockshutti@twitpic.com', '4563216993'),
(130039, 'Olympia', 'Brauner', 'obrauner4@house.gov', '1911213031'),
(132932, 'Donetta', 'McCallam', 'dmccallam7@printfriendly.com', '3643037897'),
(139377, 'Anastasie', 'Stiebler', 'astiebler1@google.com.au', '4702563149'),
(139746, 'Ephrayim', 'Poyser', 'epoyser0@plala.or.jp', '6233594956'),
(147148, 'Earvin', 'Ventris', 'eventrisf@craigslist.org', '2298300792'),
(150484, 'Grover', 'Jandac', 'gjandac2@sitemeter.com', '4336713196'),
(161339, 'Corrinne', 'Larose', 'clarose3@51.la', '5911522892'),
(163063, 'Tamara', 'Asson', 'tassonj@xrea.com', '9857216277'),
(167050, 'Roze', 'Thynn', 'rthynn8@icio.us', '8801793601'),
(168609, 'Harlan', 'Lusher', 'hlusher6@sphinn.com', '7975183343'),
(168905, 'Eldon', 'Will', 'ewillb@lulu.com', '7151384438'),
(173339, 'Salvidor', 'Andriessen', 'sandriesseng@drupal.org', '5401944973'),
(174122, 'Kissee', 'Gasken', 'kgaskend@prlog.org', '5686611469'),
(179389, 'Millie', 'Haglinton', 'mhaglintona@imdb.com', '5268267252'),
(186425, 'Waldon', 'Enochsson', 'wenochsson5@gnu.org', '4584393683'),
(192467, 'Cobby', 'Lambertini', 'clambertinic@wix.com', '3473497329'),
(197269, 'Sonnnie', 'Duetsche', 'sduetschee@hibu.com', '3807481565');

-- --------------------------------------------------------

--
-- Table structure for table `Customers_Locations`
--

CREATE TABLE `Customers_Locations` (
  `customer_fk_id` int(6) NOT NULL,
  `store_fk_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Customers_Locations`
--

INSERT INTO `Customers_Locations` (`customer_fk_id`, `store_fk_id`) VALUES
(102336, 2),
(112344, 3),
(116486, 3),
(130039, 5),
(132932, 1),
(139377, 2),
(139746, 1),
(147148, 4),
(150484, 3),
(161339, 4),
(163063, 2),
(167050, 1),
(168609, 3),
(168905, 5),
(173339, 3),
(174122, 2),
(179389, 5),
(186425, 5),
(192467, 4),
(197269, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Employees`
--

CREATE TABLE `Employees` (
  `employee_id` int(6) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `emp_manager_id` int(6) DEFAULT NULL,
  `emp_store_id` int(6) DEFAULT NULL,
  `manager_num` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Employees`
--

INSERT INTO `Employees` (`employee_id`, `first_name`, `last_name`, `start_date`, `status`, `emp_manager_id`, `emp_store_id`, `manager_num`) VALUES
(1, 'Nevins', 'De Bruyn', '2008-04-10', 'vacation', NULL, 1, 1),
(2, 'Ellynn', 'Dik', '2009-10-10', 'active', NULL, 2, 2),
(3, 'Anselm', 'Feehily', '2018-07-10', 'active', NULL, 4, 3),
(4, 'Katheryn', 'Wardlow', '2020-02-11', 'vacation', NULL, 5, 4),
(5, 'Linnet', 'Rule', '2021-01-26', 'active', NULL, 3, 5),
(6, 'Marley', 'Lehenmann', '2020-02-11', 'active', 1, 1, NULL),
(7, 'Cristina', 'Ambrozewicz', '2020-02-11', 'active', 1, 1, NULL),
(8, 'Catlee', 'Fowley', '2020-02-11', 'active', 2, 2, NULL),
(9, 'Meredith', 'Wain', '2020-02-11', 'active', 2, 2, NULL),
(10, 'Baxie', 'Corry', '2020-02-11', 'active', 3, 4, NULL),
(11, 'Janek', 'Edginton', '2020-02-11', 'active', 3, 4, NULL),
(12, 'Willem', 'Holleran', '2020-02-11', 'active', 4, 5, NULL),
(13, 'Bee', 'Penhaligon', '2020-02-11', 'active', 4, 5, NULL),
(14, 'Fabien', 'Brophy', '2020-02-11', 'active', 5, 3, NULL),
(15, 'Anetta', 'Fishley', '2020-02-11', 'active', 5, 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Ingredients`
--

CREATE TABLE `Ingredients` (
  `ingredient_id` int(6) NOT NULL,
  `order_date` date NOT NULL,
  `ingredient_name` varchar(50) NOT NULL,
  `ingredient_cost` int(4) NOT NULL,
  `order_num` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Ingredients`
--

INSERT INTO `Ingredients` (`ingredient_id`, `order_date`, `ingredient_name`, `ingredient_cost`, `order_num`) VALUES
(508572, '2020-03-15', 'pepper', 88, 71433),
(512011, '2021-01-17', 'mayonnaise', 33, 605854),
(516942, '2020-05-29', 'tomato', 38, 874609),
(520016, '2021-01-03', 'garlic', 62, 188326),
(520184, '2020-11-20', 'salt', 96, 453431),
(525253, '2020-11-05', 'ketchup', 39, 43034),
(528220, '2020-02-29', 'mayonnaise', 53, 573075),
(529100, '2020-12-12', 'ground beef', 29, 113105),
(529748, '2020-02-02', 'ketchup', 65, 750134),
(532659, '2021-02-01', 'mayonnaise', 99, 658019),
(542385, '2020-11-30', 'ketchup', 77, 262567),
(555591, '2020-03-01', 'eggs', 48, 996505),
(562714, '2020-06-28', 'garlic', 69, 509925),
(569293, '2020-12-10', 'salt', 75, 619826),
(571352, '2020-10-01', 'lettuce', 71, 435204),
(572263, '2020-02-18', 'pepper', 31, 48729),
(579539, '2020-11-24', 'onions', 75, 505339),
(591808, '2020-06-19', 'ketchup', 29, 437353),
(591892, '2020-04-08', 'tomato', 75, 24052),
(593421, '2020-10-29', 'lettuce', 62, 930798);

-- --------------------------------------------------------

--
-- Table structure for table `Ingredients_Suppliers`
--

CREATE TABLE `Ingredients_Suppliers` (
  `ing_id` int(6) NOT NULL,
  `sup_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Ingredients_Suppliers`
--

INSERT INTO `Ingredients_Suppliers` (`ing_id`, `sup_id`) VALUES
(508572, 600005),
(512011, 600031),
(516942, 600027),
(520016, 600055),
(520184, 600078),
(525253, 600024),
(528220, 600025),
(529100, 600025),
(529748, 600000),
(532659, 600055),
(542385, 600000),
(555591, 600031),
(562714, 600001),
(569293, 600078),
(571352, 600094),
(572263, 600094),
(579539, 600001),
(591808, 600027),
(591892, 600005),
(593421, 600024);

-- --------------------------------------------------------

--
-- Table structure for table `Locations`
--

CREATE TABLE `Locations` (
  `store_id` int(6) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip_code` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Locations`
--

INSERT INTO `Locations` (`store_id`, `city`, `state`, `zip_code`) VALUES
(1, 'Los Angeles', 'California', 90017),
(2, 'Tampa', 'Florida', 33661),
(3, 'Houston', 'Texas', 77005),
(4, 'Seattle', 'Washington', 98195),
(5, 'New York', 'New York', 10001);

-- --------------------------------------------------------

--
-- Table structure for table `Managers`
--

CREATE TABLE `Managers` (
  `manager_id` int(6) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `manager_store_id` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Managers`
--

INSERT INTO `Managers` (`manager_id`, `first_name`, `last_name`, `status`, `manager_store_id`) VALUES
(1, 'Nevins', 'De Bruyn', 'vacation', 1),
(2, 'Ellynn', 'Dik', 'active', 2),
(3, 'Anselm', 'Feehily', 'active', 4),
(4, 'Katheryn', 'Wardlow', 'vacation', 5),
(5, 'Linnet', 'Rule', 'active', 3);

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `order_id` int(7) NOT NULL,
  `date_time` date NOT NULL,
  `sale_amount` int(4) NOT NULL,
  `customer_num` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (`order_id`, `date_time`, `sale_amount`, `customer_num`) VALUES
(24052, '2020-04-08', 37, 168905),
(43034, '2020-11-05', 23, 186425),
(48729, '2020-02-18', 36, 139746),
(71433, '2020-03-15', 15, 139377),
(113105, '2020-12-12', 75, 116486),
(188326, '2021-01-03', 51, 150484),
(262567, '2020-11-30', 91, 173339),
(435204, '2020-10-01', 47, 179389),
(437353, '2020-06-19', 69, 174122),
(453431, '2020-11-20', 53, 102336),
(505339, '2020-11-24', 17, 132932),
(509925, '2020-06-28', 9, 112344),
(573075, '2020-02-29', 48, 167050),
(605854, '2021-01-17', 47, 130039),
(619826, '2020-12-10', 35, 163063),
(658019, '2021-02-01', 72, 192467),
(750134, '2020-02-02', 22, 168609),
(874609, '2020-05-29', 13, 161339),
(930798, '2020-10-29', 96, 147148),
(996505, '2020-03-01', 86, 197269);

-- --------------------------------------------------------

--
-- Table structure for table `Suppliers`
--

CREATE TABLE `Suppliers` (
  `supplier_id` int(6) NOT NULL,
  `supplier_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Suppliers`
--

INSERT INTO `Suppliers` (`supplier_id`, `supplier_name`) VALUES
(600000, 'Stop & Shop'),
(600001, 'Max Grocery'),
(600005, 'Burpy Grocery'),
(600024, 'The Budget Food Store'),
(600025, 'Grateful Grocer'),
(600027, 'Discount Grocery'),
(600031, 'Max Grocery'),
(600055, 'The Grocery Gurus'),
(600078, 'Freedom Foods'),
(600094, 'Neighbourhood Grocery');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone_number` (`phone_number`);

--
-- Indexes for table `Customers_Locations`
--
ALTER TABLE `Customers_Locations`
  ADD PRIMARY KEY (`customer_fk_id`,`store_fk_id`),
  ADD KEY `store_fk_id` (`store_fk_id`);

--
-- Indexes for table `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`employee_id`),
  ADD KEY `emp_manager_id` (`emp_manager_id`),
  ADD KEY `emp_store_id` (`emp_store_id`),
  ADD KEY `manager_num` (`manager_num`);

--
-- Indexes for table `Ingredients`
--
ALTER TABLE `Ingredients`
  ADD PRIMARY KEY (`ingredient_id`),
  ADD KEY `order_num` (`order_num`);

--
-- Indexes for table `Ingredients_Suppliers`
--
ALTER TABLE `Ingredients_Suppliers`
  ADD PRIMARY KEY (`ing_id`,`sup_id`),
  ADD KEY `sup_id` (`sup_id`);

--
-- Indexes for table `Locations`
--
ALTER TABLE `Locations`
  ADD PRIMARY KEY (`store_id`);

--
-- Indexes for table `Managers`
--
ALTER TABLE `Managers`
  ADD PRIMARY KEY (`manager_id`),
  ADD KEY `manager_store_id` (`manager_store_id`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_num` (`customer_num`);

--
-- Indexes for table `Suppliers`
--
ALTER TABLE `Suppliers`
  ADD PRIMARY KEY (`supplier_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Customers`
--
ALTER TABLE `Customers`
  MODIFY `customer_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=197270;

--
-- AUTO_INCREMENT for table `Employees`
--
ALTER TABLE `Employees`
  MODIFY `employee_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `Ingredients`
--
ALTER TABLE `Ingredients`
  MODIFY `ingredient_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=593422;

--
-- AUTO_INCREMENT for table `Locations`
--
ALTER TABLE `Locations`
  MODIFY `store_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Managers`
--
ALTER TABLE `Managers`
  MODIFY `manager_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Orders`
--
ALTER TABLE `Orders`
  MODIFY `order_id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=996506;

--
-- AUTO_INCREMENT for table `Suppliers`
--
ALTER TABLE `Suppliers`
  MODIFY `supplier_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=600095;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Customers_Locations`
--
ALTER TABLE `Customers_Locations`
  ADD CONSTRAINT `Customers_Locations_ibfk_1` FOREIGN KEY (`customer_fk_id`) REFERENCES `Customers` (`customer_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `Customers_Locations_ibfk_2` FOREIGN KEY (`store_fk_id`) REFERENCES `Locations` (`store_id`) ON DELETE CASCADE;

--
-- Constraints for table `Employees`
--
ALTER TABLE `Employees`
  ADD CONSTRAINT `Employees_ibfk_1` FOREIGN KEY (`emp_manager_id`) REFERENCES `Managers` (`manager_id`) ON DELETE SET NULL,
  ADD CONSTRAINT `Employees_ibfk_2` FOREIGN KEY (`emp_store_id`) REFERENCES `Locations` (`store_id`) ON DELETE SET NULL,
  ADD CONSTRAINT `Employees_ibfk_3` FOREIGN KEY (`manager_num`) REFERENCES `Managers` (`manager_id`);

--
-- Constraints for table `Ingredients`
--
ALTER TABLE `Ingredients`
  ADD CONSTRAINT `Ingredients_ibfk_1` FOREIGN KEY (`order_num`) REFERENCES `Orders` (`order_id`) ON DELETE CASCADE;

--
-- Constraints for table `Ingredients_Suppliers`
--
ALTER TABLE `Ingredients_Suppliers`
  ADD CONSTRAINT `Ingredients_Suppliers_ibfk_1` FOREIGN KEY (`ing_id`) REFERENCES `Ingredients` (`ingredient_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `Ingredients_Suppliers_ibfk_2` FOREIGN KEY (`sup_id`) REFERENCES `Suppliers` (`supplier_id`) ON DELETE CASCADE;

--
-- Constraints for table `Managers`
--
ALTER TABLE `Managers`
  ADD CONSTRAINT `Managers_ibfk_1` FOREIGN KEY (`manager_store_id`) REFERENCES `Locations` (`store_id`) ON DELETE SET NULL;

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`customer_num`) REFERENCES `Customers` (`customer_id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
