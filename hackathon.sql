-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2017 at 05:11 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hackathon`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `DATE` date DEFAULT NULL,
  `aorp` tinyint(1) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `exams`
--

CREATE TABLE `exams` (
  `exam_id` int(11) DEFAULT NULL,
  `exam_name` text,
  `exam_date` date DEFAULT NULL,
  `exam_time` time DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `exams_ut1`
-- (See below for the actual view)
--
CREATE TABLE `exams_ut1` (
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `exams_ut2`
-- (See below for the actual view)
--
CREATE TABLE `exams_ut2` (
);

-- --------------------------------------------------------

--
-- Table structure for table `holidays`
--

CREATE TABLE `holidays` (
  `holiday_id` int(11) NOT NULL,
  `day` int(2) NOT NULL,
  `month` int(2) NOT NULL,
  `weekday` varchar(10) NOT NULL,
  `hol_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `sub_id` int(11) DEFAULT NULL,
  `marks` int(11) DEFAULT NULL,
  `exam_name` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `stud_attendance`
--

CREATE TABLE `stud_attendance` (
  `stu_id` int(11) NOT NULL,
  `perc_att` double DEFAULT NULL,
  `defaulter` tinyint(1) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `stud_pers_info`
--

CREATE TABLE `stud_pers_info` (
  `stu_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `dob` date NOT NULL,
  `city` text NOT NULL,
  `study_hrs_start` time NOT NULL,
  `study_hrs_end` time NOT NULL,
  `overall_attendance` double DEFAULT NULL,
  `rela_status` tinytext NOT NULL,
  `edu_stream` tinytext NOT NULL,
  `stream_disc` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `sub_id` int(11) NOT NULL,
  `sub_name` text NOT NULL,
  `semester` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users_auth`
--

CREATE TABLE `users_auth` (
  `username` varchar(15) NOT NULL,
  `password` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure for view `exams_ut1`
--
DROP TABLE IF EXISTS `exams_ut1`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `exams_ut1`  AS  select `exams`.`stu_id` AS `stu_id`,`exams`.`exam_id` AS `exam_id`,`exams`.`exam_name` AS `exam_name`,`exams`.`exam_date` AS `exam_date`,`exams`.`exam_time` AS `exam_time`,`exams`.`class_id` AS `class_id` from `exams` where (`exams`.`exam_name` = 'IA1') ;

-- --------------------------------------------------------

--
-- Structure for view `exams_ut2`
--
DROP TABLE IF EXISTS `exams_ut2`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `exams_ut2`  AS  select `exams`.`stu_id` AS `stu_id`,`exams`.`exam_id` AS `exam_id`,`exams`.`exam_name` AS `exam_name`,`exams`.`exam_date` AS `exam_date`,`exams`.`exam_time` AS `exam_time`,`exams`.`class_id` AS `class_id` from `exams` where (`exams`.`exam_name` = 'IA2') ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `exams`
--
ALTER TABLE `exams`
  ADD UNIQUE KEY `exam_id` (`exam_id`);

--
-- Indexes for table `holidays`
--
ALTER TABLE `holidays`
  ADD PRIMARY KEY (`holiday_id`);

--
-- Indexes for table `stud_attendance`
--
ALTER TABLE `stud_attendance`
  ADD PRIMARY KEY (`stu_id`);

--
-- Indexes for table `stud_pers_info`
--
ALTER TABLE `stud_pers_info`
  ADD PRIMARY KEY (`stu_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`sub_id`);

--
-- Indexes for table `users_auth`
--
ALTER TABLE `users_auth`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `holidays`
--
ALTER TABLE `holidays`
  MODIFY `holiday_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `stud_pers_info`
--
ALTER TABLE `stud_pers_info`
  MODIFY `stu_id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `sub_id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
